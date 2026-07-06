# Rust RFC Original Source Test

**Part:** 3 — Core Model  
**Status:** Design Experiment  
**Type:** Third Original Source / Non-Code Proposal Document Test

This document proposes the third Original Source test for Part 3: Rust RFC 0001, `private-fields`.

The purpose is to check whether the Section / Occurrence / Entity interpretation works for a proposal document rather than source code.

This test is useful because an RFC already contains structured reasoning: summary, motivation, detailed design, statistics, alternatives, and unresolved questions.

The question is whether IdeaMark generation under different Projections produces different access structures even when the source itself is already well structured.

## 1. Candidate Original Source

```yaml
original_source:
  id: SRC-rust-rfc-0001-private-fields
  repository: rust-lang/rfcs
  path: text/0001-private-fields.md
  ref: master
  source_type: public_design_rfc
```

## 2. Initial Source Observations

The RFC proposes making all Rust struct fields private by default.

Its motivation includes soundness, abstraction barriers, consistency with the rest of the language, and API surface control.

The detailed design explains current privacy behavior, the proposed private-by-default behavior, syntax for public fields, tuple struct grammar changes, and behavior of private tuple fields.

The RFC also includes statistics gathered from the Rust repository, alternatives, and unresolved questions.

## 3. Why This Source Is Useful

Unlike source code, this RFC already explicitly separates:

- summary;
- motivation;
- detailed design;
- evidence/statistics;
- alternatives;
- unresolved questions.

This makes it a good test of whether IdeaMark simply reproduces source headings or creates Projection-shaped local source windows.

A good IdeaMark generation should not merely copy the RFC outline.

It should reorganize the source according to the Projection.

## 4. Candidate Generation Projections

### 4.1 Language Design Rationale Projection

```yaml
projection:
  id: rust-rfc-language-design-rationale-v0
  purpose: extract reusable reasoning about language feature defaults
  intended_activity:
    - explain why private-by-default is preferred
    - compare opt-in and opt-out API exposure
    - support future language design decisions
  focus:
    - default visibility
    - soundness
    - abstraction boundary
    - API surface
    - consistency with language rules
  non_goals:
    - complete syntax grammar
    - implementation tracking
    - historical RFC process analysis
```

Expected Sections:

```yaml
sections:
  - title: Default visibility as soundness support
  - title: Abstraction barriers for tuple structs
  - title: API surface as opt-in exposure
  - title: Consistency with existing privacy rules
  - title: Tradeoff against inherited visibility
```

Expected Entities:

```yaml
entities:
  - kind: design_rationale
    material: visibility helps achieve soundness for wrapper types
  - kind: abstraction_boundary
    material: public tuple fields prevent abstraction barriers
  - kind: api_surface_rule
    material: public fields become part of the API by default
  - kind: design_tradeoff
    material: public definitions are concise under inherited visibility
```

### 4.2 Migration Impact Projection

```yaml
projection:
  id: rust-rfc-migration-impact-v0
  purpose: extract implementation and migration consequences of a language change
  intended_activity:
    - estimate code impact
    - identify required syntax changes
    - explain compatibility risks
  focus:
    - rejected current examples
    - pub field annotations
    - priv keyword removal
    - tuple struct grammar
    - repository statistics
  non_goals:
    - philosophical language design argument
    - tutorial explanation for beginners
```

Expected Sections:

```yaml
sections:
  - title: Existing accepted code that becomes rejected
  - title: Public field annotations as migration mechanism
  - title: Removing priv from field syntax
  - title: Tuple struct grammar changes
  - title: Repository statistics as migration estimate
```

Expected Entities:

```yaml
entities:
  - kind: breaking_change_example
    material: construction of tuple and structural structs outside defining module becomes rejected
  - kind: migration_mechanism
    material: add pub qualifier to expose fields
  - kind: syntax_change
    material: tuple struct fields accept visibility qualifiers
  - kind: impact_evidence
    material: statistics estimate changes in public and private field annotations
```

### 4.3 Evidence and Empirical Support Projection

```yaml
projection:
  id: rust-rfc-evidence-support-v0
  purpose: extract empirical and argumentative support for a proposal
  intended_activity:
    - evaluate whether evidence supports the design
    - identify what evidence is missing or limited
    - compare evidence to claims
  focus:
    - statistics gathered
    - representativeness caveat
    - claims supported by counts
    - claims not directly supported by counts
  non_goals:
    - syntax design details
    - tutorial output
```

Expected Sections:

```yaml
sections:
  - title: Repository survey as evidence source
  - title: Public and private field count comparison
  - title: All-private and all-public structure patterns
  - title: Evidence limitations
  - title: Evidence-to-design connection
```

Expected Entities:

```yaml
entities:
  - kind: empirical_evidence
    material: survey counts private and public fields in mozilla/rust
  - kind: evidence_limitation
    material: repository is not representative of all projects
  - kind: supported_claim
    material: predominant pattern is all-private structs
  - kind: evidence_to_policy_link
    material: pub annotations may be fewer than priv annotations under the proposal
```

### 4.4 Teaching Projection

```yaml
projection:
  id: rust-rfc-teaching-privacy-v0
  purpose: teach Rust field privacy and the proposed private-by-default change
  intended_activity:
    - explain current and proposed visibility rules
    - generate examples
    - clarify tuple struct behavior
  focus:
    - current rules
    - proposed rules
    - struct examples
    - tuple struct examples
    - private field behavior
  non_goals:
    - policy advocacy
    - empirical evidence review
```

Expected Sections:

```yaml
sections:
  - title: Current field privacy rules
  - title: Proposed private-by-default rule
  - title: Structural struct examples
  - title: Tuple struct examples with pub fields
  - title: What private tuple fields prevent
```

Expected Entities:

```yaml
entities:
  - kind: teaching_concept
    material: tuple structs currently have public fields by default
  - kind: teaching_concept
    material: structural struct fields inherit enclosing struct privacy today
  - kind: example
    material: struct Bar(pub u64) exposes a tuple field
  - kind: behavior_rule
    material: private tuple fields cannot be matched or constructed outside the defining module
```

### 4.5 RFC Process / Decision Package Projection

```yaml
projection:
  id: rust-rfc-decision-package-v0
  purpose: reconstruct the RFC as a decision package
  intended_activity:
    - summarize decision inputs
    - identify proposed change, rationale, evidence, alternatives, and open questions
    - support governance review
  focus:
    - proposal summary
    - motivation
    - detailed design
    - alternatives
    - unresolved questions
  non_goals:
    - code migration walkthrough
    - language tutorial
```

Expected Sections:

```yaml
sections:
  - title: Proposed decision
  - title: Motivation and design rationale
  - title: Detailed design commitments
  - title: Evidence and impact estimate
  - title: Alternatives and unresolved questions
```

Expected Entities:

```yaml
entities:
  - kind: decision
    material: make struct fields private by default
  - kind: rationale
    material: reduce accidental API exposure and preserve abstraction barriers
  - kind: design_commitment
    material: public fields require pub annotations
  - kind: alternative
    material: retain inherited visibility
  - kind: unresolved_question
    material: whether all-public struct syntax is necessary
```

## 5. Expected Multi-Projection Differences

| Projection | Likely Section Shape | Entity Shape | Future Activity |
|---|---|---|---|
| Language Design Rationale | rationale windows | design rationale, tradeoff, rule consistency | design memo, language design comparison |
| Migration Impact | change-impact windows | breaking change, syntax change, migration mechanism | migration guide, compatibility review |
| Evidence Support | evidence windows | empirical evidence, limitation, supported claim | evidence critique, policy justification |
| Teaching | tutorial windows | concept, example, behavior rule | lesson, examples, learner explanation |
| Decision Package | governance windows | decision, rationale, alternative, unresolved question | review brief, decision record |

## 6. Design Hypothesis

The RFC source will likely preserve Section / Occurrence / Entity usefulness, but it will challenge the model differently from source code.

Because the source already has headings, IdeaMark generation must avoid merely copying them.

Instead, it should create Projection-shaped local source windows.

For example:

```text
RFC Motivation section
  can become rationale windows under Language Design Projection
  can become risk and impact windows under Migration Impact Projection
  can become argument-support windows under Evidence Projection
```

## 7. Expected Feedback for Part 3

This test should help answer:

1. Whether Section is still useful when Original Source already has explicit sections.
2. Whether Occurrence roles can express proposal reasoning such as motivation, alternative, evidence, and unresolved issue.
3. Whether Entity payload should preserve proposal material without becoming a full summary.
4. Whether source anchors should point to RFC headings, line ranges, paragraphs, examples, or tables.
5. Whether different generation Projections produce genuinely different IdeaMark Documents over a structured prose source.

## 8. Next Step

Generate one candidate IdeaMark-like structure under the Language Design Rationale Projection.

Then generate another candidate under the Migration Impact Projection.

Compare whether the Section / Occurrence / Entity structures differ in source focus, role assignment, and reusable materials.
