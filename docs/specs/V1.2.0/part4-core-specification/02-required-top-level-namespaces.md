# 2. Required Top-level Namespaces

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 2.1 Required Namespaces

A conforming IdeaMark Core v1.2.0 document MUST contain these top-level namespaces:

```yaml
meta:
sources:
sections:
occurrences:
entities:
```

These namespaces define the minimum interoperable Core access structure.

A document that omits any required namespace is invalid in Core mode.

A required namespace MAY be empty unless a profile or strict pipeline declares a stronger completeness rule.

## 2.2 `meta`

`meta` records document-level metadata.

It MUST be a mapping.

At minimum, `meta` MUST include:

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example-document
  status: draft
```

`meta` is responsible for:

- Core specification version declaration;
- document identity;
- document status;
- optional profile declarations;
- optional Projection references;
- optional generation metadata;
- optional compatibility and migration hints.

`meta` MUST NOT be used as a container for final meaning, reusable Entity content, full authoring session state, or broad runtime workflow state.

## 2.3 `sources`

`sources` records Original Source references.

It MUST be an array.

Each object in `sources` MUST have an `id` field.

A source object SHOULD include a `type` field.

Example:

```yaml
sources:
  - id: src-001
    type: document
    title: Example Source
    uri: ./example-source.md
```

`sources` is responsible for identifying material from which Sections, Occurrences, Entities, or traceability claims may be derived.

`sources` MUST NOT require all source media to be reducible to text spans.

## 2.4 `sections`

`sections` records Projection-shaped local source windows.

It MUST be an array.

Each object in `sections` MUST have an `id` field.

A section object SHOULD include an ordered `occurrences` array unless the section is a placeholder or draft fragment.

Example:

```yaml
sections:
  - id: sec-001
    title: Example source window
    occurrences:
      - occ-001
```

A Section is not necessarily:

- an Original Source heading;
- a topic;
- a chapter;
- a semantic unit;
- a final interpretation unit.

## 2.5 `occurrences`

`occurrences` records role-bearing placements of Entity material within Sections.

It MUST be an array.

Each object in `occurrences` MUST have an `id` field.

Each non-placeholder Occurrence MUST include:

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

An Occurrence is not merely a textual occurrence.

It is a contextual placement that says how an Entity participates in a Section.

## 2.6 `entities`

`entities` records Projection-shaped reusable material.

It MUST be an array.

Each object in `entities` MUST have an `id` field.

An Entity SHOULD contain at least one of:

- `content`
- `payload`
- `ref`

unless a profile explicitly permits placeholder Entities.

Example:

```yaml
entities:
  - id: ent-001
    kind: claim
    content: Example reusable material.
```

An Entity is not a universal meaning unit or global ontology object.

## 2.7 Optional Core-adjacent Namespaces

The following namespaces are OPTIONAL in Core v1.2.0:

```yaml
structure:
relations:
perspectives:
provenance:
extensions:
```

Optional namespaces MAY be defined by later chapters, profiles, companion specifications, or implementations.

Optional namespaces MUST NOT be required for minimum Core validity.

## 2.8 Recommended Optional Namespace Use

`structure` MAY be used to declare explicit document-level ordering or grouping.

`relations` MAY be used by profiles that need explicit Entity-to-Entity or object-to-object structural links.

`perspectives` MAY be used by profiles that need first-class Perspective records.

`provenance` MAY be used by profiles that separate provenance records from Core objects.

`extensions` SHOULD be used when a document includes declared extension namespaces or profile-specific payloads.

## 2.9 Unknown Namespace Handling

In Core mode:

- unknown top-level namespaces SHOULD produce warnings;
- unknown top-level namespaces SHOULD be preserved by formatters;
- unknown top-level namespaces MUST NOT be interpreted as required Core semantics;
- unknown top-level namespaces MUST NOT cause validation failure unless they structurally conflict with required Core processing.

In strict mode:

- unknown namespaces MAY be rejected;
- undeclared extension namespaces MAY be rejected;
- profile-declared namespaces MAY be accepted and validated by profile rules.

## 2.10 Namespace Type Requirements

The following type requirements are normative:

| Namespace | Required Type |
| --- | --- |
| `meta` | mapping |
| `sources` | array |
| `sections` | array |
| `occurrences` | array |
| `entities` | array |

A validator MUST reject a required namespace whose value has the wrong type.

A validator SHOULD report the error at the namespace path.
