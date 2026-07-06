# 14. Compatibility and Migration

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 14.1 Purpose

Compatibility and migration rules help tools move IdeaMark documents across specification versions without losing reusable access structure.

This chapter defines document-format compatibility boundaries.

It does not define Projection compatibility, intellectual equivalence, retrieval equivalence, or domain-specific migration quality.

## 14.2 Compatibility Unit

The compatibility unit is the serialized IdeaMark Core document.

A document declares its target format using:

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
```

Tools SHOULD inspect `meta.spec_version` before validation, migration, or formatting.

## 14.3 Backward Compatibility Policy

Within the v1.2.x line, compatible changes SHOULD avoid breaking existing valid v1.2.0 Core documents.

Compatible changes MAY include:

- new recommended vocabulary values;
- new optional fields;
- new optional namespaces;
- clarified validation warnings;
- additional profile conventions;
- new examples;
- non-breaking documentation clarifications.

Compatible changes MUST NOT remove required Core fields or change required namespace types without a major or explicitly incompatible version change.

## 14.4 Breaking Change Policy

Breaking changes include:

- changing required namespace names;
- changing required namespace types;
- removing required fields;
- changing reference semantics;
- making previously valid Core documents invalid in Core mode;
- changing the meaning of `sections[].occurrences` or `occurrences[].entity`;
- changing array-based object representation as the normative shape.

Breaking changes SHOULD require a new incompatible spec version.

## 14.5 Migration Goals

Migration tools SHOULD preserve:

- document identity when safe;
- Source references;
- Section identities;
- Occurrence identities;
- Entity identities;
- source anchors;
- role-bearing placements;
- extension data;
- unknown fields;
- authoring order when meaningful;
- Projection references where available.

Migration tools SHOULD avoid converting conceptual uncertainty into false certainty.

## 14.6 Migration from Keyed Maps

Earlier or experimental IdeaMark documents may represent namespaces as keyed maps.

Migration tools MAY convert keyed maps into arrays.

Example input:

```yaml
entities:
  ent-001:
    content: Example material.
```

Recommended output:

```yaml
entities:
  - id: ent-001
    content: Example material.
```

Migration tools SHOULD preserve the original key as the object's `id`.

## 14.7 Migration of Header Fields

Earlier documents may use document header fields at the top level.

Migration tools SHOULD map them into `meta` where possible.

Example:

```yaml
ideamark_version: 1
doc_id: example
status: in_progress
```

Possible output:

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example
  status: draft
  migration:
    from_spec_version: ideamark-core-v1.1.x
```

Status mapping SHOULD be conservative and documented.

## 14.8 Migration of References

Migration tools MUST preserve resolvable reference relationships where possible.

If a reference cannot be resolved, a migration tool SHOULD either:

- preserve it with a warning;
- create an explicit placeholder object;
- record a migration diagnostic;
- fail in strict migration mode.

Migration tools MUST NOT silently drop unresolved references.

## 14.9 Migration of Projection Data

Projection data from earlier drafts may appear under `perspectives`, `projection`, `refs`, or other fields.

Migration tools SHOULD preserve Projection-related information in `meta.projections`, an extension namespace, or a companion Projection document.

Migration tools MUST NOT attempt to force full Projection internals into Core `meta` if doing so would blur the Projection boundary.

## 14.10 Extension Preservation

Migration tools SHOULD preserve unknown and extension data by default.

If a migration cannot preserve extension data safely, it SHOULD report a warning or diagnostic.

A destructive migration mode MAY drop extension data only when explicitly requested.

## 14.11 Migration Metadata

Migration tools SHOULD record migration metadata when they transform a document.

Example:

```yaml
meta:
  migration:
    from_spec_version: ideamark-core-v1.1.2
    to_spec_version: ideamark-core-v1.2.0
    migrated_by: ideamark-migrate
    migrated_at: 2026-07-07T00:00:00Z
```

Migration metadata is informative.

Validators MUST validate the resulting document structure directly.

## 14.12 Compatibility Boundary

Core compatibility does not guarantee:

- Projection compatibility;
- equivalent retrieval quality;
- equivalent source interpretation;
- identical Entity granularity;
- identical authoring workflow;
- UI compatibility;
- storage schema compatibility.

Those concerns belong to profiles, Projection specifications, migration guides, or implementation documentation.
