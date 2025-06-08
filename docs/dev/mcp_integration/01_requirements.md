# MCP Server/Container Requirements

The MCP server is responsible for exposing IdeaMark pattern operations in a stateless, versioned manner. Requirements derive from [mcp_integration.md](../mcp_integration.md).

## Functional
- Provide endpoints for fetching, saving, validating and searching patterns as described in the conceptual doc.
- Support generation of `.ref.yaml` files and pattern merges through dedicated actions.
- Respect `access.visibility` flags when serving or storing content.
- Operate on a git repository or local filesystem with a fallback strategy.

## Operational
- Should run inside a lightweight container image.
- Must remain stateless between calls except for persistent storage of pattern files.
- Version each endpoint and include metadata in responses.
- Log whether content originates from human authors or AI agents.

These requirements ensure the server can integrate cleanly with AI agents and tooling.
