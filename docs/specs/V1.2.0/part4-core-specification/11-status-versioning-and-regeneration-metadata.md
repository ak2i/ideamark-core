# 11. Status, Versioning, and Regeneration Metadata

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 11.1 Purpose

IdeaMark documents are often generated, reviewed, revised, migrated, or regenerated.

This chapter defines how Core documents record status, versioning, and regeneration metadata without turning the document format into an authoring engine state format.

## 11.2 Document Status

Document-level status is recorded in `meta.status`.

Recommended document status values are:

- `draft`
- `generated`
- `reviewed`
- `deprecated`
- `superseded`
- `archived`

Example:

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example-document
  status: generated
```

Document status describes the lifecycle state of the document as a whole.

It does not automatically determine object-level status.

## 11.3 Object Status

Sources, Sections, Occurrences, and Entities MAY include `status`.

Recommended object status values are:

- `active`
- `draft`
- `provisional`
- `deprecated`
- `superseded`
- `rejected`

Example:

```yaml
occurrences:
  - id: occ-001
    entity: ent-001
    role: evidence
    status: provisional
```

Object status applies only to the object on which it appears.

## 11.4 Status Vocabulary Policy

Core mode validators SHOULD warn on unknown status values.

Strict mode MAY reject unknown status values unless declared by a profile.

Profiles MAY define additional statuses or stricter status transitions.

Core does not define workflow transition rules.

## 11.5 Specification Version

`meta.spec_version` MUST declare the target Core document format.

For this specification:

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
```

Tools SHOULD inspect `spec_version` before parsing profile-specific details or applying migration behavior.

## 11.6 Document Revision Metadata

A document MAY record its own revision metadata.

Example:

```yaml
meta:
  revision:
    id: rev-003
    previous: rev-002
    updated_at: 2026-07-07T00:00:00Z
    updated_by: example-author
```

Revision metadata is optional in Core.

Profiles MAY require it for review, publishing, or audit pipelines.

## 11.7 Supersession Metadata

A document MAY record supersession metadata.

Example:

```yaml
meta:
  supersedes:
    - document_id: previous-document
      reason: Re-generated under revised Projection.
```

Object-level supersession MAY be recorded on objects or through extension fields.

Core does not define full version graph semantics.

## 11.8 Generation Metadata

Generated documents MAY record generation metadata in `meta.generation`.

Example:

```yaml
meta:
  generation:
    tool: ideamark-cli
    tool_version: 0.2.0
    generated_at: 2026-07-07T00:00:00Z
    model: example-model
    projection_ref: projection://example/v1
```

Generation metadata SHOULD be used when a tool emits the document and traceability is important.

Core validators MUST NOT require generation metadata for manually authored documents.

## 11.9 Regeneration Metadata

A document MAY record regeneration metadata when it was produced by reprocessing previous material.

Example:

```yaml
meta:
  regeneration:
    regenerated_from: ideamark://docs/example-v1
    regenerated_at: 2026-07-07T00:00:00Z
    reason: Align with IdeaMark Core v1.2.0 object model.
```

Regeneration metadata is descriptive.

Validators MUST validate the actual document structure rather than assuming correctness from regeneration metadata.

## 11.10 Migration Metadata

A migration tool MAY record migration metadata.

Example:

```yaml
meta:
  migration:
    from_spec_version: ideamark-core-v1.1.2
    to_spec_version: ideamark-core-v1.2.0
    migrated_by: ideamark-migrate
    migrated_at: 2026-07-07T00:00:00Z
```

Migration metadata SHOULD NOT replace `meta.spec_version`.

`meta.spec_version` remains the normative current target version.

## 11.11 Boundary from Authoring Engine State

Status, generation, regeneration, and migration metadata are traceability records.

They MUST NOT require preservation of full authoring engine state, including:

- prompt plans;
- LLM call history;
- chunk scheduling;
- review queues;
- UI interaction state;
- cache state;
- retry state;
- background job state.

Such state belongs in logs, companion systems, or extension profiles.

## 11.12 Validation Requirements

A Core validator MUST check:

- `meta.spec_version` exists and is supported or explicitly handled by migration mode;
- `meta.status` exists and is a non-empty string.

A Core validator SHOULD warn when:

- document status is unknown;
- object status is unknown;
- generation timestamps appear malformed;
- migration metadata conflicts with `meta.spec_version`;
- regeneration metadata references a missing or malformed document identifier.

Strict mode MAY promote warnings to errors.
