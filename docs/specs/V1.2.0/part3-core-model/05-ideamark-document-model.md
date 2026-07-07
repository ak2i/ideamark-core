# 05 — IdeaMark Document Model

**Part:** 3 — Core Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 5.1 Purpose

This section defines the conceptual role of an IdeaMark document in the Core Model.

An IdeaMark document is the output of Projection-guided Decomposition.

It is an operational access-structure artifact that helps future humans, AI systems, and tools return to relevant Original Source material and generate activation expressions under a Projection.

It may also carry optional Skeleton Graphs that help future systems retrieve candidate structures before reconstruction.

It is not a final interpretation, knowledge base entry, summary, ontology object, workflow ontology, or replacement for the Original Source.

## 5.2 Definition

An IdeaMark document is a structured artifact generated from one or more Original Sources under one or more Projection Contexts.

Conceptually, it contains:

- document-level metadata;
- Original Source references;
- Projection Context references;
- Sections;
- Occurrences;
- Entities;
- traceability information;
- optional Skeleton Graphs;
- optional structure and ordering information;
- optional rationale, generation notes, and status information.

The document is the unit that carries enough context for later retrieval, reconstruction, and interoperability.

## 5.3 Document as Decomposition Output

The output of Decomposition is the IdeaMark document as a whole.

```text
Input:  Original Source material x Projection Context
Process: Projection-guided Decomposition
Output: IdeaMark Document
```

This means that Sections, Occurrences, Entities, anchors, metadata, optional Skeleton Graphs, structure, rationale, and status information should be understood as parts of one generated access structure.

They are not independent universal claims.

Their usefulness depends on the document, source references, Projection Context, retrieval context, and later reconstruction activity.

## 5.4 Document as Operational Snapshot

An IdeaMark document is an operational snapshot.

It records a Projection-guided structuring result at a particular time, under a particular context, from particular source material.

It should not be treated as:

- the only valid structure for the Original Source;
- a complete representation of the Original Source;
- a permanent semantic truth;
- an exhaustive knowledge extraction;
- a universal domain classification;
- a universal graph of intellectual activity;
- a final result of Human-AI Intellectual Activity.

Multiple valid IdeaMark documents may exist for the same Original Source.

Different Projections may produce different documents from the same source.

Different Projections may also produce different Skeleton Graphs from the same source.

Different tools or authors may also produce different valid documents under similar Projection Contexts.

## 5.5 Document and Original Source

An IdeaMark document does not replace its Original Source.

In most non-trivial cases, reconstruction should return to Original Source material.

The document should therefore preserve traceability through:

- document-level source references;
- Section-level anchors;
- optional Occurrence-level anchors;
- optional Entity-level anchors;
- optional Skeleton Node references to traceable structures;
- source revision metadata;
- local rationale when useful.

The document should reduce the cost of returning to the right source material.

It should not attempt to embed everything necessary for final interpretation.

## 5.6 Document and Projection Context

An IdeaMark document should record or reference the Projection Context that shaped its generation.

This is necessary because the document's Sections, Occurrences, Entities, and optional Skeleton Graphs are Projection-shaped.

Without Projection Context, later users may not know why particular source material was selected, grouped, omitted, linked, or given specific roles.

The document may record:

- a generation Projection reference;
- inline Projection notes;
- Projection version or revision;
- focus and non-goal metadata;
- intended reconstruction activities;
- intended retrieval activities;
- Skeleton Graph expectations or references;
- compatibility notes;
- multiple Projection entries.

Part 3 does not define the full Projection object.

It only requires that the document can preserve enough Projection Context for later use.

## 5.7 Document and Meaning

An IdeaMark document does not store final meaning.

It stores Projection-shaped access structures that can support later meaning activation.

For example, an Entity may contain explanatory material, but that material is not final meaning by itself.

A Section may gather source fragments, but it is not a final interpretation.

An Occurrence may assign a role, but that role is part of a Projection-shaped placement, not a universal truth claim.

A Skeleton Link may connect nodes, but that link is an activity-composition structure for retrieval, not a universal semantic Relation.

Meaning becomes observable later when the document, Original Source material, Projection, Situation, interpreter, and activation expression participate in intellectual or practical activity.

## 5.8 Conceptual Minimum

At the conceptual level, an IdeaMark document should contain enough information to support:

```text
later user or tool
  -> identify the document
  -> identify relevant Original Sources
  -> identify relevant Projection Context
  -> inspect Sections
  -> inspect Occurrences within Sections
  -> inspect Entity material
  -> follow source anchors
  -> return to Original Source material
  -> support reconstruction or activation expression generation
```

A minimal conceptual document therefore includes:

```text
meta
sections
occurrences
entities
```

Optional document-level structures may include:

```text
skeletons
structure
status
rationale
review notes
extension fields
```

Part 4 defines concrete YAML requirements.

## 5.9 Metadata

The document metadata area records context needed to understand and use the document.

It may include:

- document ID;
- spec version;
- document status;
- Original Source references;
- Projection references;
- generation timestamp;
- generator identity;
- source revisions;
- Projection revisions;
- profile information;
- local conventions;
- review notes.

Perspective and Provenance are not required separate Core namespaces.

Their practical responsibilities may be handled through metadata, source references, anchors, generation notes, and local rationale.

## 5.10 Sections

Sections are the primary local access units of an IdeaMark document.

A Section is a Projection-shaped local source window.

It groups or references material useful for later reconstruction.

A document may contain many Sections.

The same Original Source may produce different Section sets under different Projections.

A Section may include or reference:

- source anchors;
- Occurrence IDs;
- local title or label;
- rationale;
- ordering information;
- Skeleton Nodes that point to the Section;
- status or review notes;
- extension metadata.

## 5.11 Occurrences

Occurrences place Entity material within Sections under roles.

An Occurrence explains how a reusable material participates in a local source window.

A document may contain many Occurrences.

An Occurrence may include or reference:

- an Entity;
- a role;
- the Section in which it is placed;
- local rationale;
- source anchors;
- Skeleton Nodes that point to the Occurrence;
- status or review notes;
- extension metadata.

Occurrence roles are not universal Core vocabulary.

They are shaped by Projection, profile, or domain practice.

## 5.12 Entities

Entities are reusable materials shaped by Projection.

A document may contain many Entities.

An Entity may include:

- a local identifier;
- kind or type label;
- content or payload;
- source role;
- source references;
- Skeleton Nodes that point to the Entity;
- status or review notes;
- extension metadata.

Entity identity is not universal by default.

Core treats Entity IDs primarily as reference labels within document or implementation-defined scope.

## 5.13 Skeleton Graphs

The optional `skeletons` area may record one or more Intellectual Activity Skeleton Graphs.

A Skeleton Graph helps retrieve candidate IdeaMark structures by representing activity-composition patterns with nodes and Skeleton Links.

It may be useful when:

- future queries may not contain source-specific keywords;
- Projection reuse depends on structural activity slots;
- analogical matching across domains is expected;
- candidate selection should happen before full reconstruction;
- missing slots should be visible for review or failure handling;
- matching explanations should identify which activity-composition requirements were satisfied.

A Skeleton Graph may point to Sections, Occurrences, Entities, source anchors, or placeholder slots.

A Skeleton Graph does not replace source anchors, Section boundaries, Occurrence roles, or Entity material.

Core does not require all IdeaMark documents to contain Skeleton Graphs.

## 5.14 Structure

The optional `structure` area may record document-level ordering, grouping, navigation, or reconstruction paths.

It may be useful when:

- Section order matters;
- multiple Section orders are needed;
- reconstruction paths differ by Projection;
- grouped views are required;
- implementation needs explicit navigation metadata.

Core does not require `structure` to encode semantic relations.

Relation-like structures may be added by profiles or extensions, but Relation is not mandatory in Part 3 Core.

Skeleton Graphs serve a different role from `structure`: they support retrieval-oriented activity-composition matching rather than document navigation alone.

## 5.15 Local Rationale and Notes

An IdeaMark document may contain local rationale or notes.

These may explain:

- why a Section was created;
- why an Occurrence has a role;
- why an Entity is shaped in a particular way;
- why a Skeleton Node or Skeleton Link was created;
- why a source anchor is approximate;
- why certain source material was omitted;
- how the document should be used in retrieval or reconstruction.

Local rationale improves review and reuse.

However, it is not required to fully explain or reverse the Decomposition process.

## 5.16 Multi-source Documents

One IdeaMark document may reference multiple Original Sources.

This may be necessary when:

- a Projection requires comparison across sources;
- source code and documentation must be considered together;
- evidence comes from multiple records;
- a dataset and narrative explanation are combined;
- generated documents are reused as sources;
- multiple media participate in one activity.

The document should preserve enough source references and local anchors to distinguish which source material supports each structure.

Skeleton Graphs in multi-source documents should not hide which source material supports matched nodes.

## 5.17 Multi-projection Documents

One IdeaMark document may reference multiple Projections.

This may occur when:

- generation used a composite Projection;
- different Sections were generated under different Projection Contexts;
- different Skeleton Graphs were generated for different retrieval purposes;
- the document records reconstruction-reference Projections;
- the document compares multiple Projection views;
- earlier documents are merged or compared.

Part 3 allows this conceptually.

Part 4 may define representation details.

## 5.18 Multiple Documents from the Same Source

The same Original Source may produce multiple IdeaMark documents.

This is expected and valid.

For example, one source may produce:

- an algorithm-learning document;
- a performance-engineering document;
- an API-design document;
- a migration-impact document;
- a teaching document;
- a dietary-adaptation document.

Each document may be valid under its Projection.

No single document is required to cover the source completely.

Each document may also produce a different Skeleton Graph because each Projection may extract a different Intellectual Activity Skeleton.

## 5.19 Document Status

An IdeaMark document may have operational status.

Possible conceptual statuses include:

- draft;
- generated;
- reviewed;
- approved;
- deprecated;
- superseded;
- experimental;
- partial;
- failed.

Part 3 does not require this exact vocabulary.

Part 4, profiles, or implementations may define concrete status values.

At Core level, status exists to support operational management, review, regeneration, and safe reuse.

## 5.20 Document Regeneration

An IdeaMark document may be regenerated when:

- the Original Source changes;
- the Projection changes;
- the generator changes;
- review feedback changes the desired structure;
- a profile or schema changes;
- a different granularity is needed;
- a new retrieval purpose appears;
- a new reconstruction purpose appears.

Regeneration may produce a new document rather than overwriting the old one.

Part 3 does not require global identity stability across regeneration.

It only requires that documents can preserve enough metadata for comparison and traceability.

Regeneration may preserve, replace, or add Skeleton Graphs depending on Projection compatibility and retrieval requirements.

## 5.21 Document as Original Source

An IdeaMark document may itself become an Original Source for later IdeaMark generation.

This recursive possibility is allowed.

It does not make IdeaMark a knowledge base.

It means that generated access structures can themselves become material for later Projection-guided Decomposition.

When this occurs, later documents should preserve references to the prior document and, when useful, to the prior document's own Original Sources.

A later document may also use an earlier document's Skeleton Graph as Original Source material, for example to create a higher-level retrieval profile or compare multiple documents' activity composition.

## 5.22 Invalid or Weak Documents

A document may be weak or invalid as an IdeaMark document if it cannot support traceable reconstruction.

For example, a document may be weak if it:

- lacks source references;
- lacks Projection Context;
- contains only final summaries without traceability;
- has Entities but no Section context;
- has source anchors that cannot be interpreted;
- contains Skeleton Graphs whose nodes cannot lead back to reconstructable material;
- cannot explain its operational status;
- collapses into a general knowledge note rather than Projection-shaped access structure.

Part 4 may define validation levels.

Part 3 defines the conceptual risks.

## 5.23 Conceptual Example

The following shape is illustrative:

```yaml
meta:
  document_id: example-doc
  spec_version: 1.2.0
  status: draft
  sources:
    - id: SRC-001
      type: source_code
      ref: repository/path@revision
  projections:
    - role: generation
      ref_id: projection://example/v0

sections:
  SEC-001:
    title: Local source window
    source_anchor:
      source: SRC-001
      line_range: { start: 10, end: 20 }
    occurrences:
      - OCC-001

occurrences:
  OCC-001:
    entity: IE-001
    role: explains_local_use

entities:
  IE-001:
    kind: reusable_material
    content: Example reusable material shaped by Projection.

skeletons:
  - id: skel-001
    role: retrieval
    nodes:
      - id: skn-001
        ref:
          kind: occurrence
          id: OCC-001
        slot: reusable_activity_material
    links: []

structure:
  sections:
    - SEC-001
```

This example is not normative YAML.

Part 4 defines concrete syntax.

## 5.24 Invariants

An IdeaMark document should preserve the following invariants:

1. It is generated by Projection-guided Decomposition.
2. It references or records relevant Original Source material.
3. It references or records relevant Projection Context.
4. It does not store final meaning.
5. It does not replace the Original Source.
6. It contains Projection-shaped Sections.
7. It contains role-bearing Occurrences.
8. It contains Projection-shaped reusable Entities.
9. It supports traceability and later reconstruction.
10. It may contain optional Skeleton Graphs for retrieval-oriented matching.
11. Skeleton Links, when present, are not semantic Relations.
12. It may coexist with other valid documents from the same source.
13. It may be partial, draft, reviewed, regenerated, or deprecated.
14. It may itself become an Original Source for later Decomposition.

## 5.25 Summary

An IdeaMark document is the Core Model's operational unit.

It preserves Projection-shaped access structures that make later retrieval, reconstruction, and source return cheaper and more traceable.

It may also preserve optional Skeleton Graphs that help future systems find structurally useful material without relying only on keywords or domain labels.

It should be minimal enough to avoid becoming a knowledge base, but structured enough to support source return, Projection awareness, retrieval, reconstruction, and Human-AI Intellectual Activity.
