# Part 2 — Architecture of Human-AI Co-evolution

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

This part describes the reference architecture through which humans, AI systems, Projections, IdeaMark documents, retrieval systems, and Original Sources may participate in continuous co-evolution.

In this specification, co-evolution means the continuous mutual development of humans and AI through shared intellectual activities grounded in Original Sources treated as authoritative for a given Projection.

Part 1 explains why IdeaMark uses engineering through separation: reusable structure is separated from meaning so that it can be managed and reused without fixing interpretation.

Part 2 explains engineering through reconstruction at the ecosystem level.

## Sections

0. [Architectural Overview](./00-architectural-overview.md)
1. [Two-plus-one Layer Model](./01-two-plus-one-layer-model.md)
2. [Index Construction Layer](./02-index-construction-layer.md)
3. [Projection Libraries and Projection Selection](./03-projection-libraries-and-projection-selection.md)
4. [IdeaMark Generation and Repository Construction](./04-ideamark-generation-and-repository-construction.md)
5. [On-demand Generation and Background Generation](./05-on-demand-generation-and-background-generation.md)
6. [Situation Interpretation Layer](./06-situation-interpretation-layer.md)
7. [Situation-driven Reconstruction Layer](./07-reconstruction-layer.md)
8. [Original Source Open-hand Principle](./08-original-source-open-hand-principle.md)
9. [Human-AI Intellectual Activity](./09-human-ai-intellectual-activity.md)
10. [Situation Evolution and Ecosystem Feedback](./10-situation-evolution-and-ecosystem-feedback.md)
11. [Capability-Oriented Human-AI Co-evolution](./11-capability-oriented-human-ai-co-evolution.md)
12. [Architectural Boundaries and Non-prescription](./12-architectural-boundaries-and-non-prescription.md)
13. [Architecture Summary](./13-architecture-summary.md)

## Reading Notes

This part defines a reference architecture for explaining how IdeaMark may be used.

It does not prescribe a required system implementation, retrieval interface, Projection selection method, database architecture, storage engine, indexing algorithm, queueing system, user interface, governance process, or internal knowledge-management product.

When this part uses terms such as index, indexing, or index construction, those terms refer to the architectural role of IdeaMark documents as reusable access structures.

They do not define how an implementation should create database indexes or optimize storage-level search.

IdeaMark documents may be used index-like because they help future humans and AI systems find relevant Original Sources and reconstruct intellectual activity through a selected or generated Projection.

Part 2 defines roles and connections rather than the complete contents of future intellectual activities.

This non-prescriptive boundary is intentional: Original Source, Observation, Situation Vector, Projection, Human-AI Intellectual Activity, Feedback, and Capability must remain open enough to support future media, future AI systems, future social practices, and future knowledge representations.

A major design rationale of this part is interpretation cost reduction. IdeaMark does not preserve one final interpretation; it provides reusable access structures and Projections that can reduce the cost of creating, understanding, reviewing, maintaining, teaching, and reusing intellectual work.
