# Template Sections Catalog

This document lists section headings found in the existing templates. It is
intended to help plan shared vocabulary, data structures, and namespaces without
imposing a centralized dictionary. Headings are copied as-is from templates.

Slot convention (workcell-v1):
- LLM-fill targets use headings that start with `Slot:`
- LLM extraction should only read the first YAML block after each `Slot:` heading
- `### Slot:` is used when a section needs further subdivision

---

## Software Development / WorkCell v1

Template: `templates/official/software-development/workcell-v1/WorkCell-Service-Flow.ideamark.template.md`
Sections:
- Template Scope
- Flow Definition (Required Sections)
- Slot: Meta
- Slot: Actors
- Slot: Goals
- Slot: Preconditions & Triggers
- Slot: Main Flow
- Slot: Alternative Flows
- Slot: Exception Flows
- Slot: State Model (Minimal)
- Slot: Observability Hooks
- Slot: References (to Detail Templates)
- Renderings (Optional)
- Rendering Meta (Optional)
- Mermaid Sequence Diagram (Optional)

Template: `templates/official/software-development/workcell-v1/WorkCell-Integration-Spec.ideamark.template.md`
Sections:
- Slot: Provenance (source attribution) [Required]
- Slot: Integration Goals (integration purpose) [Required]
- Section 2: Canonical Vocabulary (shared vocabulary) [Required]
- Slot: Canonical IDs / Entities
- Slot: Terminology Mapping (synonyms and aliases)
- Slot: Event Catalog [Required]
- Slot: State Integration [Required]
- Section 5: Conflict Register (conflict list) [Required]
- Slot: Conflicts
- Slot: Resolution Decisions (decision rationale) [Required]
- Slot: Detail Design Hand-off (rules shared with Detail) [Required]
- Slot: Change Log (spec revision history) [Recommended]
- Slot: Renderings (Optional)

Template: `templates/official/software-development/workcell-v1/Detail-API.ideamark.template.md`
Sections:
- Slot: Provenance (source attribution) [Required]
- Slot: API Context (assumptions) [Required]
- Slot: Canonical Resources (resources) [Required]
- Slot: Commands (operations) [Required]
- Slot: Read Models (read side) [Recommended]
- Slot: State Transition Enforcement (enforcement of transitions) [Required]
- Slot: Event Emission Contract (event contract) [Required]
- Slot: Observability & Audit (monitoring and audit) [Required]
- Slot: Error Model (error conventions) [Recommended]
- Slot: References [Required]
- Renderings (Optional)

Template: `templates/official/software-development/workcell-v1/Decision6-WorkCell.ideamark.template.md`
Sections:
- Template Scope
- Node Types (Required)
- Slot: Intent
- Slot: Hypothesis
- Slot: DecisionOption
- Slot: Experiment
- Slot: Metric
- Slot: DecisionLog
- Linking Rules
- Reference Usage
- Design Principle

---

## Regional Pattern Templates

Template: `templates/official/urban-planning/pattern-v1/Urban-Planning-Regional-Pattern.ideamark.template.md`
Sections:
- Template Scope
- Pattern Core (Required)
- Urban Assets & Functions
- Mobility & Logistics
- Stakeholders & Governance
- Impact & Metrics (Optional)

Template: `templates/official/civil-engineering/pattern-v1/Civil-Engineering-Regional-Pattern.ideamark.template.md`
Sections:
- Template Scope
- Pattern Core (Required)
- Infrastructure Assets
- Safety & Risk
- Operations & Maintenance
- Impact & Metrics (Optional)

Template: `templates/official/healthcare/pattern-v1/Healthcare-Regional-Pattern.ideamark.template.md`
Sections:
- Template Scope
- Pattern Core (Required)
- Range & Granularity
- References & Evidence
- Timeline & Dependencies
- Observed Metrics
- Patterns & Hypotheses

Template: `templates/official/forestry/pattern-v1/Forestry-Regional-Pattern.ideamark.template.md`
Sections:
- Template Scope
- Pattern Core (Required)
- Forest Assets & Ecology
- Carbon & Monitoring
- Governance & Revenue
- Impact & Metrics (Optional)

Template: `templates/official/fisheries/pattern-v1/Fisheries-Regional-Pattern.ideamark.template.md`
Sections:
- Template Scope
- Pattern Core (Required)
- Catch & Supply Profile
- Cold Chain & Distribution
- Stakeholders & Governance
- Impact & Metrics (Optional)

Template: `templates/official/tourism/pattern-v1/Tourism-Regional-Pattern.ideamark.template.md`
Sections:
- Template Scope
- Pattern Core (Required)
- Visitor & Demand Profile
- Assets & Capacity
- Operations & Governance
- Impact & Metrics (Optional)

Template: `templates/official/agriculture/pattern-v1/Agriculture-Regional-Pattern.ideamark.template.md`
Sections:
- Template Scope
- Pattern Core (Required)
- Agricultural Context
- Operations & Resources
- Stakeholders & Value Chain
- Impact & Metrics (Optional)
