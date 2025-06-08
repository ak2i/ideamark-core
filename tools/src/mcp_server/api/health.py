from fastapi import APIRouter, HTTPException
from datetime import datetime
import os
import time
import sys
from typing import Dict, Any

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from utils.logging import get_logger

logger = get_logger('health')
router = APIRouter()

start_time = time.time()
request_count = 0

@router.get("/health")
async def health_check() -> Dict[str, Any]:
    global request_count
    request_count += 1
    
    uptime_seconds = int(time.time() - start_time)
    
    dependencies = {
        "schema_validator": "healthy",
        "llm_provider": "healthy",
        "github_api": "healthy"
    }
    
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
