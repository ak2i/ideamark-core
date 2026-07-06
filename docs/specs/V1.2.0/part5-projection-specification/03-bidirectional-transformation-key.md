# 3. Projection as Bidirectional Transformation Key

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## Purpose

This chapter defines Projection as a bidirectional transformation key.

Projection is not only used when generating an IdeaMark document from an Original Source.

It is also used later when a human, AI system, tool, or organization attempts to retrieve, compare, filter, adapt, or reconstruct material for a new Situation.

## Generation-side Use

On the generation side, Projection guides Decomposition.

It may determine:

- which parts of an Original Source are relevant;
- how local source windows should be formed;
- what should become reusable material;
- which roles should be assigned to placements;
- which source anchors are sufficient;
- which metadata should be recorded;
- what should be ignored;
- which uncertainties should remain provisional.

The generation-side Projection shapes the resulting IdeaMark document.

However, the document should not become inseparable from that Projection.

The document should preserve enough traceability and metadata so that later Projections can evaluate whether reuse is possible.

## Use-side Projection

On the use side, a Projection may be selected or generated from the current Situation.

It may express:

- the current activity;
- the intended audience;
- the capability level of the interpreter;
- the risk tolerance;
- the desired expression form;
- the needed depth of source return;
- the matching constraints;
- the acceptable adaptation range.

This use-side Projection may differ from the generation-side Projection.

The difference is expected.

The design goal is not exact Projection identity.

The design goal is to make compatibility, adaptation, and transformation inspectable.

## Bidirectional Flow

A simplified flow is:

```text
Original Source
    x
Generation Projection
    ↓
Projection-guided Decomposition
    ↓
IdeaMark Document
    x
Use-side Projection
    ↓
Retrieval / Matching / Filtering
    ↓
Projection-guided Reconstruction
    ↓
Activation Expression
```

The generation Projection shapes what is stored as reusable access structure.

The use-side Projection shapes what is selected and reconstructed.

The two Projections meet through compatibility judgments over documents, source references, metadata, anchors, roles, statuses, and reusable material.

## Transformation Types

A Projection MAY support several transformation types:

- **direct transformation** — the use-side Projection is close enough to the generation Projection that little adaptation is needed;
- **specialization** — the use-side Projection narrows a broader generated structure;
- **generalization** — the use-side Projection abstracts from a more specific generated structure;
- **analogical transformation** — the use-side Projection maps structure across domains;
- **capability transformation** — the use-side Projection changes expression to match the interpreter's capability;
- **medium transformation** — the use-side Projection changes the output medium or representation;
- **risk transformation** — the use-side Projection adds warnings, exclusions, or review requirements.

Part 5 does not require all Projections to support all transformation types.

A Projection SHOULD state which transformation types are intended when they materially affect reuse.

## Compatibility Rather Than Equality

Projection equality is usually too strict.

Two Projections may be useful together even when they differ in audience, domain, level of detail, source coverage, or reconstruction form.

A Projection compatibility judgment may consider:

- shared purpose;
- compatible reusable unit strategy;
- compatible source coverage;
- compatible risk assumptions;
- compatible audience assumptions;
- transformable terminology;
- traceability sufficiency;
- absence of blocking exclusions.

A Projection SHOULD distinguish between exact match, partial match, approximate match, and incompatible match when such distinctions affect reconstruction quality.

## Failure Modes

Projection mismatch may cause:

- retrieval of irrelevant documents;
- exclusion of useful documents;
- unsafe adaptation;
- overconfident reconstruction;
- loss of source traceability;
- excessive simplification;
- excessive detail;
- misunderstanding of domain constraints;
- hidden shift in responsibility.

A mature Projection or Projection Library SHOULD record known mismatch risks.
