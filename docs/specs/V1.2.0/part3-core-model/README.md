# Part 3 — Core Model

**Version:** IdeaMark Core v1.2.0  
**Status:** Planning Draft

Part 3 defines the conceptual model of IdeaMark Core.

Part 1 explains why IdeaMark exists.

Part 2 explains the reference architecture for Human-AI Intellectual Activity and reconstruction.

Part 3 explains what conceptual objects IdeaMark Core needs in order to function as reusable access structures without storing final meaning.

## Scope

Part 3 is conceptual.

It should define model roles, relationships, and constraints before YAML representation is specified in Part 4.

Part 3 should not define:

- concrete YAML syntax;
- validation schema details;
- storage architecture;
- retrieval algorithms;
- Projection authoring workflows;
- Projection quality evaluation;
- Projection library governance;
- universal domain vocabularies;
- universal coordinate systems;
- universal authority rankings;
- a taxonomy of all intellectual activities.

Those belong to later parts, companion specifications, implementations, Projections, or domain practices.

## Core Modeling Stance

IdeaMark generation is not a general extraction task performed on an Original Source in isolation.

An IdeaMark document becomes useful only when an Original Source is decomposed under a Projection for expected future reconstruction.

Projection-independent decomposition may be technically possible, but it is not the intended Core model.

Without Projection, an IdeaMark document risks becoming a detached catalog or dictionary-like artifact rather than a living access structure for Human-AI Intellectual Activity.

Part 3 therefore treats Decomposition as the conceptual bridge between Original Source, Projection Context, and the generated structures of an IdeaMark document.

```text
Original Source
        x
Projection Context
        ↓
Decomposition
        ↓
Entity / Occurrence / Section / Relation
```

Part 3 does not evaluate whether a Projection is good, legitimate, widely shareable, or socially valuable.

Part 3 only defines how a Projection-guided Decomposition can produce Core Model structures that remain traceable and reusable.

Projection evaluation, Projection lifecycle, Projection library formation, and Projection governance belong primarily to Part 5.

## Original Source Stance

An Original Source is not limited to a text document or fixed media object.

Anything may be treated as an Original Source if, when viewed through a Projection, it can participate as a component of Human-AI Intellectual Activity.

This may include documents, images, audio, video, source code, datasets, sensor logs, interaction histories, generated artifacts, streams, composites, or future media not yet supported by current tools.

However, practical use requires accessibility.

For an Original Source to be usable in current IdeaMark workflows, humans, AI systems, or supporting tools must be able to observe, reference, transform, or input it sufficiently for Decomposition and later reconstruction.

Something that cannot yet be observed by humans, supplied to AI systems, or converted into an accessible representation may be conceptually eligible as a future Original Source, but it is not practically usable in current IdeaMark authoring or reconstruction.

Part 3 should therefore define Original Source Reference in a media-independent way while preserving the practical requirement that source material must be accessible enough to support traceability and reconstruction.

## Structural Catalyst Stance

The Core Model does not attempt to encode meaning.

Its purpose is to preserve enough reusable structure so that Projection-guided Human-AI Intellectual Activity can efficiently reconstruct meaning from Original Sources.

The three-layer structural pattern of Section, Occurrence, and Entity should therefore be understood primarily as a structural catalyst rather than as a fixed semantic taxonomy.

Their names are historical and descriptive.

The Core intentionally minimizes the functional semantics assigned to them.

A Section does not have to mean a document section, workflow step, chapter, topic, or decision unit.

An Occurrence does not have to mean a textual occurrence, event, instance, or observation.

An Entity does not have to mean a concept, object, actor, term, or knowledge unit.

Those functional interpretations belong to Projection, authoring practice, domain practice, or reconstruction activity.

In the Core Model, Section, Occurrence, and Entity are structural positions that can carry ordering, anchorage, role, relation, and traceability information.

They are useful because they can be separated from both Original Source and Projection while still functioning as keys that help future humans and AI systems reactivate meaning under a Projection.

## Draft Sections

0. [Core Model Overview](./00-core-model-overview.md) *(planned)*
1. [Model Boundary and Non-goals](./01-model-boundary-and-non-goals.md) *(planned)*
2. [Original Source Reference Model](./02-original-source-reference-model.md) *(planned)*
3. [Projection Context Model](./03-projection-context-model.md) *(planned)*
4. [Decomposition Model](./04-decomposition-model.md) *(planned)*
5. [IdeaMark Document Model](./05-ideamark-document-model.md) *(planned)*
6. [Entity Model](./06-entity-model.md) *(planned)*
7. [Occurrence Model](./07-occurrence-model.md) *(planned)*
8. [Section Model](./08-section-model.md) *(planned)*
9. [Relation Model](./09-relation-model.md) *(planned)*
10. [Perspective and Provenance Model](./10-perspective-and-provenance-model.md) *(planned)*
11. [Anchorage and Traceability Model](./11-anchorage-and-traceability-model.md) *(planned)*
12. [Status, Versioning, and Regeneration Model](./12-status-versioning-and-regeneration-model.md) *(planned)*
13. [Model Invariants](./13-model-invariants.md) *(planned)*
14. [Core Model Summary](./14-core-model-summary.md) *(planned)*

## Drafting Notes

The planning notes for Part 3 are maintained in:

- [Part 3 Drafting Issues](./00-drafting-issues.md)

## Reading Notes

Part 3 should be read after Part 1 and Part 2.

The key design constraint is that the Core Model must define enough structure to support reusable access, traceability, reconstruction, and interoperability while avoiding the temptation to encode final meaning.

Part 3 should therefore model **Projection-shaped access structures**, not final interpretations and not Projection-independent extraction results.
