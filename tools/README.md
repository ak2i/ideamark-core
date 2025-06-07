# Tools for IdeaMark Core

This directory contains helper scripts and utilities for managing, validating, and visualizing IdeaMark patterns.

---

## Tool Categories

### ✅ Validation
- Schema validation for `.yaml` files against `/schema/ideamark.schema.yaml`.

### 🔄 Conversion
- Format conversion: YAML ↔ JSON ↔ Markdown.

### 🔗 Composition / Merge
- Experimental tools to support merging and composing multiple patterns (e.g., finding common `context`, resolving conflicting `solution` entries).

### 📊 Visualization
- Scripts to output pattern graphs using DOT, Mermaid, or GraphQL-like structures.

---

## How to Use

Each tool should:
- Be placed in a subfolder under `/tools/`
- Include a README or help message
- Avoid modifying files unless explicitly instructed

---

If you add a new tool, please update this file and include usage instructions.