#!/usr/bin/env python3

import yaml
import jsonschema
import sys

def validate_pattern(pattern_file, schema_file):
    """Validate a pattern file against the schema."""
    try:
        with open(schema_file, 'r') as f:
            schema = yaml.safe_load(f)

        with open(pattern_file, 'r') as f:
            pattern = yaml.safe_load(f)

        jsonschema.validate(pattern, schema)
        print(f'✓ Pattern validation passed for {pattern_file}')
        return True
        
    except jsonschema.ValidationError as e:
        print(f'✗ Validation failed for {pattern_file}: {e}')
        return False
    except Exception as e:
        print(f'✗ Error validating {pattern_file}: {e}')
        return False

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python validate_output.py <pattern_file> <schema_file>")
        sys.exit(1)
    
    pattern_file = sys.argv[1]
    schema_file = sys.argv[2]
    
    success = validate_pattern(pattern_file, schema_file)
    sys.exit(0 if success else 1)
