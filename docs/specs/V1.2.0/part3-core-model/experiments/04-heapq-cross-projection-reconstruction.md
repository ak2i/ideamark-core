# Heapq Cross-Projection Reconstruction Test

**Part:** 3 — Core Model  
**Status:** Design Experiment  
**Type:** Reconstruction / Projection Compatibility Test

This document tests what happens when the candidate IdeaMark-like structure generated from CPython `Lib/heapq.py` under a Performance Engineering Projection is reconstructed under each Projection proposed in `02-code-original-source-experiment.md`.

The purpose is to evaluate whether an IdeaMark Document generated under one Projection can still function as a reusable access structure under another compatible or partially compatible Projection.

This revision preserves the working assumption that Section / Occurrence / Entity remains a plausible structure. It does not assume replacement by `activity_frame`.

## 1. Source Candidate

Base candidate:

```text
docs/specs/V1.2.0/part3-core-model/03-heapq-performance-candidate.md
```

Original Source:

```text
Repository: python/cpython
Path: Lib/heapq.py
Ref: main
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

The base candidate contains four source-anchored Sections:

1. Heap invariant as performance boundary.
2. Comparison-cost-aware sift strategy.
3. Choosing heap operations for fixed-size workflows.
4. Heapify as bottom-up construction.

## 2. Projection 1 — Performance Engineering

This is the same Projection used during generation.

```yaml
projection:
  id: code-design-performance-heapq-v0
  purpose: extract implementation and performance reasoning from source code
  intended_activity:
    - explain why the implementation makes specific optimization choices
    - help engineers reuse the reasoning in other data-structure implementations
  focus:
    - heap invariant
    - comparison cost
    - implementation rationale
    - empirical comparison counts
```

### 2.1 Retrieved Structures

```yaml
retrieved:
  sections:
    - SEC-001
    - SEC-002
    - SEC-003
    - SEC-004
  entities:
    - IE-001
    - IE-002
    - IE-003
    - IE-004
    - IE-005
    - IE-006
    - IE-007
    - IE-008
    - IE-009
  occurrences:
    - OCC-001
    - OCC-002
    - OCC-003
    - OCC-004
    - OCC-005
    - OCC-006
    - OCC-007
    - OCC-008
    - OCC-009
```

### 2.2 Reconstruction Result

Possible activation expression:

> CPython's heap implementation shows a performance-engineering pattern: define the invariant first, then optimize the repair path under the real cost model. The heap invariant keeps the smallest item at index 0, but the interesting implementation choice is in `_siftup`: it avoids an apparent early-exit optimization because repeated pop workloads tend to move a large item to the root, and comparisons may be expensive when priorities are hidden inside custom comparison methods or tuple ordering. The source commentary therefore preserves not only an algorithm, but an engineering judgment about the workload and cost model.

### 2.3 Evaluation

The candidate works best under its generation Projection.

The Sections and Occurrences provide enough material to reconstruct an explanation without treating the IdeaMark Document as a substitute for the Original Source.

### 2.4 Implication

Generation Projection remains an important compatibility signal.

The document is strongest when the use-side Projection overlaps closely with the generation Projection.

## 3. Projection 2 — Algorithm Learning

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

> A heap can be introduced as an array that behaves like a binary tree. The key invariant is that each parent is no larger than its children, which makes the smallest item available at index 0. Removing the smallest item requires restoring that invariant: move a lower-level item to the root, then percolate it down. To build a heap efficiently from an existing list, `heapify` works bottom-up from the last parent node rather than inserting items one by one.

### 3.3 Evaluation

The base candidate supports a basic learning reconstruction, but it is not ideal for learners.

The generation Projection preserved the invariant, restoration pattern, and heapify construction, but omitted learner-friendly materials such as the tree diagram, child index walkthrough, examples, and exercises.

### 3.4 Implication

Cross-Projection reuse works when the generation Projection preserves enough shared structural material.

For learner-facing use, Section anchors should help reopen the Original Source and recover omitted explanatory material.

## 4. Projection 3 — API Design

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

### 4.1 Retrieved Structures

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

### 4.2 Reconstruction Result

Possible activation expression:

> CPython's heap API is designed to behave naturally as a Python list while exposing priority-queue operations. The 0-based indexing and min-heap orientation make `heap[0]` the smallest item, which avoids surprises for Python users. The API also includes combined operations such as `heapreplace` and `heappushpop` for fixed-size or threshold-style workflows, where avoiding separate pop and push operations better matches user intent and performance expectations.

### 4.3 Evaluation

The candidate was not generated as an API design document, but it retained enough API-related material for a useful reconstruction.

The API Design Projection overlaps strongly with the performance candidate around fixed-size heap operations and host-language ergonomics.

### 4.4 Implication

This is a successful cross-Projection case.

It suggests that Section / Occurrence / Entity can support Projection compatibility without a separate Relation object.

## 5. Projection 4 — Data Processing / Stream Merge

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

### 5.1 Retrieved Structures

```yaml
retrieved:
  sections: []
  entities: []
  occurrences: []
  source_pointer:
    source: SRC-heapq-py
    likely_region: merge function
```

### 5.2 Reconstruction Result

The base candidate does not contain the `merge` function material.

A future LLM or tool should reopen the Original Source and apply this Projection to the relevant region.

Possible activation expression if the source is reopened:

> The `merge` function is a stream-oriented pattern: it assumes each input iterable is already sorted, keeps only the current frontier of each stream in a heap, and yields merged output lazily rather than materializing and sorting all input items at once.

### 5.3 Evaluation

This is a useful non-match case.

The existing candidate is not a bad IdeaMark Document; it is simply a Projection-limited access structure.

It can point to the Original Source, but it does not itself contain the local Sections needed for stream-merge reconstruction.

### 5.4 Implication

IdeaMark should distinguish between:

```text
Projection-compatible local structure exists.
```

and:

```text
The Original Source may contain relevant material, but a new Projection-guided Decomposition is needed.
```

This distinction is more important than whether the document can reconstruct everything by itself.

## 6. Projection 5 — Domain Adaptation / Scheduler Design

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

### 6.1 Retrieved Structures

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
  source_pointer:
    source: SRC-heapq-py
    likely_region: explanatory scheduler commentary
```

### 6.2 Reconstruction Result

Possible activation expression using the candidate structure:

> A heap can support scheduler design because the invariant keeps the next priority item at the root. For an event scheduler, that root can represent the next scheduled event. After processing the event, the heap is repaired by replacing the root and restoring the invariant.

Possible activation expression if the Original Source is reopened:

> The source commentary explicitly connects heaps to simulation schedulers: the heap holds incoming events, and the winning condition is the smallest scheduled time. When an event schedules future events, those new events can be inserted into the heap because they occur after the event just processed.

### 6.3 Evaluation

The candidate partially supports scheduler reconstruction through general heap material, but it omitted the source's explicit scheduler example.

The Section anchor for heap invariant is still useful, but the candidate should not be treated as complete coverage for this Projection.

### 6.4 Implication

This case supports a two-level retrieval interpretation:

1. **Local structure reuse** — existing Sections and Occurrences provide partial materials.
2. **Source-mediated continuation** — the document points back to the Original Source for a new or extended Decomposition.

## 7. Summary of All Projection Results

| Projection from 02 | Relationship to Generation Projection | Direct Local Structure Reuse | Source Reopening Value | Result |
|---|---|---:|---:|---|
| Performance Engineering | Same | High | Medium | Strong reconstruction; best fit. |
| Algorithm Learning | Partial overlap | Medium | High | Works for invariant and heapify; source needed for teaching detail. |
| API Design | Strong overlap | High | Medium | Successful cross-Projection reuse. |
| Data Processing / Stream Merge | Weak overlap | Low | High | Existing candidate mostly acts as source pointer. |
| Domain Adaptation / Scheduler | Partial overlap | Medium-Low | High | General heap material transfers; scheduler source passage should be reopened. |

## 8. Design Findings

### 8.1 IdeaMark Document does not need self-contained reconstruction

The important question is not whether the IdeaMark Document alone can reconstruct the activation expression.

The more faithful question is:

> Does the IdeaMark Document reduce the cost of returning to the right Original Source material under a new or compatible Projection?

In most non-trivial cases, reconstruction should involve the Original Source again.

### 8.2 Section-like structures remain useful

The test supports keeping something like Section.

A Section acts as a Projection-shaped local window into Original Source material.

It is not a document chapter and not a stored intellectual activity.

It is a reusable local source context that helps future reconstruction begin cheaply.

### 8.3 Occurrence-like structures remain useful as placements

Occurrence-like structures are useful when treated as placements of reusable material within a Section.

They carry role and local rationale without requiring a separate Relation object.

### 8.4 Entity-like structures remain useful but require discipline

Entity-like structures are useful as reusable materials, but their payload can become too explanatory.

Part 3 should clarify that Entity content should preserve reconstruction material, not final meaning.

### 8.5 Projection coverage should be visible but lightweight

The test suggests value in recording lightweight coverage or focus metadata.

This metadata should help systems decide whether a Section is directly useful, partially useful, or mainly a source pointer.

However, coverage should not become a universal ontology.

### 8.6 Relation remains unnecessary

All tested Projections were handled through Section grouping, Occurrence roles, Entity payloads, source anchors, ordering, and metadata.

No separate Relation object was needed.

## 9. Implication for Part 3

The current Section / Occurrence / Entity structure remains defensible if reinterpreted as:

```text
Section
  = Projection-shaped local source window

Occurrence
  = role-bearing placement of reusable material within that window

Entity
  = reusable material that can participate in future reconstruction
```

This interpretation appears more consistent with Part 1 and Part 2 than replacing the model with `activity_frame`.

The name `Section` may remain acceptable if the specification explicitly says it is not a document chapter.

## 10. Next Step

Run the same Projection-compatibility test on a second Original Source from a different project.

The second source should ideally differ from `heapq.py` in one or more ways:

- less explanatory prose;
- more architectural structure;
- more configuration or data-processing logic;
- stronger domain assumptions;
- different language or ecosystem.

This will test whether the Section / Occurrence / Entity interpretation generalizes beyond a heavily commented algorithm module.
