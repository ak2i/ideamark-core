import yaml
import jsonschema
from pathlib import Path
from typing import Dict, Any, List
from ..utils.logging import get_logger

logger = get_logger('validators')

class PatternValidator:
    def __init__(self, schema_path: str = None):
        if schema_path is None:
            schema_path = Path(__file__).resolve().parents[2] / "schema" / "ideamark.schema.yaml"
        
        with open(schema_path, 'r') as f:
            self.schema = yaml.safe_load(f)
        
        self.validator = jsonschema.Draft202012Validator(self.schema)
    
    def validate_pattern(self, pattern: Dict[str, Any]) -> List[str]:
        errors = []
        for error in self.validator.iter_errors(pattern):
            error_path = '.'.join(str(p) for p in error.path) if error.path else 'root'
            errors.append(f"Validation error at {error_path}: {error.message}")
        
        return errors
    
    def is_valid(self, pattern: Dict[str, Any]) -> bool:
        return len(self.validate_pattern(pattern)) == 0
    
    def validate_and_raise(self, pattern: Dict[str, Any]) -> None:
        errors = self.validate_pattern(pattern)
        if errors:
            error_msg = "Pattern validation failed:\n" + "\n".join(f"  - {error}" for error in errors)
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        logger.debug("Pattern validation successful")

def validate_ref_structure(ref_data: Dict[str, Any]) -> List[str]:
    errors = []
    
    if 'ref' not in ref_data:
        errors.append("Missing 'ref' key in reference file")
        return errors
    
    ref = ref_data['ref']
    required_fields = ['id', 'title', 'access']
    
    for field in required_fields:
        if field not in ref:
            errors.append(f"Missing required field in ref: {field}")
    
    if 'access' in ref:
        access = ref['access']
        if 'uri' not in access:
            errors.append("Missing 'uri' in access field")
        if 'visibility' not in access:
            errors.append("Missing 'visibility' in access field")
    
    return errors
