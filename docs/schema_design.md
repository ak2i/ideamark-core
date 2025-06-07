# Schema Design Rationale for IdeaMark

## Why a Schema?

IdeaMark's schema is not just a data contract — it's a philosophy about **how knowledge can be structured to support collaboration and synthesis** across complex systems.

The schema embodies a way to express real-world design fragments that:

- Are reusable and composable
- Can be referenced or linked across domains
- Make sense to both humans and machines

Where traditional schemas aim for rigidity and constraint, IdeaMark's schema is designed for **semantic flexibility and evolving granularity**.

---

## Design Goals

### 1. ✅ **Structured yet Open**
The schema enforces a basic structure (`context`, `problem`, `solution`) while allowing open-ended metadata (tags, scale, examples) to reflect varied use cases.

### 2. 🌐 **Cross-domain Compatibility**
It is intentionally domain-agnostic, supporting:
- Business pivots
- Social infrastructure design
- Environmental policy
- Technological platforms
All using the same core structure.

### 3. 🔁 **Designed for Composition**
Every field in the schema is designed to support:
- Comparison between patterns
- Conflict detection and resolution
- Meaningful synthesis (e.g. combining multiple `context` or `solution` fields)

### 4. 🧠 **LLM-Ready**
By using regular, consistent field names and YAML-friendly formatting, the schema is easy for LLMs to:
- Ingest
- Compare
- Complete
- Merge

---

## The Scalefactor Innovation

Most frameworks label items as "micro", "macro", etc.  
But such labels are relative and ambiguous.

Instead, IdeaMark introduces `metadata.scalefactor`:

```yaml
scalefactor:
  timewindow: "2–5 years"
  spacemetrics: "regional corridor"
  regions: ["Kii Peninsula", "coastal towns"]
  organizations: ["municipal governments", "local cooperatives"]
```

This allows AI and humans alike to:
- Understand scope without hardcoded levels
- Match or filter patterns by geography or time horizon
- Guide synthesis using meaningful dimensions

---

## URI & Access Model

Each IdeaMark carries:

```yaml
access:
  uri: https://github.com/org/ideamark/patterns/xyz.yaml
  visibility: public
```

This enables:
- Decentralized hosting
- Retrieval by AI agents
- Integration with GitHub, internal knowledge bases, or restricted datasets

---

## Reference Entries (`ref:`)

To support fast lookup, filtering, and LLM summarization, a parallel `.ref.yaml` structure is used:

- Contains `id`, `title`, `access`, and select `metadata`
- Lightweight representation for lists, indexes, or batch processing
- Ideal for merging, clustering, or prompting

---

## The Schema as a Social Contract

By standardizing *how* we describe patterns, the schema enables:
- Collective authorship
- AI-supported augmentation
- Cross-disciplinary reuse
- Generative design discourse

It is not simply for data storage — it is a grammar for collaborative intelligence.