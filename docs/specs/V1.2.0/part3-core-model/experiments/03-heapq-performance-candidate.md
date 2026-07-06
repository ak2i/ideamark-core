# Heapq Performance Candidate IdeaMark Experiment

**Part:** 3 — Core Model  
**Status:** Design Experiment  
**Type:** Candidate IdeaMark-like Document / Structural Test

> Note: YAML fragments in this experiment are exploratory design artifacts. They predate the Part 4 array-based object representation and are not normative IdeaMark Core v1.2.0 examples. See Part 4 normalized samples for implementation-oriented YAML.

This document is a manual candidate IdeaMark-like structure generated from CPython `Lib/heapq.py` under a Performance Engineering Projection.

It is not intended to define final YAML syntax.

It is an experiment for evaluating whether the current structural assumptions of Part 3 are sufficient.

## 1. Experiment Setup

```yaml
meta:
  experiment_id: part3-heapq-performance-001
  status: exploratory
  original_sources:
    - id: SRC-heapq-py
      repository: python/cpython
      path: Lib/heapq.py
      ref: main
      source_type: public_source_code
  projections:
    - role: generation
      id: code-design-performance-heapq-v0
      purpose: extract implementation and performance reasoning from source code
      intended_activity:
        - explain why the implementation makes specific optimization choices
        - help engineers reuse the reasoning in other data-structure implementations
      audience:
        - software engineer
        - LLM code assistant
      focus:
        - heap invariant
        - comparison cost
        - implementation rationale
        - empirical comparison counts
      non_goals:
        - full code documentation
        - line-by-line explanation
        - proof of correctness
```

## 2. Candidate Structure

This candidate keeps the familiar Section / Occurrence / Entity pattern, but treats it only as a structural solution.

The experiment should test whether these names and layers are still useful or whether a different minimal structure should replace them.

```yaml
sections:
  SEC-001:
    title: Heap invariant as performance boundary
    anchor:
      source: SRC-heapq-py
      line_ranges:
        - start: 3
          end: 32
        - start: 41
          end: 76
      anchor_type: source_context
    occurrences:
      - OCC-001
      - OCC-002
      - OCC-003

  SEC-002:
    title: Comparison-cost-aware sift strategy
    anchor:
      source: SRC-heapq-py
      line_ranges:
        - start: 58
          end: 95
      anchor_type: implementation_rationale
    occurrences:
      - OCC-004
      - OCC-005
      - OCC-006

  SEC-003:
    title: Choosing heap operations for fixed-size workflows
    anchor:
      source: SRC-heapq-py
      line_ranges:
        - start: 150
          end: 171
      anchor_type: api_performance_choice
    occurrences:
      - OCC-007
      - OCC-008

  SEC-004:
    title: Heapify as bottom-up construction
    anchor:
      source: SRC-heapq-py
      line_ranges:
        - start: 173
          end: 182
      anchor_type: algorithm_construction
    occurrences:
      - OCC-009

entities:
  IE-001:
    kind: structural_principle
    content: |
      A heap is represented as an array constrained by an invariant that keeps the smallest item at index 0.
    source_role: invariant

  IE-002:
    kind: design_choice
    content: |
      CPython's heap API uses 0-based indexing and exposes a min-heap interface to behave naturally as a Python list.
    source_role: api_alignment

  IE-003:
    kind: algorithmic_operation
    content: |
      Removing the root is handled by moving a lower-level item into the root and percolating it down until the invariant is restored.
    source_role: invariant_restoration

  IE-004:
    kind: implementation_rationale
    content: |
      The implementation deliberately avoids an early break in _siftup because the moved item after a heap pop tends to be large, and early comparisons often do not pay off.
    source_role: optimization_rationale

  IE-005:
    kind: performance_factor
    content: |
      Comparison operations may be expensive because the priority may be hidden in custom comparison methods or tuple comparison.
    source_role: cost_model

  IE-006:
    kind: empirical_evidence
    content: |
      Commented comparison counts suggest that the selected sift strategy reduces comparisons substantially for exhaustive heappop operations on random arrays.
    source_role: empirical_support

  IE-007:
    kind: api_performance_choice
    content: |
      heapreplace is more efficient than heappop followed by heappush when maintaining a fixed-size heap, but its returned value may be larger than the inserted item.
    source_role: fixed_size_heap_choice

  IE-008:
    kind: api_performance_choice
    content: |
      heappushpop conditionally replaces the root only when the new item is larger than the current smallest item, avoiding unnecessary heap growth.
    source_role: combined_operation_choice

  IE-009:
    kind: construction_strategy
    content: |
      heapify builds a heap bottom-up from the last parent node, enabling in-place linear-time construction.
    source_role: bottom_up_heap_construction

occurrences:
  OCC-001:
    entity: IE-001
    role: establishes_performance_boundary
    rationale: |
      The heap invariant defines what must be preserved by every operation. Without this, the later optimization choices cannot be interpreted.

  OCC-002:
    entity: IE-002
    role: frames_api_design
    rationale: |
      The API design is not merely user-facing; it constrains how users can reason about heap behavior as a normal Python list.

  OCC-003:
    entity: IE-003
    role: explains_restoration_strategy
    rationale: |
      The pop operation shows the central repair pattern: replace root, then restore invariant through percolation.

  OCC-004:
    entity: IE-004
    role: explains_non_textbook_choice
    rationale: |
      This is a reusable performance-engineering lesson: do not assume a local early-exit optimization improves the real workload.

  OCC-005:
    entity: IE-005
    role: identifies_cost_driver
    rationale: |
      The cost model explains why comparison count matters beyond asymptotic complexity.

  OCC-006:
    entity: IE-006
    role: supports_design_choice
    rationale: |
      The empirical numbers support the selected implementation strategy and provide material for future engineering explanation.

  OCC-007:
    entity: IE-007
    role: maps_api_to_workload
    rationale: |
      The operation is meaningful when the workflow maintains a fixed heap size and accepts the documented constraint.

  OCC-008:
    entity: IE-008
    role: maps_api_to_workload
    rationale: |
      The combined operation captures a common top-k or threshold-style workflow where unnecessary push/pop work should be avoided.

  OCC-009:
    entity: IE-009
    role: describes_construction_optimization
    rationale: |
      Bottom-up heap construction gives a reusable implementation pattern distinct from repeated insertion.

structure:
  sections:
    - SEC-001
    - SEC-002
    - SEC-003
    - SEC-004
```

## 3. Reconstruction Test

Given the candidate structure above, a future LLM or human should be able to generate an activation expression such as:

> When implementing a mutable priority queue, first identify the invariant that must always hold. Then examine whether your repair path should optimize local exits or global comparison count. In CPython's heap implementation, avoiding an early break in `_siftup` reduces expensive comparisons during repeated pop workloads, because the replacement item tends to be large and custom comparisons may be costly.

This activation expression is not stored as the meaning of the IdeaMark document.

It is generated from the candidate structure, the Original Source, and the Performance Engineering Projection.

## 4. Constraint Review

### 4.1 Projection-guided generation

Satisfied.

The candidate is generated under a specific Performance Engineering Projection, not as general code documentation.

### 4.2 Separation from Original Source

Mostly satisfied.

The candidate does not copy the full source file, but it preserves source anchors through source IDs and line ranges.

### 4.3 No stored final meaning

Partially satisfied.

The `content` fields are still fairly explanatory and risk becoming mini-summaries.

This suggests that Part 3 must clarify how much explanatory payload is acceptable before the structure becomes a meaning store.

### 4.4 Reconstruction support

Satisfied.

The candidate gives enough material for a human or LLM to return to the source and generate an engineering explanation.

### 4.5 Traceability

Satisfied at Section level.

The candidate uses Section-level anchors and local rationale notes.

This supports the hypothesis that anchoring the local activity space may be more important than anchoring every Entity individually.

### 4.6 Minimal Core

Not yet satisfied.

The candidate still uses Section / Occurrence / Entity, and the amount of structure may be more than necessary.

The next evaluation should try a flatter alternative.

## 5. Model Feedback

### 5.1 Section appears useful

Section functions as a local activity space.

It groups source anchors and ordered occurrences into a unit that can be selected or reconstructed under a Projection.

This supports keeping something like Section, even if the name changes.

### 5.2 Occurrence is useful but may be too semantically loaded

Occurrence currently wraps an Entity with a role and rationale.

This is useful for reconstruction, but the name may imply source appearance or event occurrence more strongly than intended.

A more neutral term such as `use`, `placement`, `slot`, `activation_item`, or `frame_item` may be worth considering later.

### 5.3 Entity is useful as reusable payload but risks becoming a summary

Entity provides reusable payload, but the candidate shows a risk that Entity content becomes a compact explanation.

Part 3 should clarify whether Entity is allowed to contain explanatory text or should instead hold only minimal reusable material.

### 5.4 Relation is not needed in this experiment

No separate Relation object was needed.

Ordering, Section grouping, role, local rationale, and source anchors were sufficient for this Projection.

### 5.5 Perspective and Provenance are not needed as separate objects

Projection references and source references in `meta` were sufficient for this candidate.

Local rationale and generation notes can be attached where useful without creating separate Perspective or Provenance namespaces.

### 5.6 Anchorage may be Section-level

The candidate supports the user's intuition that anchorage-like information may belong primarily to Section-level structures.

A Section-level anchor can identify the Original Source context from which the local activity material was extracted.

The contained Occurrences and Entities may then be interpreted within that local source context.

## 6. Alternative Structure to Test Next

The next experiment should test whether the same material can be represented without Section / Occurrence / Entity names.

Possible neutral shape:

```yaml
activity_frames:
  - id: AF-001
    title: Comparison-cost-aware sift strategy
    source_anchor:
      source: SRC-heapq-py
      line_ranges:
        - { start: 58, end: 95 }
    items:
      - role: optimization_rationale
        payload: Avoid early break in _siftup because comparison savings differ by workload.
      - role: cost_driver
        payload: Comparisons may be expensive due to custom comparison methods or tuple priorities.
      - role: empirical_support
        payload: Commented comparison counts support the selected strategy.
```

This alternative may reveal whether Section / Occurrence / Entity are still helpful or whether the true minimal structure is closer to `activity_frame` plus ordered role-bearing items.

## 7. Next Step

Create a second candidate using the flatter `activity_frame` structure and compare it against the Section / Occurrence / Entity candidate.

Evaluate both against `01-ideamark-document-constraints.md`.
