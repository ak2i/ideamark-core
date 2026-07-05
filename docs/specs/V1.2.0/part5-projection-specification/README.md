# Part 5 — Projection Specification

**Version:** IdeaMark Core v1.2.0  
**Status:** Planning Draft

This part defines Projection as an external but interoperable specification.

Projection is a reuse strategy for making Original Sources accessible to future intellectual activities.

Projection should be treated as a reusable intellectual asset, not merely a prompt parameter.

## Core Stance

Projection is the mechanism that allows multiple layers of requirements to be treated as a finite, reusable strategy for Decomposition and reconstruction.

A Projection may combine requirements from many layers, such as:

- national law and social practice;
- industry rules and conventions;
- organizational procedures;
- departmental routines;
- role expectations;
- user capability and literacy assumptions;
- risk, urgency, and responsibility constraints;
- intended future search and reconstruction needs.

These requirements may originate from large-scale Situation context, but Projection does not simply contain the entire Situation Vector.

Projection exists partly because Situation space is effectively unbounded, while IdeaMark generation and retrieval require finite, reusable strategies that can complete in finite steps.

Projection therefore serves as a practical boundary between unbounded Situation interpretation and finite Decomposition of Original Sources.

## Projection and Decomposition

Part 3 defines Decomposition as the Projection-guided modeling act that produces IdeaMark Core Model structures.

Part 5 defines how Projection describes the requirements, assumptions, strategies, and evaluation criteria that guide such Decomposition.

```text
Situation Observation
        ↓
Situation Vector
        ↓
Projection Selection / Generation
        ↓
Projection
        ↓
Decomposition of Original Source
        ↓
IdeaMark Document
```

The Situation Vector may inform Projection selection or generation.

However, Projection should remain separable from both the particular Situation and the generated IdeaMark document so that it can be reused, compared, governed, refined, shared, or kept private.

## Projection Libraries

Projection Libraries are collections of reusable Projections.

They are not merely template catalogs.

They may function as repositories of accumulated interpretation-cost reduction strategies.

A Projection Library may help users and AI systems act effectively even when the immediate subject does not fully understand all layers of law, custom, domain practice, organizational procedure, or expert reasoning required to create a Projection from scratch.

Projection Library use can therefore reduce interpretation cost and allow practical use to begin earlier.

Repeated use may generate feedback, which may then lead to finer-grained, more intentional, and higher-quality Projections.

## Private and Shared Projection

A Projection may be private, organizational, domain-specific, public, experimental, deprecated, or standardized.

Sharing a Projection can increase organizational or social capability when it helps many participants reduce interpretation cost and coordinate reconstruction.

However, some Projections may remain private because they depend on personal circumstances, confidential organizational practice, legal constraints, strategic value, or sensitive context.

Part 5 should describe how Projection may be reused and referenced without requiring that all Projections be public.

## Proposed Sections

0. Projection Overview
1. Projection as Reuse Strategy
2. Projection as Requirement Bundling
3. Projection and Situation Boundary
4. Projection and Decomposition Guidance
5. Projection Metadata
6. Intended Reuse Context
7. Search and Reconstruction Tasks
8. Entity Decomposition Strategy
9. Occurrence Strategy
10. Section Strategy
11. Relation and Coordinate Preferences
12. Source Coverage Policy
13. Evaluation Criteria
14. Projection Versioning and Lifecycle
15. Projection Libraries and Templates
16. Private, Shared, and Institutional Projection
17. Projection Non-goals
18. Projection Examples

## Relationship to Core

Projection is not part of the Core in the strict sense.

However, IdeaMark Core must be able to record which Projection or Projection Context guided Decomposition and authoring.

The same Original Source may have multiple valid Projections, and those Projections may produce different IdeaMark documents.

Part 3 defines the Core Model output of Projection-guided Decomposition.

Part 5 defines the Projection-side responsibilities that make such Decomposition reusable, inspectable, and improvable.

## Scope

Part 5 should define how Projection describes reuse strategy, requirement bundling, Decomposition guidance, intended reconstruction tasks, evaluation criteria, lifecycle, and library use.

It should not redefine Core objects, YAML validation rules, retrieval algorithms, or domain-specific vocabularies unless they are explicitly declared as Projection-specific.

Part 5 also should not require that every Projection be fully formal, public, standardized, or authored by experts.

A Projection may be carefully designed, gradually cultivated, AI-generated, experimentally discovered, or accidentally retained because it works.
