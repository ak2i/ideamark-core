from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import os
import sys
from datetime import datetime
from typing import Dict, Any
import logging

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from api.patterns import router as patterns_router
from api.health import router as health_router
from api.mcp_metadata import router as metadata_router
from auth import get_current_user
from auth.oauth import router as oauth_router
from utils.logging import get_logger
from utils.config import Config

logger = get_logger("mcp_server")


def create_app() -> FastAPI:
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

    app.include_router(health_router, prefix="", tags=["health"])
    app.include_router(patterns_router, prefix="/v1", tags=["patterns"])
    app.include_router(metadata_router, prefix="", tags=["metadata"])
    app.include_router(oauth_router, prefix="", tags=["oauth"])

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": {
                    "code": exc.status_code,
                    "message": exc.detail,
                    "timestamp": datetime.utcnow().isoformat() + "Z",
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
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                }
            },
        )

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    log_level = os.getenv("LOG_LEVEL", "info").lower()

    uvicorn.run("main:app", host=host, port=port, log_level=log_level, reload=False)
