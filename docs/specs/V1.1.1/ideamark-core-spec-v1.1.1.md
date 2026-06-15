# IdeaMark Core Specification v1.1.1

## 0. Version Positioning

This document integrates the v1.1.1 Core Philosophy, Core Model, and Core Constraints.

Scope:

- Core Philosophy
- Perspective
- Entity
- Occurrence
- Section
- Relations
- Validation / Constraints

Status:

- Draft Specification v1.1.1

Key change from v1.1.0:

> IdeaMark is not a knowledge-representation format.
> IdeaMark is a payload-agnostic meaning-structure framework for reusing traces of intellectual activity.

---

## 1. Core Philosophy

### 1.1 Core Hypothesis

> Meaning is not stored in text itself.
> Meaning emerges through structured interpretation.

### 1.2 Representation Independence

> Representation is not Meaning.

IdeaMark standardizes reusable structure rather than representation formats.

### 1.3 Meaning Is Not Stored

> Meaning is not preserved.
> Only reusable traces of meaning-making are preserved.

### 1.4 Formal Model

Reality → Projection → Log → IdeaMark Structure → Projection → New Meaning

### 1.5 Log-Centric Knowledge Reuse

IdeaMark treats documents as records of intellectual activity.

Examples:

- conversations
- reports
- essays
- observations
- plans
- analyses

IdeaMark preserves reusable structural traces rather than original meanings.

### 1.6 Payload-Agnostic Core

Payload formats are external concerns.

IdeaMark is responsible for:

- Entity boundaries
- Occurrence activation
- Section interpretation
- Perspective guidance
- Relation structure

### 1.7 Core Positioning

> A payload-agnostic meaning-structure framework for organizing,
> retrieving, reprojecting, and recomposing reusable traces of intellectual activity.

---

## 2. Perspective

### 2.1 Positioning

Perspective does not define meaning.

Instead:

> Perspective is a reusable trace of projection.

Perspective records clues regarding interpretive direction.

### 2.2 Schema

```yaml
perspectives:
  {perspective_id}:
    description: string
    base: perspective_ref
    modifiers: [string, ...]
```

### 2.3 Perspective Scope

Perspective MAY exist at:

- document level
- section level
- entity extraction level

Perspective does not guarantee future meaning outcomes.

---

## 3. Entity

### 3.1 Positioning

Entity is the fundamental reusable meaning-boundary unit.

> Entity defines the boundary of a reusable trace of meaning-making.

### 3.2 Atomicity

Atomicity depends on:

- Perspective
- POR
- Intended reuse

### 3.3 Payload-Agnostic Entity

Entities MAY reference:

- Markdown
- OKF
- TPCG
- JSON
- YAML
- future formats

### 3.4 Entity Schema

```yaml
entities:
  {entity_id}:
    kind: string

    payload:
      format:
        media_type: string
        profile: string
        version: string
        definition_ref: uri

      body: string

      ref:
        uri: string
        selector: string

      cache:
        body: string
        captured_at: datetime
        source_hash: string

    atomicity_basis: interpretive | lexical | structural
    perspective_scope: [perspective_ref, ...]
```

### 3.5 Identity

Entity identity is independent from payload identity.

---

## 4. Occurrence

### 4.1 Positioning

Occurrence activates an Entity within a specific intellectual activity.

> Occurrence records how an Entity functioned within a meaning-making process.

### 4.2 Schema

```yaml
occurrences:
  {occurrence_id}:
    entity: entity_ref
    role: string
```

### 4.3 Examples

Roles MAY include:

- claim
- evidence
- observation
- assumption
- objective
- constraint

---

## 5. Section

### 5.1 Positioning

Section is the primary interpretation boundary.

> Section defines how a set of occurrences should be read together.

### 5.2 Schema

```yaml
sections:
  {section_id}:
    title: string
    perspectives: [perspective_ref, ...]
    anchorage:
      view: [string, ...]
      phase: [string, ...]
    occurrences: [occurrence_ref, ...]
```

---

## 6. Relations

### 6.1 Positioning

Relations connect structured units.

> Relations form the graph structure of IdeaMark.

### 6.2 Schema

```yaml
relations:
  {relation_id}:
    type: string
    from: reference
    to: reference
```

Supported references:

- entity_ref
- section_ref

---

## 7. Validation / Constraints

### 7.1 Philosophy

Validation constrains structure, not meaning.

### 7.2 Required Structures

Documents MUST contain:

- entities
- occurrences
- sections

### 7.3 Payload Requirements

Each Entity MUST define:

```yaml
payload
```

At least one of:

```yaml
payload.body
payload.ref
payload.cache
```

MUST be present.

### 7.4 Payload Format

Recommendations:

| Field | Requirement |
|---------|---------|
| media_type | SHOULD |
| profile | MAY |
| version | MAY |
| definition_ref | MAY |

### 7.5 References

If:

```yaml
payload.ref
```

exists,

then:

```yaml
ref.uri
```

MUST exist.

`selector` is optional.

### 7.6 Validation Boundary

Core validation DOES validate:

- YAML structure
- references
- completeness

Core validation DOES NOT validate:

- payload meaning
- profile semantics
- external resource existence
- URI reachability
- selector interpretation

---

## 8. Compatibility Note

IdeaMark v1.1.1 is an active design-stage specification.

Formal migration rules are outside the scope of the Core Specification.

Compatibility and migration behavior are considered tooling concerns.

Within the v1.1.x series, differences MAY be resolved through normalization tools or LLM-assisted rewriting.

Future major conceptual changes SHOULD define migration guidance when transitioning across larger version boundaries.
