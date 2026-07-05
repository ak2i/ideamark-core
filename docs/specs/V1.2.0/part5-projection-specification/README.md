# Part 5 — Projection Specification

**Version:** IdeaMark Core v1.2.0  
**Status:** Planning Draft

This part defines Projection as an external but interoperable specification.

Projection is a reusable transformation key for making Original Sources, IdeaMark documents, and future expressions usable in Human-AI Intellectual Activity.

Projection should be treated as a reusable intellectual asset, not merely a prompt parameter.

## Core Stance

Projection is the mechanism that allows multiple layers of requirements to be treated as a finite, reusable strategy for Decomposition, retrieval, matching, filtering, and reconstruction.

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

Projection exists partly because Situation space is effectively unbounded, while IdeaMark generation, retrieval, matching, and reconstruction require finite, reusable strategies that can complete in finite steps.

Projection therefore serves as a practical boundary between unbounded Situation interpretation and finite operations over Original Sources, IdeaMark documents, and activation expressions.

## Projection as Bidirectional Transformation Key

Projection is not used only when generating an IdeaMark document from an Original Source.

It is also used when searching for IdeaMark documents, selecting relevant Original Sources, matching partially compatible structures, filtering candidates, and reconstructing expressions that can support Human-AI Intellectual Activity.

Projection may therefore function in at least four roles:

1. **Decomposition Key** — guides how Original Source material is decomposed into IdeaMark Core Model structures.
2. **Retrieval Key** — helps find IdeaMark documents or Original Sources relevant to a Situation or intended activity.
3. **Matching and Filtering Key** — supports full match, partial match, approximate match, inclusion, specialization, exclusion, or other compatibility judgments among Projections, IdeaMark documents, and sources.
4. **Reconstruction Key** — guides how retrieved materials are transformed into expressions appropriate for a future interpreter, capability level, Situation, or activity.

The Projection used to generate an IdeaMark document and the Projection used later to retrieve or reconstruct from it do not need to be identical.

Useful reuse may occur through partial overlap, compatible intent, shared functional structure, or transformable assumptions.

For example, a Projection used to generate an IdeaMark document about professional cooking technique may later be partially matched by a household-cooking Projection that seeks functional guidance about how to increase umami, substitute ingredients, or adjust taste and texture for a specific dish.

In that case, reuse does not depend on matching the same keyword such as a named ingredient or cooking term.

It depends on whether the generated IdeaMark structures can help retrieve and transform relevant Original Source material for the current intellectual activity.

## Projection and Decomposition

Part 3 defines Decomposition as the Projection-guided modeling act that produces IdeaMark Core Model structures.

Part 5 defines how Projection describes the requirements, assumptions, strategies, compatibility conditions, and evaluation criteria that guide such Decomposition and later reuse.

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

## Projection and Reconstruction

Projection also guides the use side of IdeaMark.

```text
Current Situation
        ↓
Situation Vector
        ↓
Projection Selection / Generation
        ↓
Projection
        ↓
IdeaMark Retrieval / Matching / Filtering
        ↓
Original Source Access
        ↓
Projection-guided Reconstruction
        ↓
Activation Expression
        ↓
Human-AI Intellectual Activity
```

The reconstruction-side Projection may differ from the generation-side Projection.

This difference is expected, not exceptional.

Part 5 should therefore define how Projection can support compatibility, adaptation, and transformation rather than assuming exact identity between generation and use.

## Projection Libraries

Projection Libraries are collections of reusable Projections.

They are not merely template catalogs.

They may function as repositories of accumulated interpretation-cost reduction strategies and transformation keys.

A Projection Library may help users and AI systems act effectively even when the immediate subject does not fully understand all layers of law, custom, domain practice, organizational procedure, or expert reasoning required to create a Projection from scratch.

Projection Library use can therefore reduce interpretation cost and allow practical use to begin earlier.

Repeated use may generate feedback, which may then lead to finer-grained, more intentional, and higher-quality Projections.

A mature Projection Library may preserve not only common decomposition strategies, but also common retrieval, matching, filtering, and reconstruction strategies that have proven useful in practice.

## Private and Shared Projection

A Projection may be private, organizational, domain-specific, public, experimental, deprecated, or standardized.

Sharing a Projection can increase organizational or social capability when it helps many participants reduce interpretation cost and coordinate reconstruction.

However, some Projections may remain private because they depend on personal circumstances, confidential organizational practice, legal constraints, strategic value, or sensitive context.

Part 5 should describe how Projection may be reused and referenced without requiring that all Projections be public.

## Proposed Sections

0. Projection Overview
1. Projection as Reuse Strategy
2. Projection as Requirement Bundling
3. Projection as Bidirectional Transformation Key
4. Projection and Situation Boundary
5. Projection and Decomposition Guidance
6. Projection and Retrieval
7. Projection Matching and Compatibility
8. Projection-guided Reconstruction
9. Projection Metadata
10. Intended Reuse Context
11. Search and Reconstruction Tasks
12. Entity Decomposition Strategy
13. Occurrence Strategy
14. Section Strategy
15. Relation and Coordinate Preferences
16. Source Coverage Policy
17. Evaluation Criteria
18. Projection Versioning and Lifecycle
19. Projection Libraries and Templates
20. Private, Shared, and Institutional Projection
21. Projection Non-goals
22. Projection Examples

## Relationship to Core

Projection is not part of the Core in the strict sense.

However, IdeaMark Core must be able to record which Projection or Projection Context guided Decomposition and authoring.

The same Original Source may have multiple valid Projections, and those Projections may produce different IdeaMark documents.

The same IdeaMark document may later be reused under a different Projection when sufficient compatibility, partial match, or transformability exists.

Part 3 defines the Core Model output of Projection-guided Decomposition.

Part 5 defines the Projection-side responsibilities that make such Decomposition, retrieval, matching, filtering, and reconstruction reusable, inspectable, and improvable.

## Scope

Part 5 should define how Projection describes reuse strategy, requirement bundling, Decomposition guidance, retrieval intent, matching and compatibility behavior, intended reconstruction tasks, evaluation criteria, lifecycle, and library use.

It should not redefine Core objects, YAML validation rules, retrieval algorithms, or domain-specific vocabularies unless they are explicitly declared as Projection-specific.

Part 5 also should not require that every Projection be fully formal, public, standardized, or authored by experts.

A Projection may be carefully designed, gradually cultivated, AI-generated, experimentally discovered, or accidentally retained because it works.
