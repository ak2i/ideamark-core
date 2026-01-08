# Usage Scenarios for IdeaMark

IdeaMark is designed to support a range of collaborative and computational tasks — especially those involving complex, cross-domain problem solving.  
This document positions those scenarios in terms of the data IdeaMark describes, how it is used, and the mechanisms required to make that use practical.

---

## 1. Pattern Discovery

**Who:** Researchers, designers, policymakers, strategists  
**What:** Search and browse existing patterns by tags, context, or region  
**How:**
- Index patterns by `metadata.tags`, `scalefactor`, and `context`
- Surface `refs/` entries for lightweight scanning and comparison
- Filter by time horizon, geographic scope, or organizational scale

---

## 2. Composition and Hybridization

**Who:** Facilitators, AI agents, innovation teams  
**What:** Combine two or more patterns into a synthesized solution  
**How:**
- Compare `problem` and `solution` sections explicitly, keeping them separable
- Record `linked_patterns` to trace ancestry and alternative paths
- Retain assumptions and conditions to preserve design intent across contexts

---

## 3. AI-Augmented Pattern Generation

**Who:** Prompt engineers, domain experts, AI copilots  
**What:** Use AI systems to draft new IdeaMark entries or complete partial ones  
**How:**
- Start from a minimal stub that captures `context`, `problem`, and `solution`
- Use the schema to validate structure and ensure machine legibility
- Provide existing patterns as examples to preserve continuity of language

---

## 4. Human–AI Collaborative Facilitation

**Who:** Design teams, urban planners, multi-stakeholder groups  
**What:** Use IdeaMark as a shared structure in dialog between humans and AIs  
**How:**
- Let participants submit partial patterns with explicit uncertainty or gaps
- Use AI to surface overlaps, clusters, and conflicts between patterns
- Recompose or revise patterns while preserving rationale and dissent

---

## 5. Strategic Mapping and Portfolio Design

**Who:** Policy labs, NGOs, innovation ecosystems  
**What:** Map a set of related patterns into a strategy or action portfolio  
**How:**
- Group by region, theme, or impact scope
- Visualize pattern graphs or heatmaps to reveal dependency structures
- Tag gaps, redundancies, and tensions in current knowledge

---

## 6. Export, Publish, and Integrate

**Who:** Knowledge managers, civic technologists  
**What:** Publish or embed IdeaMark patterns in other platforms  
**How:**
- Link patterns via `access.uri` for traceable reuse
- Export to HTML, JSON-LD, or Markdown for integration
- Include `version` and `visibility` metadata to preserve lineage

---

## 7. Conflict and Tradeoff Navigation

**Who:** Planners, mediators, AI agents  
**What:** Identify and reason about conflicts between patterns  
**How:**
- Capture incompatibilities as explicit links via `relations`, `linked_patterns`, and `design.applicability.tradeoffs`
- Preserve competing solutions as parallel entries via `relations.siblings` and `relations.derived_from`
- Record tradeoff signals in `hypotheses`, `patterns`, and `evidence` for inspection over time

---

## 8. Learning from Failure and Revision

**Who:** Field operators, researchers, auditors  
**What:** Preserve unsuccessful attempts as reusable design memory  
**How:**
- Record failures with `hypotheses`, `observed_metrics`, and `patterns` to capture what broke
- Preserve conditions with `context`, `metadata.scalefactor`, `range`, and `dependencies`
- Link to revisions via `relations.derived_from` and `linked_patterns`, citing `evidence` and `reference`

---

## Flexibility & Future Directions

IdeaMark usage is expected to expand as tools evolve:
- UI editors
- Pattern graph exploration and analytics
- LLM-based recommender agents
- Community-driven pattern curation
- Integration into civic data platforms

The schema is stable, but the applications are open-ended — and growing.  
This keeps the core expressive space intact while allowing multiple methodologies to coexist.
