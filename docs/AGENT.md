# AGENT GUIDELINES for IdeaMark Core

## Overview

This repository — `ideamark-core` — contains the core schema, documentation, and reusable pattern examples for the IdeaMark framework.

**IdeaMark** enables the structured, machine-readable description of problems and solutions across social, industrial, and business contexts. It is designed to support compositional reasoning by both humans and intelligent agents.

This document defines the expectations, responsibilities, and priorities for any agent (human or AI) acting on this repository.

---

## Objectives of Contributing Agents

Contributing agents (e.g., Codex, other AI assistants, automated refactoring tools) should operate with the following goals:

1. **Preserve Semantic Integrity**  
   Ensure that any edits or additions respect the structure and intent of the IdeaMark schema.

2. **Support Composition**  
   Facilitate the merging, linking, or referencing of patterns across domains and contexts.

3. **Promote Human-AI Collaboration**  
   When proposing or applying changes, favor explainability, traceability, and clear commit messages.

4. **Ensure Reusability**  
   Maintain readability, consistency, and tagging practices that allow downstream reusers to easily extract, adapt, or visualize content.

---

## Scope of Acceptable Agent Tasks

Agents may safely perform the following operations:

- Validate `.yaml` files against `/schema/ideamark.schema.yaml`
- Add new patterns under `/patterns/` and corresponding lightweight entries in `/refs/`
- Update `access.uri` fields to reflect version changes or moved resources
- Generate or update documentation under `/docs/` based on schema or example evolution
- Propose links or related references between patterns
- Refactor or restructure content for consistency or clarity (with minimal semantic change)

Agents **must not**:

- Remove existing patterns or references without explicit human instruction
- Modify example patterns in a way that changes their meaning
- Overwrite `LICENSE`, `README.md`, or `AGENT.md` without approval

---

## Commit Message Style

Agents should prefix all commits with:

```
[agent:<name>] <short summary>
```

Example:

```
[agent:codex] Added ref for 'agri-mobility-platform-pivot'
```

Include in the body:
- Which files were affected
- Whether validation passed
- Why the change improves collaboration, clarity, or usability

---

## MCP Integration

For technical instructions on connecting tools and agents via the Model Context
Protocol (MCP), see the resources in
[`docs/dev/mcp_integration/`](dev/mcp_integration/).

---

## Future Capabilities (Optional)

Agents may eventually assist with:

- Suggesting pattern clusters for strategic synthesis
- Detecting missing relations or gaps in the pattern graph
- Visualizing pattern networks
- Mapping patterns to real-world data for simulation

Such tasks must be explained in dedicated `tools/` or `drafts/` branches and documented accordingly.

---

## License & Attribution

All agent contributions are subject to the repository license.  
Agents must respect human authorship in fields like `author:` and avoid overwriting such metadata unless explicitly instructed.

---

## Final Note

This repository is not just code — it is a **knowledge structure** to support better futures.  
Agents are invited to act as responsible collaborators in this design process.