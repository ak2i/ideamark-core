# Rust RFC Multi-Projection Candidate Test

**Part:** 3 — Core Model  
**Status:** Design Experiment  
**Type:** Multi-Projection Candidate IdeaMark-like Documents

This document generates two small candidate IdeaMark-like structures from Rust RFC 0001 `private-fields` under different generation Projections.

The purpose is to test whether a structured prose source still produces different Section / Occurrence / Entity structures depending on the Projection.

## 1. Original Source

```yaml
original_sources:
  - id: SRC-rust-rfc-0001-private-fields
    repository: rust-lang/rfcs
    path: text/0001-private-fields.md
    ref: master
    source_type: public_design_rfc
```

The RFC proposes making all Rust struct fields private by default.

It includes motivation, detailed design, syntax changes, statistics, alternatives, and unresolved questions.

## 2. Candidate A — Language Design Rationale Projection

```yaml
meta:
  experiment_id: rust-rfc-language-design-rationale-candidate-001
  status: exploratory
  projections:
    - role: generation
      id: rust-rfc-language-design-rationale-v0
      purpose: extract reusable reasoning about language feature defaults
      focus:
        - default visibility
        - soundness
        - abstraction boundary
        - API surface
        - consistency with language rules
```

### 2.1 Candidate Structure

```yaml
sections:
  SEC-RAT-001:
    title: Private-by-default as soundness support
    anchor:
      source: SRC-rust-rfc-0001-private-fields
      line_ranges:
        - start: 14
          end: 20
      anchor_type: design_motivation
    occurrences:
      - OCC-RAT-001

  SEC-RAT-002:
    title: Tuple struct privacy as abstraction boundary
    anchor:
      source: SRC-rust-rfc-0001-private-fields
      line_ranges:
        - start: 21
          end: 24
        - start: 80
          end: 116
      anchor_type: abstraction_boundary
    occurrences:
      - OCC-RAT-002
      - OCC-RAT-003

  SEC-RAT-003:
    title: API surface should be opt-in
    anchor:
      source: SRC-rust-rfc-0001-private-fields
      line_ranges:
        - start: 30
          end: 35
      anchor_type: api_surface_reasoning
    occurrences:
      - OCC-RAT-004

  SEC-RAT-004:
    title: Privacy consistency across language constructs
    anchor:
      source: SRC-rust-rfc-0001-private-fields
      line_ranges:
        - start: 25
          end: 29
      anchor_type: consistency_reasoning
    occurrences:
      - OCC-RAT-005

  SEC-RAT-005:
    title: Counterweight from inherited visibility
    anchor:
      source: SRC-rust-rfc-0001-private-fields
      line_ranges:
        - start: 36
          end: 42
      anchor_type: tradeoff_context
    occurrences:
      - OCC-RAT-006

entities:
  IE-RAT-001:
    kind: design_rationale
    content: |
      Visibility helps achieve soundness for types that wrap unsafe or implementation-specific behavior.
    source_role: soundness_rationale

  IE-RAT-002:
    kind: abstraction_boundary
    content: |
      Public tuple struct fields reduce the ability to create abstraction barriers because tuple structs can be destructured.
    source_role: abstraction_rationale

  IE-RAT-003:
    kind: behavior_rule
    content: |
      Private tuple fields prevent external pattern binding and construction by specifying private fields.
    source_role: privacy_behavior

  IE-RAT-004:
    kind: api_surface_rule
    content: |
      Public fields are part of a type's API, so fields should opt in to public exposure with pub.
    source_role: api_surface_control

  IE-RAT-005:
    kind: consistency_rationale
    content: |
      Private-by-default field visibility aligns struct fields with most other Rust privacy behavior.
    source_role: language_consistency

  IE-RAT-006:
    kind: design_tradeoff
    content: |
      Inherited visibility keeps public struct definitions concise and easy to read.
    source_role: alternative_rationale

occurrences:
  OCC-RAT-001:
    entity: IE-RAT-001
    role: supports_default_private_policy
    rationale: |
      Soundness is used as a reason to require explicit public exposure.

  OCC-RAT-002:
    entity: IE-RAT-002
    role: identifies_abstraction_problem
    rationale: |
      Tuple structs expose a specific abstraction problem that motivates the change.

  OCC-RAT-003:
    entity: IE-RAT-003
    role: connects_design_to_behavior
    rationale: |
      The detailed behavior shows how the rationale becomes enforceable language semantics.

  OCC-RAT-004:
    entity: IE-RAT-004
    role: frames_api_design_principle
    rationale: |
      The RFC treats public fields as explicit API commitments.

  OCC-RAT-005:
    entity: IE-RAT-005
    role: supports_language_consistency
    rationale: |
      Consistency reduces the conceptual exception represented by current struct fields.

  OCC-RAT-006:
    entity: IE-RAT-006
    role: preserves_counterargument
    rationale: |
      The Projection includes the opposing rationale to preserve design tradeoff structure.

structure:
  sections:
    - SEC-RAT-001
    - SEC-RAT-002
    - SEC-RAT-003
    - SEC-RAT-004
    - SEC-RAT-005
```

### 2.2 Possible Activation Expression

> The RFC can be read as a language-design argument about defaults. Its core claim is that field visibility should default to privacy because public fields are API commitments, visibility can protect soundness and abstraction barriers, and private-by-default better matches Rust's broader privacy model. The argument also preserves a counterweight: inherited visibility is concise for public structs, so the design must justify trading convenience for explicit API exposure.

## 3. Candidate B — Migration Impact Projection

```yaml
meta:
  experiment_id: rust-rfc-migration-impact-candidate-001
  status: exploratory
  projections:
    - role: generation
      id: rust-rfc-migration-impact-v0
      purpose: extract implementation and migration consequences of a language change
      focus:
        - rejected current examples
        - pub field annotations
        - priv keyword removal
        - tuple struct grammar
        - repository statistics
```

### 3.1 Candidate Structure

```yaml
sections:
  SEC-MIG-001:
    title: Current accepted code that becomes rejected
    anchor:
      source: SRC-rust-rfc-0001-private-fields
      line_ranges:
        - start: 43
          end: 68
      anchor_type: breaking_change_example
    occurrences:
      - OCC-MIG-001

  SEC-MIG-002:
    title: Public field annotations as migration mechanism
    anchor:
      source: SRC-rust-rfc-0001-private-fields
      line_ranges:
        - start: 69
          end: 79
      anchor_type: migration_mechanism
    occurrences:
      - OCC-MIG-002
      - OCC-MIG-003

  SEC-MIG-003:
    title: Tuple struct grammar and examples
    anchor:
      source: SRC-rust-rfc-0001-private-fields
      line_ranges:
        - start: 80
          end: 107
      anchor_type: syntax_change
    occurrences:
      - OCC-MIG-004
      - OCC-MIG-005

  SEC-MIG-004:
    title: Repository statistics as impact estimate
    anchor:
      source: SRC-rust-rfc-0001-private-fields
      line_ranges:
        - start: 118
          end: 144
      anchor_type: empirical_impact_estimate
    occurrences:
      - OCC-MIG-006
      - OCC-MIG-007

  SEC-MIG-005:
    title: Remaining migration question
    anchor:
      source: SRC-rust-rfc-0001-private-fields
      line_ranges:
        - start: 157
          end: 167
      anchor_type: unresolved_migration_question
    occurrences:
      - OCC-MIG-008

entities:
  IE-MIG-001:
    kind: breaking_change_example
    content: |
      Code that constructs tuple structs or structural structs through fields outside the defining module may be rejected after the change.
    source_role: rejected_current_behavior

  IE-MIG-002:
    kind: migration_mechanism
    content: |
      Public structural fields remain possible through explicit pub field qualifiers.
    source_role: explicit_public_annotation

  IE-MIG-003:
    kind: removed_syntax
    content: |
      The priv visibility modifier is no longer allowed on struct fields.
    source_role: syntax_removal

  IE-MIG-004:
    kind: syntax_change
    content: |
      Tuple struct grammar is changed so each field may include an optional visibility qualifier.
    source_role: grammar_update

  IE-MIG-005:
    kind: behavior_change
    content: |
      Private tuple fields prevent external construction, destructuring, and pattern binding.
    source_role: tuple_privacy_effect

  IE-MIG-006:
    kind: impact_evidence
    content: |
      Repository statistics compare inherited visibility with private-by-default visibility for field counts and struct patterns.
    source_role: statistics_basis

  IE-MIG-007:
    kind: impact_claim
    content: |
      The RFC argues that pub annotations would be needed less often than priv annotations under the previous approach.
    source_role: migration_cost_argument

  IE-MIG-008:
    kind: unresolved_question
    content: |
      It remains open whether syntax for an all-public struct is necessary.
    source_role: future_compatibility_question

occurrences:
  OCC-MIG-001:
    entity: IE-MIG-001
    role: identifies_breaking_behavior
    rationale: |
      Migration analysis begins by identifying accepted code that changes behavior.

  OCC-MIG-002:
    entity: IE-MIG-002
    role: provides_migration_path
    rationale: |
      Explicit pub annotations are the primary migration mechanism for public fields.

  OCC-MIG-003:
    entity: IE-MIG-003
    role: identifies_removed_construct
    rationale: |
      Removing priv changes how existing code expresses privacy.

  OCC-MIG-004:
    entity: IE-MIG-004
    role: records_grammar_change
    rationale: |
      Tuple struct grammar must be updated to support explicit visibility.

  OCC-MIG-005:
    entity: IE-MIG-005
    role: states_behavioral_consequence
    rationale: |
      Migration impact includes not only syntax but external construction and matching behavior.

  OCC-MIG-006:
    entity: IE-MIG-006
    role: provides_impact_basis
    rationale: |
      Statistics provide the quantitative basis for estimating migration cost.

  OCC-MIG-007:
    entity: IE-MIG-007
    role: interprets_statistics_for_migration
    rationale: |
      The RFC uses statistics to argue that the new annotation burden is acceptable.

  OCC-MIG-008:
    entity: IE-MIG-008
    role: marks_unresolved_followup
    rationale: |
      The all-public struct syntax question affects future migration ergonomics.

structure:
  sections:
    - SEC-MIG-001
    - SEC-MIG-002
    - SEC-MIG-003
    - SEC-MIG-004
    - SEC-MIG-005
```

### 3.2 Possible Activation Expression

> Under a migration-impact Projection, the same RFC becomes a map of code changes. The key issue is that currently accepted construction of tuple and structural structs outside the defining module may become rejected unless fields are explicitly marked public. The migration path is to add `pub` to fields that are part of the public API, remove reliance on `priv` field syntax, and account for tuple struct grammar changes. The RFC supports the burden estimate with repository statistics, while leaving open whether all-public struct syntax is needed.

## 4. Comparison Between Candidate A and Candidate B

| Aspect | Language Design Rationale Projection | Migration Impact Projection |
|---|---|---|
| Primary source regions | motivation and rationale, selected behavior details | detailed design, examples, statistics, unresolved question |
| Section shape | rationale and tradeoff windows | migration and impact windows |
| Entity kinds | design rationale, abstraction boundary, API surface rule | breaking change, migration mechanism, syntax change, impact evidence |
| Occurrence roles | supports policy, frames principle, preserves counterargument | identifies behavior, provides path, records grammar, estimates impact |
| Activation expression | design memo / language policy argument | migration guide / compatibility review |
| Treatment of statistics | mostly omitted or secondary | central impact evidence |
| Treatment of unresolved question | mostly omitted | follow-up migration ergonomics issue |

## 5. Part 3 Finding

The RFC test shows that Projection-shaped generation is not merely source-outline reproduction.

Even though the RFC already has explicit headings, the two candidates reorganize the source differently.

The Language Design Rationale Projection collects material around why the default should change.

The Migration Impact Projection collects material around what code and syntax must change.

This supports the claim that Section is not a source heading.

It is a Projection-shaped local source window.

## 6. Cross-Source Comparison

Across `heapq.py`, SQLite `pager.c`, and Rust RFC 0001, the same pattern appears:

```text
Original Source + Projection
  -> different local source windows
  -> different role placements
  -> different reusable materials
  -> different future activation expressions
```

The source type changes, but the structural pattern remains useful.

## 7. Feedback for Part 3

The RFC test strengthens the case for retaining Section / Occurrence / Entity if they are defined functionally rather than semantically:

```text
Section
  = Projection-shaped local source window

Occurrence
  = role-bearing placement of reusable material within that window

Entity
  = reusable material shaped by Projection and available for later reconstruction
```

The test also suggests that Part 3 should explicitly warn against treating source headings as Sections by default.

Source headings may provide anchors, but Section boundaries are determined by Projection-guided Decomposition.
