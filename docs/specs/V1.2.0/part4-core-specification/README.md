# Part 4 — Core Specification

**Version:** IdeaMark Core v1.2.0  
**Status:** Initial Draft Complete

Part 4 defines the normative representation, required fields, compatibility rules, and validation constraints for IdeaMark Core v1.2.0.

Part 4 is expected to be the primary reference for CLI parser, formatter, validator, migration tooling, retrieval indexing, and interoperability implementations.

Part 4 encodes the conceptual model defined in Part 3 and the Projection boundary clarified in Part 5.

It should not re-expand Core by restoring concepts that Part 3 intentionally kept outside the required Core Model.

The optional `skeletons` namespace is added as a Core-adjacent retrieval structure. It does not make semantic `relations` a required Core namespace.

## Drafting Inputs

Part 4 was drafted after reviewing:

- [Part 3 — Core Model](../part3-core-model/README.md)
- [Part 5 — Projection Specification](../part5-projection-specification/README.md)
- [Part 4 Serialization Decisions](./00-serialization-decisions.md)

## Sections

0. [Part 4 Serialization Decisions](./00-serialization-decisions.md) *(decision memo)*
1. [Specification Overview](./00-specification-overview.md) *(draft)*
2. [Document Structure](./01-document-structure.md) *(draft)*
3. [Required Top-level Namespaces](./02-required-top-level-namespaces.md) *(draft)*
4. [Common Object Requirements](./03-common-object-requirements.md) *(draft)*
5. [Metadata and Projection References](./04-metadata-and-projection-references.md) *(draft)*
6. [Original Source References](./05-original-source-references.md) *(draft)*
7. [Source Anchors and Traceability](./06-source-anchors-and-traceability.md) *(draft)*
8. [Sections](./07-sections.md) *(draft)*
9. [Occurrences](./08-occurrences.md) *(draft)*
10. [Entities](./09-entities.md) *(draft)*
11. [Structure and Ordering](./10-structure-and-ordering.md) *(draft)*
12. [Status, Versioning, and Regeneration Metadata](./11-status-versioning-and-regeneration-metadata.md) *(draft)*
13. [Optional Extensions](./12-optional-extensions.md) *(draft)*
14. [Validation Rules](./13-validation-rules.md) *(draft)*
15. [Compatibility and Migration](./14-compatibility-and-migration.md) *(draft)*
16. [Serialization Requirements](./15-serialization-requirements.md) *(draft)*
17. [Normative Examples](./16-normative-examples.md) *(draft)*
18. [Core Specification Non-goals](./17-core-specification-non-goals.md) *(draft)*
19. [Skeleton Graph YAML Extension](./20-skeleton-graph-yaml-extension.md) *(draft)*

## Review Notes

- [Sample Conformance Review](./18-sample-conformance-review.md) *(review note)*
- [Open Review Issues](./19-open-review-issues.md) *(review note)*

## Normalized Samples

- [Part 4 Normalized YAML Samples](./samples/README.md)

The normalized samples are implementation-oriented examples derived from Part 3 design experiments and rewritten into the Part 4 array-based object representation.

They are intended to support parser, validator, formatter, migration, retrieval-indexing, and conformance-suite development.

## Required Core Namespaces

Part 4 defines the normative representation for the required Core access-structure namespaces:

- `meta`
- `sources`
- `sections`
- `occurrences`
- `entities`

These namespaces are required because they represent the minimum interoperable Core access-structure model.

Required namespaces may be empty during draft, template, partial generation, or staged authoring.

## Optional or Profile-defined Namespaces

The following are not required Core namespaces in v1.2.0:

- `structure`
- `skeletons`
- `relations`
- `perspectives`
- `provenance`
- domain-specific vocabularies;
- Projection Library internals;
- runtime session state;
- authoring engine internal state.

`structure` is defined as an optional Core-adjacent namespace for document-level ordering and grouping.

`skeletons` is defined as an optional Core-adjacent namespace for retrieval-oriented Intellectual Activity Skeleton Graphs.

Other optional namespaces may appear in profiles, extensions, companion specifications, or implementation-specific documents.

## Projection Boundary

Part 4 defines how an IdeaMark document records Projection references, inline Projection notes, and Projection-related metadata.

Part 4 does not define the full content model of Projection itself.

Projection authoring, Projection evaluation, Projection compatibility modeling, Projection lifecycle, Projection Skeleton Graph requirements, and Projection Library governance belong primarily to Part 5 or companion specifications.

## Runtime Context Boundary

Part 4 allows metadata fields that record generation environment, tool identity, timestamps, local notes, or runtime parameters when useful for traceability.

However, runtime context is not a required Core object.

Part 4 does not require IdeaMark documents to preserve the full execution state of a human workflow, AI session, CLI command, or authoring engine.

## Authoring Engine Boundary

Part 4 defines the document representation that authoring engines may emit, validate, exchange, normalize, migrate, or index for retrieval.

It does not define how those documents are produced.

Authoring engines may include CLI workflows, batch converters, visual editors, IDE plugins, AI agents, or companion systems such as Progressive Occurrence Resolution.

Part 4 does not define chunking algorithms, internal IR, session state, prompt orchestration, review queues, cache state, progressive scheduling, graph matching algorithms, or other engine-specific authoring behavior.

## Normative Role

Part 4 is the first primarily normative part of the v1.2.0 specification.

It encodes the conceptual model defined in Part 3 without expanding the Core beyond the design scope defined in Part 1.

It also preserves the Projection boundaries defined in Part 5 so that concrete YAML representation remains interoperable without becoming a Projection authoring schema.

## Scope

Part 4 defines YAML-level requirements and validation behavior.

It does not define Projection content, authoring strategy, retrieval ranking, storage engines, runtime session state, authoring engine algorithms, graph database representation, or user-interface behavior.

## Review Focus

The next review pass should focus on:

1. checking that the resolved decisions in [Open Review Issues](./19-open-review-issues.md) are reflected consistently across the normative chapters;
2. deciding whether `meta.projections.inline` needs additional scope guidance;
3. deciding whether anchor `role` / `purpose` should appear in normative examples;
4. deciding how much legacy migration detail belongs in Part 4;
5. extending normalized samples into a reusable conformance suite;
6. confirming that CLI diagnostic codes and command behavior remain outside Part 4;
7. validating that optional `skeletons` improves retrieval without replacing Sections, Occurrences, Entities, or anchors.
