# 3. Common Object Requirements

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 3.1 Scope

This chapter defines common requirements for objects in the required Core namespaces:

- `sources[]`
- `sections[]`
- `occurrences[]`
- `entities[]`

Namespace-specific chapters MAY add additional requirements.

## 3.2 Object Shape

Each item in `sources`, `sections`, `occurrences`, and `entities` MUST be a mapping object.

The following is invalid:

```yaml
entities:
  - ent-001
```

The following is valid object shape:

```yaml
entities:
  - id: ent-001
    content: Example reusable material.
```

A validator MUST reject scalar, null, or array items inside required Core object arrays unless a profile explicitly defines a migration or shorthand mode.

## 3.3 Required `id`

Each Source, Section, Occurrence, and Entity object MUST have an `id` field.

The `id` field MUST be a non-empty string.

Example:

```yaml
occurrences:
  - id: occ-001
    entity: ent-001
    role: evidence
```

A validator MUST reject objects with missing, null, empty, or non-string `id` values.

## 3.4 ID Scope

Core IDs are document-local by default.

The following namespaces each have their own ID scope:

- Source IDs in `sources[]`;
- Section IDs in `sections[]`;
- Occurrence IDs in `occurrences[]`;
- Entity IDs in `entities[]`.

A validator MUST reject duplicate IDs within the same namespace.

A validator SHOULD warn when the same ID appears in multiple namespaces and the document does not declare an intentional cross-namespace ID policy.

## 3.5 ID Stability

IDs SHOULD remain stable across edits when the object remains conceptually the same object.

Tools SHOULD NOT regenerate IDs merely because array order, formatting, comments, optional fields, or local wording changed.

Migration tools SHOULD preserve IDs when converting from earlier IdeaMark formats unless the original IDs conflict or cannot be represented safely.

## 3.6 ID Prefixes

The following ID prefixes are RECOMMENDED:

| Object | Prefix |
| --- | --- |
| Source | `src-` |
| Section | `sec-` |
| Occurrence | `occ-` |
| Entity | `ent-` |

These prefixes are informative.

Core mode validators MUST NOT reject a document solely because an ID uses a different prefix.

Strict mode MAY enforce profile-declared ID patterns.

## 3.7 Status Field

Core objects MAY include a `status` field.

When present, `status` SHOULD be a string.

Recommended object status values are:

- `active`
- `draft`
- `provisional`
- `deprecated`
- `superseded`
- `rejected`

Core mode validators SHOULD warn on unknown status values unless a profile declares them.

Strict mode MAY reject unknown status values.

## 3.8 Notes and Rationale

Core objects MAY include human-readable explanatory fields such as:

- `title`
- `label`
- `note`
- `notes`
- `rationale`
- `description`

These fields are optional unless a namespace-specific chapter or profile requires them.

Tools MUST NOT treat these fields as replacements for required Core references.

For example, a Section title cannot replace `sections[].occurrences`, and an Occurrence rationale cannot replace `occurrences[].entity`.

## 3.9 Anchors

Core objects MAY include an `anchors` field when traceability to sources is useful.

When present, `anchors` SHOULD be an array of anchor objects.

The common anchor shape is defined in the Source Anchors and Traceability chapter.

Section anchors SHOULD be supported.

Occurrence anchors MAY be supported.

Entity anchors MAY be supported.

Document-level source references MUST be supported through the `sources` namespace.

## 3.10 Extension Fields

Core objects MAY include extension fields.

Extension fields SHOULD use one of the following conventions:

- profile-declared field names;
- namespaced field names such as `x-example-org`;
- an explicit object under an `extensions` field.

Example:

```yaml
entities:
  - id: ent-001
    content: Example reusable material.
    x-example-org:
      review_state: needs_domain_review
```

Core mode validators SHOULD preserve extension fields.

Core mode validators SHOULD warn when extension fields are not profile-declared and not clearly namespaced.

Strict mode MAY reject undeclared extension fields.

## 3.11 Unknown Fields

Unknown fields inside Core objects MUST NOT be interpreted as required Core semantics.

Core mode validators SHOULD preserve unknown fields during round-trip formatting.

Core mode validators MAY emit warnings for unknown fields.

Strict mode MAY reject unknown fields unless they are allowed by a profile or extension declaration.

## 3.12 Null Values

A required field MUST NOT be null.

Optional fields MAY be omitted.

Optional fields SHOULD NOT be serialized with null values unless a profile uses null to represent a meaningful explicit state.

Validators SHOULD warn about null optional fields when omission would be clearer.

## 3.13 References

Core object references MUST be strings unless a namespace-specific chapter explicitly defines a structured reference object.

The following reference fields are Core reference fields:

- `sections[].occurrences[]` references `occurrences[].id`;
- `occurrences[].entity` references `entities[].id`;
- `anchors[].source` references `sources[].id`.

A validator MUST reject unresolved required Core references.

A validator MAY warn about unused objects, unreferenced Entities, or unreachable Occurrences, but these are not Core errors by themselves unless a profile declares them.

## 3.14 Placeholder Objects

A placeholder object is an object that has an `id` but lacks enough required fields to participate in normal Core reconstruction.

Examples include:

```yaml
entities:
  - id: ent-placeholder
```

Core mode MAY allow placeholder objects during draft, template, partial generation, or staged authoring.

Validators SHOULD warn about placeholder objects.

Strict mode MAY reject placeholder objects.

Profiles MAY define explicit placeholder rules.

## 3.15 Round-trip Preservation

Tools that format, normalize, or migrate Core documents SHOULD preserve:

- required Core fields;
- optional Core fields;
- unknown fields;
- extension fields;
- unknown namespaces;
- array order, unless a canonical ordering mode is explicitly requested.

Tools MUST NOT drop unknown data silently during a normal round-trip operation.

A destructive normalization mode MAY remove unknown or extension data only when explicitly requested by the user or pipeline.
