# 11. Retrieval-Oriented Evaluation

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 11.1 Purpose

Retrieval-oriented evaluation asks whether an IdeaMark Document supports future knowledge reuse.

It is not enough for a document to be valid YAML or to pass Core conformance.

A useful IdeaMark Document should help future humans, AI systems, and tools find, inspect, reconstruct, and activate reusable material under one or more Projections.

## 11.2 Reuse Is the Main Evaluation Axis

IdeaMark authoring should be evaluated primarily by reuse.

The question is not only:

```text
Is the document correct?
```

The stronger question is:

```text
Can this document help future activity reuse knowledge under the Projection?
```

This may include:

- finding the right Section;
- returning to the right source region;
- reusing an Entity in a new Section;
- reconstructing an explanation, checklist, design rationale, warning, or plan;
- comparing decompositions across Projections;
- supporting later regeneration or migration.

## 11.3 Retrieval Targets

Before evaluating retrieval, identify what future users are expected to retrieve.

Possible retrieval targets include:

- a Section as a local activity unit;
- an Occurrence with a specific role;
- an Entity of a useful kind;
- a source anchor;
- a Projection reference;
- a group of Sections in optional structure ordering;
- a warning or review marker;
- a profile-specific object.

Evaluation should be shaped by the intended future activity.

## 11.4 Evaluation Questions

Useful evaluation questions include:

1. Can a user find the relevant local activity unit?
2. Can a user identify which reusable material matters?
3. Can a user return to the source region when needed?
4. Can a future AI system reconstruct a useful activation expression?
5. Does the document avoid irrelevant material that would pollute retrieval?
6. Can the same source be compared under another Projection?
7. Are placeholders, uncertainty, and warnings visible?
8. Does the document support correction or regeneration?

## 11.5 Retrieval Scenarios

A retrieval scenario describes a future use case that the IdeaMark Document should support.

Examples:

- Explain why a data-structure implementation avoids a locally obvious optimization.
- Find API operations suitable for a fixed-size heap workflow.
- Identify ingredients that provide umami in a recipe.
- Locate recovery invariants in a state-machine design.
- Retrieve compatibility constraints from RFC-like design prose.

Scenarios help evaluate whether the authoring choices are useful.

## 11.6 Reconstruction Tasks

A reconstruction task asks a human or AI system to produce an activation expression from the IdeaMark Document and Original Source.

Examples of activation expressions:

- explanation;
- teaching note;
- warning;
- code review comment;
- migration note;
- decision memo;
- checklist;
- comparison table;
- search query;
- follow-up question.

The resulting activation expression is not necessarily stored in the IdeaMark Document.

It is generated from the reusable access structure.

## 11.7 Precision and Noise

Retrieval-oriented evaluation should consider both missing material and noisy material.

A document may fail because it omits material required for reuse.

It may also fail because it includes too much material that distracts from the Projection.

Useful omission improves retrieval.

Generic over-extraction weakens retrieval.

## 11.8 Multi-Projection Evaluation

Comparing documents generated from the same Original Source under different Projections can reveal whether the Projections and authoring choices are meaningful.

```mermaid
flowchart TD
    SRC[Same Original Source] --> D1[IdeaMark A]
    SRC --> D2[IdeaMark B]
    D1 --> Q1[Retrieval scenario A]
    D2 --> Q2[Retrieval scenario B]
    Q1 --> CMP[Compare reuse behavior]
    Q2 --> CMP
```

If two different Projections always produce the same retrieval behavior, the Projections may not be distinct enough or the authoring may be too generic.

## 11.9 Evaluation and Samples

Part 4 normalized samples can seed retrieval-oriented evaluation.

For example:

- heapq performance and heapq API design samples can test same-source/different-Projection behavior;
- recipe execution and recipe substitution samples can test non-technical source decomposition;
- SQLite pager samples can test state-machine and correctness-oriented retrieval;
- RFC design prose samples can test rationale and compatibility retrieval.

Samples should be used to test not only validators, but also authoring judgments.

## 11.10 Evaluation Signals

Possible evaluation signals include:

- successful retrieval;
- failed retrieval;
- noisy retrieval;
- ambiguous Section boundary;
- missing anchor;
- weak Entity granularity;
- unclear Occurrence role;
- Projection drift;
- successful reconstruction;
- reconstruction requiring too much hidden context.

These signals may become review notes, warnings, test cases, or future profile rules.

## 11.11 Authoring Checks

Review retrieval-oriented quality with questions such as:

1. What future retrieval scenario does this document support?
2. Which Sections should be found for that scenario?
3. Which Entities should be reusable?
4. Which Occurrence roles matter?
5. Can the source be revisited?
6. Does the document include too much irrelevant material?
7. Can a useful activation expression be reconstructed?
8. What failed retrievals should become correction tasks?
