# Usage Scenarios for IdeaMark

IdeaMark is designed to support a range of collaborative and computational tasks — especially those involving complex, cross-domain problem solving.  
Below are core scenarios where IdeaMark can be applied effectively.

---

## 1. 🧭 Pattern Discovery

**Who:** Researchers, designers, policymakers, strategists  
**What:** Search and browse existing patterns by tags, context, or region  
**How:**
- Use `metadata.tags`, `scalefactor`, or `context` fields
- Navigate `refs/` entries for lightweight scanning
- Filter by time horizon or geographic scope

---

## 2. 🔗 Composition and Hybridization

**Who:** Facilitators, AI agents, innovation teams  
**What:** Combine two or more patterns into a synthesized solution  
**How:**
- Compare `problem` and `solution.approach` fields
- Use tools in `/tools/merge/` to assist with structural composition
- Record `linked_patterns` in new entries to trace ancestry

---

## 3. 🤖 AI-Augmented Pattern Generation

**Who:** Prompt engineers, domain experts, AI copilots  
**What:** Use LLMs to generate new IdeaMark templates or complete partially drafted ones  
**How:**
- Start from a `ref:` or minimal stub
- Use `schema/ideamark.schema.yaml` to guide completion
- Feed existing patterns as examples for few-shot prompting

---

## 4. 🧠 Human–AI Collaborative Facilitation

**Who:** Design teams, urban planners, multi-stakeholder groups  
**What:** Use IdeaMark as a shared structure in dialog between humans and AIs  
**How:**
- Let participants submit partial patterns
- Use LLM to find overlaps, clusters, or conflicts
- Merge or recompose in shared discussion environments

---

## 5. 🗂 Strategic Mapping and Portfolio Design

**Who:** Policy labs, NGOs, innovation ecosystems  
**What:** Map a set of related patterns into a strategy or action portfolio  
**How:**
- Group by region, theme, or impact scope
- Visualize pattern graphs or heatmaps
- Tag gaps or redundancies in current knowledge

---

## 6. 📦 Export, Publish, and Integrate

**Who:** Knowledge managers, civic technologists  
**What:** Publish or embed IdeaMark patterns in other platforms  
**How:**
- Link from `access.uri` into GitHub, Notion, Web portals
- Convert to HTML, JSON-LD, or Markdown using scripts
- Include `version` and `visibility` metadata for traceability

---

## Flexibility & Future Directions

IdeaMark usage is expected to expand as tools evolve:
- UI editors
- LLM-based recommender agents
- Community-driven pattern curation
- Integration into civic data platforms

The schema is stable, but the applications are open-ended — and growing.