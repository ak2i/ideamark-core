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
- universal domain vocabularies;
- universal coordinate systems;
- universal authority rankings;
- a taxonomy of all intellectual activities.

Those belong to later parts, companion specifications, implementations, Projections, or domain practices.

## Draft Sections

0. [Core Model Overview](./00-core-model-overview.md) *(planned)*
1. [Model Boundary and Non-goals](./01-model-boundary-and-non-goals.md) *(planned)*
2. [Original Source Reference Model](./02-original-source-reference-model.md) *(planned)*
3. [Projection Context Model](./03-projection-context-model.md) *(planned)*
4. [IdeaMark Document Model](./04-ideamark-document-model.md) *(planned)*
5. [Entity Model](./05-entity-model.md) *(planned)*
6. [Occurrence Model](./06-occurrence-model.md) *(planned)*
7. [Section Model](./07-section-model.md) *(planned)*
8. [Relation Model](./08-relation-model.md) *(planned)*
9. [Perspective and Provenance Model](./09-perspective-and-provenance-model.md) *(planned)*
10. [Anchorage and Traceability Model](./10-anchorage-and-traceability-model.md) *(planned)*
11. [Status, Versioning, and Regeneration Model](./11-status-versioning-and-regeneration-model.md) *(planned)*
12. [Model Invariants](./12-model-invariants.md) *(planned)*
13. [Core Model Summary](./13-core-model-summary.md) *(planned)*

## Drafting Notes

The planning notes for Part 3 are maintained in:

- [Part 3 Drafting Issues](./00-drafting-issues.md)

## Reading Notes

Part 3 should be read after Part 1 and Part 2.

The key design constraint is that the Core Model must define enough structure to support reusable access, traceability, reconstruction, and interoperability while avoiding the temptation to encode final meaning.

Part 3 should therefore model **access structures**, not final interpretations.
