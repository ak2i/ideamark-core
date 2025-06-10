import sys
sys.path.append('/home/ubuntu/repos/ideamark-core')

from lib.mcp_server.auth.jwt_auth import create_dev_token, verify_token
import json

token = create_dev_token('test-user@example.com', admin=True)
print('Generated JWT token:', token)

payload = verify_token(token)
print('Token payload:')
print(json.dumps(payload, indent=2, default=str))

required_fields = ['sub', 'iss', 'aud', 'scopes', 'permissions']
for field in required_fields:
    if field in payload:
        print(f'✓ {field}: {payload[field]}')
    else:
        print(f'✗ Missing {field}')
