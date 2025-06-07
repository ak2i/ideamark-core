# Pattern Merge Tool Specification

## Purpose

The Pattern Merge Tool enables the AI-assisted composition of multiple IdeaMark patterns into a synthesized or hybrid pattern.  
It supports both **explicit merging** (selected refs) and **suggested composition** (contextual graph inference).

This tool is designed to be run by a developer or agent, and relies on existing IdeaMark pattern YAML files and their associated refs.

---

## Inputs

### 1. Required

- One or more `ref.yaml` files (from `/refs/`) — minimum two
- The corresponding full pattern files must exist in `/patterns/` and match `access.uri`

### 2. Optional

- Merge intent: `intersection`, `union`, `hybrid`, `synthesis`
- Conflict resolution strategy: `manual`, `prefer-a`, `prefer-b`, `annotate`

---

## Outputs

- A new YAML file (full IdeaMark pattern), placed in a specified directory
- Optional summary report (Markdown or JSON) including:
  - ID and titles of source patterns
  - Conflicts detected and how they were resolved
  - Composition strategy used
  - Linked source IDs in `linked_patterns`

---

## Core Logic

### 1. Pattern Loading
- Load full patterns from their `access.uri` based on `ref.id`

### 2. Conflict Detection
- Compare `problem.summary`, `solution.approach`, and any shared `metadata`
- Flag fields with semantically distinct content

### 3. Merge Strategy
- If `manual`: leave placeholders and generate TODO notes
- If `prefer-a`: pattern A takes priority
- If `synthesis`: attempt LLM-assisted rewrite based on similarity

### 4. Composition
- Combine `context`, `problem.factors`, `solution.components`, `metadata.tags`, etc.
- Create a new unique `id` and populate `linked_patterns` with source IDs

---

## CLI Interface (Suggested)

```bash
python merge_tool.py \
  --refs refs/a.ref.yaml refs/b.ref.yaml \
  --strategy synthesis \
  --out patterns/merged-agri-tourism.yaml
```

---

## AI Integration (Optional)

This tool may optionally use an LLM to:
- Summarize common elements across patterns
- Rewrite the `solution.approach` or `problem.summary`
- Generate conflict resolution annotations

---

## Design Goals

- Modular architecture for easy extension
- Human-readable outputs, editable post-hoc
- Designed to support conversation-style AI workflows