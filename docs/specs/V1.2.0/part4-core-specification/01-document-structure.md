# 1. Document Structure

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 1.1 Document Unit

An IdeaMark Core document is a single YAML document or YAML-compatible mapping containing required Core namespaces and optional extension namespaces.

A conforming document MUST have exactly one top-level mapping.

The top-level mapping MUST contain the following required namespaces:

```yaml
meta:
sources:
sections:
occurrences:
entities:
```

These namespaces MAY be empty during draft generation, template authoring, staged authoring, or partial conversion.

A profile MAY require non-empty namespaces for a complete, reviewed, published, or exchange-ready document.

## 1.2 Required Namespace Order

The RECOMMENDED top-level order is:

```yaml
meta:
sources:
sections:
occurrences:
entities:
structure:
extensions:
```

This order is recommended for human readability and LLM authoring stability.

Validators MUST NOT reject a document solely because top-level namespaces appear in a different order.

Formatters SHOULD preserve user-authored order when round-tripping unless a normalization mode explicitly applies canonical ordering.

## 1.3 Array-based Object Representation

`sources`, `sections`, `occurrences`, and `entities` MUST be represented as arrays of objects in the normative Core YAML representation.

The following shape is normative:

```yaml
sources:
  - id: src-001
    type: document

sections:
  - id: sec-001
    occurrences:
      - occ-001

occurrences:
  - id: occ-001
    entity: ent-001
    role: evidence

entities:
  - id: ent-001
    content: Example reusable material.
```

Keyed-map representations MAY be accepted by migration tools or legacy compatibility tools, but they are not the normative v1.2.0 Core representation.

Tools MAY normalize arrays into internal maps for validation, indexing, or lookup.

Such internal maps are implementation details and MUST NOT be required in serialized Core documents.

## 1.4 Object Identity

Each object in `sources`, `sections`, `occurrences`, and `entities` MUST have an `id` field.

The `id` field is document-local unless it is explicitly expressed as a URI-like or globally scoped identifier.

References among Core objects MUST use the target object's `id` value.

Validators MUST detect duplicate IDs within each required namespace.

Validators SHOULD warn when the same `id` is reused across different namespaces if the reuse is likely to confuse authoring or tooling.

However, cross-namespace ID uniqueness is not required by Core unless a profile declares it.

## 1.5 Recommended ID Prefixes

The following prefixes are RECOMMENDED but not mandatory:

| Namespace | Prefix |
| --- | --- |
| `sources` | `src-` |
| `sections` | `sec-` |
| `occurrences` | `occ-` |
| `entities` | `ent-` |

Validators SHOULD NOT reject a document solely because an ID does not use the recommended prefix.

Strict mode MAY require a profile-declared ID pattern.

## 1.6 Reference Direction

Core references SHOULD point from structural context toward reusable material.

The primary required reference directions are:

- Section to Occurrence: `sections[].occurrences[]`
- Occurrence to Entity: `occurrences[].entity`
- Anchor to Source: `anchors[].source`

This produces a reconstruction path:

```text
Document -> Section -> Occurrence -> Entity
```

A document MAY include additional reverse indexes, relation links, or profile-specific indexes as extension data.

Such indexes MUST NOT be required for Core reconstruction.

## 1.7 Minimal Valid Document

The following is the minimal Core shape:

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example-minimal
  status: draft
sources: []
sections: []
occurrences: []
entities: []
```

A Core validator MUST accept this shape in Core mode if no profile requires content completeness.

## 1.8 Single-source Example

The following example illustrates one source, one section, one occurrence, and one entity:

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example-single-source
  status: draft
sources:
  - id: src-001
    type: document
    title: Example Source
    uri: ./example-source.md
sections:
  - id: sec-001
    title: Local source window
    anchors:
      - source: src-001
        type: line_range
        ranges:
          - start: 1
            end: 10
        precision: exact
    occurrences:
      - occ-001
occurrences:
  - id: occ-001
    entity: ent-001
    role: evidence
    status: active
entities:
  - id: ent-001
    kind: claim
    content: Example reusable material extracted from the source window.
```

## 1.9 Empty Namespaces and Completeness

Required namespaces MAY be empty.

An empty required namespace means that the document is structurally prepared for that namespace but does not currently contain objects in it.

Core mode MUST NOT treat an empty required namespace as invalid by itself.

A profile or publishing pipeline MAY define completeness rules such as:

- at least one source is required;
- at least one section is required;
- every section must contain at least one occurrence;
- every occurrence must point to an entity;
- every entity must contain reusable material.

Those completeness rules are outside the minimum Core unless explicitly adopted by a profile.

## 1.10 Unknown Top-level Namespaces

A Core validator MUST validate required Core namespaces.

A Core validator SHOULD preserve unknown top-level namespaces during round-trip formatting.

A Core validator SHOULD warn when unknown top-level namespaces are present without an extension or profile declaration.

A strict validator MAY reject unknown top-level namespaces.

Unknown namespaces MUST NOT be silently interpreted as required Core semantics.
