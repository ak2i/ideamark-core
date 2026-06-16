# IdeaMark Concepts

This section explains the core concepts behind IdeaMark in a reader-friendly form.

The formal specification lives under [`docs/specs/V1.1.1`](../specs/V1.1.1/). This directory is intended for conceptual guides that help readers understand why the model exists and how its parts fit together.

## Central Idea

IdeaMark is a framework for reusing how people think, not just what they wrote.

It does not treat documents as containers of fixed meaning. Instead, it treats them as logs of meaning-making activity.

```text
Reality -> Projection -> Log -> IdeaMark Structure -> Projection -> New Meaning
```

IdeaMark preserves reusable structure so that future readers, tools, and AI systems can generate meaning again in new contexts.

## Key Concepts

Future concept guides may include:

- `meaning-reuse.md` — why IdeaMark reuses meaning-making traces rather than stored meaning
- `projection-and-perspective.md` — how Projection and Perspective differ
- `entity-occurrence-section.md` — why IdeaMark separates reusable boundaries, contextual activation, and interpretation boundaries
- `payload-agnostic-core.md` — how IdeaMark works with heterogeneous payload formats
- `controlled-divergence.md` — why meaning may vary while remaining structurally guided

## Relationship to the Specification

Concept documents should explain the model without replacing the specification.

Use the specification for normative definitions:

- [`ideamark-core-philosophy-v1.1.1.md`](../specs/V1.1.1/ideamark-core-philosophy-v1.1.1.md)
- [`ideamark-core-model-v1.1.1.md`](../specs/V1.1.1/ideamark-core-model-v1.1.1.md)
- [`ideamark-core-constraints-v1.1.1.md`](../specs/V1.1.1/ideamark-core-constraints-v1.1.1.md)
- [`ideamark-core-spec-v1.1.1.md`](../specs/V1.1.1/ideamark-core-spec-v1.1.1.md)
