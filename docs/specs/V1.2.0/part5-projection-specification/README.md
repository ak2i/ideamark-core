# Part 5 — Projection Specification

**Version:** IdeaMark Core v1.2.0  
**Status:** Initial Specification Draft Started

Part 5 defines Projection as an external but interoperable specification for guiding Decomposition, retrieval, matching, filtering, and reconstruction.

Projection is a reusable transformation key for making Original Sources, IdeaMark documents, and future activation expressions usable in Human-AI Intellectual Activity.

Projection should be treated as a reusable intellectual asset, not merely a prompt parameter.

## Scope

Part 5 defines the responsibilities of Projection-side specifications.

It describes how a Projection may express:

- intended reuse purpose;
- requirement bundles;
- Situation boundaries;
- Decomposition guidance;
- retrieval and matching intent;
- reconstruction guidance;
- evaluation criteria;
- metadata, lifecycle, and library use;
- progressive authoring engine boundaries.

Part 5 does not define the concrete YAML representation of IdeaMark documents. That belongs to Part 4.

Part 5 also does not define retrieval algorithms, ranking systems, organizational governance rules, legal taxonomies, domain vocabularies, universal coordinate systems, progressive authoring algorithms, or Progressive Occurrence Resolution internals. Those may be supplied by implementations, Projection Libraries, companion specifications, or domain practices.

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

## Sections

0. [Projection Overview](./00-projection-overview.md) *(drafted)*
1. [Projection as Reuse Strategy](./01-projection-as-reuse-strategy.md) *(drafted)*
2. [Projection as Requirement Bundling](./02-projection-as-requirement-bundling.md) *(drafted)*
3. [Projection as Bidirectional Transformation Key](./03-bidirectional-transformation-key.md) *(drafted)*
4. [Projection and Situation Boundary](./04-projection-and-situation-boundary.md) *(drafted)*
5. [Projection and Decomposition Guidance](./05-decomposition-guidance.md) *(drafted)*
6. [Projection Retrieval, Matching, and Compatibility](./06-retrieval-matching-and-compatibility.md) *(drafted)*
7. [Projection-guided Reconstruction](./07-projection-guided-reconstruction.md) *(drafted)*
8. [Projection Metadata, Lifecycle, and Libraries](./08-metadata-lifecycle-and-libraries.md) *(drafted)*
9. [Projection Non-goals and Open Issues](./09-non-goals-and-open-issues.md) *(drafted)*
10. [Projection Profile](./10-projection-profile.md) *(drafted)*
11. [Projection Compatibility Model](./11-compatibility-model.md) *(drafted)*
12. [Projection Evaluation](./12-projection-evaluation.md) *(drafted)*
13. [Progressive Authoring Engines and POR Boundary](./13-progressive-authoring-engines-and-por-boundary.md) *(drafted)*

## Relationship to Core

Projection is not part of the Core in the strict sense.

However, IdeaMark Core must be able to record which Projection or Projection Context guided Decomposition and authoring.

The same Original Source may have multiple valid Projections, and those Projections may produce different IdeaMark documents.

The same IdeaMark document may later be reused under a different Projection when sufficient compatibility, partial match, or transformability exists.

Part 3 defines the Core Model output of Projection-guided Decomposition.

Part 5 defines the Projection-side responsibilities that make such Decomposition, retrieval, matching, filtering, and reconstruction reusable, inspectable, and improvable.

## Relationship to Progressive Occurrence Resolution

Progressive Occurrence Resolution, abbreviated as POR in the IdeaMark ecosystem, is a companion mechanism for stateful progressive Decomposition of large, streaming, composite, or difficult Original Sources.

Part 5 recognizes that progressive authoring engines may consume Projection as input and emit IdeaMark-compatible structures as output.

Part 5 does not define POR algorithms, internal IR, session state, LLM orchestration, context-force reinterpretation, or progressive scheduling.

Those responsibilities belong to the IdeaMark-POR repository or another companion specification.

## Reading Notes

Part 5 should be read after Part 3.

Part 3 explains that Section, Occurrence, and Entity are Projection-shaped Core Model structures.

Part 5 explains what kinds of responsibilities a Projection may carry so that those structures can be generated, searched, matched, filtered, reconstructed, evaluated, shared, versioned, or kept private.

The key design constraint is that Projection should reduce interpretation cost without pretending to contain the whole Situation, the whole domain, the final meaning of future activity, or the internal algorithm of a progressive authoring engine.
