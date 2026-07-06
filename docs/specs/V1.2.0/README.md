# IdeaMark Core Specification v1.2.0

**Status:** Draft

IdeaMark Core v1.2.0 is organized as an RFC-like specification library.

Each part is written as an independently reviewable document set with design rationale, non-goals, and future work where appropriate.

## Parts

1. [Part 1 — Philosophy](./part1-philosophy/README.md)
2. [Part 2 — Architecture of Human-AI Co-evolution](./part2-architecture/README.md)
3. [Part 3 — Core Model](./part3-core-model/README.md) *(initial specification draft complete)*
4. [Part 4 — Core Specification](./part4-core-specification/README.md) *(planned)*
5. [Part 5 — Projection Specification](./part5-projection-specification/README.md) *(initial specification draft started)*
6. [Part 6 — Authoring Guide](./part6-authoring-guide/README.md) *(planned)*

## Design Policy

- Prefer RFC-like clarity over terse schema-only descriptions.
- Record design rationale alongside concepts.
- Separate normative specification from informative background.
- Treat IdeaMark as an evolving intellectual activity infrastructure rather than a fixed knowledge representation format.
- Treat human-AI co-evolution as a central architectural motivation rather than a secondary usage pattern.
- Treat Projection as a reuse strategy and reusable intellectual asset.
- Keep meanings, goals, vocabularies, coordinate systems, workflows, and implementations outside the Core whenever possible.
- Treat Interpretation Cost Reduction as a design rationale for reusable access structures and Projection use.

## Drafting Order

The recommended drafting order is:

1. Part 1 — Philosophy
2. Part 2 — Architecture of Human-AI Co-evolution
3. Part 3 — Core Model
4. Part 5 — Projection Specification
5. Part 4 — Core Specification
6. Part 6 — Authoring Guide

Part 4 is intentionally drafted after the conceptual model and Projection responsibilities are clearer, because the YAML representation should encode the model rather than prematurely define it.

## Current Focus

Part 1 and Part 2 are drafted as the philosophical and architectural foundation.

Part 3 is complete enough for consistency review and transition planning toward Part 4.

The current drafting focus is Part 5 — Projection Specification, so that Projection responsibilities, compatibility, reconstruction, lifecycle, and library boundaries are clear before the concrete Core YAML representation is finalized.
