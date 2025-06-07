# IdeaMark Format Guides

This document explains how to write and use IdeaMark files, focusing on the two primary formats:

- Full Pattern Files (`.yaml`)
- Reference Entries (`.ref.yaml`)

---

## 📘 Full Pattern Format (`.yaml`)

These files live in the `/patterns/` directory and follow the `ideamark.schema.yaml` specification.

They include all essential fields for:

- Contextual understanding
- Problem/solution expression
- Compositional metadata
- AI- or human-led merging

### Key Fields

```yaml
id: IdeaMark-<UUID>
title: Example Pattern Title
type: digital_commerce_model
author: your-name@domain.com
context: [...]
problem:
  summary: ...
  factors: [...]
solution:
  approach: ...
  components: [...]
  examples: [...]
access:
  uri: https://github.com/org/ideamark-core/patterns/example.yaml
  visibility: public
metadata:
  tags: [logistics, aging_population]
  scalefactor:
    timewindow: "2–5 years"
    spacemetrics: "urban neighborhood"
    regions: ["Shikoku"]
    organizations: ["city council"]
```

**Tips:**
- Keep field names lowercase and snake_case
- Use plain strings or simple arrays — avoid deep nesting
- Use `linked_patterns`, `children`, or `relations` to structure the network

---

## 📄 Reference Format (`.ref.yaml`)

Reference entries are lightweight descriptors used for:

- Indexing
- Search & filtering
- Input to merge/synthesis tools
- Prompt input to LLMs

These files live in `/refs/` and contain a `ref:` key with a subset of fields.

### Example

```yaml
ref:
  id: IdeaMark-abc123-def456
  title: Localized Logistics Hub for Aging Communities
  access:
    uri: https://github.com/org/ideamark-core/patterns/local-logistics.yaml
    visibility: public
  metadata:
    tags: [mobility, health]
    scalefactor:
      timewindow: "1–3 years"
      regions: ["Tohoku"]
```

**Tips:**
- Match the `id` exactly with the source pattern
- Avoid redundancy — use only the fields needed for identification and filtering
- Keep ref files small (<1KB ideally)

---

## ✅ Best Practices

- One pattern = one `.yaml` file, one `.ref.yaml` file
- Match filenames: `example.yaml` and `example.ref.yaml`
- Use UUID-based `id` fields to ensure global uniqueness
- Validate pattern files against the schema before publishing

---

## Tooling Support

- Validation and merge tools are being added to `/tools/`
- LLM prompts can directly ingest `.ref.yaml` lists
- Conversion scripts (YAML ↔ JSON ↔ Markdown) are supported in community tools

---

IdeaMark formats are designed to be accessible, readable, and extensible — use them flexibly but consistently.