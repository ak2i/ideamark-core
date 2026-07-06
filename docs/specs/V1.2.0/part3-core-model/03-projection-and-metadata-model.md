# 03 — Projection and Metadata Model

**Part:** 3 — Core Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 3.1 Purpose

This section defines how Projection references and document metadata are treated in the IdeaMark Core Model.

Projection shapes Decomposition.

Metadata records enough document-level context to support traceability, reconstruction, comparison, regeneration, and interoperability.

Part 3 does not define Projection authoring, Projection evaluation, Projection library governance, or Projection compatibility scoring.

Those belong primarily to Part 5 or to implementations and profiles.

## 3.2 Projection in Part 3

A Projection is the reuse strategy, interpretive constraint, or generation strategy that shapes how Original Source material is decomposed into an IdeaMark document.

In Part 3, Projection is treated only as a conceptual input to Decomposition and as metadata needed for later reconstruction.

A Projection may include or reference:

- purpose;
- intended future activity;
- audience;
- focus areas;
- non-goals;
- assumptions;
- exclusion rules;
- granularity preferences;
- expected reconstruction use;
- compatibility hints;
- role vocabularies;
- source-selection criteria.

Projection is not final meaning.

It is also not merely a prompt.

It is the conceptual input that makes Decomposition Projection-guided rather than general extraction.

Part 5 defines Projection responsibilities in more detail.

## 3.3 Projection, Metadata, and Runtime Context

Part 3 does not introduce Projection Context as a separate Core object.

The responsibilities previously associated with Projection Context are handled by:

- **Projection** — the reusable strategy that shapes Decomposition and reconstruction;
- **Projection metadata** — document-level records of which Projection, reference, fragment, version, or note shaped generation;
- **runtime context** — implementation- or workflow-specific conditions supplied when a Projection is applied.

Runtime context may include current user, permissions, current date, active task, local overrides, tool settings, available media, or session state.

Runtime context can affect authoring or reconstruction, but it is not defined as a required Core object in Part 3.

Part 4 or companion specifications may define concrete fields for runtime parameters if needed.

```text
Original Source material
        x
Projection
        x
runtime context when applicable
        ↓
Projection-guided Decomposition
        ↓
IdeaMark Document
```

The same Original Source may generate different IdeaMark documents under different Projections.

For example:

- a code file may be decomposed for algorithm learning, API design, performance engineering, or stream processing;
- a database subsystem file may be decomposed for correctness invariants, state-machine review, locking, or recovery analysis;
- a design RFC may be decomposed for rationale, migration impact, evidence evaluation, teaching, or governance review;
- a recipe may be decomposed for cooking execution, ingredient substitution, shopping, teaching, or dietary adaptation.

Projection determines which local source windows become Sections, how reusable material is shaped into Entities, and what role placements become Occurrences.

## 3.4 Projection Is Not Projection Governance

Part 3 does not decide whether a Projection is:

- correct;
- high quality;
- safe;
- legally appropriate;
- socially appropriate;
- institutionally approved;
- broadly reusable;
- publishable in a Projection Library;
- compatible with another Projection.

Part 3 only requires that the Projection relevant to generation can be recorded or referenced sufficiently for later use.

Projection governance belongs to Part 5, profiles, institutions, communities, or implementations.

## 3.5 Generation Projection and Reconstruction Projection

The Projection used for generation and the Projection used later for reconstruction do not need to be identical.

A later reconstruction may use:

- the same Projection;
- a newer version of the same Projection;
- a narrower Projection;
- a broader Projection;
- a compatible Projection;
- a different Projection that partially overlaps;
- a Projection that finds only source pointers and requires new Decomposition.

The IdeaMark document should preserve enough Projection metadata for later systems to judge whether existing Sections, Occurrences, and Entities are likely to be useful.

Part 3 does not require a formal compatibility algorithm.

## 3.6 Projection-shaped Coverage

Coverage in IdeaMark is Projection-relative.

An IdeaMark document does not claim to cover the entire Original Source unless the Projection and metadata explicitly indicate such intent.

A document generated under one Projection may omit source material that is important under another Projection.

For example, a `heapq.py` document generated for performance engineering may preserve comparison-cost reasoning but omit stream-merge material.

This is not a failure of the document.

It means the document is a Projection-shaped access structure, not a complete source representation.

Metadata may record focus, non-goals, or coverage notes when useful.

## 3.7 Metadata Definition

Metadata is document-level context recorded to support traceability, reconstruction, review, versioning, and interoperability.

Metadata may include:

- document identity;
- spec version;
- document status;
- Original Source references;
- Projection references;
- inline Projection material;
- generation timestamp;
- generator or tool identity;
- source revision information;
- Projection revision information;
- review notes;
- local rationale conventions;
- compatibility notes;
- profile information;
- license or access notes where relevant.

Metadata should help future users understand how the document was generated and how it may be used.

Metadata should not become a container for final meaning.

## 3.8 Required Metadata Responsibilities

At the conceptual level, metadata should support the following responsibilities:

1. **Document identity** — distinguish the document from other IdeaMark documents.
2. **Specification awareness** — identify the IdeaMark Core version or profile used.
3. **Source traceability** — record references to Original Sources.
4. **Projection traceability** — record the Projection, Projection reference, or Projection fragment that shaped Decomposition.
5. **Operational status** — record whether the document is draft, generated, reviewed, deprecated, or otherwise operationally marked.
6. **Revision awareness** — record source and Projection revisions where relevant.
7. **Regeneration support** — preserve enough context to support later regeneration or comparison.

Part 4 may define concrete required fields.

## 3.9 Projection References

A Projection may be recorded by reference, inline definition, or both.

A Projection reference may identify:

- a Projection library entry;
- a local file;
- a URI;
- a versioned identifier;
- a Git revision;
- a document section;
- an inline authoring note;
- an implementation-defined object.

A document may include multiple Projection entries with roles such as:

```yaml
projections:
  - role: generation
    ref_id: projection://performance-engineering/heapq/v0
  - role: reconstruction_reference
    ref_id: projection://api-design/library-interface/v0
  - role: inline_note
    inline_yaml: |
      purpose: extract fixed-size heap operation reasoning
      audience: software engineer
```

This example is illustrative, not normative YAML for Part 3.

## 3.10 Projection Roles

Projection metadata may distinguish roles.

Common conceptual roles include:

- **generation** — Projection used to generate the document or structure.
- **reconstruction_reference** — Projection expected to be useful for later reconstruction.
- **comparison** — Projection used to compare generated structures.
- **inline_note** — local Projection-like context recorded directly in metadata.
- **compatibility_hint** — note that another Projection may partially reuse the document.

Part 3 does not require a fixed role vocabulary.

Part 4 or profiles may define required role values.

## 3.11 Multiple Projections

One IdeaMark document may reference multiple Projections.

This may occur when:

- the document is generated from a composite Projection;
- multiple source regions were decomposed under different Projections;
- the document records reconstruction-reference Projections;
- the document is designed to compare multiple Projection views;
- the document aggregates structures from earlier IdeaMark documents.

Part 3 allows this conceptually.

Part 4 should define how multiple Projection references are represented.

## 3.12 Multiple Original Sources and Projections

A document may involve multiple Original Sources and multiple Projections.

The Core Model should allow systems to record enough context to understand which source material and Projection shaped a given structure.

Possible conceptual patterns include:

```text
Document-level source and Projection metadata
  -> Section-level anchors
  -> Occurrence-level roles
  -> Entity-level reusable material
```

or:

```text
Source x Projection generation records
  -> generated Sections
```

Part 3 does not require one universal representation for all such cases.

Part 4 may define a concrete representation.

## 3.13 Metadata and Perspective

Perspective is not a required Core namespace in Part 3.

Earlier Perspective responsibilities are handled by:

- Projection;
- Projection metadata;
- purpose and audience notes;
- focus and non-goal fields;
- local rationale;
- reconstruction-reference notes.

A profile may define a `perspective` field or namespace if useful.

Core does not require it.

## 3.14 Metadata and Provenance

Provenance is not a required Core namespace in Part 3.

Earlier Provenance responsibilities are handled by:

- Original Source references;
- source revisions;
- source anchors;
- generation metadata;
- generator or tool notes;
- timestamps;
- review status;
- local rationale;
- regeneration notes.

A profile may define richer provenance structures.

Core does not require them.

## 3.15 Metadata and Final Meaning

Metadata must not be used to smuggle final meaning into the Core Model.

It may record why a document was generated, what Projection shaped it, what source revisions were used, or what local conventions apply.

It should not claim that the document contains a complete final interpretation of the Original Source.

Metadata supports access and reconstruction.

It does not replace interpretation.

## 3.16 Conceptual Minimum

At the conceptual level, an IdeaMark document should record enough metadata for:

```text
later user or tool
  -> identify document
  -> identify relevant Original Sources
  -> identify generation Projection
  -> understand status or revision context
  -> follow source anchors
  -> evaluate whether reconstruction is likely to be useful
```

Part 4 may define concrete fields such as:

```yaml
meta:
  document_id:
  spec_version:
  status:
  sources:
  projections:
  generated_at:
  generator:
```

This example is illustrative, not normative for Part 3.

## 3.17 Invariants

Projection and metadata should preserve the following invariants:

1. Decomposition is Projection-guided, not general extraction.
2. Projection shapes Sections, Occurrences, and Entities.
3. Projection metadata supports later reconstruction but does not store final meaning.
4. A generation Projection and reconstruction Projection may differ.
5. Coverage is Projection-relative.
6. One document may reference multiple Projections.
7. One document may reference multiple Original Sources.
8. Perspective and Provenance are not required Core namespaces.
9. Metadata should support traceability, revision awareness, and regeneration without becoming workflow governance.

## 3.18 Summary

Projection explains why an IdeaMark document has the structure it has.

Metadata records enough context for future traceability and reconstruction.

Part 3 requires Projection and metadata responsibilities conceptually, but leaves concrete representation to Part 4 and Projection lifecycle questions to Part 5.
