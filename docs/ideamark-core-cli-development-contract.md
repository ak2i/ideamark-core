# IdeaMark Core / CLI Development Contract (v0)

## Purpose

This document defines the **minimum, non-negotiable contract** for developing `ideamark-core` and `ideamark-cli`.

Its goal is to ensure that:
- Humans and AI (LLMs) can collaboratively author IdeaMark documents
- All outputs remain **machine-verifiable**
- Core logic stays **template-agnostic and model-agnostic**
- Templates, not core code, define methodology and structure

This document is authoritative for implementation decisions.
If another document conflicts with this one, **this document takes precedence**.

---

## Design Principles (Binding)

### 1. Core Is a Tool, Not a Methodology
- `ideamark-core` **must not encode domain logic**
- Templates define *what to write*
- Core defines *how to verify, normalize, and reference what was written*

### 2. Templates Are Forms, Not Mere Examples
- Files under `templates/**/*.ideamark.template.md` are **structured input forms**
- They are designed to be filled by:
  - Humans
  - LLMs
  - Human–AI collaboration
- Core/CLI must treat templates as **first-class specifications**

### 3. AI Is a Participant, Not an Authority
- AI output is always treated as **proposed content**
- All AI-assisted output **must pass validation**
- Core must remain **LLM-provider independent**

---

## IdeaMark Document Contract (Minimal)

### File Format
- Markdown (`.md`)
- YAML frontmatter at the top
- Optional structured blocks in the body (YAML / JSON / others)

### Frontmatter (Required Fields)

```yaml
ideamark_version: 1
template_id: "<template identifier>"
doc_id: "<unique document identifier>"
created_at: "<ISO 8601 timestamp>"
lang: "<language tag>"
```

### Frontmatter (Recommended, Not Mandatory)

```yaml
created_by: "<human | ai | hybrid>"
provenance:
  - source: "<description>"
    at: "<timestamp>"
```

> **Core must not require more than the Required fields.**

---

## Body Structure Policy

- Core **must not assume** a fixed semantic model for body blocks
- Core **may**:
  - Detect structured blocks
  - Extract metadata (block type, id, references)
  - Validate syntactic correctness
- Core **must not**:
  - Impose meaning on block contents
  - Assume blocks are “nodes” in a fixed ontology

Block semantics are **template-defined**, not core-defined.

---

## ideamark-core Responsibilities

### Must Do
- Parse Markdown + frontmatter
- Validate frontmatter against minimal contract
- Extract structured blocks without interpreting meaning
- Perform schema validation *if explicitly requested by template*
- Provide stable APIs for:
  - `parse`
  - `validate`
  - `normalize`
  - `extract`

### Must Not Do
- Call LLM APIs
- Encode template-specific rules
- Perform generation or auto-completion

---

## ideamark-cli Responsibilities

### Core Commands (v0)

#### `ideamark new --template <path>`
- Copy template to working directory
- Generate document-specific frontmatter
- Preserve all template structure

#### `ideamark validate <file>`
- Validate document using ideamark-core
- Fail on contract violations
- Produce machine-readable error output

### AI-Related Commands (Explicit & Optional)

If implemented, AI assistance must be:
- Explicitly invoked (e.g. `ideamark assist`)
- Non-destructive by default
- Always followed by validation

---

## Non-Goals (Explicit)

The following are **out of scope for v0**:
- Semantic reasoning over document contents
- Automatic decision-making
- Template interpretation inside core
- Enforcement of domain-specific correctness

---

## Evolution Policy

- This contract is expected to evolve
- Backward compatibility should be preserved when possible
- Breaking changes require a new contract version

---

## Summary (For AI Implementers)

When in doubt:
- Prefer **less interpretation**
- Prefer **templates over code**
- Prefer **validation over generation**
- Prefer **explicitness over convenience**

This is a **design memory tool**, not an intelligent agent.
