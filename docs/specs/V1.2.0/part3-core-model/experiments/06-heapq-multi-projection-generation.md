# Heapq Multi-Projection Generation Test

**Part:** 3 — Core Model  
**Status:** Design Experiment  
**Type:** Multi-Projection Generation / Structural Comparison

This document tests whether different generation Projections applied to the same Original Source produce meaningfully different IdeaMark-like structures.

The Original Source is CPython `Lib/heapq.py`.

The experiment complements `04-heapq-cross-projection-reconstruction.md`, which tested reconstruction under different Projections after generating a candidate under only one Projection.

## 1. Experiment Question

The central question is:

> If the same Original Source is decomposed under different Projections, does the resulting IdeaMark Document change in ways that support different future Human-AI Intellectual Activities?

This is important because Part 3 assumes that IdeaMark generation is Projection-guided, not general extraction.

If different Projections produce nearly identical IdeaMark structures, then Projection may not be doing enough work.

If different Projections produce different local Sections, Occurrence roles, Entity payloads, and source anchors, then the Section / Occurrence / Entity structure is likely capturing Projection-shaped access.

## 2. Original Source

```yaml
original_source:
  id: SRC-heapq-py
  repository: python/cpython
  path: Lib/heapq.py
  ref: main
  source_type: public_source_code
```

## 3. Projection A — Performance Engineering

This is the candidate already created in `03-heapq-performance-candidate.md`.

### 3.1 Expected Sections

```yaml
sections:
  - id: SEC-PERF-001
    title: Heap invariant as performance boundary
    source_focus: heap invariant and root property
  - id: SEC-PERF-002
    title: Comparison-cost-aware sift strategy
    source_focus: _siftup comments and comparison-count rationale
  - id: SEC-PERF-003
    title: Choosing heap operations for fixed-size workflows
    source_focus: heapreplace and heappushpop performance behavior
  - id: SEC-PERF-004
    title: Heapify as bottom-up construction
    source_focus: linear-time bottom-up heap construction
```

### 3.2 Typical Entities

```yaml
entities:
  - kind: structural_principle
    material: heap invariant preserves smallest item at index 0
  - kind: implementation_rationale
    material: avoid early break in _siftup under repeated pop workloads
  - kind: performance_factor
    material: comparisons may be expensive
  - kind: empirical_evidence
    material: comparison-count examples support the implementation choice
```

### 3.3 Likely Activation Expression

Performance note, optimization rationale, code review explanation, or engineering design memo.

## 4. Projection B — Algorithm Learning

```yaml
projection:
  id: code-algorithm-learning-heapq-v0
  purpose: teach heap algorithms to learners
  focus:
    - heap invariant
    - array-to-tree mapping
    - push and pop behavior
    - heapify construction
    - complexity intuition
```

### 4.1 Expected Sections

```yaml
sections:
  - id: SEC-LEARN-001
    title: Heap as an array-shaped binary tree
    source_focus: invariant, child index formulas, tournament diagram
  - id: SEC-LEARN-002
    title: Push and pop as invariant-preserving operations
    source_focus: heappush, heappop, _siftdown, _siftup
  - id: SEC-LEARN-003
    title: Heapify as bottom-up construction
    source_focus: heapify loop and last-parent explanation
  - id: SEC-LEARN-004
    title: Complexity intuition
    source_focus: logarithmic percolation and linear heapify
```

### 4.2 Typical Entities

```yaml
entities:
  - kind: teaching_concept
    material: array index k has children 2*k+1 and 2*k+2
  - kind: teaching_concept
    material: root contains the smallest item
  - kind: operation_walkthrough
    material: pop replaces root then restores invariant
  - kind: exercise_seed
    material: trace heapify from the last parent node
```

### 4.3 Difference from Performance Engineering

The learner Projection expands source regions that were secondary in the performance candidate.

It would likely preserve the tree diagram and child-index explanation, which the performance candidate mostly omitted.

The same Original Source therefore yields a different Section set and different Entity kinds.

## 5. Projection C — API Design

```yaml
projection:
  id: code-api-design-heapq-v0
  purpose: reconstruct API design reasoning from source code
  focus:
    - API shape
    - user expectations
    - operation naming
    - fixed-size workflow support
    - compatibility with host language idioms
```

### 5.1 Expected Sections

```yaml
sections:
  - id: SEC-API-001
    title: Python-list-compatible heap API
    source_focus: 0-based indexing, min-heap orientation, heap[0]
  - id: SEC-API-002
    title: Operation vocabulary for common heap workflows
    source_focus: heappush, heappop, heapreplace, heappushpop
  - id: SEC-API-003
    title: Fixed-size heap operations and user constraints
    source_focus: heapreplace and heappushpop documentation
  - id: SEC-API-004
    title: Max-heap variants as API symmetry
    source_focus: heappush_max, heappop_max, heapify_max, replace variants
```

### 5.2 Typical Entities

```yaml
entities:
  - kind: api_design_choice
    material: min-heap API keeps heap[0] as smallest item
  - kind: api_design_choice
    material: 0-based indexing aligns with Python list conventions
  - kind: workload_api_mapping
    material: heapreplace supports fixed-size heap replacement with constraints
  - kind: api_symmetry
    material: max-heap variants mirror min-heap operations
```

### 5.3 Difference from Performance Engineering

The API Projection gives more weight to naming, user expectation, and workflow fit.

It may use the same source fragments as the performance Projection, but Occurrence roles change.

For example, `heapreplace` is not merely a performance optimization; it becomes a user-facing API contract.

## 6. Projection D — Data Processing / Stream Merge

```yaml
projection:
  id: code-data-pipeline-stream-merge-v0
  purpose: reuse source code as a data processing design pattern
  focus:
    - sorted input streams
    - generator-based output
    - bounded memory
    - key functions
    - reverse ordering
```

### 6.1 Expected Sections

```yaml
sections:
  - id: SEC-MERGE-001
    title: Lazy merge of sorted streams
    source_focus: merge function docstring and generator behavior
  - id: SEC-MERGE-002
    title: Heap frontier over multiple iterables
    source_focus: heap state inside merge
  - id: SEC-MERGE-003
    title: Ordering customizations
    source_focus: key parameter and reverse parameter
  - id: SEC-MERGE-004
    title: Memory behavior versus materialized sorting
    source_focus: sorted(chain(...)) comparison in docstring
```

### 6.2 Typical Entities

```yaml
entities:
  - kind: data_processing_pattern
    material: merge sorted inputs without pulling all data into memory
  - kind: stream_processing_assumption
    material: each input stream is already sorted
  - kind: ordering_strategy
    material: key function determines ordering
  - kind: implementation_pattern
    material: heap stores the current frontier of each stream
```

### 6.3 Difference from Performance Engineering

This Projection would generate almost no overlap with the existing performance candidate.

It focuses on the `merge` function and data pipeline behavior, which the performance candidate did not preserve.

This is strong evidence that generation Projection changes the produced IdeaMark Document.

## 7. Projection E — Domain Adaptation / Scheduler Design

```yaml
projection:
  id: code-domain-adaptation-scheduler-v0
  purpose: transfer heap-based reasoning to event scheduler design
  focus:
    - event time as priority
    - future event insertion
    - stability of worst-case behavior
    - simulation use cases
```

### 7.1 Expected Sections

```yaml
sections:
  - id: SEC-SCHED-001
    title: Heap as tournament over future events
    source_focus: tournament metaphor and winner-at-root property
  - id: SEC-SCHED-002
    title: Event time as priority
    source_focus: scheduler commentary and smallest scheduled time
  - id: SEC-SCHED-003
    title: Future event insertion during simulation
    source_focus: events schedule other events into the future
  - id: SEC-SCHED-004
    title: Worst-case stability as scheduler design criterion
    source_focus: average and worst-case behavior discussion
```

### 7.2 Typical Entities

```yaml
entities:
  - kind: transfer_pattern
    material: heap root corresponds to next scheduled event
  - kind: domain_mapping
    material: win condition maps to smallest scheduled time
  - kind: dynamic_workload_condition
    material: processed events may schedule future events
  - kind: design_tradeoff
    material: stable worst-case behavior may matter more than better average case
```

### 7.3 Difference from Performance Engineering

This Projection treats explanatory prose as transfer material rather than as algorithm documentation.

Sections are organized around domain mapping, not implementation details.

## 8. Comparison Matrix

| Generation Projection | Primary Source Regions | Section Shape | Entity Shape | Likely Future Activity |
|---|---|---|---|---|
| Performance Engineering | invariant, _siftup comments, comparison table, heapify | optimization windows | rationale, cost factor, evidence | optimization memo, code review |
| Algorithm Learning | invariant, diagram, push/pop, heapify | teaching progression | concept, walkthrough, exercise seed | lesson, diagram, exercise |
| API Design | API docstrings, usage block, fixed-size operations, max variants | API decision frames | design choice, API contract, workflow mapping | API review, library design note |
| Stream Merge | merge function and docstring | data pipeline pattern windows | stream pattern, assumption, ordering strategy | pipeline recipe, implementation sketch |
| Scheduler Adaptation | tournament explanation, scheduler commentary | domain transfer windows | transfer pattern, domain mapping, design tradeoff | scheduler design guidance |

## 9. Key Finding

The same Original Source yields different IdeaMark-like Documents depending on the generation Projection.

The difference appears in:

- which source regions are selected;
- how Sections are titled and ordered;
- which Occurrence roles are useful;
- what counts as reusable Entity material;
- what future activation expressions become cheap to generate;
- whether later cross-Projection reuse is direct, partial, or source-mediated.

This supports the Part 3 claim that IdeaMark generation is not Projection-independent extraction.

## 10. Design Implications

### 10.1 Section remains useful

A Section can be understood as a Projection-shaped local source window.

Different generation Projections create different windows over the same Original Source.

### 10.2 Occurrence remains useful

An Occurrence can be understood as role-bearing placement of material within a Section.

The same material can have different roles under different Projections.

### 10.3 Entity remains useful but Projection-shaped

An Entity should not be treated as a universal semantic atom.

It is reusable material shaped by the generation Projection.

### 10.4 Metadata must record generation Projection

Without generation Projection metadata, later systems cannot judge why source regions were included or omitted.

### 10.5 Coverage is Projection-relative

Coverage should not mean coverage of the Original Source as a whole.

It should mean coverage under a Projection.

## 11. Next Step

Repeat this multi-Projection generation test using:

1. SQLite `src/pager.c` as a code/design source with explicit invariants and state transitions.
2. A public RFC document as a proposal/design source with motivation, alternatives, and unresolved questions.

The goal is to test whether Section / Occurrence / Entity remains useful across source types that differ from CPython `heapq.py`.
