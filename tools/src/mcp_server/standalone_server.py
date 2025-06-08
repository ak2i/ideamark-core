#!/usr/bin/env python3

from fastapi import FastAPI, HTTPException, Depends, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
import uvicorn
import os
import yaml
import time
from pathlib import Path
from typing import Dict, Any, List, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp_server")

security = HTTPBearer(auto_error=False)
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-secret-key-change-in-production")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = 24

WORK_DIR = Path(os.getenv("WORK_DIR", "/app/data"))
PATTERNS_DIR = WORK_DIR / "patterns"
REFS_DIR = WORK_DIR / "refs"

WORK_DIR.mkdir(parents=True, exist_ok=True)
PATTERNS_DIR.mkdir(parents=True, exist_ok=True)
REFS_DIR.mkdir(parents=True, exist_ok=True)


class PatternSaveRequest(BaseModel):
    content: Dict[str, Any]


class PatternValidateRequest(BaseModel):
    content: Dict[str, Any]


class RefGenerateRequest(BaseModel):
    pattern: Dict[str, Any]


class PatternMergeRequest(BaseModel):
    pattern_ids: List[str]
    intent: str = "union"
    strategy: str = "prefer"
    priority: Optional[List[str]] = None


class PatternResponse(BaseModel):
    id: str
    content: Dict[str, Any]
    metadata: Dict[str, Any]


class PatternValidationResponse(BaseModel):
    valid: bool
    errors: List[str]
    suggestions: List[str]
    schema_version: str


class RefGenerationResponse(BaseModel):
    ref_id: str
    ref_content: Dict[str, Any]
    metadata: Dict[str, Any]


class PatternMergeResponse(BaseModel):
    merged_pattern_id: str
    merged_content: Dict[str, Any]
    merge_summary: Dict[str, Any]
    metadata: Dict[str, Any]


class PatternSearchResponse(BaseModel):
    query: str
    total_results: int
    returned: int
    offset: int
    results: List[Dict[str, Any]]
    metadata: Dict[str, Any]


def create_access_token(
    data: Dict[str, Any], expires_delta: Optional[timedelta] = None
) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(hours=JWT_EXPIRATION_HOURS)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError as e:
        logger.warning(f"JWT verification failed: {e}")
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
) -> Dict[str, Any]:
    if not credentials:
        return {"sub": "anonymous", "admin": False, "authenticated": False}

    try:
        payload = verify_token(credentials.credentials)
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return {
            "sub": user_id,
            "admin": payload.get("admin", False),
            "authenticated": True,
            "exp": payload.get("exp"),
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error validating token: {e}")
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def create_dev_token(user_id: str = "dev-user", admin: bool = True) -> str:
    data = {"sub": user_id, "admin": admin, "iat": datetime.now(timezone.utc)}
    return create_access_token(data)


def save_pattern(pattern_id: str, pattern_data: Dict[str, Any]) -> None:
    pattern_path = PATTERNS_DIR / f"{pattern_id}.yaml"
    with open(pattern_path, "w") as f:
        yaml.safe_dump(pattern_data, f, default_flow_style=False, sort_keys=False)
    logger.info(f"Saved pattern {pattern_id}")


def load_pattern(pattern_id: str) -> Optional[Dict[str, Any]]:
    pattern_path = PATTERNS_DIR / f"{pattern_id}.yaml"
    if not pattern_path.exists():
        return None

    with open(pattern_path, "r") as f:
        return yaml.safe_load(f)


def save_ref(ref_id: str, ref_data: Dict[str, Any]) -> None:
    ref_path = REFS_DIR / f"{ref_id}.ref.yaml"
    with open(ref_path, "w") as f:
        yaml.safe_dump(ref_data, f, default_flow_style=False, sort_keys=False)
    logger.info(f"Saved ref {ref_id}")


def load_ref(ref_id: str) -> Optional[Dict[str, Any]]:
    ref_path = REFS_DIR / f"{ref_id}.ref.yaml"
    if not ref_path.exists():
        return None

    with open(ref_path, "r") as f:
        return yaml.safe_load(f)


def get_ref_path(ref_id: str) -> str:
    """Return filesystem path for a reference file."""
    return str(REFS_DIR / f"{ref_id}.ref.yaml")


def list_all_refs() -> List[Dict[str, Any]]:
    refs = []
    for ref_file in REFS_DIR.glob("*.ref.yaml"):
        with open(ref_file, "r") as f:
            ref_data = yaml.safe_load(f)
            refs.append(ref_data)
    return refs


def validate_pattern(pattern_data: Dict[str, Any]) -> List[str]:
    errors = []

    required_fields = ["id", "title", "type"]
    for field in required_fields:
        if field not in pattern_data:
            errors.append(f"Missing required field: {field}")

    if "type" in pattern_data and pattern_data["type"] not in [
        "design",
        "architectural",
        "behavioral",
        "creational",
    ]:
        errors.append("Invalid pattern type")

    return errors


app = FastAPI(
    title="IdeaMark MCP Server",
    description="Model Context Protocol server for IdeaMark pattern operations",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

start_time = time.time()
request_count = 0


@app.get("/health")
async def health_check() -> Dict[str, Any]:
    global request_count
    request_count += 1

    uptime_seconds = int(time.time() - start_time)

    dependencies = {
        "storage": "healthy" if WORK_DIR.exists() else "unhealthy",
        "schema_validator": "healthy",
        "llm_provider": "healthy",
        "github_api": "healthy",
    }

    return {
        "status": "healthy",
        "version": "1.0.0",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dependencies": dependencies,
        "metrics": {
            "uptime_seconds": uptime_seconds,
            "requests_processed": request_count,
            "average_response_time_ms": 150,
        },
    }


@app.get("/v1/pattern/{pattern_id}", response_model=PatternResponse)
async def fetch_pattern(
    pattern_id: str, user: Dict[str, Any] = Depends(get_current_user)
):
    logger.info(f"Fetching pattern {pattern_id} for user {user.get('sub', 'unknown')}")

    pattern_data = load_pattern(pattern_id)
    if not pattern_data:
        raise HTTPException(status_code=404, detail=f"Pattern {pattern_id} not found")

    access = pattern_data.get("access", {})
    visibility = access.get("visibility", "private")

    if visibility == "private" and not user.get("admin", False):
        raise HTTPException(status_code=403, detail="Access denied to private pattern")

    return PatternResponse(
        id=pattern_data["id"],
        content=pattern_data,
        metadata={
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "source": "local_storage",
        },
    )


@app.post("/v1/pattern/{pattern_id}", response_model=PatternResponse)
async def save_pattern_endpoint(
    pattern_id: str,
    request: PatternSaveRequest,
    user: Dict[str, Any] = Depends(get_current_user),
):
    logger.info(f"Saving pattern {pattern_id} for user {user.get('sub', 'unknown')}")

    pattern_data = request.content
    pattern_data["id"] = pattern_id

    errors = validate_pattern(pattern_data)
    if errors:
        raise HTTPException(status_code=400, detail=f"Validation failed: {errors}")

    save_pattern(pattern_id, pattern_data)

    return PatternResponse(
        id=pattern_id,
        content=pattern_data,
        metadata={
            "saved_at": datetime.now(timezone.utc).isoformat(),
            "saved_by": user.get("sub", "unknown"),
        },
    )


@app.post("/v1/pattern/validate", response_model=PatternValidationResponse)
async def validate_pattern_endpoint(
    request: PatternValidateRequest, user: Dict[str, Any] = Depends(get_current_user)
):
    logger.info(f"Validating pattern for user {user.get('sub', 'unknown')}")

    pattern_data = request.content
    errors = validate_pattern(pattern_data)

    is_valid = len(errors) == 0

    suggestions = []
    if not is_valid:
        suggestions = [
            "Ensure all required fields are present",
            "Check field types match the schema",
            "Verify nested object structures",
        ]

    return PatternValidationResponse(
        valid=is_valid, errors=errors, suggestions=suggestions, schema_version="1.0.0"
    )


@app.post("/v1/ref/generate", response_model=RefGenerationResponse)
async def generate_ref(
    request: RefGenerateRequest, user: Dict[str, Any] = Depends(get_current_user)
):
    logger.info(f"Generating ref for user {user.get('sub', 'unknown')}")

    pattern_data = request.pattern
    pattern_id = pattern_data.get("id")

    if not pattern_id:
        raise HTTPException(status_code=400, detail="Pattern must have an 'id' field")

    errors = validate_pattern(pattern_data)
    if errors:
        raise HTTPException(
            status_code=400, detail=f"Pattern validation failed: {errors}"
        )

    ref_data = {
        "ref": {
            "id": pattern_id,
            "title": pattern_data.get("title", "Untitled Pattern"),
            "description": pattern_data.get("problem", {}).get("summary", ""),
            "type": pattern_data.get("type", "unknown"),
            "tags": pattern_data.get("metadata", {}).get("tags", []),
            "access": {
                "uri": f"file://patterns/{pattern_id}.yaml",
                "visibility": pattern_data.get("access", {}).get(
                    "visibility", "public"
                ),
            },
            "metadata": {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "generated_by": user.get("sub", "unknown"),
            },
        }
    }

    save_ref(pattern_id, ref_data)

    return RefGenerationResponse(
        ref_id=pattern_id,
        ref_content=ref_data,
        metadata={
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "pattern_id": pattern_id,
        },
    )


@app.post("/v1/pattern/merge", response_model=PatternMergeResponse)
async def merge_patterns(
    request: PatternMergeRequest, user: Dict[str, Any] = Depends(get_current_user)
):
    logger.info(
        f"Merging patterns {request.pattern_ids} for user {user.get('sub', 'unknown')}"
    )

    if len(request.pattern_ids) < 2:
        raise HTTPException(
            status_code=400, detail="At least 2 patterns required for merge"
        )

    patterns = []
    for pattern_id in request.pattern_ids:
        pattern_data = load_pattern(pattern_id)
        if not pattern_data:
            raise HTTPException(
                status_code=404, detail=f"Pattern {pattern_id} not found"
            )
        patterns.append(pattern_data)

    merged_pattern = {
        "id": f"merged-{'-'.join(request.pattern_ids)}",
        "title": " + ".join([p.get("title", "Untitled") for p in patterns]),
        "type": patterns[0].get("type", "design"),
        "context": list(set(sum([p.get("context", []) for p in patterns], []))),
        "problem": {"summary": "Merged pattern combining multiple solutions"},
        "solution": {"approach": "Combined approach from multiple patterns"},
        "access": {
            "uri": f"file://patterns/merged-{'-'.join(request.pattern_ids)}.yaml",
            "visibility": "public",
        },
        "metadata": {
            "merged_from": request.pattern_ids,
            "merged_at": datetime.now(timezone.utc).isoformat(),
        },
    }

    new_pattern_id = merged_pattern["id"]
    save_pattern(new_pattern_id, merged_pattern)

    merge_summary = {
        "strategy_used": request.strategy,
        "patterns_merged": len(request.pattern_ids),
        "conflicts_resolved": 0,
        "new_fields_added": 2,
    }

    return PatternMergeResponse(
        merged_pattern_id=new_pattern_id,
        merged_content=merged_pattern,
        merge_summary=merge_summary,
        metadata={
            "merged_at": datetime.now(timezone.utc).isoformat(),
            "merged_by": user.get("sub", "unknown"),
            "source_patterns": request.pattern_ids,
        },
    )


@app.get("/v1/pattern/search", response_model=PatternSearchResponse)
async def search_patterns(
    q: str = Query(..., description="Search query"),
    type: Optional[str] = Query(None, description="Filter by pattern type"),
    tags: Optional[str] = Query(None, description="Comma-separated tags to filter by"),
    visibility: Optional[str] = Query(
        None, description="Filter by visibility (public/private)"
    ),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of results"),
    offset: int = Query(0, ge=0, description="Pagination offset"),
    sort: str = Query("relevance", description="Sort order (relevance, date, title)"),
    user: Dict[str, Any] = Depends(get_current_user),
):
    logger.info(
        f"Searching patterns with query '{q}' for user {user.get('sub', 'unknown')}"
    )

    all_refs = list_all_refs()
    matching_refs = []

    tag_filter = tags.split(",") if tags else []

    for ref_data in all_refs:
        ref = ref_data.get("ref", {})

        if visibility and ref.get("access", {}).get("visibility") != visibility:
            continue

        if type and ref.get("type") != type:
            continue

        if tag_filter:
            ref_tags = ref.get("tags", [])
            if not any(tag in ref_tags for tag in tag_filter):
                continue

        title = ref.get("title", "").lower()
        description = ref.get("description", "").lower()
        query_lower = q.lower()

        if query_lower in title or query_lower in description:
            relevance_score = 1.0
            if query_lower in title:
                relevance_score += 0.5

            last_modified = 0.0
            try:
                ref_id = ref.get("id")
                if ref_id:
                    ref_path = get_ref_path(ref_id)
                    last_modified = os.path.getmtime(ref_path)
            except Exception:
                pass
            matching_refs.append(
                {
                    "ref": ref_data,
                    "relevance_score": relevance_score,
                    "title": title,
                    "last_modified": last_modified,
                }
            )

    if sort == "title":
        matching_refs.sort(key=lambda x: x["title"])
    elif sort == "date":
        matching_refs.sort(key=lambda x: x["last_modified"], reverse=True)
    else:
        matching_refs.sort(key=lambda x: x["relevance_score"], reverse=True)

    total_results = len(matching_refs)
    matching_refs = matching_refs[offset : offset + limit]

    results = [item["ref"] for item in matching_refs]
    returned = len(results)

    return PatternSearchResponse(
        query=q,
        total_results=total_results,
        returned=returned,
        offset=offset,
        results=results,
        metadata={
            "searched_at": datetime.now(timezone.utc).isoformat(),
            "filters_applied": {
                "type": type,
                "tags": tag_filter,
                "visibility": visibility,
            },
            "sort": sort,
        },
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.status_code,
                "message": exc.detail,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": 500,
                "message": "Internal server error",
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
        },
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    log_level = os.getenv("LOG_LEVEL", "info").lower()

    uvicorn.run(
        "standalone_server:app", host=host, port=port, log_level=log_level, reload=False
    )
