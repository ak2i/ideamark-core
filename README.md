# IdeaMark Core

IdeaMark Core is a payload-agnostic meaning-structure framework for organizing, retrieving, reprojecting, and recomposing reusable traces of intellectual activity.

It is not a command-line tool, application framework, or knowledge-representation format. This repository provides the official IdeaMark Core specifications, design philosophy, conceptual model, constraints, examples, and official template library.

## What IdeaMark Is

IdeaMark starts from the hypothesis that meaning is not stored directly in text or data. Meaning emerges through structured interpretation.

IdeaMark therefore preserves reusable traces of meaning-making rather than attempting to preserve meaning itself. These traces can later be retrieved, reinterpreted, recomposed, and projected into new contexts.

In short:

> IdeaMark does not define meaning.  
> It defines the conditions under which meaning can emerge without collapsing into chaos.

## Core Positioning

IdeaMark Core separates the following concerns:

| Concern | Role in IdeaMark |
|---|---|
| Representation | External payload such as Markdown, YAML, JSON, OKF, TPCG, or other formats |
| Entity | Boundary of a reusable trace of meaning-making |
| Occurrence | Contextual activation of an Entity within intellectual activity |
| Section | Local interpretation boundary that groups Occurrences |
| Perspective | Reusable trace of projection / interpretive direction |
| Relations | Graph structure connecting IdeaMark units |
| Constraints | Structural validation without constraining meaning |

This separation allows IdeaMark to work across heterogeneous knowledge formats without requiring a single universal representation format.

## What This Repository Contains

This repository is intended to provide:

- IdeaMark Core specifications
- Core philosophy and design rationale
- Core model definitions
- Structural constraints and validation boundaries
- Official examples
- Official template library
- Notes on applications and usage patterns

This repository intentionally does **not** provide:

- CLI commands
- GUI applications
- server implementations
- validators as executable tools
- application-specific payload processors

Tooling may be built in separate repositories on top of IdeaMark Core.

## Current Specification

The current active design-stage specification is **IdeaMark Core v1.1.1**.

Primary specification documents:

- [`docs/specs/V1.1.1/ideamark-core-spec-v1.1.1.md`](docs/specs/V1.1.1/ideamark-core-spec-v1.1.1.md) — integrated core specification
- [`docs/specs/V1.1.1/ideamark-core-philosophy-v1.1.1.md`](docs/specs/V1.1.1/ideamark-core-philosophy-v1.1.1.md) — philosophy and design hypothesis
- [`docs/specs/V1.1.1/ideamark-core-model-v1.1.1.md`](docs/specs/V1.1.1/ideamark-core-model-v1.1.1.md) — core structural model
- [`docs/specs/V1.1.1/ideamark-core-constraints-v1.1.1.md`](docs/specs/V1.1.1/ideamark-core-constraints-v1.1.1.md) — validation and structural constraints

## Core Model Overview

### Entity

An Entity is the fundamental reusable meaning-boundary unit.

It does not own or preserve meaning itself. Instead, it defines the boundary of a reusable trace of meaning-making. Entity identity is independent from payload identity.

Entities are payload-agnostic and may reference plain text, Markdown, OKF, TPCG, JSON, YAML, or future formats.

### Occurrence

An Occurrence activates an Entity within a specific intellectual activity.

It records how an Entity functioned within a meaning-making process. The same Entity may participate in multiple Occurrences with different roles such as claim, evidence, observation, assumption, objective, or constraint.

### Section

A Section groups Occurrences into an interpretable unit.

It is the primary local interpretation boundary. A Section defines how a set of Occurrences should be read together.

### Perspective

Perspective is not meaning itself.

It records reusable clues regarding interpretive direction. It is a trace of projection, not a guarantee that future readers will derive identical meaning.

### Relations

Relations connect structured IdeaMark units and form the graph structure of an IdeaMark document.

Relations may connect Entities or Sections depending on the document design.

## Payload-Agnostic Design

IdeaMark Core is responsible for structure, not payload semantics.

It constrains:

- Entity boundaries
- Occurrence activation
- Section interpretation
- Perspective guidance
- Relation structure

It does not constrain:

- payload meaning
- payload correctness
- payload profile semantics
- external resource existence
- URI reachability
- selector interpretation

Payload-specific processing belongs to profile-specific tooling or downstream applications.

## Minimal Structural Shape

An IdeaMark document must contain the following top-level structures:

```yaml
entities:
  E1:
    kind: claim
    payload:
      body: "Meaning is not stored directly in text."
    atomicity_basis: interpretive

occurrences:
  O1:
    entity: E1
    role: claim

sections:
  S1:
    title: "Core hypothesis"
    occurrences: [O1]
```

Relations and perspectives are optional in Core, although they are important for richer reuse and interpretation.

## Validation Boundary

IdeaMark Core validation guarantees structural integrity while preserving interpretive flexibility.

Core validation checks:

- required structures
- reference integrity
- identifier uniqueness
- occurrence completeness
- section completeness
- entity payload presence
- payload reference shape

Core validation does not check whether a payload is true, meaningful, reachable, semantically correct, or valid under an external profile.

## Design Status

IdeaMark Core v1.1.1 is an active design-stage specification.

The v1.1.x series emphasizes:

- representation independence
- payload-agnostic structure
- controlled divergence of interpretation
- reusable traces of intellectual activity
- separation of meaning boundary, contextual activation, and interpretive direction

Formal migration rules are outside the current Core specification and are considered tooling concerns.

## License

See the repository license file for licensing terms.
