# 8. Occurrences

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 8.1 Purpose

An Occurrence represents a role-bearing placement of Entity material within a Section.

An Occurrence answers the question:

> How does this reusable material participate here?

Occurrence is necessary because the same Entity may appear in different Sections with different roles, local rationales, anchors, statuses, or reconstruction functions.

An Occurrence is not merely a text span, event, mention, or duplicate of an Entity.

## 8.2 Required Shape

`occurrences` MUST be an array.

Each item in `occurrences` MUST be a mapping object.

Each Occurrence object MUST contain an `id` field.

Each non-placeholder Occurrence MUST contain:

- `entity`
- `role`

Example:

```yaml
occurrences:
  - id: occ-001
    entity: ent-001
    role: evidence
    status: active
```

## 8.3 Required Fields

| Field | Type | Requirement |
| --- | --- | --- |
| `id` | string | MUST |
| `entity` | string | MUST for non-placeholder Occurrences |
| `role` | string | MUST for non-placeholder Occurrences |

A validator MUST reject an Occurrence whose `id` is missing, null, empty, or non-string.

A validator MUST reject duplicate Occurrence IDs within `occurrences`.

A validator MUST reject unresolved `entity` references for non-placeholder Occurrences.

## 8.4 Recommended Fields

| Field | Type | Meaning |
| --- | --- | --- |
| `status` | string | Occurrence lifecycle state |
| `rationale` | string | Why this Entity has this role here |
| `anchors` | array | Source anchors specific to this placement |
| `confidence` | number | Confidence in this placement or role |
| `note` / `notes` | string or array | Human-readable notes |

`rationale` is recommended when the role assignment may be non-obvious.

`anchors` are recommended when the Occurrence needs more precise traceability than the containing Section.

## 8.5 `entity` Reference

`occurrences[].entity` MUST reference an existing Entity ID unless the Occurrence is an explicitly permitted placeholder.

Example:

```yaml
occurrences:
  - id: occ-001
    entity: ent-001
    role: supports
```

An Occurrence MUST NOT inline full Entity content as a substitute for referencing an Entity in the normative Core representation.

Migration tools MAY accept legacy inline forms and normalize them into separate Entity objects.

## 8.6 `role`

`role` is required for non-placeholder Occurrences because role-bearing placement is the main reason Occurrence exists.

Example:

```yaml
occurrences:
  - id: occ-001
    entity: ent-001
    role: problem_core
```

Core does not require a universal closed role vocabulary.

Roles may be:

- Core-recommended;
- profile-defined;
- Projection-shaped;
- domain-specific;
- document-local.

Core mode validators SHOULD warn on missing or unknown roles when an Occurrence is not marked as a placeholder.

Strict mode MAY require profile-declared role vocabularies.

## 8.7 Recommended Role Vocabulary

The following role values are recommended as common starting points:

- `context`
- `claim`
- `evidence`
- `problem`
- `constraint`
- `risk`
- `measure`
- `decision`
- `outcome`
- `example`
- `definition`
- `rationale`
- `counterpoint`
- `question`
- `answer`
- `source_pattern`
- `target_application`
- `projection_note`

This list is not exhaustive.

Core validators MUST NOT reject unknown role values in Core mode solely because they are not listed here.

## 8.8 Occurrence Status

An Occurrence MAY include `status`.

Recommended Occurrence status values are:

- `active`
- `draft`
- `provisional`
- `deprecated`
- `superseded`
- `rejected`

Occurrence status describes the placement, not necessarily the referenced Entity.

For example, an Entity may remain active while one particular Occurrence is rejected.

## 8.9 Occurrence Anchors

An Occurrence MAY include `anchors`.

Occurrence anchors are useful when:

- the Section anchor is broad;
- the Entity is derived from a specific subregion;
- multiple Occurrences in the same Section correspond to different source fragments;
- the role assignment needs precise support.

Example:

```yaml
occurrences:
  - id: occ-001
    entity: ent-001
    role: evidence
    anchors:
      - source: src-001
        type: line_range
        ranges:
          - start: 20
            end: 23
```

Occurrence anchors MUST satisfy the common anchor requirements.

## 8.10 Occurrence Rationale

`rationale` MAY explain why the Entity is placed with a particular role.

Example:

```yaml
occurrences:
  - id: occ-001
    entity: ent-001
    role: risk
    rationale: The same mechanism creates a failure mode when source conditions change.
```

Rationale is human-readable.

Core validators MUST NOT attempt to prove the correctness of rationale text.

## 8.11 Confidence

An Occurrence MAY include `confidence`.

Example:

```yaml
occurrences:
  - id: occ-001
    entity: ent-001
    role: evidence
    confidence: 0.82
```

When present, `confidence` SHOULD be a number between 0 and 1 inclusive.

Core mode validators SHOULD warn when confidence is outside that range.

Strict mode MAY reject invalid confidence values.

Confidence describes the placement or interpretation of the Occurrence, not necessarily the truth of the Entity content.

## 8.12 Placeholder Occurrences

A placeholder Occurrence may have an `id` but lack `entity` or `role`.

Example:

```yaml
occurrences:
  - id: occ-placeholder
    status: draft
```

Core mode MAY allow placeholder Occurrences during draft, template, partial generation, or staged authoring.

Validators SHOULD warn about placeholder Occurrences.

Strict mode MAY reject placeholder Occurrences.

Profiles MAY define explicit placeholder behavior.

## 8.13 Occurrence Reuse and Multiplicity

An Occurrence SHOULD normally appear in one Section's `occurrences` list.

However, Core does not forbid the same Occurrence ID from being referenced by multiple Sections.

Validators SHOULD warn when one Occurrence is referenced by multiple Sections, because this may indicate that the author intended multiple role-bearing placements and should create separate Occurrences.

If the same Entity participates in multiple Sections, the preferred representation is multiple Occurrences referencing the same Entity.

## 8.14 Occurrence and Entity Separation

Entity content should not be duplicated across Occurrences.

The preferred shape is:

```yaml
occurrences:
  - id: occ-001
    entity: ent-001
    role: evidence
entities:
  - id: ent-001
    content: Reusable material.
```

This separation allows the same reusable material to be placed in different local contexts without redefining it.

## 8.15 Occurrence Extension Fields

Occurrences MAY include extension fields.

Example:

```yaml
occurrences:
  - id: occ-001
    entity: ent-001
    role: evidence
    x-example-org:
      reviewer: domain-specialist
```

Core mode validators SHOULD preserve extension fields.

Strict mode MAY reject undeclared extension fields.

## 8.16 Validation Requirements

A Core validator MUST check:

- `occurrences` exists;
- `occurrences` is an array;
- every Occurrence is a mapping object;
- every Occurrence has a valid `id`;
- Occurrence IDs are unique within `occurrences`;
- non-placeholder Occurrences have `entity`;
- non-placeholder Occurrences have `role`;
- `occurrences[].entity` resolves to an existing Entity ID;
- if `anchors` exists, it satisfies common anchor requirements.

A Core validator SHOULD warn when:

- an Occurrence has no `entity` or no `role`;
- role is unknown and not profile-declared;
- status is unknown;
- confidence is outside 0 to 1;
- the same Occurrence is referenced by multiple Sections;
- an Occurrence is never referenced by any Section;
- extension fields are undeclared.

Strict mode MAY promote warnings to errors.
