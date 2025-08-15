import sys
sys.path.append('/home/ubuntu/repos/ideamark-core')

from lib.mcp_server.auth.jwt_auth import create_dev_token, verify_token


def test_jwt_token_creation_and_verification() -> None:
    token = create_dev_token('test-user@example.com', admin=True)
    payload = verify_token(token)

    required_fields = ['sub', 'iss', 'aud', 'scopes', 'permissions']
    for field in required_fields:
        assert field in payload, f'missing field {field}'
