# IdeaMark Core Specification v1.1.2

## 0. Version Positioning

This document integrates the v1.1.2 Core Philosophy, Core Model, and Core Constraints.

Scope:

- Core Philosophy
- Perspective
- Entity
- Occurrence
- Section
- Relations
- Validation / Constraints

Status:

- Draft Specification v1.1.2

Key changes from v1.1.1:

- Core registries use ordered list-style ID-bearing records as the canonical YAML representation.
- Occurrence may activate one or more Entities through `entity_roles`.
- Single-Entity `entity` + `role` occurrences remain valid shorthand.
- Mapping-style registries from v1.1.1 may be accepted as compatibility input by tooling.

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
  - id: perspective_id
    description: string
    base: perspective_ref
    modifiers: [string, ...]
```

Perspective records are ID-bearing list items in canonical v1.1.2 YAML.

### 2.3 Perspective Scope

Perspective MAY exist at:

- document level
- section level
- entity extraction level

Perspective does not guarantee future meaning outcomes.

### 2.4 Perspective Reference Resolution

perspective_ref appears in:

- perspectives.{id}.base
- sections.{id}.perspectives
- entities.{id}.perspective_scope

A bare perspective_ref SHOULD resolve to a perspective defined in the same document.

An unresolved bare perspective_ref is NOT an error. Implementations SHOULD report it as a warning.

External reference forms are opaque to Core validation.

Reference integrity (§7.4) intentionally excludes perspective_ref: perspectives are interpretive clues, not structural references.

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
  - id: entity_id
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

Occurrence activates one or more Entities within a specific intellectual activity.

> Occurrence records how one or more Entities functioned together within a meaning-making process.

Occurrence is a contextual activation layer. It is not merely an appearance record.

### 4.2 Schema

Canonical multi-Entity form:

```yaml
occurrences:
  - id: occurrence_id
    role: string
    entity_roles:
      - entity: entity_ref
        role: string
    context:
      body: string
```

Single-Entity shorthand form:

```yaml
occurrences:
  - id: occurrence_id
    entity: entity_ref
    role: string
```

The shorthand form is valid and MAY be normalized into `entity_roles`.

### 4.3 Examples

Roles MAY include:

- claim
- evidence
- observation
- assumption
- objective
- constraint
- explanation
- recommendation

---

## 5. Section

### 5.1 Positioning

Section is the primary interpretation boundary.

> Section defines how a set of occurrences should be read together.

### 5.2 Schema

```yaml
sections:
  - id: section_id
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
  - id: relation_id
    type: string
    from: reference
    to: reference
```

Supported references:

- entity_ref
- section_ref

### 6.3 Reference Resolution

A reference in `from` / `to` MAY be written in a typed form or as a bare identifier.

- A typed reference form (as defined by tooling, addressing `entities/...` or `sections/...`) resolves within the indicated namespace.
- A bare identifier resolves against the entity namespace first, then the section namespace.
- An identifier present in both namespaces is ambiguous: implementations SHOULD report the ambiguity, and authors SHOULD disambiguate using a typed reference form.

Canonicalizing tools SHOULD rewrite bare identifiers into typed reference forms following the same resolution order.

---

## 6.4 Registry Representation

In v1.1.2, canonical registries are ordered lists of ID-bearing records.

Examples:

```yaml
entities:
  - id: ENT-001
    kind: instrument
    payload:
      body: "..."

occurrences:
  - id: OCC-001
    entity: ENT-001
    role: evidence

sections:
  - id: SEC-001
    title: "..."
    occurrences:
      - OCC-001
```

Processors MUST build internal ID indexes for reference resolution.

Mapping-style registries from v1.1.1 MAY be accepted as compatibility input, but canonical v1.1.2 output SHOULD use list-style registries.

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

IdeaMark v1.1.2 is an active design-stage specification.

Formal migration rules are outside the scope of the Core Specification.

Compatibility and migration behavior are considered tooling concerns.

Within the v1.1.x series, differences MAY be resolved through normalization tools or LLM-assisted rewriting.

Future major conceptual changes SHOULD define migration guidance when transitioning across larger version boundaries.

---

## 9. Document Identity and External References

Logically this section extends §3.5 Identity and §7.6 Validation Boundary.

### 9.1 Document Identity

Every IdeaMark document declares a document identifier:

```yaml
doc_id: string
```

- `doc_id` is an opaque string. Core does not prescribe its internal structure: a human-readable name, a UUID, or an authority-qualified path are all equally valid.
- `doc_id` is immutable once assigned. Canonicalization bakes `doc_id` into every reference, so changing it breaks both internal canonical references and inbound references from other documents.
- The uniqueness scope of `doc_id` is its resolution context (a corpus, a repository, a registry). Guaranteeing uniqueness within that scope is the responsibility of the corpus operator or registry, not of Core validation.
- Documents intended for publication or global registration SHOULD use collision-resistant identifiers (e.g. UUID).
- Display naming belongs to other fields; `doc_id` is an identifier, not a title.

### 9.2 Canonical External Reference Form

The canonical form for referencing an element of a document is:

```
ideamark://docs/{doc_id}#/{entities|occurrences|sections|perspectives}/{element_id}
```

A shorthand form MAY be used where element type information is not needed:

```
{doc_id}#{element_id}
```

Element identity across documents is determined by exact string comparison of the `(doc_id, element_id)` pair.

- No URI normalization is applied.
- No equivalence inference (sameAs-style entity resolution) is performed.

> Referencing the same `(doc_id, entity_id)` pair activates the same Entity.
> Copying a payload under a new id creates a different Entity.

This is the normative expression of authorial identity declaration: identity is declared by reference, never inferred.

### 9.3 Resolution

Resolving a `doc_id` to a document instance is outside Core.

A local corpus index and a global registry are different resolvers for the same reference syntax; documents move between contexts without rewriting.

External references are opaque to Core validation: no existence, reachability, or type checks are performed (§7.6 Validation Boundary).

Other URI schemes MAY appear in reference positions. They are opaque to Core and outside the identity comparison rule of §9.2.
