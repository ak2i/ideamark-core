from fastapi import APIRouter
from typing import Dict, Any, List
import os

from ..storage.local_storage import LocalStorage
from ...utils.config import load_prompts
from ...utils.logging import get_logger

logger = get_logger('mcp_metadata')
router = APIRouter()

storage = LocalStorage()


def _get_tools() -> List[Dict[str, Any]]:
    return [
        {
            "operation": "pattern.fetch",
            "method": "GET",
            "path": "/mcp/v1/pattern/{pattern_id}",
            "description": "Retrieve a pattern by ID",
        },
        {
            "operation": "pattern.save",
            "method": "POST",
            "path": "/mcp/v1/pattern/{pattern_id}",
            "description": "Save or update a pattern",
        },
        {
            "operation": "pattern.validate",
            "method": "POST",
            "path": "/mcp/v1/pattern/validate",
            "description": "Validate pattern content against the schema",
        },
        {
            "operation": "ref.generate",
            "method": "POST",
            "path": "/mcp/v1/ref/generate",
            "description": "Generate a .ref.yaml from pattern content",
        },
        {
            "operation": "pattern.merge",
            "method": "POST",
            "path": "/mcp/v1/pattern/merge",
            "description": "Merge multiple patterns together",
        },
        {
            "operation": "pattern.search",
            "method": "GET",
            "path": "/mcp/v1/pattern/search",
            "description": "Search available pattern references",
        },
    ]


@router.get("/mcp/v1/tools/list")
async def list_tools() -> Dict[str, Any]:
    """Return metadata describing available MCP operations.

    Example response:
    {
        "tools": [
            {"operation": "pattern.fetch", "method": "GET", "path": "/mcp/v1/pattern/{pattern_id}"},
            {"operation": "pattern.save", "method": "POST", "path": "/mcp/v1/pattern/{pattern_id}"}
        ]
    }
    """
    return {"tools": _get_tools()}


@router.get("/mcp/v1/resources/list")
async def list_resources() -> Dict[str, Any]:
    """List pattern and reference resources accessible from this server.

    Example response:
    {
        "patterns": [
            {"id": "urban-waste-recycling-logistics", "title": "Urban waste recycling logistics"}
        ],
        "refs": [
            {"id": "urban-waste-recycling-logistics", "title": "Urban waste recycling logistics"}
        ]
    }
    """
    patterns = [
        {"id": p.get("id"), "title": p.get("title", "")}
        for p in storage.list_all_patterns()
    ]
    refs = [
        {
            "id": r.get("ref", {}).get("id"),
            "title": r.get("ref", {}).get("title", ""),
        }
        for r in storage.list_all_refs()
    ]
    return {"patterns": patterns, "refs": refs}


@router.get("/mcp/v1/prompts/list")
async def list_prompts() -> Dict[str, Any]:
    """Return available prompt templates for LLM operations.

    Example response:
    {
        "prompts": [
            {"name": "problem_summary", "template": "Combine the following IdeaMark problem summaries..."}
        ]
    }
    """
    prompts = load_prompts()
    prompt_list = [
        {"name": name, "template": template}
        for name, template in prompts.items()
    ]
    return {"prompts": prompt_list}
