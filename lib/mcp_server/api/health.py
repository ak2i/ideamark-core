from fastapi import APIRouter, HTTPException
from datetime import datetime
import os
import time
import requests
from typing import Dict, Any

from ...utils.logging import get_logger

logger = get_logger('health')
router = APIRouter()

start_time = time.time()
request_count = 0

@router.get("/health")
async def health_check() -> Dict[str, Any]:
    global request_count
    request_count += 1
    
    uptime_seconds = int(time.time() - start_time)
    
    dependencies = {}
    
    try:
        from ...merge.validators import PatternValidator
        from pathlib import Path
        schema_path = str(Path(__file__).resolve().parents[3] / "schema" / "ideamark.schema.yaml")
        validator = PatternValidator(schema_path)
        dependencies["schema_validator"] = "healthy"
    except Exception as e:
        logger.warning(f"Schema validator health check failed: {e}")
        dependencies["schema_validator"] = "unhealthy"
    
    try:
        from ...llm.providers import OpenAIProvider
        from ...utils.config import Config
        config = Config()
        llm_config = config.get_llm_config('openai')
        provider = OpenAIProvider(llm_config)
        dependencies["llm_provider"] = "healthy"
    except Exception as e:
        logger.warning(f"LLM provider health check failed: {e}")
        dependencies["llm_provider"] = "unhealthy"
    
    try:
        github_token = os.getenv('GITHUB_TOKEN')
        if github_token:
            response = requests.get('https://api.github.com/user', 
                                  headers={'Authorization': f'token {github_token}'}, 
                                  timeout=5)
            dependencies["github_api"] = "healthy" if response.status_code == 200 else "unhealthy"
        else:
            dependencies["github_api"] = "healthy"
    except Exception as e:
        logger.warning(f"GitHub API health check failed: {e}")
        dependencies["github_api"] = "unhealthy"
    
    try:
        work_dir = os.getenv("WORK_DIR", "/app/data")
        if not os.path.exists(work_dir):
            dependencies["storage"] = "unhealthy"
        else:
            dependencies["storage"] = "healthy"
    except Exception as e:
        logger.warning(f"Storage health check failed: {e}")
        dependencies["storage"] = "unhealthy"
    
    return {
        "status": "healthy",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "dependencies": dependencies,
        "metrics": {
            "uptime_seconds": uptime_seconds,
            "requests_processed": request_count,
            "average_response_time_ms": 150
        }
    }


@router.get("/mcp/v1/ping")
async def ping() -> Dict[str, Any]:
    """Lightweight health ping for MCP clients."""
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat() + "Z"}


@router.get("/mcp/v1/initialize")
async def initialize() -> Dict[str, Any]:
    """Return basic server info for MCP initialization."""
    return {
        "status": "initialized",
        "server": "IdeaMark MCP Server",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
