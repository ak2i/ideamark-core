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
- authoring engines such as CLI workflows, batch converters, visual editors, AI agents, and companion systems such as Progressive Occurrence Resolution.

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

Required namespaces MAY be empty arrays during draft generation, template authoring, partial generation, or staged authoring.

For example:

```yaml
sources: []
sections: []
occurrences: []
entities: []
```

Validators SHOULD accept empty required namespaces in Core mode.

Profiles or strict pipelines MAY require non-empty namespaces when the document claims to be complete, reviewed, or exchange-ready.

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

`structure` is optional. It may be used when explicit document ordering or grouping is needed beyond array order or local reference order.

`relations`, `perspectives`, and `provenance` should not be required in Core v1.2.0. They may appear as optional extension or profile-level namespaces.

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

Sections, Occurrences, Entities, and Sources should be represented as arrays of objects, not keyed maps.

This decision is made for authoring reliability.

LLMs often generate array-oriented YAML more consistently than deeply keyed map structures, especially when producing partial documents, adding examples, or revising generated output.

Recommended shape:

```yaml
sources:
  - id: src-001
    type: document
    title: Example Source

sections:
  - id: sec-001
    title: Example Section
    occurrences:
      - occ-001

occurrences:
  - id: occ-001
    entity: ent-001
    role: evidence

entities:
  - id: ent-001
    kind: claim
    content: Example reusable material.
```

Rationale:

- LLMs generate arrays more reliably than keyed maps;
- array items can be appended, reordered, and revised naturally;
- `id` remains explicit and visible in each object;
- examples are easier for humans and LLMs to copy;
- object shape remains uniform across namespaces;
- validators can still detect duplicate IDs.

Part 4 should not use keyed-map object shape as the normative Core representation.

A tool MAY normalize arrays into internal maps for validation, indexing, or lookup, but that normalized representation is an implementation detail.

## 0.6 Identifier Policy

Each major Core object should have a stable `id` field.

Recommended policy:

- `id` is mandatory for each Source, Section, Occurrence, and Entity object;
- IDs are document-local unless explicitly declared as global or URI-like;
- validators MUST detect duplicate IDs within each namespace;
- validators SHOULD warn when ID prefixes do not match common conventions, but prefixes should not be mandatory;
- references use the target object's `id` value.

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
- authoring engine sessions;
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

## 0.10 Authoring Engine Boundary

Part 4 should include an Authoring Engine Boundary.

This boundary is needed because many systems may produce IdeaMark documents while maintaining internal behavior that does not belong in Core YAML.

Authoring engines may include:

- CLI workflows;
- batch converters;
- visual authoring tools;
- IDE plugins;
- AI agents;
- progressive large-source processors;
- companion systems such as Progressive Occurrence Resolution.

Part 4 defines the document representation that these engines may emit, validate, exchange, or normalize.

Part 4 does not define how those documents are produced.

The boundary prevents Part 4 from accidentally becoming a specification for:

- chunk scheduling;
- OCR or media preprocessing;
- internal intermediate representation;
- prompt orchestration;
- LLM call planning;
- review queues;
- approval workflows;
- session state;
- cache state;
- progressive reinterpretation;
- engine-specific recovery behavior.

This section is not intended to make any particular authoring engine central to Core.

It exists to protect the Core YAML boundary: Part 4 specifies the document format, not the authoring process.

## 0.11 Source Reference Policy

`sources` should represent Original Source references in a media-independent way.

Recommended minimal shape:

```yaml
sources:
  - id: src-001
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

## 0.12 Source Anchor and Traceability Policy

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
anchors:
  - source: src-001
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

## 0.13 Section Serialization Decision

A Section should represent a Projection-shaped local source window.

Recommended minimal shape:

```yaml
sections:
  - id: sec-001
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

- `id`;
- title or label;
- source anchors;
- ordered Occurrence references;
- local notes;
- status;
- optional profile or extension fields.

A Section should not be required to correspond to an Original Source heading.

## 0.14 Occurrence Serialization Decision

An Occurrence should represent a role-bearing placement of Entity material within a Section.

Recommended minimal shape:

```yaml
occurrences:
  - id: occ-001
    entity: ent-001
    role: evidence
    status: active
    rationale:
```

An Occurrence should be able to contain:

- `id`;
- Entity reference;
- role;
- status;
- local rationale;
- anchors when needed;
- ordering when not provided by Section;
- optional profile or extension fields.

`role` SHOULD be mandatory for Occurrences, because role-bearing placement is the main reason Occurrence exists.

## 0.15 Entity Serialization Decision

An Entity should represent Projection-shaped reusable material.

`content` is not mandatory.

An Entity SHOULD contain at least one of `content`, `payload`, or `ref` unless a profile explicitly permits placeholder Entities.

These three fields represent different ways of carrying or pointing to reusable material:

- `content` is the simple human-readable text field;
- `payload` is the structured value field;
- `ref` points to externally held material.

Recommended minimal shapes:

```yaml
entities:
  - id: ent-001
    kind: claim
    content: Human-readable reusable text.
```

```yaml
entities:
  - id: ent-002
    kind: structured_observation
    payload:
      metric: latency
      value: 120
      unit: ms
```

```yaml
entities:
  - id: ent-003
    kind: external_reference
    ref: source-fragment://example
```

An Entity should be able to contain:

- `id`;
- optional kind or type;
- `content` for human-readable textual reusable material;
- `payload` for structured YAML data or non-text reusable material;
- `ref` for reference-only reusable material;
- status;
- source role or local notes;
- optional anchors;
- optional profile or extension fields.

`payload` is not removed from the model.

Part 4 should avoid requiring a universal Entity kind taxonomy.

Entity `kind` may be profile-defined or open vocabulary, and should be recommended rather than mandatory in Core mode.

## 0.16 Status Policy

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

## 0.17 Ordering Policy

Ordering should be explicit when it affects reconstruction.

Recommended policy:

- Array order MAY be considered authoring order but should not be the only normative reconstruction order.
- Section-level `occurrences` arrays define Occurrence order within a Section.
- Optional `structure` namespace may define document-level Section order.

Example:

```yaml
structure:
  sections:
    - sec-001
    - sec-002
```

`structure` should be optional.

Sections can still be referenced directly and may also appear in array order.

## 0.18 Validation Modes

Part 4 should define validation behavior for at least two modes:

### Core mode

Validates required Core structure and required fields.

Allows extension fields and unknown namespaces with warnings.

### Strict mode

Rejects unknown namespaces, unknown fields, or unknown vocabulary values unless declared by profile.

Strict mode is useful for tests, CLI validation, and controlled pipelines.

A future profile mode may validate additional profile-defined fields.

## 0.19 Extension Policy

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
  - id: ent-001
    kind: constraint
    content: ...
    x-example-org:
      custom_field: ...
```

Part 4 should choose a recommended extension style.

## 0.20 Compatibility and Migration Policy

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

## 0.21 Serialization Format Decision

YAML should remain the primary human-authored serialization format for IdeaMark Core v1.2.0.

Part 4 may define JSON-equivalent behavior for tools.

Recommended policy:

- YAML is the primary authoring and documentation format;
- JSON may be used as a normalized machine representation;
- YAML anchors and advanced YAML features should be discouraged or prohibited for interoperability;
- ordering-sensitive semantics should be represented explicitly rather than relying only on YAML array or map order.

## 0.22 Normative Examples Policy

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

## 0.23 Resolved Decisions for Initial Draft

The following decisions are accepted for the initial Part 4 draft:

1. Required namespaces must exist, but empty arrays are allowed during draft, template, partial generation, or staged authoring.
2. `structure` is optional.
3. `occurrence.role` is mandatory.
4. `entity.kind` is recommended but not mandatory in Core mode.
5. `entity.content` is not mandatory.
6. An Entity should contain at least one of `content`, `payload`, or `ref` unless a profile permits placeholder Entities.
7. Source anchors should use a common base shape with type-specific extension fields.
8. Unknown fields and namespaces should be preserved and warned about in Core mode.
9. Strict mode may reject unknown fields, namespaces, or vocabulary values.
10. Part 4 defines Document Format, not Authoring Engine internals.

## 0.24 Remaining Open Decisions Before Full Draft

The following decisions should be finalized while drafting Part 4:

1. Which `meta` fields are mandatory beyond `spec_version`, `document_id`, and `status`?
2. Should source anchor shape be unified into a single `anchors` array format everywhere?
3. Should inline Projection fragments be limited to simple notes in Core?
4. Should placeholder Entities be allowed in Core mode or only by profile?
5. Which exact validation severities should be used: error, warning, info?

## 0.25 Initial Recommendation

The initial Part 4 draft should begin with a conservative array-based Core:

```yaml
meta:
sources:
  - id: src-001
sections:
  - id: sec-001
occurrences:
  - id: occ-001
    role: example_role
entities:
  - id: ent-001
    content: Example reusable material.
```

It should allow optional `structure` and `extensions`.

It should not require `relations`, `perspectives`, or `provenance`.

It should record Projection references but should not define Projection internals.

It should define an Authoring Engine Boundary so that Part 4 remains a document serialization specification rather than an authoring process specification.

It should prioritize traceability, LLM generation reliability, explicit IDs, validator clarity, and round-trip preservation over broad semantic expressiveness.
