# Heapq Cross-Projection Reconstruction Test

**Part:** 3 — Core Model  
**Status:** Design Experiment  
**Type:** Reconstruction / Projection Compatibility Test

This document tests what happens when the candidate IdeaMark-like structure generated from CPython `Lib/heapq.py` under a Performance Engineering Projection is reconstructed under different Projections.

The purpose is to evaluate whether an IdeaMark Document generated under one Projection can still function as a reusable access structure under another compatible or partially compatible Projection.

## 1. Source Candidate

Base candidate:

```text
docs/specs/V1.2.0/part3-core-model/03-heapq-performance-candidate.md
```

Generation Projection:

```yaml
id: code-design-performance-heapq-v0
purpose: extract implementation and performance reasoning from source code
focus:
  - heap invariant
  - comparison cost
  - implementation rationale
  - empirical comparison counts
```

The base candidate contains four local source-anchored structures:

1. Heap invariant as performance boundary.
2. Comparison-cost-aware sift strategy.
3. Choosing heap operations for fixed-size workflows.
4. Heapify as bottom-up construction.

## 2. Reconstruction Projection A — API Design

```yaml
projection:
  id: code-api-design-heapq-v0
  purpose: reconstruct API design reasoning from source code
  intended_activity:
    - explain why an API exposes certain operations
    - help library designers evaluate user-facing tradeoffs
  focus:
    - API shape
    - user expectations
    - operation naming
    - fixed-size workflow support
    - compatibility with host language idioms
  non_goals:
    - low-level proof of heap correctness
    - exhaustive performance benchmarking
```

### 2.1 Retrieved Structures

Likely retrieved from the base candidate:

```yaml
retrieved:
  sections:
    - SEC-001
    - SEC-003
  entities:
    - IE-002
    - IE-007
    - IE-008
  occurrences:
    - OCC-002
    - OCC-007
    - OCC-008
```

### 2.2 Reconstruction Result

Possible activation expression:

> CPython's heap API is designed to feel like normal Python list usage while exposing priority-queue operations. The min-heap orientation and 0-based indexing make `heap[0]` the smallest item and allow the heap to remain list-compatible. The API also includes combined operations such as `heapreplace` and `heappushpop` for fixed-size or threshold-style workflows, where avoiding separate pop and push operations can better match the user's actual workload.

### 2.3 Evaluation

The generated candidate was not primarily an API design document, but it retained enough API-related material for a useful reconstruction.

This supports the claim that generation Projection and reconstruction Projection need not be identical.

However, the reconstruction is incomplete for full API design because it lacks user-error cases, naming alternatives, historical API discussion, and comparative analysis against other priority queue APIs.

### 2.4 Implication

A Section-like structure with role-bearing items can support partial cross-Projection reuse if the Projection overlap is sufficient.

For API Design, the useful overlap was:

```text
performance-oriented fixed-size heap operations
        overlaps with
user-facing operation selection and API ergonomics
```

## 3. Reconstruction Projection B — Algorithm Learning

```yaml
projection:
  id: code-algorithm-learning-heapq-v0
  purpose: teach heap algorithms to learners
  intended_activity:
    - explain heap operations step by step
    - generate diagrams or exercises
    - distinguish invariant, operation, and complexity
  focus:
    - heap invariant
    - array-to-tree mapping
    - push and pop behavior
    - heapify construction
    - complexity intuition
  non_goals:
    - library API history
    - micro-optimization rationale
    - production engineering tradeoffs
```

### 3.1 Retrieved Structures

Likely retrieved from the base candidate:

```yaml
retrieved:
  sections:
    - SEC-001
    - SEC-004
  entities:
    - IE-001
    - IE-003
    - IE-009
  occurrences:
    - OCC-001
    - OCC-003
    - OCC-009
```

### 3.2 Reconstruction Result

Possible activation expression:

> A heap can be taught as an array that behaves like a binary tree. The important invariant is that each parent is no larger than its children, so the smallest item is always at index 0. To remove the smallest item, the implementation moves a lower-level item to the root and restores the invariant by percolating it down. To build a heap efficiently from an existing list, `heapify` works bottom-up from the last parent node rather than inserting items one by one.

### 3.3 Evaluation

The base candidate can support an introductory explanation, but the learner-facing reconstruction is thinner than ideal.

The base candidate did not preserve enough source material about tree diagrams, child index formulas, or worked examples because the generation Projection focused on performance reasoning.

### 3.4 Implication

Cross-Projection reconstruction works, but the quality depends on whether the generation Projection preserved enough material for the later Projection.

This suggests that IdeaMark Documents should record generation Projection metadata so later retrieval systems can judge fit and expected loss.

## 4. Reconstruction Projection C — Data Processing / Stream Merge

```yaml
projection:
  id: code-data-pipeline-stream-merge-v0
  purpose: reuse source code as a data processing design pattern
  intended_activity:
    - design memory-efficient stream merge workflows
    - explain when heap-based merging is useful
    - generate implementation sketches for sorted streams
  focus:
    - sorted input streams
    - generator-based output
    - bounded memory
    - key functions
    - reverse ordering
  non_goals:
    - heap invariant proof
    - comparison-count optimization
    - fixed-size heap API design
```

### 4.1 Retrieved Structures

Likely retrieved from the base candidate:

```yaml
retrieved:
  sections: []
  entities: []
  occurrences: []
```

### 4.2 Reconstruction Result

The base candidate does not contain the `merge` function material.

A future LLM could still discover it by returning to the Original Source and applying the new Projection to the file, but the existing candidate IdeaMark-like document does not directly support this reconstruction.

Possible result if source re-reading is allowed:

> The `merge` function is a stream-oriented pattern: it assumes each input iterable is already sorted, keeps only the current frontier of each stream in a heap, and yields merged output lazily rather than materializing and sorting all input items at once.

### 4.3 Evaluation

This is a useful failure case.

The document was generated under a Performance Engineering Projection focused on heap invariant, comparison cost, and heap operations. It did not preserve stream-merge material.

The candidate can still point to the Original Source, but it cannot itself answer a stream-merge reconstruction request without additional Decomposition or source reading.

### 4.4 Implication

IdeaMark Documents should not pretend to cover the full Original Source.

Projection metadata is necessary so retrieval systems can distinguish:

```text
This document contains useful material for the new Projection.
```

from:

```text
This document only points to a source that may contain useful material.
```

This strengthens the need for explicit coverage or focus metadata at the document or local-frame level.

## 5. Reconstruction Projection D — Domain Adaptation / Scheduler Design

```yaml
projection:
  id: code-domain-adaptation-scheduler-v0
  purpose: transfer heap-based reasoning to event scheduler design
  intended_activity:
    - explain why heaps are useful for scheduling future events
    - generate scheduler design guidance
    - identify when heap assumptions match a domain
  focus:
    - event time as priority
    - future event insertion
    - stability of worst-case behavior
    - simulation use cases
  non_goals:
    - complete heap API documentation
    - benchmark-level implementation analysis
```

### 5.1 Retrieved Structures

Likely retrieved from the base candidate:

```yaml
retrieved:
  sections:
    - SEC-001
  entities:
    - IE-001
    - IE-003
  occurrences:
    - OCC-001
    - OCC-003
```

### 5.2 Reconstruction Result

Possible activation expression using only the base candidate:

> A heap can support scheduler design because it preserves an invariant that keeps the next item at the root. For an event scheduler, that root can represent the next scheduled event. After removing the next event, the heap is repaired by moving another item to the root and restoring the invariant.

Possible activation expression if the Original Source is re-read:

> The source commentary explicitly connects heaps to simulation schedulers: the heap holds incoming events, and the winning condition is the smallest scheduled time. When an event schedules future events, those new events can be inserted into the heap because they occur after the event just processed.

### 5.3 Evaluation

The base candidate partially supports scheduler reconstruction through general heap material, but it does not preserve the source's explicit scheduler explanation.

This suggests that cross-Projection reconstruction has two modes:

1. **Direct reuse** — the IdeaMark Document already contains relevant local frames or items.
2. **Source-mediated reuse** — the IdeaMark Document only helps locate or reopen Original Source material for a new Decomposition.

## 6. Summary of Cross-Projection Results

| Reconstruction Projection | Direct Reuse Quality | Source Re-reading Needed | Notes |
|---|---:|---:|---|
| API Design | High | Low | Fixed-size operation material transfers well. |
| Algorithm Learning | Medium | Medium | Core invariant and heapify material help, but examples are thin. |
| Data Processing / Stream Merge | Low | High | `merge` material was outside the generated candidate. |
| Scheduler Domain Adaptation | Medium-Low | Medium-High | General heap material helps, but explicit scheduler commentary was omitted. |

## 7. Design Findings

### 7.1 Projection metadata is necessary

A later retrieval or reconstruction system needs to know the generation Projection in order to estimate whether a candidate IdeaMark Document is likely to contain relevant material.

### 7.2 Coverage metadata may be necessary

The candidate's `meta.projections.focus` helps, but it may not be enough.

A local frame may need lightweight coverage tags such as:

```yaml
coverage:
  includes:
    - comparison_cost
    - fixed_size_heap_operations
  excludes:
    - stream_merge
    - scheduler_domain_adaptation
```

This should probably remain optional metadata, not a Core semantic ontology.

### 7.3 Section-like local frames remain useful

The source-anchored local frame is the strongest structural unit in this test.

It supports retrieval, partial reconstruction, source re-opening, and comparison across Projections.

### 7.4 Entity-like reusable payloads help but can over-summarize

The entity payloads made reconstruction easy, but some of them act like mini-interpretations.

This remains a risk if IdeaMark is meant to preserve structure rather than final meaning.

### 7.5 Occurrence-like wrappers are useful as role placements

The occurrence layer is useful when understood as placement of reusable material inside a local activity frame.

The term `Occurrence` may still be misleading, but the role-bearing wrapper remains useful.

### 7.6 Relation remains unnecessary

Cross-Projection reconstruction did not require a separate Relation object.

Section ordering, frame grouping, source anchoring, item roles, and projection metadata were sufficient.

## 8. Candidate Model Refinement

The test suggests a possible simplification:

```yaml
activity_frames:
  - id: AF-001
    title: Comparison-cost-aware sift strategy
    source_anchor:
      source: SRC-heapq-py
      line_ranges:
        - { start: 58, end: 95 }
    projection_fit:
      generated_for:
        - comparison_cost
        - implementation_rationale
      compatible_with:
        - performance_engineering
        - api_design
      weak_for:
        - stream_merge
        - scheduler_domain_adaptation
    items:
      - role: optimization_rationale
        material: avoid early break in siftup
        rationale: local early-exit optimization may increase total comparison cost
      - role: cost_driver
        material: comparisons may be expensive
      - role: empirical_support
        material: comparison-count examples support the chosen implementation
```

This shape may better express the actual structure used in reconstruction:

```text
source-anchored local activity frame
  -> ordered role-bearing materials
  -> projection-fit metadata
```

## 9. Next Step

The next experiment should simulate JSON conversion and MongoDB-style retrieval using both:

1. the current Section / Occurrence / Entity candidate; and
2. the flatter activity-frame candidate.

The goal is not to test MongoDB itself, but to reason about what searches become easy or difficult depending on the document shape.
