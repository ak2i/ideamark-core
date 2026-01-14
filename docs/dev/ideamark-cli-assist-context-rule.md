# ideamark-cli assist: context rule draft

This document defines draft rules for how assist commands interpret and use
context tags (`focus`, `phase`, `origin`) to guide flow control, question
prioritization, and slot completion in IdeaMark templates.

---

## Goals

- Make problem/solution orientation explicit and reusable
- Distinguish hypothesis/plan/outcome to avoid mixing intent and evidence
- Enable assist to ask fewer, higher-leverage questions
- Keep rules simple enough to run in CLI and in WebUI
- Support structural transforms for Breakdown and Convergent flows

---

## Functional Requirements: Breakdown / Convergent

assist must support two foundational operations, and the document structure
must allow a node.js script to process them deterministically.

### Breakdown

- Input: a single IdeaMark document
- Output: a set of derived IdeaMark fragments
- Requirement: Problem and Solution viewpoints are separable
- Requirement: Each fragment carries its own focus/phase/origin context

### Convergent

- Input: multiple IdeaMark documents
- Output: a synthesized IdeaMark document
- Requirement: Sources are traceable back to origin IdeaMark docs
- Requirement: Each merged slot retains focus/phase/origin context

---

## Structural Requirements for Processing

Documents must be representable in a way that supports both LLM reasoning and
deterministic node.js transforms.

### Required Separation

- Problem content and Solution content must be distinguishable
- The separation can be done by tags, slots, or explicit sections
- focus, phase, origin must be explicitly represented per unit of content

### Minimal Shape (Illustrative)

```yaml
idea:
  id: "..."
  problem:
    - text: "..."
      context: { focus: "problem", phase: "hypothesis", origin: "new" }
  solution:
    - text: "..."
      context: { focus: "solution", phase: "plan", origin: "new" }
  links:
    - from: "problem[0]"
      to: "solution[0]"
      relation: "addresses"
```

The natural language parts may still require LLMs for semantic parsing, but
the surrounding structure must be parseable, stable, and scriptable.

---

## Context Tags

Template slots may include the following optional tags:

```yaml
context:
  focus: "problem | solution | both"
  phase: "hypothesis | plan | outcome | other"
  origin: "new | observed | reused | retroactive"
```

### Semantics

- focus:
  - problem: statement about pain, constraint, gap, risk, or uncertainty
  - solution: statement about design choice, implementation, or action
  - both: inherently bridges problem and solution (e.g., decision tradeoff)
- phase:
  - hypothesis: unvalidated assumption or expectation
  - plan: intended action or proposed approach
  - outcome: observed result or measured fact
  - other: supporting info or context not fitting above
- origin:
  - new: created for the current work
  - observed: derived from existing data or external sources
  - reused: copied/adapted from prior IdeaMark docs
  - retroactive: written after the fact to backfill history

---

## Inference Rules (Draft)

assist should infer context tags if absent, and confirm them when ambiguous.

### Default Inference by Slot

- Intent
  - focus: problem
  - phase: hypothesis
  - origin: new
- Hypothesis
  - focus: solution
  - phase: hypothesis
  - origin: new
- DecisionOption
  - focus: both
  - phase: plan
  - origin: new
- Experiment
  - focus: solution
  - phase: plan
  - origin: new
- Metric
  - focus: problem
  - phase: plan
  - origin: observed
- DecisionLog
  - focus: both
  - phase: outcome
  - origin: retroactive

### Override Signals

If any of the following are present, prefer these tags and ask for confirmation:

- focus=problem:
  - keywords: issue, pain, bottleneck, risk, unknown, constraint, defect
- focus=solution:
  - keywords: implement, adopt, choose, build, deploy, architecture, algorithm
- phase=hypothesis:
  - modal verbs: might, could, expected, assume, likely, hypothesis
- phase=plan:
  - verbs: plan, propose, intend, design, schedule, execute
- phase=outcome:
  - evidential: measured, observed, resulted, achieved, failed, incident
- origin=reused:
  - references to other IdeaMark docs or "from previous"
- origin=retroactive:
  - phrases: after the fact, backfill, hindsight, postmortem

If the signals conflict, assist should label as both/other and ask a single
clarifying question rather than multiple.

---

## Assist Behavior Rules

### 1) Question Prioritization

Order of questions when data is missing:

1. focus
2. phase
3. origin
4. slot-specific required fields

When multiple slots are missing, prioritize those with focus=problem and
phase=hypothesis first.

### 2) Fill Strategy

- If focus=problem:
  - prefer constraints, impact, and evidence references
  - avoid proposing solutions unless asked
- If focus=solution:
  - require at least one decision_option or experiment link
  - request tradeoffs (pros/cons) and prerequisites
- If focus=both:
  - require explicit linkage to both a problem statement and a solution choice

### 3) Consistency Checks

assist should warn (not block) when:

- Intent is focus=solution but no problem statement exists
- DecisionLog is phase=hypothesis or plan
- Metric is phase=outcome but no collection method is defined
- Experiment has focus=problem with no solution element referenced

### 4) Retroactive Handling

When origin=retroactive:

- ask for evidence_refs or refs
- mark phase=outcome unless the user explicitly keeps hypothesis/plan

---

## CLI UX Guidelines

- In CLI, keep to one clarification question per slot by default
- Offer quick-pick answers (e.g., [problem/solution/both])
- Allow a `--assume` flag to accept inferred tags without questions
- Allow `--strict` to require explicit tags before writing

---

## WebUI Notes (Non-normative)

- Provide a single toggle for focus/phase/origin per slot
- Show inline explanations of how tags affect assist behavior
- Keep confirmations lightweight (single dialog or toast)

---

## Open Questions

- Should Metric default focus be problem or both?
- Should DecisionOption phase default be plan or hypothesis?
- Should Intent allow phase=outcome for postmortem docs?
