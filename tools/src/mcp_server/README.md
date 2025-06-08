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
- `GET /v1/pattern/{id}` - Fetch pattern by ID
- `POST /v1/pattern/{id}` - Save/update pattern
- `POST /v1/pattern/validate` - Validate pattern schema compliance
- `POST /v1/pattern/merge` - Merge multiple patterns
- `GET /v1/pattern/search` - Search patterns with filters

### Reference Operations
- `POST /v1/ref/generate` - Auto-generate .ref.yaml from pattern

### Health & Monitoring
- `GET /health` - Health check with dependency status

## Quick Start

### Local Development

1. **Install dependencies**:
```bash
cd tools
pip install -r requirements.txt
```

2. **Set environment variables**:
```bash
export WORK_DIR=/tmp/mcp_data
export JWT_SECRET_KEY=dev-secret-key
export LOG_LEVEL=INFO
```

3. **Run the server**:
```bash
cd src/mcp_server
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

4. **Access the API**:
- API Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

### Docker Deployment

1. **Build the container**:
```bash
cd tools/src/mcp_server
docker build -t ideamark-mcp-server .
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
| `LOG_LEVEL` | `INFO` | Logging level |
| `CORS_ORIGINS` | `*` | CORS allowed origins |
| `HOST` | `0.0.0.0` | Server bind host |
| `PORT` | `8000` | Server port |

## Authentication

The server supports JWT token authentication. For local development, you can generate a dev token:

```python
from mcp_server.auth.jwt_auth import create_dev_token
token = create_dev_token("dev-user", admin=True)
print(f"Authorization: Bearer {token}")
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
  http://localhost:8000/v1/pattern/IdeaMark-123
```

### Validate Pattern
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"content": {"id": "test", "title": "Test Pattern"}}' \
  http://localhost:8000/v1/pattern/validate
```

### Search Patterns
```bash
curl "http://localhost:8000/v1/pattern/search?q=authentication&type=security&limit=5" \
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
cd tools
python -m pytest src/mcp_server/tests/
```

### Code Style
```bash
black src/mcp_server/
flake8 src/mcp_server/
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
