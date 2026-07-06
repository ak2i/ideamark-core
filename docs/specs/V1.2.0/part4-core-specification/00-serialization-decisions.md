# 0. Part 4 Serialization Decisions

**Version:** IdeaMark Core v1.2.0  
**Status:** Drafting Decision Memo

## Purpose

This document records the serialization decisions that should guide Part 4 before normative YAML chapters are written.

Part 4 should not rediscover the model while writing YAML syntax.

It should translate the conceptual decisions from Part 3 and the Projection boundary from Part 5 into a concrete, interoperable, validator-friendly representation.

This document is therefore a bridge between:

- Part 3 — Core Model;
- Part 5 — Projection Specification;
- Part 4 — Core Specification;
- IdeaMark CLI parser, formatter, validator, and migration tools;
- companion authoring engines such as Progressive Occurrence Resolution.

## 0.1 Serialization Goal

The primary serialization goal is to represent an IdeaMark document as a reusable access-structure artifact.

The serialized document should help future humans, AI systems, and tools:

- identify the document;
- identify relevant Original Sources;
- identify the Projection or Projection references that shaped Decomposition;
- follow source anchors;
- understand Section, Occurrence, and Entity structure;
- preserve enough ordering and status information for reconstruction;
- validate required structure;
- tolerate compatible extension data without confusing it with Core.

The serialized document should not attempt to store final meaning.

## 0.2 Required Top-level Namespaces

Part 4 should define the following required top-level namespaces:

```yaml
meta:
sources:
sections:
occurrences:
entities:
```

These are required because they represent the minimum interoperable Core access-structure model.

### `meta`

`meta` records document-level identity, specification version, status, Projection references, tool notes, timestamps, and other document-level metadata.

`meta` should not become a container for final meaning or broad workflow state.

### `sources`

`sources` records Original Source references.

It should support media-independent source references, including documents, code, datasets, media, generated artifacts, streams, composites, and future source types.

### `sections`

`sections` records Projection-shaped local source windows.

A Section is not necessarily a heading, topic, chapter, or semantic unit.

### `occurrences`

`occurrences` records role-bearing placements of reusable Entity material within Sections.

An Occurrence is not necessarily a textual occurrence or event.

### `entities`

`entities` records Projection-shaped reusable material.

An Entity is not a universal meaning unit or global ontology object.

## 0.3 Optional Top-level Namespaces

Part 4 may allow optional or profile-defined namespaces, but they should not be required for Core v1.2.0.

Potential optional namespaces include:

```yaml
structure:
relations:
perspectives:
provenance:
extensions:
```

### `structure`

`structure` may be allowed when explicit document ordering or grouping is needed beyond map order.

It should not introduce final meaning.

### `relations`

`relations` should not be required in Core v1.2.0.

If allowed, relations should be treated as an optional extension or profile-level namespace.

### `perspectives`

`perspectives` should not be required in Core v1.2.0.

Earlier Perspective responsibilities are handled by Projection references, Projection metadata, purpose notes, audience notes, local rationale, and reconstruction references.

### `provenance`

`provenance` should not be required as a separate Core namespace.

Provenance responsibilities are handled by source references, source anchors, generation metadata, tool notes, timestamps, review status, and local rationale.

### `extensions`

`extensions` may be used by profiles, tools, domains, or companion specifications.

Part 4 should define how validators treat extension data.

## 0.4 Unknown Namespace Policy

Part 4 should define a clear policy for unknown top-level namespaces.

Recommended policy:

- Core validators MUST validate required Core namespaces.
- Core validators SHOULD preserve unknown namespaces when formatting or round-tripping.
- Core validators SHOULD warn when unknown namespaces appear without an extension declaration.
- Core validators MAY reject unknown namespaces in strict mode.
- Core validators MUST NOT treat unknown namespaces as required Core semantics.

This allows interoperability while keeping Core small.

## 0.5 Object Shape Decision

Sections, Occurrences, Entities, and Sources should be represented as keyed maps rather than only arrays.

Recommended shape:

```yaml
sections:
  sec-001:
    ...

occurrences:
  occ-001:
    ...

entities:
  ent-001:
    ...

sources:
  src-001:
    ...
```

Rationale:

- stable references are easier;
- validators can detect duplicate IDs naturally;
- diffs are easier to inspect;
- partial updates are easier;
- references from Sections to Occurrences and Occurrences to Entities remain explicit.

Part 4 may allow array form as a compatibility profile only if the normalization behavior is defined.

## 0.6 Identifier Policy

Each major Core object should have a stable identifier.

For keyed maps, the map key may serve as the object identifier.

Part 4 should decide whether an object may also contain an explicit `id` field.

Recommended policy:

- map key is the canonical local ID;
- optional `id` field may be allowed only if it matches the map key;
- validators should warn or error on mismatch;
- local IDs should be document-local unless explicitly declared as global or URI-like.

Suggested prefixes are informative, not mandatory:

```text
src-   source
sec-   section
occ-   occurrence
ent-   entity
```

Part 4 should not require one global ID style too early.

## 0.7 Metadata Decision

`meta` should be required.

At minimum, `meta` should support:

```yaml
meta:
  spec_version:
  document_id:
  status:
  projections:
  generated_at:
  generator:
```

Part 4 should decide which of these fields are mandatory for all documents and which are conditionally required.

Recommended minimum mandatory fields:

- `spec_version`
- `document_id`
- `status`

Recommended conditionally required fields:

- `projections` when document content was produced under a known Projection;
- `sources` or source references when the document claims traceability to Original Sources;
- `generated_at` and `generator` when generated by a tool.

## 0.8 Projection Reference Policy

Part 4 should define how documents record Projection references.

It should not define the full Projection content model.

Recommended shape:

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

Recommended Projection roles:

- `generation`
- `reconstruction_reference`
- `comparison`
- `compatibility_hint`
- `inline_note`

Part 4 should not freeze the complete role vocabulary unless required for validation.

Unknown Projection roles may be allowed with warnings or profile declarations.

## 0.9 Runtime Context Policy

Runtime context is not a required Core object.

Part 4 may allow metadata fields for generation environment, tool options, timestamps, local overrides, or runtime notes.

However, Part 4 should not require documents to preserve full execution state of:

- human workflows;
- AI sessions;
- CLI commands;
- web applications;
- Progressive Occurrence Resolution sessions;
- external storage systems.

Recommended policy:

```yaml
meta:
  generation:
    tool:
    tool_version:
    generated_at:
    notes:
```

This records enough operational context for traceability without turning Core into a session-state format.

## 0.10 Source Reference Policy

`sources` should represent Original Source references in a media-independent way.

Recommended minimal shape:

```yaml
sources:
  src-001:
    type: document
    title:
    uri:
    revision:
    access:
    media_type:
```

Different source types may require different fields.

Part 4 should define common fields and allow type-specific extension fields.

Possible source types include:

- `document`
- `web_page`
- `code_file`
- `repository`
- `dataset`
- `image`
- `audio`
- `video`
- `stream`
- `generated_artifact`
- `composite`
- `other`

The type vocabulary may start as recommended rather than exhaustive.

## 0.11 Source Anchor and Traceability Policy

Traceability should be represented as source anchors or traceability claims.

Anchors should not be text-span-only.

Part 4 should allow anchors such as:

- line ranges;
- character ranges;
- paragraph references;
- heading paths;
- page ranges;
- media time ranges;
- image regions;
- dataset rows or columns;
- code symbols;
- repository paths;
- composite source fragments;
- approximate anchors.

Recommended shape:

```yaml
anchor:
  source: src-001
  type: line_range
  ranges:
    - start: 10
      end: 25
  precision: exact
```

or:

```yaml
anchors:
  - source: src-001
    type: media_time_range
    start: 00:01:20
    end: 00:02:05
    precision: approximate
```

Part 4 should define whether anchors may appear on Sections, Occurrences, Entities, or metadata.

Recommended default:

- Section anchors SHOULD be supported;
- Occurrence anchors MAY be supported;
- Entity anchors MAY be supported;
- document-level source references MUST be supported.

## 0.12 Section Serialization Decision

A Section should represent a Projection-shaped local source window.

Recommended minimal shape:

```yaml
sections:
  sec-001:
    title:
    anchors:
      - source: src-001
        type: line_range
        ranges:
          - start: 10
            end: 25
    occurrences:
      - occ-001
      - occ-002
```

A Section should be able to contain:

- title or label;
- source anchors;
- ordered Occurrence references;
- local notes;
- status;
- optional profile or extension fields.

A Section should not be required to correspond to an Original Source heading.

## 0.13 Occurrence Serialization Decision

An Occurrence should represent a role-bearing placement of Entity material within a Section.

Recommended minimal shape:

```yaml
occurrences:
  occ-001:
    entity: ent-001
    role: evidence
    status: active
    rationale:
```

An Occurrence should be able to contain:

- Entity reference;
- role;
- status;
- local rationale;
- anchors when needed;
- ordering when not provided by Section;
- optional profile or extension fields.

Part 4 should decide whether `role` is mandatory.

Recommended: `role` SHOULD be required for Occurrences, because role-bearing placement is the main reason Occurrence exists.

## 0.14 Entity Serialization Decision

An Entity should represent Projection-shaped reusable material.

Recommended minimal shape:

```yaml
entities:
  ent-001:
    kind:
    content:
    status: active
```

An Entity should be able to contain:

- kind or type;
- content or payload;
- status;
- source role or local notes;
- optional anchors;
- optional profile or extension fields.

Part 4 should avoid requiring a universal Entity kind taxonomy.

Entity `kind` may be profile-defined or open vocabulary.

## 0.15 Status Policy

Part 4 should define a small status vocabulary for documents and Core objects.

Recommended document statuses:

- `draft`
- `generated`
- `reviewed`
- `deprecated`
- `superseded`
- `archived`

Recommended object statuses:

- `active`
- `draft`
- `provisional`
- `deprecated`
- `superseded`
- `rejected`

Part 4 should decide whether these vocabularies are strict.

Recommended initial policy:

- document status SHOULD use a controlled vocabulary;
- object status MAY use a controlled vocabulary with extension allowance;
- validators SHOULD warn on unknown statuses unless a profile declares them.

## 0.16 Ordering Policy

Ordering should be explicit when it affects reconstruction.

Recommended policy:

- Section-level `occurrences` arrays define Occurrence order within a Section.
- Optional `structure` namespace may define document-level Section order.
- YAML map order should not be the only normative ordering mechanism.

Example:

```yaml
structure:
  sections:
    - sec-001
    - sec-002
```

Part 4 should decide whether `structure.sections` is required.

Recommended: allow but do not require it; Sections can still be referenced directly.

## 0.17 Validation Modes

Part 4 should define validation behavior for at least two modes:

### Core mode

Validates required Core structure and required fields.

Allows extension fields and unknown namespaces with warnings.

### Strict mode

Rejects unknown namespaces, unknown fields, or unknown vocabulary values unless declared by profile.

Strict mode is useful for tests, CLI validation, and controlled pipelines.

A future profile mode may validate additional profile-defined fields.

## 0.18 Extension Policy

Part 4 should allow extension without weakening Core.

Recommended policy:

- extension namespaces may exist at top level;
- extension fields may exist inside Core objects;
- validators should preserve extension data during round-trip formatting;
- extension data should not be required to interpret Core semantics;
- extensions should be namespaced or profile-declared when possible.

Example:

```yaml
extensions:
  example.org/custom:
    ...
```

or:

```yaml
entities:
  ent-001:
    kind: constraint
    content: ...
    x-example-org:
      custom_field: ...
```

Part 4 should choose a recommended extension style.

## 0.19 Compatibility and Migration Policy

Part 4 should define how documents declare specification version and profile compatibility.

Recommended fields:

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  profiles:
    - ideamark-core-minimal-v1
```

Migration tools should be able to inspect:

- spec version;
- profile declarations;
- Projection references;
- source anchor formats;
- object ID structure;
- required namespace presence.

Part 4 should define compatibility at the document format level, not Projection compatibility in full.

Projection compatibility belongs primarily to Part 5.

## 0.20 Serialization Format Decision

YAML should remain the primary human-authored serialization format for IdeaMark Core v1.2.0.

Part 4 may define JSON-equivalent behavior for tools.

Recommended policy:

- YAML is the primary authoring and documentation format;
- JSON may be used as a normalized machine representation;
- YAML anchors and advanced YAML features should be discouraged or prohibited for interoperability;
- ordering-sensitive semantics should be represented explicitly rather than relying on YAML map order.

## 0.21 Normative Examples Policy

Part 4 should include normative examples.

Examples should be small, complete, and validator-oriented.

Recommended example set:

1. minimal document;
2. document with one source, one section, one occurrence, one entity;
3. document with multiple sources;
4. document with Projection references;
5. document with source anchors;
6. document with optional extension namespace;
7. invalid examples for validation rules.

## 0.22 Open Decisions Before Full Draft

The following decisions should be finalized while drafting Part 4:

1. Are `sources`, `sections`, `occurrences`, and `entities` all strictly required even for empty or partial documents?
2. Is `structure` optional or required for document-level ordering?
3. Is `role` mandatory for every Occurrence?
4. Is Entity `kind` mandatory or optional?
5. Is `content` mandatory for every Entity, or may an Entity be reference-only?
6. Which `meta` fields are mandatory?
7. Should source anchor shape be unified or allow multiple anchor schemas?
8. Should validators preserve unknown fields by default?
9. Should unknown top-level namespaces produce warning or error in default mode?
10. Should inline Projection fragments be limited to simple notes in Core?

## 0.23 Initial Recommendation

The initial Part 4 draft should begin with a conservative Core:

```yaml
meta:
sources:
sections:
occurrences:
entities:
```

It should allow optional `structure` and `extensions`.

It should not require `relations`, `perspectives`, or `provenance`.

It should record Projection references but should not define Projection internals.

It should prioritize traceability, stable object references, validator clarity, and round-trip preservation over broad semantic expressiveness.
