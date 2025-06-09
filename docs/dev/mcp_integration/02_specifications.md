# MCP Server Technical Specifications

This document provides detailed technical specifications for implementing the MCP server based on the requirements in [01_requirements.md](01_requirements.md).  The code samples below use Python for clarity, but any language capable of serving JSON-RPC (for example Node.js or Deno) can implement the same endpoints.

## API Endpoint Specifications

### 1. Pattern Retrieval: `pattern.fetch(id)`

**Endpoint**: `GET /v1/pattern/{id}`

**Description**: Retrieve a complete pattern by its unique identifier.

**Parameters**:
- `id` (path, required): Pattern ID in format `IdeaMark-{uuid}`
- `format` (query, optional): Response format (`json` | `yaml`), defaults to `json`
- `include_refs` (query, optional): Include reference metadata (`true` | `false`), defaults to `false`

**Request Headers**:
- `Authorization: Bearer <token>` (required for private/restricted patterns)
- `Accept: application/json` or `application/yaml`

**Response Format**:
```json
{
  "version": "1.0",
  "timestamp": "2025-06-08T04:15:47Z",
  "pattern": {
    "id": "IdeaMark-550e8400-e29b-41d4-a716-446655440000",
    "title": "Adaptive Reuse of Industrial Infrastructure",
    "type": "urban_design",
    "problem": {
      "summary": "Abandoned industrial sites create urban blight...",
      "factors": ["Economic decline", "Environmental contamination"]
    },
    "solution": {
      "approach": "Systematic adaptive reuse framework...",
      "components": ["Site assessment", "Community engagement"],
      "examples": ["High Line NYC", "Tate Modern London"]
    },
    "access": {
      "uri": "https://github.com/ak2i/ideamark-core/blob/main/patterns/example.yaml",
      "visibility": "public"
    }
  },
  "metadata": {
    "source": "github",
    "last_modified": "2025-06-07T10:30:00Z",
    "author_type": "human"
  }
}
```

**Error Responses**:
- `404 Not Found`: Pattern ID does not exist
- `403 Forbidden`: Insufficient permissions for private/restricted pattern
- `401 Unauthorized`: Invalid or missing authentication token

**Implementation Integration**:
- Use `PatternLoader.load_pattern_from_uri()` for content retrieval
- Apply `PatternValidator.validate_pattern()` before returning
- Respect `access.visibility` flags for authorization

### 2. Pattern Storage: `pattern.save(id, content)`

**Endpoint**: `POST /v1/pattern/{id}`

**Description**: Save or update a pattern with validation and access control.

**Parameters**:
- `id` (path, required): Pattern ID in format `IdeaMark-{uuid}`

**Request Headers**:
- `Authorization: Bearer <token>` (required)
- `Content-Type: application/json` or `application/yaml`

**Request Body**:
```json
{
  "pattern": {
    "id": "IdeaMark-550e8400-e29b-41d4-a716-446655440000",
    "title": "Updated Pattern Title",
    "type": "urban_design",
    "problem": { "summary": "..." },
    "solution": { "approach": "..." },
    "access": {
      "uri": "https://github.com/ak2i/ideamark-core/blob/main/patterns/new-pattern.yaml",
      "visibility": "public"
    }
  },
  "metadata": {
    "author": "user@example.com",
    "commit_message": "Update pattern with new solution components"
  }
}
```

**Response Format**:
```json
{
  "version": "1.0",
  "timestamp": "2025-06-08T04:15:47Z",
  "status": "saved",
  "pattern_id": "IdeaMark-550e8400-e29b-41d4-a716-446655440000",
  "validation": {
    "valid": true,
    "errors": []
  },
  "storage": {
    "location": "github:ak2i/ideamark-core/patterns/new-pattern.yaml",
    "commit_sha": "abc123def456"
  }
}
```

**Error Responses**:
- `400 Bad Request`: Invalid pattern structure or schema validation failure
- `403 Forbidden`: Insufficient permissions to modify pattern
- `409 Conflict`: Pattern ID already exists (for new patterns)
- `422 Unprocessable Entity`: Pattern fails business logic validation

**Implementation Integration**:
- Use `PatternValidator.validate_and_raise()` for schema validation
- Integrate with GitHub API for repository storage
- Generate commit messages following existing format conventions

### 3. Pattern Validation: `pattern.validate(content)`

**Endpoint**: `POST /v1/pattern/validate`

**Description**: Validate pattern content against the IdeaMark schema without saving.

**Request Headers**:
- `Content-Type: application/json` or `application/yaml`

**Request Body**:
```json
{
  "pattern": {
    "id": "IdeaMark-550e8400-e29b-41d4-a716-446655440000",
    "title": "Test Pattern",
    "type": "business_model",
    "problem": { "summary": "Test problem" },
    "solution": { "approach": "Test solution" }
  }
}
```

**Response Format**:
```json
{
  "version": "1.0",
  "timestamp": "2025-06-08T04:15:47Z",
  "validation": {
    "valid": true,
    "errors": [],
    "warnings": [
      "Optional field 'author' not specified",
      "Consider adding usage scenarios for better discoverability"
    ]
  },
  "schema_version": "2020-12",
  "suggestions": {
    "missing_optional_fields": ["author", "context", "usage_scenarios"],
    "enhancement_opportunities": ["Add more specific problem factors", "Include real-world examples"]
  }
}
```

**Error Response Example**:
```json
{
  "version": "1.0",
  "timestamp": "2025-06-08T04:15:47Z",
  "validation": {
    "valid": false,
    "errors": [
      "Validation error at id: Pattern ID must match format ^IdeaMark-[a-fA-F0-9\\-]{36}$",
      "Validation error at problem.summary: Field is required but missing"
    ],
    "warnings": []
  }
}
```

**Implementation Integration**:
- Use `PatternValidator.validate_pattern()` for comprehensive validation
- Return detailed error messages with field paths
- Include suggestions for improvement using LLM providers

### 4. Reference Generation: `ref.generate(pattern)`

**Endpoint**: `POST /v1/ref/generate`

**Description**: Generate a `.ref.yaml` file from pattern content with proper metadata.

**Request Headers**:
- `Content-Type: application/json` or `application/yaml`

**Request Body**:
```json
{
  "pattern": {
    "id": "IdeaMark-550e8400-e29b-41d4-a716-446655440000",
    "title": "Adaptive Reuse Framework",
    "type": "urban_design",
    "problem": { "summary": "..." },
    "solution": { "approach": "..." },
    "access": {
      "uri": "https://github.com/ak2i/ideamark-core/blob/main/patterns/adaptive-reuse.yaml",
      "visibility": "public"
    }
  },
  "options": {
    "include_summary": true,
    "auto_tags": true
  }
}
```

**Response Format**:
```json
{
  "version": "1.0",
  "timestamp": "2025-06-08T04:15:47Z",
  "ref_content": {
    "ref": {
      "id": "IdeaMark-550e8400-e29b-41d4-a716-446655440000",
      "title": "Adaptive Reuse Framework",
      "summary": "A systematic approach to transforming abandoned industrial sites into vibrant community spaces through stakeholder engagement and sustainable design principles.",
      "type": "urban_design",
      "tags": ["adaptive_reuse", "urban_planning", "sustainability", "community_development"],
      "access": {
        "uri": "https://github.com/ak2i/ideamark-core/blob/main/patterns/adaptive-reuse.yaml",
        "visibility": "public"
      },
      "metadata": {
        "created": "2025-06-08T04:15:47Z",
        "last_updated": "2025-06-08T04:15:47Z",
        "version": "1.0"
      }
    }
  },
  "suggested_filename": "adaptive-reuse.ref.yaml"
}
```

**Implementation Integration**:
- Use `validate_ref_structure()` to ensure generated refs are valid
- Leverage LLM providers for automatic summary generation
- Extract tags from pattern content and metadata

### 5. Pattern Merging: `pattern.merge([ids])`

**Endpoint**: `POST /v1/pattern/merge`

**Description**: Merge multiple patterns using configurable strategies and LLM assistance.

**Request Headers**:
- `Authorization: Bearer <token>` (required)
- `Content-Type: application/json`

**Request Body**:
```json
{
  "pattern_ids": [
    "IdeaMark-550e8400-e29b-41d4-a716-446655440000",
    "IdeaMark-660f9511-f3ac-52e5-b827-557766551111"
  ],
  "merge_options": {
    "intent": "union",
    "strategy": "prefer",
    "priority": ["IdeaMark-550e8400-e29b-41d4-a716-446655440000"],
    "llm_assistance": true
  },
  "output_options": {
    "generate_new_id": true,
    "target_visibility": "public"
  }
}
```

**Response Format**:
```json
{
  "version": "1.0",
  "timestamp": "2025-06-08T04:15:47Z",
  "merged_pattern": {
    "id": "IdeaMark-770a0622-04bd-63f6-c938-668877662222",
    "title": "Integrated Urban Renewal Framework",
    "type": "urban_design",
    "problem": {
      "summary": "Combined problem statement from source patterns...",
      "factors": ["Factor from pattern 1", "Factor from pattern 2"]
    },
    "solution": {
      "approach": "Synthesized approach combining both methodologies...",
      "components": ["Component A", "Component B", "Component C"],
      "examples": ["Example 1", "Example 2"]
    },
    "linked_patterns": [
      "IdeaMark-550e8400-e29b-41d4-a716-446655440000",
      "IdeaMark-660f9511-f3ac-52e5-b827-557766551111"
    ],
    "access": {
      "uri": "https://github.com/ak2i/ideamark-core/blob/main/patterns/merged-770a0622.yaml",
      "visibility": "public"
    }
  },
  "merge_summary": {
    "sources": ["IdeaMark-550e8400-e29b-41d4-a716-446655440000", "IdeaMark-660f9511-f3ac-52e5-b827-557766551111"],
    "strategy": "prefer",
    "conflicts_resolved": 3,
    "llm_assistance_used": true,
    "total_patterns_merged": 2
  }
}
```

**Implementation Integration**:
- Use `PatternMerger.merge_patterns()` for core merge logic
- Leverage `MergeStrategy` and `ConflictResolver` classes
- Integrate with configured LLM providers for conflict resolution

### 6. Pattern Search: `pattern.search(query)`

**Endpoint**: `GET /v1/pattern/search`

**Description**: Search patterns by keywords, tags, or metadata with relevance ranking.

**Parameters**:
- `q` (query, required): Search query string
- `type` (query, optional): Filter by pattern type
- `tags` (query, optional): Comma-separated list of tags
- `visibility` (query, optional): Filter by visibility (`public`, `private`, `restricted`)
- `limit` (query, optional): Maximum results to return (default: 20, max: 100)
- `offset` (query, optional): Pagination offset (default: 0)
- `sort` (query, optional): Sort order (`relevance`, `date`, `title`)

**Request Headers**:
- `Authorization: Bearer <token>` (required for private/restricted results)

**Response Format**:
```json
{
  "version": "1.0",
  "timestamp": "2025-06-08T04:15:47Z",
  "query": {
    "text": "urban sustainability",
    "filters": {
      "type": "urban_design",
      "visibility": "public"
    }
  },
  "results": {
    "total": 15,
    "returned": 10,
    "offset": 0,
    "patterns": [
      {
        "id": "IdeaMark-550e8400-e29b-41d4-a716-446655440000",
        "title": "Adaptive Reuse Framework",
        "type": "urban_design",
        "summary": "A systematic approach to transforming abandoned industrial sites...",
        "tags": ["adaptive_reuse", "sustainability", "urban_planning"],
        "relevance_score": 0.95,
        "access": {
          "uri": "https://github.com/ak2i/ideamark-core/blob/main/patterns/adaptive-reuse.yaml",
          "visibility": "public"
        },
        "metadata": {
          "last_updated": "2025-06-07T10:30:00Z",
          "author_type": "human"
        }
      }
    ]
  },
  "facets": {
    "types": {
      "urban_design": 8,
      "business_model": 4,
      "social_innovation": 3
    },
    "tags": {
      "sustainability": 12,
      "community": 8,
      "technology": 5
    }
  }
}
```

**Implementation Integration**:
- Use `PatternLoader` to access pattern repositories
- Implement full-text search across pattern content
- Respect visibility flags for access control

## Authentication & Security

### Token-Based Authentication

**Token Format**: JWT tokens with the following claims:
```json
{
  "sub": "user@example.com",
  "iss": "ideamark-mcp-server",
  "aud": "ideamark-api",
  "exp": 1717819047,
  "iat": 1717732647,
  "scopes": ["read", "write"],
  "permissions": {
    "patterns": ["read", "write"],
    "refs": ["generate"],
    "merge": ["execute"]
  }
}
```

**Authorization Header**: `Authorization: Bearer <jwt_token>`

**Scope Definitions**:
- `read`: Access to public patterns and user's private patterns
- `write`: Create and modify patterns
- `admin`: Full access including restricted patterns

### Access Control Implementation

**Visibility Enforcement**:
```python
def check_pattern_access(pattern, user_token):
    visibility = pattern.get('access', {}).get('visibility', 'private')
    
    if visibility == 'public':
        return True
    elif visibility == 'private':
        return user_token.has_scope('read') and user_token.user_id == pattern.get('author')
    elif visibility == 'restricted':
        return user_token.has_scope('admin')
    
    return False
```

**GitHub API Integration**:
- Use GitHub Personal Access Tokens for repository access
- Store tokens securely using environment variables
- Implement token rotation and expiration handling
- Support GitHub App authentication for organization-wide access

### Security Headers

**Required Response Headers**:
```
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-src 'self'
```

## Integration Architecture

### Component Integration

**PatternValidator Integration**:
```python
from lib.merge.validators import PatternValidator

validator = PatternValidator()
errors = validator.validate_pattern(pattern_data)
if errors:
    return {"validation": {"valid": False, "errors": errors}}
```

An implementation written in TypeScript might use a comparable validation library:

```ts
import { validatePattern } from "./lib/validators.ts";

const errors = validatePattern(patternData);
if (errors.length) {
  return { validation: { valid: false, errors } };
}
```

**LLM Provider Integration**:
```python
from lib.llm.providers import create_llm_provider

llm_provider = create_llm_provider('openai', config)
if llm_provider:
    synthesis_result = llm_provider.generate(merge_prompt)
```

The same concept can be expressed in JavaScript using a different SDK:

```js
import { createLlmProvider } from './lib/llm.js';

const provider = createLlmProvider('openai', config);
if (provider) {
  const synthesisResult = await provider.generate(mergePrompt);
}
```

**Configuration Management**:
```python
from lib.utils.config import Config

config = Config()
github_token = os.getenv('GITHUB_TOKEN')
llm_config = config.get_llm_config('openai')
```

In a Deno environment configuration might be loaded with environment utilities:

```ts
import { config as loadEnv } from "https://deno.land/std/dotenv/mod.ts";

const env = await loadEnv();
const githubToken = env["GITHUB_TOKEN"];
```

### External Service Integration

**GitHub API Configuration**:
```yaml
github:
  api_url: "https://api.github.com"
  token: "${GITHUB_TOKEN}"
  repositories:
    - "ak2i/ideamark-core"
  rate_limit:
    requests_per_hour: 5000
```

**LLM Service Configuration**:
```yaml
llm:
  providers:
    openai:
      api_key: "${OPENAI_API_KEY}"
      model: "gpt-4"
      max_tokens: 2000
      temperature: 0.3
    anthropic:
      api_key: "${ANTHROPIC_API_KEY}"
      model: "claude-3-sonnet-20240229"
    mistral:
      api_key: "${MISTRAL_API_KEY}"
      model: "mistral-large"
    google:
      api_key: "${GOOGLE_API_KEY}"
      model: "gemini-pro"
```

## Deployment Architecture

### Container Specification

**Dockerfile**:
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

If you prefer a JavaScript runtime, a comparable container might use a Node.js or Deno base image:

```dockerfile
FROM denoland/deno:latest
WORKDIR /app
COPY deps.ts .
RUN deno cache deps.ts
COPY . .
EXPOSE 8000
CMD ["deno", "run", "--allow-env", "--allow-net", "main.ts"]
```

**Environment Variables**:
```bash
# Authentication
JWT_SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# GitHub Integration
GITHUB_TOKEN=ghp_your_token_here
GITHUB_API_URL=https://api.github.com

# LLM Providers
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here
MISTRAL_API_KEY=sk-mistral-your-key
GOOGLE_API_KEY=sk-google-your-key

# Server Configuration
LOG_LEVEL=INFO
CORS_ORIGINS=*
API_VERSION=1.0
```

To select a specific LLM backend at startup, set the `LLM_PROVIDER` environment
variable (or pass a comparable CLI flag) to one of the keys defined under
`llm.providers`. For example:

```bash
export LLM_PROVIDER=mistral
python standalone_server.py
```

### Health Checks

**Health Check Endpoint**: `GET /health`
```json
{
  "status": "healthy",
  "version": "1.0",
  "timestamp": "2025-06-08T04:15:47Z",
  "dependencies": {
    "github_api": "healthy",
    "llm_provider": "healthy",
    "schema_validator": "healthy"
  },
  "metrics": {
    "uptime_seconds": 3600,
    "requests_processed": 1250,
    "average_response_time_ms": 150
  }
}
```

### Monitoring & Observability

**Prometheus Metrics**:
- `mcp_requests_total{method, endpoint, status}`
- `mcp_request_duration_seconds{method, endpoint}`
- `mcp_pattern_operations_total{operation, status}`
- `mcp_github_api_calls_total{status}`
- `mcp_llm_requests_total{provider, status}`

**Structured Logging**:
```json
{
  "timestamp": "2025-06-08T04:15:47Z",
  "level": "INFO",
  "service": "mcp-server",
  "operation": "pattern.fetch",
  "pattern_id": "IdeaMark-550e8400-e29b-41d4-a716-446655440000",
  "user_id": "user@example.com",
  "duration_ms": 150,
  "status": "success"
}
```

### Scaling Considerations

**Stateless Design**:
- No server-side session storage
- All state maintained in external systems (GitHub, databases)
- Horizontal scaling through load balancers

**Caching Strategy**:
- Redis for frequently accessed patterns
- CDN for static reference files
- In-memory caching for schema validation

**Performance Optimization**:
- Async/await for I/O operations
- Connection pooling for external APIs
- Batch processing for bulk operations

This specification provides comprehensive implementation guidance for building a production-ready MCP server that integrates seamlessly with the existing IdeaMark ecosystem while maintaining security, performance, and scalability requirements.
