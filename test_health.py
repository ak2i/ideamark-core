import sys
sys.path.append('/home/ubuntu/repos/ideamark-core')

from lib.mcp_server.api.health import health_check
import asyncio
import json

async def test_health():
    try:
        result = await health_check()
        print('Health check response:')
        print(json.dumps(result, indent=2, default=str))
        
        required_fields = ['status', 'version', 'timestamp', 'dependencies', 'metrics']
        for field in required_fields:
            if field in result:
                print(f'✓ {field}: present')
            else:
                print(f'✗ Missing {field}')
                
        deps = result.get('dependencies', {})
        expected_deps = ['schema_validator', 'llm_provider', 'github_api', 'storage']
        for dep in expected_deps:
            if dep in deps:
                print(f'✓ dependency {dep}: {deps[dep]}')
            else:
                print(f'✗ Missing dependency {dep}')
                
    except Exception as e:
        print(f'Health check failed: {e}')
        import traceback
        traceback.print_exc()

asyncio.run(test_health())
