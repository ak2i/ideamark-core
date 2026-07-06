# 9. Entities

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 9.1 Purpose

An Entity represents Projection-shaped reusable material.

An Entity is the reusable object that Occurrences place into Sections with specific roles.

An Entity is not a universal meaning unit, global ontology object, final interpretation, or required semantic atom.

The boundary of an Entity is shaped by the document's authoring purpose, Projection, profile, and reuse context.

## 9.2 Required Shape

`entities` MUST be an array.

Each item in `entities` MUST be a mapping object.

Each Entity object MUST contain an `id` field.

Example:

```yaml
entities:
  - id: ent-001
    kind: claim
    content: Example reusable material.
```

## 9.3 Required Fields

| Field | Type | Requirement |
| --- | --- | --- |
| `id` | string | MUST |

A validator MUST reject an Entity whose `id` is missing, null, empty, or non-string.

A validator MUST reject duplicate Entity IDs within `entities`.

## 9.4 Reusable Material Fields

An Entity SHOULD contain at least one of:

- `content`
- `payload`
- `ref`

unless a profile explicitly permits placeholder Entities.

Example with `content`:

```yaml
entities:
  - id: ent-001
    content: Human-readable reusable material.
```

Example with `payload`:

```yaml
entities:
  - id: ent-002
    kind: structured_observation
    payload:
      metric: latency
      value: 120
      unit: ms
```

Example with `ref`:

```yaml
entities:
  - id: ent-003
    ref: ./external-material.yaml#/items/42
```

## 9.5 `content`

`content` is the simple human-readable text field for reusable material.

When present, `content` SHOULD be a string.

`content` MAY contain natural language, short statements, extracted claims, authored observations, design notes, or other reusable textual material.

Core does not require that `content` be atomic, true, complete, or domain-normalized.

Profiles MAY impose stronger constraints.

## 9.6 `payload`

`payload` is the structured value field.

It MAY contain mapping, array, scalar, or profile-defined structured data.

Example:

```yaml
entities:
  - id: ent-001
    kind: measurement
    payload:
      subject: api_latency
      p50_ms: 120
      p95_ms: 310
      sample_count: 5000
```

`payload` is useful when reusable material is not best represented as a single text string.

Core validators SHOULD preserve payload data.

Core validators MUST NOT require a universal payload schema.

Profiles MAY define payload schemas.

## 9.7 `ref`

`ref` points to externally held reusable material.

Example:

```yaml
entities:
  - id: ent-001
    ref: ideamark://docs/example-source#/entities/external-ent-001
```

`ref` MAY point to:

- another IdeaMark object;
- a source fragment;
- a structured data object;
- a repository object;
- a profile-defined reference target;
- an external URI.

Core validators SHOULD validate that `ref` is a non-empty string when present.

Core validators are not required to dereference external references.

## 9.8 `kind`

`kind` MAY classify the Entity.

Example:

```yaml
entities:
  - id: ent-001
    kind: constraint
    content: The operation depends on a stable external supply chain.
```

`kind` is recommended but not mandatory in Core mode.

Core does not require a universal Entity kind taxonomy.

Entity kind values may be:

- Core-recommended;
- profile-defined;
- Projection-shaped;
- domain-specific;
- document-local.

Core mode validators SHOULD warn on unknown `kind` values only when a profile declares a vocabulary.

Strict mode MAY require profile-declared Entity kinds.

## 9.9 Recommended Entity Kinds

The following kind values are recommended as common starting points:

- `claim`
- `observation`
- `evidence`
- `context`
- `constraint`
- `risk`
- `measure`
- `mechanism`
- `decision`
- `outcome`
- `question`
- `definition`
- `example`
- `pattern`
- `structured_observation`
- `reference`

This list is not exhaustive.

Core validators MUST NOT reject unknown kind values in Core mode solely because they are not listed here.

## 9.10 Entity Status

An Entity MAY include `status`.

Recommended Entity status values are:

- `active`
- `draft`
- `provisional`
- `deprecated`
- `superseded`
- `rejected`

Entity status describes the reusable material itself.

It does not automatically determine the status of Occurrences that reference it.

## 9.11 Entity Anchors

An Entity MAY include `anchors`.

Entity anchors are useful when reusable material is directly traceable to source locations independent of a specific Occurrence.

Example:

```yaml
entities:
  - id: ent-001
    kind: claim
    content: Example reusable claim.
    anchors:
      - source: src-001
        type: line_range
        ranges:
          - start: 10
            end: 12
```

Entity anchors MUST satisfy common anchor requirements.

In many cases, Section or Occurrence anchors are preferable because they preserve local context and role.

## 9.12 Entity Language

An Entity MAY include `lang` when its reusable material language differs from the document default or source language.

Example:

```yaml
entities:
  - id: ent-001
    lang: ja-JP
    content: 再利用可能な知的素材。
```

`lang` SHOULD use a BCP 47 language tag.

Profiles MAY require language declarations for multilingual documents.

## 9.13 Entity Granularity

Core does not define a universal rule for Entity granularity.

Entity boundaries are shaped by reuse purpose and Projection.

An Entity SHOULD be small enough to be reused meaningfully and large enough to preserve the reusable structure intended by the Projection.

Core validators MUST NOT attempt to judge whether an Entity is conceptually atomic.

Profiles, authoring guides, or Projection definitions MAY define granularity rules.

## 9.14 Placeholder Entities

A placeholder Entity has an `id` but lacks `content`, `payload`, and `ref`.

Example:

```yaml
entities:
  - id: ent-placeholder
    status: draft
```

Core mode MAY allow placeholder Entities during draft, template, partial generation, or staged authoring.

Validators SHOULD warn about placeholder Entities.

Strict mode MAY reject placeholder Entities.

Profiles MAY define explicit placeholder behavior.

## 9.15 Entity Replacement

An Entity MAY include replacement metadata as extension or profile-defined fields.

Example:

```yaml
entities:
  - id: ent-002
    content: Revised reusable material.
    supersedes: ent-001
```

Core does not require replacement metadata.

If present, replacement references SHOULD resolve to existing Entity IDs or documented external references.

Profiles MAY define replacement semantics.

## 9.16 Entity Reuse Across Occurrences

The same Entity MAY be referenced by multiple Occurrences.

This is a normal and important use case.

Example:

```yaml
occurrences:
  - id: occ-001
    entity: ent-001
    role: evidence
  - id: occ-002
    entity: ent-001
    role: counterpoint
entities:
  - id: ent-001
    content: Reusable material whose role changes by context.
```

This preserves the distinction between reusable material and local role-bearing placement.

## 9.17 Entity Extension Fields

Entities MAY include extension fields.

Example:

```yaml
entities:
  - id: ent-001
    kind: claim
    content: Example claim.
    x-example-org:
      review_state: accepted
```

Core mode validators SHOULD preserve extension fields.

Strict mode MAY reject undeclared extension fields.

## 9.18 Validation Requirements

A Core validator MUST check:

- `entities` exists;
- `entities` is an array;
- every Entity is a mapping object;
- every Entity has a valid `id`;
- Entity IDs are unique within `entities`;
- if `content` exists, it is a string;
- if `ref` exists, it is a non-empty string;
- if `anchors` exists, it satisfies common anchor requirements.

A Core validator SHOULD warn when:

- an Entity has none of `content`, `payload`, or `ref`;
- Entity kind is unknown when a profile vocabulary exists;
- Entity status is unknown;
- Entity language tag appears malformed;
- an Entity is never referenced by any Occurrence;
- extension fields are undeclared.

Strict mode MAY promote warnings to errors.
