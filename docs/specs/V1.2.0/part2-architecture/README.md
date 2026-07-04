# Part 2 — Architecture of Human-AI Co-evolution

**Version:** IdeaMark Core v1.2.0  
**Status:** Planned

This part describes the architecture through which humans, AI systems, projections, IdeaMark documents, retrieval systems, and authoritative original sources may participate in continuous co-evolution.

In this specification, co-evolution means the continuous mutual development of humans and AI through shared intellectual activities grounded in authoritative original sources.

Part 1 explains why IdeaMark uses engineering through separation: reusable structure is separated from meaning so that it can be managed and reused without fixing interpretation.

Part 2 explains engineering through reconstruction at the ecosystem level.

The architecture described in this part is a reference architecture for explaining how IdeaMark may be used.

It does not prescribe a required system implementation, retrieval interface, projection selection method, or database architecture.

The reference architecture is organized as a two-plus-one layer model:

1. Index Construction Layer
2. Reconstruction Layer
3. Ecosystem Feedback Layer

The first two layers describe common operational concerns. The third layer describes how projections, sources, IdeaMark documents, retrieval behavior, and human-AI practices may improve over time.

## Proposed Sections

0. Architectural Overview
1. Two-plus-one Layer Model
2. Index Construction Layer
3. Projection Libraries and Projection Selection
4. IdeaMark Generation and Repository Construction
5. On-demand Generation and Background Generation
6. Reconstruction Layer
7. Retrieval as Navigation to Intellectual Activity
8. AI Interpretation and Human Interpretation
9. Human Action and New Original Sources
10. Ecosystem Feedback Layer
11. Capability-Oriented Human-AI Co-evolution
12. Architectural Non-goals
13. Architecture Summary

## Layer 1: Index Construction

The Index Construction Layer creates reusable structural indexes from combinations of original sources and projections.

```text
Original Source Collection
        x
Projection Library
        ↓
IdeaMark Generation
        ↓
IdeaMark Repository / DB
```

This is a reference pattern, not a required implementation.

For example, if an organization has 100,000 source files and 30 projections, an implementation may eventually generate up to 3,000,000 source-projection IdeaMark combinations.

This generation may occur through background processing, prioritized processing, on-demand generation when a missing combination is needed, or another implementation-specific strategy.

## Projection Sources

Projection may be created, selected, shared, or standardized in many ways.

For example, Projection may be:

- created by an individual;
- shared within an organization;
- maintained as an organizational standard;
- published through an open-source Projection library;
- provided by consultants or domain experts;
- standardized by an industry group;
- generated or refined by AI systems.

IdeaMark Core should not privilege one origin of Projection over another.

The architectural requirement is that Projection can guide the construction or retrieval of IdeaMark structures in an interoperable way.

## Layer 2: Reconstruction

The Reconstruction Layer uses IdeaMark structures to support future intellectual activity.

```text
User / Situation
        ↓
Projection Selection or Projection Generation
        ↓
IdeaMark Retrieval
        ↓
Original Source Access
        ↓
AI Interpretation
        ↓
Human Interpretation
        ↓
Decision / Action
        ↓
New Original Source
```

This layer reconstructs meaning from authoritative original sources under current situations and projections.

The diagram does not define a required retrieval interface.

A system may accept a situation description, a selected Projection, a generated Projection, multiple Projections, a query, a task, a workflow state, an API request, or another implementation-specific input.

Part 2 should explain architectural responsibilities without constraining how retrieval input is provided.

## Plus-one Layer: Ecosystem Feedback

The Ecosystem Feedback Layer improves the system over time.

```text
Usage / Retrieval Results / Human Feedback / New Sources
        ↓
Projection Improvement
        ↓
IdeaMark Regeneration
        ↓
Repository Improvement
        ↓
Improved Reconstruction
```

This layer explains why Projection should be treated as a reusable intellectual asset and why IdeaMark documents are operational snapshots rather than immutable final representations.

## Scope

Part 2 should explain the system-level architecture before the Core Model is specified.

It should not define YAML fields, validation rules, storage engines, queueing systems, database schemas, retrieval input methods, user interfaces, Projection governance models, or implementation-specific retrieval algorithms.

The purpose of Part 2 is to describe architectural relationships, not to specify a particular IdeaMark DB system or internal knowledge-management product.
