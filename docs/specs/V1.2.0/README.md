# IdeaMark Core Specification v1.2.0

**Status:** Draft

IdeaMark Core v1.2.0 is organized as an RFC-like specification library.

Each part is written as an independently reviewable document set with design rationale, non-goals, and future work where appropriate.

## Parts

1. [Part 1 — Philosophy](./part1-philosophy/README.md)
2. [Part 2 — Architecture of Human-AI Co-evolution](./part2-architecture/README.md)
3. [Part 3 — Core Model](./part3-core-model/README.md) *(initial specification draft complete)*
4. [Part 4 — Core Specification](./part4-core-specification/README.md) *(initial specification draft complete)*
5. [Part 5 — Projection Specification](./part5-projection-specification/README.md) *(initial specification draft complete)*
6. [Part 6 — Authoring Guide](./part6-authoring-guide/README.md) *(initial guide draft complete)*

## Design Policy

- Prefer RFC-like clarity over terse schema-only descriptions.
- Record design rationale alongside concepts.
- Separate normative specification from informative background.
- Treat IdeaMark as an evolving intellectual activity infrastructure rather than a fixed knowledge representation format.
- Treat human-AI co-evolution as a central architectural motivation rather than a secondary usage pattern.
- Treat Projection as a reuse strategy and reusable intellectual asset.
- Keep meanings, goals, vocabularies, coordinate systems, workflows, and implementations outside the Core whenever possible.
- Treat Interpretation Cost Reduction as a design rationale for reusable access structures and Projection use.
- Treat Authoring as knowledge reuse design rather than generic summarization or YAML editing.

## Drafting Order

1. Part 1 — Philosophy
2. Part 2 — Architecture of Human-AI Co-evolution
3. Part 3 — Core Model
4. Part 5 — Projection Specification
5. Part 4 — Core Specification
6. Part 6 — Authoring Guide

Part 4 intentionally follows Parts 3 and 5 so that the YAML representation encodes the settled conceptual model and Projection boundary rather than driving them.

Part 6 follows Part 4 so that authoring guidance can use the settled Core Model, Projection boundary, and Part 4 array-based representation without redefining Core conformance.

## Current Focus

Parts 1 through 6 now have initial drafts.

The current focus should shift from expanding the specification text to review, terminology alignment, Part 4 sample verification, and implementation planning for IdeaMark CLI and related authoring tools.
