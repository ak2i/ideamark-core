# Template Sections Catalog

This document lists section headings found in the existing templates. It is
intended to help plan shared vocabulary, data structures, and namespaces without
imposing a centralized dictionary. Headings are copied as-is from templates.

---

## Software Development / WorkCell v1

Template: `templates/official/software-development/workcell-v1/WorkCell-Service-Flow.ideamark.template.md`
Sections:
- Template Scope
- Flow Definition (Required Sections)
- Meta
- Actors
- Goals
- Preconditions & Triggers
- Main Flow
- Alternative Flows
- Exception Flows
- State Model (Minimal)
- Observability Hooks
- References (to Detail Templates)
- Renderings (Optional)
- Rendering Meta (Optional)
- Mermaid Sequence Diagram (Optional)

Template: `templates/official/software-development/workcell-v1/WorkCell-Integration-Spec.ideamark.template.md`
Sections:
- Section 0: Provenance (source attribution) [Required]
- Section 1: Integration Goals (integration purpose) [Required]
- Section 2: Canonical Vocabulary (shared vocabulary) [Required]
- Section 2.1: Canonical IDs / Entities
- Section 2.2: Terminology Mapping (synonyms and aliases)
- Section 3: Event Catalog [Required]
- Section 4: State Integration [Required]
- Section 5: Conflict Register (conflict list) [Required]
- Section 5.1: Conflict Types (classification)
- Section 5.2: Conflicts
- Section 6: Resolution Decisions (decision rationale) [Required]
- Section 7: Detail Design Hand-off (rules shared with Detail) [Required]
- Section 8: Change Log (spec revision history) [Recommended]
- Renderings (Optional)

Template: `templates/official/software-development/workcell-v1/Detail-API.ideamark.template.md`
Sections:
- Section 0: Provenance (source attribution) [Required]
- Section 1: API Context (assumptions) [Required]
- Section 2: Canonical Resources (resources) [Required]
- Section 3: Commands (operations) [Required]
- Section 4: Read Models (read side) [Recommended]
- Section 5: State Transition Enforcement (enforcement of transitions) [Required]
- Section 6: Event Emission Contract (event contract) [Required]
- Section 7: Observability & Audit (monitoring and audit) [Required]
- Section 8: Error Model (error conventions) [Recommended]
- Section 9: References [Required]
- Renderings (Optional)

Template: `templates/official/software-development/workcell-v1/Decision6-WorkCell.ideamark.template.md`
Sections:
- Template Scope
- Node Types (Required)
- Intent
- Hypothesis
- DecisionOption
- Experiment
- Metric
- DecisionLog
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
