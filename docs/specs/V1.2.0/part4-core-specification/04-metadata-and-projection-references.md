# 4. Metadata and Projection References

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 4.1 Purpose

`meta` records document-level identity, Core version, document status, optional profile declarations, optional Projection references, and optional generation metadata.

`meta` is required because every IdeaMark Core document must be self-describing enough for validators, migration tools, authoring engines, and future readers to determine how it should be interpreted as a document format.

`meta` does not store final meaning.

`meta` does not replace Sources, Sections, Occurrences, or Entities.

## 4.2 Required Shape

`meta` MUST be a mapping.

At minimum, `meta` MUST contain:

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example-document
  status: draft
```

The following fields are required in Core mode:

| Field | Type | Requirement |
| --- | --- | --- |
| `spec_version` | string | MUST |
| `document_id` | string | MUST |
| `status` | string | MUST |

## 4.3 `spec_version`

`meta.spec_version` identifies the target IdeaMark Core document format.

For this specification, the normative value is:

```yaml
spec_version: ideamark-core-v1.2.0
```

Validators MUST reject documents whose `spec_version` is missing.

Validators SHOULD reject unsupported `spec_version` values unless a migration or compatibility mode is explicitly enabled.

Migration tools SHOULD inspect `spec_version` before applying transformation rules.

## 4.4 `document_id`

`meta.document_id` identifies the document.

It MUST be a non-empty string.

The value MAY be:

- a document-local identifier;
- a repository-local identifier;
- a URI-like identifier;
- an externally assigned document ID.

Core does not require a globally unique ID scheme.

Profiles MAY impose stronger document ID rules.

## 4.5 `status`

`meta.status` records document-level lifecycle state.

Recommended document status values are:

- `draft`
- `generated`
- `reviewed`
- `deprecated`
- `superseded`
- `archived`

Core mode validators SHOULD warn on unknown document status values.

Strict mode MAY reject unknown document status values unless declared by a profile.

`meta.status` is document-level status and MUST NOT be used to infer the status of every Source, Section, Occurrence, or Entity.

## 4.6 Recommended Metadata Fields

The following fields are RECOMMENDED but not required in Core mode:

```yaml
meta:
  title: Example IdeaMark Document
  description: Human-readable document description.
  created_at: 2026-07-07T00:00:00Z
  updated_at: 2026-07-07T00:00:00Z
  lang: en-US
  profiles:
    - ideamark-core-minimal-v1
```

Recommended field meanings:

| Field | Meaning |
| --- | --- |
| `title` | Human-readable document title |
| `description` | Human-readable document summary |
| `created_at` | Document creation timestamp |
| `updated_at` | Last document update timestamp |
| `lang` | Default human language of the document |
| `profiles` | Profile identifiers applied to this document |

`lang` SHOULD use a BCP 47 language tag when present.

## 4.7 Profile Declarations

`meta.profiles` MAY declare one or more document profiles.

Example:

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example-with-profile
  status: draft
  profiles:
    - ideamark-core-minimal-v1
    - example.org/field-report-profile-v1
```

Profiles MAY define:

- additional required fields;
- stricter vocabularies;
- required extension namespaces;
- completeness rules;
- ID conventions;
- source anchor requirements;
- domain-specific validation.

Core validators MAY ignore profile declarations that they do not support, but SHOULD warn that profile-specific validation was not performed.

Strict validation MAY fail when a declared profile is not available and profile enforcement is required by the caller.

## 4.8 Projection References

`meta.projections` records Projection references or limited inline Projection notes that shaped document generation, reconstruction, comparison, or compatibility.

Projection references are optional in Core mode.

They are conditionally RECOMMENDED when the document was generated under a known Projection.

Example:

```yaml
meta:
  projections:
    - role: generation
      ref: projection://example/projection/v1
      version: v1
    - role: reconstruction_reference
      ref: projection://example/reconstruction/v1
    - role: inline_note
      inline:
        purpose: explain professional cooking guidance for household use
        audience: non-specialist
```

## 4.9 Projection Reference Object

Each item in `meta.projections` SHOULD be a mapping.

A Projection reference object SHOULD include a `role` field.

It SHOULD include at least one of:

- `ref`
- `inline`

Recommended fields:

| Field | Type | Meaning |
| --- | --- | --- |
| `role` | string | How the Projection relates to this document |
| `ref` | string | External Projection reference |
| `version` | string | Projection version or revision |
| `inline` | mapping | Limited inline Projection note or fragment |
| `description` | string | Human-readable explanation |

## 4.10 Projection Roles

Recommended Projection roles are:

- `generation`
- `reconstruction_reference`
- `comparison`
- `compatibility_hint`
- `inline_note`

Core mode validators SHOULD warn on unknown Projection roles unless a profile declares them.

Strict mode MAY reject unknown Projection roles.

Part 4 MUST NOT freeze the complete Projection role vocabulary.

## 4.11 Inline Projection Boundary

Core MAY allow limited inline Projection fragments for local traceability.

Inline Projection data SHOULD be small and explanatory.

Inline Projection data MUST NOT be required to implement the full Projection content model.

A Core document SHOULD prefer external Projection references when the Projection is reusable, versioned, governed, or shared across documents.

Part 5 defines Projection as a reusable intellectual asset; Part 4 only records references needed by the Core document.

## 4.12 Generation Metadata

`meta.generation` MAY record tool or authoring environment metadata.

Example:

```yaml
meta:
  generation:
    tool: ideamark-cli
    tool_version: 0.2.0
    generated_at: 2026-07-07T00:00:00Z
    model: example-model
    notes: Generated from a source document under a Projection.
```

Generation metadata is for traceability.

It MUST NOT be required for Core validity unless a profile or pipeline requires generated documents to declare it.

## 4.13 Runtime Context Boundary

`meta` MAY contain small traceability records about tools, timestamps, or generation parameters.

`meta` MUST NOT require preservation of full runtime context such as:

- human workflow state;
- AI session history;
- prompt orchestration state;
- cache state;
- review queue state;
- CLI invocation history;
- web application state;
- external storage engine state.

Such data belongs in authoring engine logs, provenance profiles, companion systems, or extension namespaces.

## 4.14 Compatibility Metadata

`meta.compatibility` MAY record compatibility hints.

Example:

```yaml
meta:
  compatibility:
    previous_spec_version: ideamark-core-v1.1.2
    migrated_by: ideamark-migrate
    migrated_at: 2026-07-07T00:00:00Z
```

Compatibility metadata is optional.

Migration tools MAY use it, but Core validators MUST validate the actual serialized structure rather than trusting compatibility metadata alone.

## 4.15 Validation Requirements

A Core validator MUST check:

- `meta` exists;
- `meta` is a mapping;
- `meta.spec_version` exists and is a non-empty string;
- `meta.document_id` exists and is a non-empty string;
- `meta.status` exists and is a non-empty string.

A Core validator SHOULD warn when:

- status value is unknown;
- declared profiles are unsupported;
- Projection references are malformed but not required for Core processing;
- inline Projection data appears too large or appears to define a full Projection model inside Core.

Strict mode MAY promote those warnings to errors.
