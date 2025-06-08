# MCP Integration for IdeaMark

## Purpose

This document outlines how **Model Context Protocol (MCP)** can be used to enhance the lifecycle of IdeaMark patterns — enabling AI agents (such as ChatGPT, Codex, or other LLM-based systems) to interact with, generate, update, and merge structured knowledge via standardized interfaces.

MCP enables external tools and data sources to be connected with AI sessions, turning conversational exploration into persistent, reusable structured insights.

---

## Why MCP?

The IdeaMark workflow is conversational at its core — problems and ideas emerge organically through discussion.  
MCP bridges the gap between **interactive dialogue** and **structured knowledge artifacts**, enabling:

- Real-time drafting of `.yaml` pattern files
- Validation and ref generation via external CLI tools
- Live access to the pattern repository
- Assisted composition, comparison, and merge actions
- Version-aware updates to public or restricted knowledge graphs

## MCP Self-Descriptive Mechanisms

MCP servers expose three categories of metadata so that agents can discover capabilities dynamically:

- **Tools** – callable operations with names, descriptions and input schemas
- **Resources** – URIs or contextual data the server can provide
- **Prompts** – reusable instructions or templates for downstream LLM calls

Clients typically retrieve these via `tools/list`, `resources/list`, and `prompts/list` RPC methods. A server might be written in Python with FastAPI, Deno with Oak, or Node.js with Express—the contract remains the same. This flexibility allows any runtime to plug into the IdeaMark workflow.

---

## Architecture

### Agents

- **LLM Session Agent**: Primary interface with the user
- **MCP Client**: Manages outbound calls to tools, APIs, validators

### External Tools via MCP

- `pattern.fetch(id)` → returns YAML content
- `pattern.save(id, content)` → persists content
- `pattern.validate(content)` → schema compliance check
- `ref.generate(pattern)` → auto-generate `.ref.yaml`
- `pattern.merge([ids])` → synthesize a new pattern
- `pattern.search(query)` → return matching refs

---

## Typical Workflow (Example)

1. **User**: "We're exploring how to reuse disused fishing port buildings for tourism and disaster response."
2. **LLM**: Proposes to create a new IdeaMark and initializes a draft structure.
3. **MCP**: 
   - Validates structure via `pattern.validate()`
   - Checks for similar patterns via `pattern.search()`
   - Suggests `linked_patterns`
4. **User & LLM**: Fill in details together
5. **MCP**: 
   - Saves new pattern to GitHub via `pattern.save()`
   - Generates `.ref.yaml` via `ref.generate()`

---

## Benefits of MCP for IdeaMark

| Functionality           | Benefit                                      |
|------------------------|----------------------------------------------|
| Dynamic Drafting        | Patterns emerge from natural conversation    |
| Assisted Composition    | Connects related ideas on the fly            |
| Toolchain Automation    | Validates, stores, and links via MCP         |
| Multi-agent Collaboration | External AI agents can use shared schema     |
| Decentralized Hosting   | Access URIs allow non-centralized repositories |

---

## Developer Considerations

- MCP endpoints should be stateless and versioned
- Agents must respect `access.visibility` flags
- Logging must distinguish AI-written vs human-authored content
- GitHub or local file APIs should support fallback modes

---

## Future Extensions

- Triggering visualizers (e.g., Mermaid or Graph view) from within the LLM session
- Embedding IdeaMark authoring into external knowledge systems (Notion, Obsidian)
- LLM-driven discovery bots that monitor the repo for combinable patterns

---

## Further Reading
- [MCP Server/Container Requirements](mcp_integration/01_requirements.md)
- [MCP Server Detailed Specifications](mcp_integration/02_specifications.md)

This document serves as a conceptual specification for developers implementing MCP clients or servers in an IdeaMark-compatible environment.
