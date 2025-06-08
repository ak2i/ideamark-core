from pydantic import BaseModel
from typing import Dict, Any, List, Optional


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
