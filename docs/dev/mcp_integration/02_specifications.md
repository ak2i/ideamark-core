# MCP Server Detailed Specifications

This document expands on the requirements in [01_requirements.md](01_requirements.md) and describes the API surface and flow for integrating IdeaMark with external agents.

## API Endpoints
- `GET /v1/pattern/{id}` – return a full YAML pattern.
- `POST /v1/pattern/{id}` – save or update a pattern document.
- `POST /v1/pattern/validate` – validate supplied YAML content.
- `POST /v1/ref/generate` – produce a `.ref.yaml` from a pattern.
- `POST /v1/pattern/merge` – merge multiple pattern IDs and return new content.
- `GET /v1/pattern/search?q=<query>` – search refs by keyword or tag.

Endpoints return JSON or YAML according to the `Accept` header and include a `version` field in each response.

## Authentication
- Use token-based authentication via the `Authorization` header.
- Tokens may be scoped to read or write operations.
- Requests without valid credentials should receive `401` responses.

## Integration Flow
1. The LLM session or tool calls `GET /pattern/{id}` to load an existing idea.
2. User edits are validated via `POST /pattern/validate` before saving.
3. Final content is stored using `POST /pattern/{id}`.
4. A reference file can be generated with `POST /ref/generate`.
5. When merging patterns, call `POST /pattern/merge` with a list of IDs.

These specifications provide a consistent interface for agents and automation to interact with IdeaMark patterns through the MCP server.
