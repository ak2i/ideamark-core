# Contributing to IdeaMark Core

We welcome contributions from designers, researchers, engineers, policymakers, and AI agents alike.

This repository forms the foundation of a reusable, AI-friendly knowledge framework for pattern-based thinking.  
Your additions help expand its utility across domains and geographies.

---

## How to Contribute

### 🧩 Add a New Pattern
1. Create a YAML file under `/patterns/` following the schema in `/schema/ideamark.schema.yaml`.
2. Use a globally unique ID: `IdeaMark-<UUID>`.
3. Include an `access.uri` field that points to where it is published (e.g., your repo, your website).
4. Add a lightweight entry under `/refs/` with the same filename but `.ref.yaml`.

### 🔁 Update or Link Patterns
- Edit metadata or add `children`, `relations`, or `linked_patterns` fields to show connectivity.
- When referencing other patterns, use their `id` and verify their presence in `/refs/`.

### 🛠 Propose New Tools or Scripts
- Place them under `/tools/` and include a description in `/tools/README.md`.

---

## Validation

Before submitting a pull request:

- ✅ Validate your pattern using the schema in `/schema/ideamark.schema.yaml`.
- ✅ Ensure your YAML files parse correctly.
- ✅ Verify links (`access.uri`) are reachable or clearly marked `draft`.

---

## Communication Style

- Explain **why** the change improves reuse, clarity, or collaboration.
- For AI-generated contributions, follow the [`AGENT.md`](./AGENT.md) guidelines.

---

Thank you for contributing to the IdeaMark ecosystem!