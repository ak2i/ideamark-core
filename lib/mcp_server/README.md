# IdeaMark MCP Server

A Docker-based Model Context Protocol (MCP) server for IdeaMark pattern operations.

## Features

- **6 REST API Endpoints**: Complete pattern lifecycle management
- **JWT Authentication**: Token-based security with minimal local auth
- **Local Storage**: File-based storage using WORK_DIR environment variable
- **Docker Support**: Containerized deployment with health checks
- **Integration**: Seamless integration with existing IdeaMark components

## API Endpoints

### Pattern Operations
- `GET /mcp/v1/pattern/{id}` - Fetch pattern by ID
- `POST /mcp/v1/pattern/{id}` - Save/update pattern
- `POST /mcp/v1/pattern/validate` - Validate pattern schema compliance
- `POST /mcp/v1/pattern/merge` - Merge multiple patterns
- `GET /mcp/v1/pattern/search` - Search patterns with filters

### Reference Operations
- `POST /mcp/v1/ref/generate` - Auto-generate .ref.yaml from pattern

### Health & Monitoring
- `GET /health` - Health check with dependency status
- `GET /oauth/login` - Redirect to OAuth provider
- `GET /oauth/callback` - Exchange code for token

## Quick Start

### Local Development

1. **Install dependencies**:
```bash
cd tools
pip install -r requirements.txt
cd ..
```

2. **Copy the sample environment file**:
```bash
cp .env.example .env
```
   Edit `.env` if you need to customize any values.

3. **Run the server**:
```bash
python -m uvicorn lib.mcp_server.main:app --host 0.0.0.0 --port 8000 --reload
```

4. **Access the API**:
- API Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

### Docker Deployment

1. **Build the container**:
```bash
# Run from the repository root so shared modules are included
docker build -f lib/mcp_server/Dockerfile -t ideamark-mcp-server .
```

2. **Run with environment variables**:
```bash
docker run -d \
  -p 8000:8000 \
  -e WORK_DIR=/app/data \
  -e JWT_SECRET_KEY=your-secret-key \
  -v /host/data:/app/data \
  ideamark-mcp-server
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `WORK_DIR` | `/app/data` | Directory for patterns and refs storage |
| `JWT_SECRET_KEY` | `dev-secret-key` | JWT signing secret |
| `JWT_ALGORITHM` | `HS256` | JWT algorithm |
| `JWT_EXPIRATION_HOURS` | `24` | Token expiration time |
| `AUTH_DISABLED` | `false` | Set to `true` to disable authentication |
| `LOG_LEVEL` | `INFO` | Logging level |
| `OAUTH_CLIENT_ID` | | OAuth client ID |
| `OAUTH_CLIENT_SECRET` | | OAuth client secret |
| `CORS_ORIGINS` | `*` | CORS allowed origins |
| `HOST` | `0.0.0.0` | Server bind host |
| `PORT` | `8000` | Server port |
| `OAUTH_AUTHORIZATION_URL` | | OAuth authorization endpoint |
| `OAUTH_TOKEN_URL` | | OAuth token endpoint |
| `OAUTH_REDIRECT_URI` | | Redirect URI registered with provider |
| `OAUTH_SCOPE` | `openid profile email` | OAuth scopes requested |
| `OPENAI_API_KEY` | | OpenAI API key |
| `ANTHROPIC_API_KEY` | | Anthropic API key |
| `MISTRAL_API_KEY` | | Mistral API key |
| `GOOGLE_API_KEY` | | Google API key |
| `LLM_PROVIDER` | `openai` | Preferred LLM backend |

## Authentication

Authentication defaults to JWT or OAuth tokens. To disable all authentication (useful for local ChatGPT integration), set `AUTH_DISABLED=true`.

The server supports JWT token authentication. For local development, you can generate a dev token:

```python
from lib.mcp_server.auth.jwt_auth import create_dev_token
token = create_dev_token("dev-user", admin=True)
print(f"Authorization: Bearer {token}")
```

## OAuth Authentication

You can also authenticate via an external OAuth2 provider. After login the
provider returns an access token, which is used the same as a JWT token in
`Authorization: Bearer` headers.

Set your OAuth credentials:

```bash
export OAUTH_CLIENT_ID=my-client-id
export OAUTH_CLIENT_SECRET=my-secret
export OAUTH_ISSUER_URL=https://auth.example.com
```

Initiate the login flow from your application:

```python
import webbrowser

auth_url = f"{OAUTH_ISSUER_URL}/authorize?client_id={OAUTH_CLIENT_ID}&response_type=token"
webbrowser.open(auth_url)
```

## Storage Structure

The `WORK_DIR` contains:
```
/app/data/
├── patterns/
│   ├── pattern-id-1.yaml
│   └── pattern-id-2.yaml
└── refs/
    ├── pattern-id-1.ref.yaml
    └── pattern-id-2.ref.yaml
```

## API Examples

### Fetch Pattern
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8000/mcp/v1/pattern/IdeaMark-123
```

### Validate Pattern
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"content": {"id": "test", "title": "Test Pattern"}}' \
  http://localhost:8000/mcp/v1/pattern/validate
```

### Search Patterns
```bash
curl "http://localhost:8000/mcp/v1/pattern/search?q=authentication&type=security&limit=5" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Integration with Existing Components

The MCP server integrates with:
- **PatternValidator**: Schema validation and compliance checking
- **PatternMerger**: Multi-pattern synthesis and conflict resolution
- **PatternLoader**: Flexible content loading from various sources
- **LLM Providers**: AI-powered pattern operations

## Development

### Running Tests
```bash
python lib/mcp_server/simple_test.py
```

### Code Style
```bash
black lib/mcp_server/
flake8 lib/mcp_server/
```

## Monitoring

The server provides structured logging and health checks:
- Health endpoint includes dependency status
- Request/response logging with correlation IDs
- Error tracking and metrics collection

## Security

- JWT token validation for all endpoints
- Access control based on pattern visibility
- Environment variable based secret management
- CORS configuration for cross-origin requests

## Connecting Chat LLMs via MCP

To connect ChatGPT, Claude, or any other chat-based LLM with this server, set `MCP_SERVER_URL` (or the equivalent variable for your client) to the base URL of the MCP server. During initialization the client will call `<MCP_SERVER_URL>/tools/list` to discover available tools.

You can generate a development JWT for testing:

```python
from lib.mcp_server.auth.jwt_auth import create_dev_token

token = create_dev_token("chat-client-dev", admin=True)
print(token)
```

Include the token when your chat client makes requests:

```bash
curl -H "Authorization: Bearer $TOKEN" http://localhost:8000/mcp/v1/pattern/example
```

See the [OpenAI MCP documentation](https://platform.openai.com/docs/mcp) for more details.

## LLM Connectivity Test with Docker

You can verify that the MCP server can reach providers such as OpenAI or
Anthropic without relying on your local Python environment. The example below
uses the provided Dockerfile.

1. **Build the Docker image**
   ```bash
   # Build from the repository root so all modules are copied
   docker build -f lib/mcp_server/Dockerfile -t ideamark-mcp-server .
   ```

2. **Run the server with API keys**
   Set the keys for the providers you want to test and expose port `8000`.
   ```bash
   docker run -d --name mcp-test \
      -p 8000:8000 \
      -e OPENAI_API_KEY=sk-your-openai-key \
      -e ANTHROPIC_API_KEY=sk-your-anthropic-key \
      -e LLM_PROVIDER=openai \
      ideamark-mcp-server
   ```

3. **Create a development token**
   ```bash
   TOKEN=$(docker run --rm ideamark-mcp-server python - <<'PY'
from lib.mcp_server.auth.jwt_auth import create_dev_token
print(create_dev_token("llm-test", admin=True))
PY
)
   ```

4. **Send test requests**
   After saving two patterns, call `/mcp/v1/pattern/merge` with `strategy=synthesis`.
   The response should include a `merged_content` field produced by the chosen LLM.
   ```bash
   curl -X POST -H "Content-Type: application/json" \
        -H "Authorization: Bearer $TOKEN" \
        -d '{"content":{"id":"A","title":"Pattern A","problem":{"summary":"A"},"solution":{"approach":"A"}}}' \
        http://localhost:8000/mcp/v1/pattern/A

   curl -X POST -H "Content-Type: application/json" \
        -H "Authorization: Bearer $TOKEN" \
        -d '{"content":{"id":"B","title":"Pattern B","problem":{"summary":"B"},"solution":{"approach":"B"}}}' \
        http://localhost:8000/mcp/v1/pattern/B

   curl -X POST -H "Content-Type: application/json" \
        -H "Authorization: Bearer $TOKEN" \
        -d '{"pattern_ids":["A","B"],"strategy":"synthesis"}' \
        http://localhost:8000/mcp/v1/pattern/merge
   ```

5. **Stop the container** when you are done:
   ```bash
   docker rm -f mcp-test
   ```
