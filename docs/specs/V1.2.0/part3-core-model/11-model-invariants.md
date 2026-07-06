# 11 — Model Invariants

**Part:** 3 — Core Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 11.1 Purpose

This section defines the Core Model invariants for IdeaMark Core v1.2.0 Part 3.

An invariant is a condition that should remain true across valid IdeaMark documents, regardless of source domain, Projection, authoring method, storage format, or implementation.

The purpose of these invariants is to keep IdeaMark from collapsing into:

- a summary format;
- a knowledge base;
- a universal ontology;
- a source replacement;
- a workflow engine;
- a Projection governance system;
- a text-only anchoring format.

## 11.2 Core Flow Invariant

An IdeaMark document is produced by Projection-guided Decomposition.

```text
Original Source material
        x
Projection Context
        ↓
Projection-guided Decomposition
        ↓
IdeaMark Document
```

The document should be interpreted as the output of this flow.

It should not be interpreted as a general extraction result from an Original Source alone.

## 11.3 No Final Meaning Invariant

An IdeaMark document does not store final meaning.

Meaning is not contained entirely in:

- the Original Source;
- the Projection;
- the IdeaMark document;
- the generated explanation;
- any single Section, Occurrence, or Entity.

Meaning becomes observable when expression, interpretation, Situation, and activity produce intellectual, practical, or observational consequence.

Core objects preserve access structures for later meaning activation.

They do not complete meaning by themselves.

## 11.4 Source Non-replacement Invariant

An IdeaMark document does not replace Original Source material.

In most non-trivial cases, reconstruction should return to Original Source material.

The document should reduce the cost of returning to the right source material.

It should not attempt to embed all source meaning inside itself.

## 11.5 Projection-shaped Invariant

Sections, Occurrences, and Entities are Projection-shaped.

The same Original Source may produce different structures under different Projections.

A document generated under one Projection is not required to cover source material that would be important under another Projection.

Coverage is Projection-relative.

## 11.6 Section Invariant

A Section is a Projection-shaped local source window.

A Section is not necessarily:

- a source heading;
- a document chapter;
- a topic;
- a workflow step;
- a final unit of meaning.

A Section should preserve a useful local context for later reconstruction.

Section-level anchorage is the primary Core expectation.

## 11.7 Occurrence Invariant

An Occurrence is a role-bearing placement of Entity material within a Section.

An Occurrence is not merely:

- a textual occurrence;
- a source appearance;
- an event;
- an observation;
- an instance of a universal concept.

The Occurrence role is meaningful relative to Section and Projection Context.

Core does not define a universal role vocabulary.

## 11.8 Entity Invariant

An Entity is Projection-shaped reusable material.

An Entity is not by default:

- a universal semantic object;
- an ontology node;
- a globally stable knowledge item;
- a final meaning unit;
- a complete summary of source material.

Entity identity is local unless a profile or implementation defines stronger identity rules.

Entity kind vocabulary is not Core-defined.

## 11.9 Traceability Invariant

Traceability to Original Source material is a Core responsibility.

An anchor is a traceability claim connecting an IdeaMark structure to source material.

Anchors may be:

- exact;
- approximate;
- composite;
- inferred;
- tool-specific;
- human-readable;
- machine-resolvable.

Anchors are not limited to text spans or line ranges.

A document with no usable source traceability is weak as an IdeaMark document.

## 11.10 Metadata Invariant

Metadata should preserve enough context for later traceability, reconstruction, review, and regeneration.

Metadata may record:

- document identity;
- specification version;
- document status;
- Original Source references;
- Projection references;
- source revisions;
- Projection revisions;
- generation notes;
- generator information;
- review notes;
- local conventions.

Metadata supports reconstruction.

It does not store final meaning.

## 11.11 Perspective and Provenance Invariant

Perspective and Provenance are not required Core namespaces in Part 3 v1.2.0.

Their practical responsibilities are handled through:

- Projection metadata;
- Original Source references;
- source anchors;
- generation notes;
- local rationale;
- status and versioning metadata;
- profile-defined extensions when needed.

Core should not require separate Perspective or Provenance objects.

## 11.12 Relation Invariant

Relation is not a required Core namespace in Part 3 v1.2.0.

The Core Model should not require relation objects for a document to be valid.

Ordering, Section grouping, Occurrence roles, Entity material, anchors, and metadata are sufficient for the Core structure.

Relation-like structures may be introduced by profiles, extensions, companion specifications, or implementations.

## 11.13 Media Independence Invariant

Original Sources and anchors must be media-independent.

Core must support sources beyond text, including:

- code;
- images;
- audio;
- video;
- datasets;
- sensor logs;
- conversations;
- generated artifacts;
- composite source bundles;
- future accessible media.

Text line ranges are one anchor form, not the universal model.

## 11.14 Local Identity Invariant

IDs for documents, Sections, Occurrences, and Entities are reference labels unless a profile defines stronger identity rules.

Core does not require global identity stability across:

- documents;
- repositories;
- Projections;
- source revisions;
- regenerations;
- implementations.

Regeneration may preserve IDs when useful, but Core does not require this.

## 11.15 Multiple Valid Documents Invariant

Multiple valid IdeaMark documents may exist for the same Original Source.

They may differ because of:

- different Projections;
- different source revisions;
- different authoring tools;
- different granularity choices;
- different reconstruction purposes;
- different review decisions;
- regeneration.

No single document is required to be the final representation of a source.

## 11.16 Multi-source and Multi-projection Invariant

An IdeaMark document may reference multiple Original Sources.

An IdeaMark document may reference multiple Projections.

Multiple documents may later be retrieved, compared, or reconstructed together.

Core does not require a universal source aggregation model or Projection compatibility algorithm.

It only requires enough source and Projection context for later use.

## 11.17 Decomposition Non-reversibility Invariant

Decomposition is not assumed to be fully reversible.

An IdeaMark document may include rationale, generation notes, anchors, and metadata that explain some generation decisions.

However, it is not required to contain a complete inverse mapping of the Decomposition process.

## 11.18 Algorithm Non-prescription Invariant

Core does not prescribe algorithms for:

- Decomposition;
- retrieval;
- ranking;
- reconstruction;
- source selection;
- Projection compatibility;
- anchor repair;
- review;
- regeneration.

Implementations may define such algorithms.

Part 3 defines conceptual responsibilities and invariants only.

## 11.19 Operational Snapshot Invariant

An IdeaMark document is an operational snapshot.

Status and versioning are operational metadata.

They do not turn the document into final truth.

A document may be:

- draft;
- generated;
- reviewed;
- approved;
- experimental;
- partial;
- deprecated;
- superseded;
- failed;
- archived.

Part 4, profiles, or implementations may define concrete status vocabularies.

## 11.20 Review and Governance Boundary Invariant

Review and governance are outside Core as workflows.

Core should support review by preserving traceability, rationale, metadata, and status.

Core should not define who has authority to approve a document, Projection, or source.

Authority, trust, institutional approval, legal appropriateness, and governance belong to profiles, institutions, repositories, or companion specifications.

## 11.21 Recursive Source Invariant

An IdeaMark document may itself become an Original Source for later IdeaMark generation.

This does not make IdeaMark a knowledge base.

It means that generated access structures, like other artifacts, can participate in later Projection-guided Decomposition.

## 11.22 Weak Document Indicators

A document may be weak as an IdeaMark document if it:

- lacks Original Source references;
- lacks Projection Context;
- lacks usable traceability;
- contains only summaries;
- treats Entities as final meanings;
- treats Sections as copied source headings without reuse purpose;
- uses Occurrences without roles;
- cannot support source-mediated reconstruction;
- collapses into a general knowledge note.

Part 4 or profiles may define validation levels.

Part 3 identifies these conceptual risks.

## 11.23 Invariant Summary

The Core Model can be summarized by the following invariant pattern:

```text
Original Source material
        x
Projection Context
        ↓
Projection-guided Decomposition
        ↓
IdeaMark Document
        ↓
Projection-shaped Sections
        ↓
role-bearing Occurrences
        ↓
Projection-shaped reusable Entities
        ↓
source-mediated reconstruction
        ↓
future activation expression
```

The Core Model is successful when it preserves enough structure to make this path cheaper, more traceable, and more reusable without storing final meaning.
