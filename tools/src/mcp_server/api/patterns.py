from fastapi import APIRouter, HTTPException, Depends, Query
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
import os
import uuid
from datetime import datetime

from auth import get_current_user
from storage.local_storage import LocalStorage
from models.pattern_models import (
    PatternResponse,
    PatternValidationResponse,
    RefGenerationResponse,
    PatternMergeResponse,
    PatternSearchResponse,
)
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from merge.validators import PatternValidator, validate_ref_structure
from merge.core import PatternMerger
from io.pattern_loader import PatternLoader
from utils.config import Config
from utils.logging import get_logger

logger = get_logger("patterns_api")
router = APIRouter()

config = Config()
storage = LocalStorage()
validator = PatternValidator()
loader = PatternLoader(config)
merger = PatternMerger(config)


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


@router.get("/pattern/{pattern_id}", response_model=PatternResponse)
async def fetch_pattern(
    pattern_id: str, user: Dict[str, Any] = Depends(get_current_user)
):
    try:
        logger.info(
            f"Fetching pattern {pattern_id} for user {user.get('sub', 'unknown')}"
        )

        pattern_data = storage.load_pattern(pattern_id)
        if not pattern_data:
            raise HTTPException(
                status_code=404, detail=f"Pattern {pattern_id} not found"
            )

        access = pattern_data.get("access", {})
        visibility = access.get("visibility", "private")

        if visibility == "private" and not user.get("admin", False):
            raise HTTPException(
                status_code=403, detail="Access denied to private pattern"
            )

        return PatternResponse(
            id=pattern_data["id"],
            content=pattern_data,
            metadata={
                "retrieved_at": datetime.utcnow().isoformat() + "Z",
                "source": "local_storage",
            },
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching pattern {pattern_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/pattern/{pattern_id}", response_model=PatternResponse)
async def save_pattern(
    pattern_id: str,
    request: PatternSaveRequest,
    user: Dict[str, Any] = Depends(get_current_user),
):
    try:
        logger.info(
            f"Saving pattern {pattern_id} for user {user.get('sub', 'unknown')}"
        )

        pattern_data = request.content
        pattern_data["id"] = pattern_id

        validator.validate_and_raise(pattern_data)

        storage.save_pattern(pattern_id, pattern_data)

        return PatternResponse(
            id=pattern_id,
            content=pattern_data,
            metadata={
                "saved_at": datetime.utcnow().isoformat() + "Z",
                "saved_by": user.get("sub", "unknown"),
            },
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error saving pattern {pattern_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/pattern/validate", response_model=PatternValidationResponse)
async def validate_pattern(
    request: PatternValidateRequest, user: Dict[str, Any] = Depends(get_current_user)
):
    try:
        logger.info(f"Validating pattern for user {user.get('sub', 'unknown')}")

        pattern_data = request.content
        errors = validator.validate_pattern(pattern_data)

        is_valid = len(errors) == 0

        suggestions = []
        if not is_valid:
            suggestions = [
                "Ensure all required fields are present",
                "Check field types match the schema",
                "Verify nested object structures",
            ]

        return PatternValidationResponse(
            valid=is_valid,
            errors=errors,
            suggestions=suggestions,
            schema_version="1.0.0",
        )

    except Exception as e:
        logger.error(f"Error validating pattern: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/ref/generate", response_model=RefGenerationResponse)
async def generate_ref(
    request: RefGenerateRequest, user: Dict[str, Any] = Depends(get_current_user)
):
    try:
        logger.info(f"Generating ref for user {user.get('sub', 'unknown')}")

        pattern_data = request.pattern
        pattern_id = pattern_data.get("id")

        if not pattern_id:
            raise HTTPException(
                status_code=400, detail="Pattern must have an 'id' field"
            )

        validator.validate_and_raise(pattern_data)

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
                    "generated_at": datetime.utcnow().isoformat() + "Z",
                    "generated_by": user.get("sub", "unknown"),
                },
            }
        }

        ref_errors = validate_ref_structure(ref_data)
        if ref_errors:
            raise HTTPException(
                status_code=400, detail=f"Generated ref validation failed: {ref_errors}"
            )

        storage.save_ref(pattern_id, ref_data)

        return RefGenerationResponse(
            ref_id=pattern_id,
            ref_content=ref_data,
            metadata={
                "generated_at": datetime.utcnow().isoformat() + "Z",
                "pattern_id": pattern_id,
            },
        )

    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error generating ref: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/pattern/merge", response_model=PatternMergeResponse)
async def merge_patterns(
    request: PatternMergeRequest, user: Dict[str, Any] = Depends(get_current_user)
):
    try:
        logger.info(
            f"Merging patterns {request.pattern_ids} for user {user.get('sub', 'unknown')}"
        )

        if len(request.pattern_ids) < 2:
            raise HTTPException(
                status_code=400, detail="At least 2 patterns required for merge"
            )

        ref_paths = []
        for pattern_id in request.pattern_ids:
            ref_path = storage.get_ref_path(pattern_id)
            if not os.path.exists(ref_path):
                raise HTTPException(
                    status_code=404,
                    detail=f"Reference file not found for pattern {pattern_id}",
                )
            ref_paths.append(ref_path)

        merged_pattern, summary_data = merger.merge_patterns(
            ref_paths=ref_paths,
            intent=request.intent,
            strategy=request.strategy,
            priority=request.priority or [],
        )

        new_pattern_id = merged_pattern["id"]
        storage.save_pattern(new_pattern_id, merged_pattern)

        return PatternMergeResponse(
            merged_pattern_id=new_pattern_id,
            merged_content=merged_pattern,
            merge_summary=summary_data,
            metadata={
                "merged_at": datetime.utcnow().isoformat() + "Z",
                "merged_by": user.get("sub", "unknown"),
                "source_patterns": request.pattern_ids,
            },
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error merging patterns: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/pattern/search", response_model=PatternSearchResponse)
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
    try:
        logger.info(
            f"Searching patterns with query '{q}' for user {user.get('sub', 'unknown')}"
        )

        all_refs = storage.list_all_refs()
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
                        ref_path = storage.get_ref_path(ref_id)
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
                "searched_at": datetime.utcnow().isoformat() + "Z",
                "filters_applied": {
                    "type": type,
                    "tags": tag_filter,
                    "visibility": visibility,
                },
                "sort": sort,
            },
        )

    except Exception as e:
        logger.error(f"Error searching patterns: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
