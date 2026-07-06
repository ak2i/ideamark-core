# Code Original Source Experiment

**Part:** 3 — Core Model  
**Status:** Design Experiment  
**Type:** Original Source / Projection / Decomposition Test

This note proposes a concrete Part 3 experiment using public source code as Original Source material.

The goal is to test whether IdeaMark can treat source code as an Original Source and extract reusable materials for Human-AI Intellectual Activity such as algorithm design, implementation design, data processing design, performance reasoning, and educational reconstruction.

## 1. Experiment Purpose

Part 3 has so far defined IdeaMark as a Projection-guided access structure rather than a meaning store.

The next design question is:

> What minimal structure must an IdeaMark Document preserve so that future humans and AI systems can retrieve source material, apply a Projection or compatible Projection, and generate expressions that activate useful Human-AI Intellectual Activity?

Public source code is a useful test case because it often contains multiple kinds of reusable intellectual activity:

- algorithmic design;
- data structure selection;
- API design;
- performance tradeoff reasoning;
- implementation technique;
- domain adaptation;
- explanatory comments;
- usage examples;
- historical design rationale.

## 2. Candidate Original Source

Initial candidate:

```text
Repository: python/cpython
Path: Lib/heapq.py
Ref: main
Original Source type: public source code module
```

Reason for selection:

- The file implements a compact and well-known data structure.
- It includes algorithmic explanation, API usage, implementation details, optimization rationale, and application examples.
- It is small enough to inspect manually but rich enough to test multiple Projections.
- It contains both executable code and explanatory prose.

## 3. Initial Source Observations

The module begins by defining the heap invariant and the property that `heap[0]` is always the smallest element.

It also explains Python-specific API decisions, including the use of 0-based indexing and returning the smallest item rather than the largest item.

The source includes explanatory material about tournament interpretation, scheduler applications, big disk sorts, and comparison-cost tradeoffs.

Implementation comments also describe why `_siftup` deliberately does not break early when the new item is already smaller than both children, because comparison costs can be significant and theory plus experiments support the chosen approach.

## 4. Candidate Projections

The same Original Source may be decomposed under different Projections.

### 4.1 Algorithm Learning Projection

Purpose:

- Help a learner understand heap algorithms as reusable algorithmic knowledge.

Likely extracted materials:

- heap invariant;
- array-to-tree mapping;
- smallest-item-at-root property;
- push/pop/heapify operations;
- logarithmic percolation behavior;
- linear-time heapify explanation.

Expected activation expression:

- explanation, diagram, walk-through, exercise, or teaching note.

### 4.2 API Design Projection

Purpose:

- Help a library designer understand how implementation choices shape API expectations.

Likely extracted materials:

- 0-based indexing decision;
- min-heap instead of max-heap decision;
- compatibility with Python list behavior;
- `heap.sort()` preserving heap invariant;
- fixed-size heap use cases for `heapreplace` and `heappushpop`.

Expected activation expression:

- API design rationale, design checklist, tradeoff explanation, or code review guidance.

### 4.3 Performance Engineering Projection

Purpose:

- Help an engineer reason about comparison cost, asymptotic behavior, and empirical tradeoffs.

Likely extracted materials:

- logarithmic pop behavior;
- linear heapify;
- comparison-count discussion;
- early-break rejection in `_siftup`;
- heapify versus repeated heappush;
- heap sort versus list sort comparison.

Expected activation expression:

- performance note, benchmark interpretation, optimization rationale, or engineering decision memo.

### 4.4 Data Processing / Stream Merge Projection

Purpose:

- Help a developer design memory-efficient processing of multiple sorted streams.

Likely extracted materials:

- `merge` behavior;
- generator-based operation;
- assumption that inputs are already sorted;
- memory efficiency compared with sorting chained iterables;
- key-function support;
- reverse handling.

Expected activation expression:

- data pipeline design pattern, streaming merge recipe, or implementation sketch.

### 4.5 Domain Adaptation Projection

Purpose:

- Help a user transfer heap-based reasoning to another domain such as scheduling, simulation, disk sorting, task queues, or event processing.

Likely extracted materials:

- scheduler example;
- event scheduling into the future;
- tournament metaphor;
- big disk sort runs;
- two-heap melting/growing strategy.

Expected activation expression:

- analogy, transfer hypothesis, design pattern, or domain-specific adaptation plan.

## 5. What This Experiment Tests

This experiment should test whether the current Core Model needs Section / Occurrence / Entity, or whether a simpler or different structure is sufficient.

For each Projection, we should ask:

1. What is the unit that helps later retrieval and reconstruction?
2. What needs to be anchored to the Original Source?
3. What must be ordered?
4. What role-like information is actually needed?
5. What metadata is sufficient to remember the Projection Context?
6. What would an LLM need in order to generate an activation expression?
7. What can be omitted without losing reconstruction usefulness?

## 6. Proposed Decomposition Exercise

For the first manual experiment, choose one Projection and produce a small IdeaMark-like structure.

Recommended first Projection:

```yaml
projection:
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

Potential Original Source anchors:

- module-level heap invariant and API rationale;
- `_siftup` explanatory comments;
- comparison-count table;
- `heapify` bottom-up implementation;
- `heappushpop` and `heapreplace` fixed-size heap behavior.

## 7. Expected Outputs from the Experiment

The experiment should produce at least three artifacts:

1. **Candidate IdeaMark Document**
   - A small structured document generated from `heapq.py` under one Projection.

2. **Constraint Review**
   - A note evaluating whether the candidate structure satisfies `01-ideamark-document-constraints.md`.

3. **Model Feedback**
   - A note about whether Section / Occurrence / Entity is still sufficient, should be simplified, or should be replaced.

## 8. Open Questions

- Is the minimum useful structure still Section / Occurrence / Entity?
- Is Anchorage best understood as a Section-level source anchor, or as a more general traceability mechanism?
- Should code spans, comment spans, function names, and line ranges be treated uniformly as Original Source anchors?
- Does Projection metadata alone explain why the chosen source fragments matter?
- How much local rationale should be recorded in the IdeaMark Document?
- Can relation-like information be represented through role, ordering, and payload without restoring Relation as a Core object?

## 9. Success Criteria

The experiment is successful if the generated structure allows a future human or AI system to:

- identify the relevant Original Source material;
- understand which Projection shaped the extraction;
- retrieve the code/comment fragments needed for reconstruction;
- generate an explanation, design note, or implementation guidance that activates useful intellectual activity;
- do so without requiring final meaning to be stored inside the IdeaMark document.

## 10. Next Step

Use `python/cpython:Lib/heapq.py` as the first concrete Original Source and manually generate a small candidate IdeaMark-like document under the Performance Engineering Projection.

Then evaluate whether the current Part 3 structural assumptions are sufficient.
