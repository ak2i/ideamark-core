# Part 4 — Core Specification

**Version:** IdeaMark Core v1.2.0  
**Status:** Planned / Ready for Drafting

Part 4 defines the normative representation, required fields, compatibility rules, and validation constraints for IdeaMark Core v1.2.0.

Part 4 is expected to be the primary reference for CLI parser, formatter, validator, migration tooling, and interoperability implementations.

Part 4 should encode the conceptual model defined in Part 3 and the Projection boundary clarified in Part 5.

It should not re-expand Core by restoring concepts that Part 3 intentionally kept outside the required Core Model.

## Drafting Inputs

Part 4 should be drafted after reviewing:

- [Part 3 — Core Model](../part3-core-model/README.md)
- [Part 5 — Projection Specification](../part5-projection-specification/README.md)
- [Part 4 Serialization Decisions](./00-serialization-decisions.md)

## Proposed Sections

0. [Specification Overview](./00-specification-overview.md) *(planned)*
1. [Document Structure](./01-document-structure.md) *(planned)*
2. [Required Top-level Namespaces](./02-required-top-level-namespaces.md) *(planned)*
3. [Common Object Requirements](./03-common-object-requirements.md) *(planned)*
4. [Metadata and Projection References](./04-metadata-and-projection-references.md) *(planned)*
5. [Original Source References](./05-original-source-references.md) *(planned)*
6. [Source Anchors and Traceability](./06-source-anchors-and-traceability.md) *(planned)*
7. [Sections](./07-sections.md) *(planned)*
8. [Occurrences](./08-occurrences.md) *(planned)*
9. [Entities](./09-entities.md) *(planned)*
10. [Structure and Ordering](./10-structure-and-ordering.md) *(planned)*
11. [Status, Versioning, and Regeneration Metadata](./11-status-versioning-and-regeneration-metadata.md) *(planned)*
12. [Optional Extensions](./12-optional-extensions.md) *(planned)*
13. [Validation Rules](./13-validation-rules.md) *(planned)*
14. [Compatibility and Migration](./14-compatibility-and-migration.md) *(planned)*
15. [Serialization Requirements](./15-serialization-requirements.md) *(planned)*
16. [Normative Examples](./16-normative-examples.md) *(planned)*
17. [Core Specification Non-goals](./17-core-specification-non-goals.md) *(planned)*

## Required Core Namespaces

Part 4 should define the normative representation for the required Core access-structure namespaces.

The expected required namespaces are:

- `meta`
- `sources`
- `sections`
- `occurrences`
- `entities`

A structure or ordering namespace may also be defined if needed, but it should not introduce semantic meaning beyond ordering, grouping, or document organization.

## Optional or Profile-defined Namespaces

The following should not be required Core namespaces in v1.2.0:

- `relations`
- `perspectives`
- `provenance`
- domain-specific vocabularies;
- Projection Library internals;
- runtime session state;
- POR internal state.

These may appear in profiles, extensions, companion specifications, or implementation-specific documents.

If Part 4 allows optional namespaces, it should define how unknown or extension namespaces are preserved, ignored, warned about, or rejected by validators.

## Projection Boundary

Part 4 should define how an IdeaMark document records Projection references, inline Projection fragments, and Projection-related metadata.

Part 4 should not define the full content model of Projection itself.

Projection authoring, Projection evaluation, Projection compatibility modeling, Projection lifecycle, and Projection Library governance belong primarily to Part 5 or companion specifications.

## Runtime Context Boundary

Part 4 may allow metadata fields that record generation environment, tool identity, timestamps, local notes, or runtime parameters when useful for traceability.

However, runtime context is not a required Core object.

Part 4 should not require IdeaMark documents to preserve the full execution state of a human workflow, AI session, CLI command, or progressive authoring engine.

## Progressive Occurrence Resolution Boundary

Progressive Occurrence Resolution, abbreviated as POR in the IdeaMark ecosystem, may produce IdeaMark-compatible structures.

Part 4 should define the document representation that POR may emit or validate against.

Part 4 should not define POR algorithms, internal IR, session state, LLM orchestration, context-force reinterpretation, or progressive scheduling.

## Normative Role

Part 4 is the first primarily normative part of the v1.2.0 specification.

It should encode the conceptual model defined in Part 3 without expanding the Core beyond the design scope defined in Part 1.

It should also preserve the Projection boundaries defined in Part 5 so that concrete YAML representation remains interoperable without becoming a Projection authoring schema.

## Scope

Part 4 should define YAML-level requirements and validation behavior.

It should not define Projection content, authoring strategy, retrieval ranking, storage engines, runtime session state, progressive authoring algorithms, or user-interface behavior.
