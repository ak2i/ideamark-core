# 1. Two-plus-one Layer Model

**Part:** 2 — Architecture of Human-AI Co-evolution  
**Status:** Draft Rev001  
**Type:** Informative / Reference Architecture

Part 2 organizes the reference architecture as a two-plus-one layer model.

The two primary layers describe common operational concerns.

The plus-one layer describes long-term ecosystem improvement.

```text
Layer 1: Index Construction Layer
Layer 2: Reconstruction Layer
Plus-one: Ecosystem Feedback Layer
```

The term index in this model refers to the access-structure role of IdeaMark documents.

It does not define database indexing, search engine indexing, or storage optimization.

## 1.1 Layer 1: Index Construction Layer

The Index Construction Layer creates IdeaMark documents from combinations of authoritative original sources and Projections.

```text
Original Source Collection
        x
Projection Library or Projection Definition
        ↓
IdeaMark Generation
        ↓
IdeaMark Document Set
```

The output of this layer is not final meaning.

The output is a reusable access structure that can later assist reconstruction.

This layer answers questions such as:

- Which original sources are available?
- Which Projection should be applied?
- What reusable structures should be extracted or generated?
- How should the resulting IdeaMark document remain traceable to the original source?
- Should generation happen in advance, on demand, or both?

These questions are architectural responsibilities.

They do not imply a required storage engine, indexing method, database schema, job queue, or generation pipeline.

## 1.2 Layer 2: Reconstruction Layer

The Reconstruction Layer uses IdeaMark documents to support future intellectual activity.

```text
Current Situation
        ↓
Projection Selection or Projection Generation
        ↓
IdeaMark Retrieval or IdeaMark Generation
        ↓
Original Source Access
        ↓
AI Interpretation and Human Interpretation
        ↓
Decision / Action / Explanation
        ↓
New Original Source
```

This layer is where meaning is reconstructed.

The Reconstruction Layer does not treat the IdeaMark document as the final answer.

Instead, the IdeaMark document helps identify relevant original sources and reusable structures, while the current Projection guides how those sources should be interpreted for the present situation.

A system may enter this layer through many kinds of input:

- a user situation description;
- a task;
- a question;
- a selected Projection;
- a generated Projection;
- a workflow state;
- an API request;
- a human review process;
- an AI agent plan.

Part 2 does not prescribe which input form is required.

## 1.3 Plus-one Layer: Ecosystem Feedback Layer

The Ecosystem Feedback Layer improves the conditions for future reconstruction.

```text
Usage / Retrieval Results / Human Feedback / New Sources
        ↓
Projection Improvement
        ↓
IdeaMark Regeneration or Coexistence
        ↓
Repository and Practice Improvement
        ↓
Improved Reconstruction
```

This layer explains why IdeaMark documents are operational snapshots rather than immutable final artifacts.

As humans and AI use IdeaMark documents, they may discover:

- useful Projections;
- missing Projections;
- weak source coverage;
- better entity boundaries;
- more useful occurrence structures;
- more effective retrieval patterns;
- new original sources;
- changing user capabilities;
- new organizational practices.

The ecosystem may respond by improving Projections, regenerating IdeaMark documents, preserving multiple versions, refining authoring practices, or adding new authoritative sources.

## 1.4 Why Two-plus-one?

The first two layers are enough to describe ordinary operation.

One layer constructs reusable access structures.

The other layer uses them to reconstruct meaning under a current situation.

However, human-AI co-evolution cannot be explained by those two layers alone.

If use does not improve Projections, source collections, retrieval practices, authoring practices, or human capability, the system becomes a static automation pipeline.

The plus-one layer keeps the architecture capability-oriented.

It makes improvement of the intellectual ecosystem a first-class architectural concern.

## 1.5 Relationship to Projection

Projection participates in all three layers.

In the Index Construction Layer, Projection guides which reusable structures are generated from original sources.

In the Reconstruction Layer, Projection guides how IdeaMark documents and original sources are interpreted under the current situation.

In the Ecosystem Feedback Layer, Projection itself may be evaluated, refined, shared, standardized, replaced, or specialized.

This is why Projection should be treated as a reusable intellectual asset rather than a temporary prompt parameter.

## 1.6 Relationship to Original Sources

Original sources remain authoritative across all layers.

The Index Construction Layer begins from original sources.

The Reconstruction Layer returns to original sources.

The Ecosystem Feedback Layer may create, discover, revise, or reorganize original sources.

IdeaMark documents improve access to original sources, but they do not replace them.

## 1.7 Relationship to AI Systems

AI systems may participate in each layer.

They may help generate IdeaMark documents, propose Projections, retrieve relevant structures, interpret original sources, explain results, identify missing information, and summarize feedback.

However, Part 2 does not assume that AI fully automates the architecture.

Human participation remains essential because the goal is capability expansion, not merely answer production.

A useful architecture should help humans and AI continue producing better intellectual activities together.

## 1.8 Layer Boundaries Are Conceptual

The layers are conceptual boundaries.

An implementation may combine them in one application, distribute them across services, perform them manually, automate parts of them, or execute them asynchronously.

For example:

- a batch process may generate IdeaMark documents before any user request;
- an interactive assistant may generate a temporary IdeaMark document during a conversation;
- a repository may keep multiple IdeaMark versions for different Projections;
- a human team may revise a Projection after observing repeated retrieval failures;
- an AI agent may suggest missing original sources.

All of these are compatible with the model if the architectural responsibilities remain clear.

## 1.9 Summary

The two-plus-one layer model explains IdeaMark as part of a living human-AI intellectual ecosystem.

The Index Construction Layer creates reusable access structures.

The Reconstruction Layer uses those structures to return to original sources and reconstruct meaning under current situations and Projections.

The Ecosystem Feedback Layer improves the future conditions for both construction and reconstruction.

Together, the three layers describe how IdeaMark can support continuous human-AI co-evolution without prescribing implementation-specific storage, indexing, retrieval, or user interface mechanisms.
