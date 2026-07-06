# Part 3 Drafting Issues

**Part:** 3 — Core Model  
**Status:** Specification Drafting Notes  
**Type:** Drafting Notes / Editorial Planning

This document identifies the remaining issues that should be resolved while drafting Part 3.

Earlier exploratory questions have been narrowed by the design experiments in this directory.

Part 3 should now proceed from the following working interpretation:

```text
Section
  = Projection-shaped local source window

Occurrence
  = role-bearing placement of reusable material within that window

Entity
  = reusable material shaped by Projection and available for later reconstruction
```

## 0.1 Central Drafting Question

The central question for Part 3 is:

> What minimal conceptual objects must IdeaMark Core define so that future humans and AI systems can return to relevant Original Source material through Projections without storing final meaning?

This question replaces the earlier framing of reconstructing useful interpretations directly from the IdeaMark document.

IdeaMark should reduce the cost of returning to the right Original Source material and generating activation expressions under a Projection.

It should not be required to reconstruct everything from itself alone.

## 0.2 Model Orientation

Part 3 should model:

- reusable access structures;
- traceability to Original Sources;
- Projection-shaped local source windows;
- role-bearing placement of reusable material;
- document-level identity and context;
- Decomposition as the bridge between Original Source and Core Model structures;
- status, versioning, and regeneration responsibilities;
- invariants that preserve reconstruction usefulness.

Part 3 should avoid modeling:

- final meaning;
- universal truth;
- universal authority ranking;
- universal ontology;
- universal domain vocabulary;
- universal coordinate system;
- complete intellectual activity content;
- Projection quality evaluation;
- Projection library governance;
- implementation storage or retrieval design.

## 0.3 Required and Non-required Conceptual Objects

The following conceptual objects appear necessary for Part 3 Core:

1. **Original Source Reference** — a traceable reference to source material used as the basis for Projection-guided generation or reconstruction.
2. **Projection Context** — the reuse strategy or Projection identity that shaped the IdeaMark document.
3. **Decomposition** — the Projection-guided modeling act that transforms Original Source material into an IdeaMark Document.
4. **IdeaMark Document** — an operational access-structure artifact generated from Original Source(s) under Projection Context.
5. **Section** — a Projection-shaped local source window.
6. **Occurrence** — a role-bearing placement of reusable Entity material within a Section.
7. **Entity** — Projection-shaped reusable material.
8. **Source Anchor / Traceability Claim** — a media-independent claim connecting structures to Original Source material.
9. **Status and Versioning** — operational state of documents across regeneration, coexistence, review, and deprecation.

The following are not required Core namespaces in Part 3 v1.2.0:

1. **Relation** — may be added later as an extension, profile, or companion specification.
2. **Perspective** — responsibilities are handled through Projection metadata and document context.
3. **Provenance** — responsibilities are handled through metadata, generation notes, source references, anchors, and local rationale.

The exact YAML form of these concepts belongs to Part 4.

## 0.4 Resolved Findings from Experiments

The following design findings are considered sufficiently resolved for Part 3 drafting.

### 0.4.1 Projection changes generation

The same Original Source can produce meaningfully different IdeaMark-like structures under different generation Projections.

This was observed across:

- CPython `heapq.py`;
- SQLite `pager.c`;
- Rust RFC 0001;
- a recipe test fixture.

The difference appears in selected source regions, Section boundaries, Occurrence roles, Entity kinds, and likely future activation expressions.

### 0.4.2 Section is not a source heading

Section should not be defined as a document heading or source chapter.

It should be defined as a Projection-shaped local source window.

A Section may align with a source heading, but this is not required.

### 0.4.3 Occurrence is not merely source occurrence

Occurrence should not be defined as a textual occurrence or source appearance.

It should be defined as a role-bearing placement of reusable Entity material within a Section.

The same source fragment may participate in different Occurrences under different Projections.

### 0.4.4 Entity is not universal meaning

Entity should not be defined as a final semantic object or globally stable knowledge unit.

It should be defined as Projection-shaped reusable material.

Entity identity may be local to the document unless a profile or implementation defines a broader identity system.

### 0.4.5 Relation is not required for Core

The experiments did not require a separate Relation namespace.

Ordering, Section grouping, Occurrence roles, Entity payloads, source anchors, and metadata were sufficient.

Relation should not be mandatory in v1.2.0 Core.

### 0.4.6 Perspective and Provenance can remain metadata

Perspective and Provenance do not need to be separate Core Model objects.

Projection references, source references, generation context, source anchors, local rationale, and notes are sufficient for Core.

More elaborate provenance or perspective systems may be defined by profiles or companion specifications.

## 0.5 Remaining Drafting Issues

The remaining questions are specification-level issues rather than conceptual blockers.

### 0.5.1 Required versus optional fields

Part 3 should decide which fields are conceptually required for interoperability and which are representation details for Part 4.

Likely conceptual minimum:

```yaml
meta:
  spec_version:
  sources:
  projections:

sections:
  <id>:
    occurrences:

occurrences:
  <id>:
    entity:
    role:

entities:
  <id>:
    kind:
    content:
```

Open questions:

- Is `title` required for Section, or only recommended?
- Is `source_anchor` required for every Section, or only for practical profiles?
- Should `role` be required for every Occurrence?
- Can Entity `content` be replaced by external reference in some profiles?

### 0.5.2 Source anchor model

Anchorage should be defined as a generalized traceability claim.

It must support:

- line ranges;
- paragraphs;
- code spans;
- ingredient lines;
- recipe steps;
- media time ranges;
- image regions;
- dataset rows or columns;
- composite source fragments;
- approximate anchors;
- tool-specific anchors.

Open questions:

- Should Part 3 define a conceptual `source_anchor` object?
- Should anchors attach primarily to Sections, or also to Occurrences and Entities?
- Should unanchored structures be allowed during draft or speculative authoring?

Likely direction:

Source anchors should be allowed at multiple levels, but Section-level anchors are the primary Core expectation.

### 0.5.3 Entity payload boundary

Entity content can easily become a summary or mini-meaning store.

Part 3 should warn against treating Entity payload as final meaning.

Open questions:

- How explanatory may Entity content be?
- Can Entity content include interpretation-like text if it is Projection-shaped and source-traceable?
- Should Part 3 distinguish `content`, `label`, `payload`, and `source_ref` conceptually?

Likely direction:

Entity content may be explanatory enough to support reconstruction, but it remains Projection-shaped reusable material and must not replace Original Source material.

### 0.5.4 Occurrence role vocabulary

Core should not define a universal role ontology.

Open questions:

- Should `role` be a required free string?
- Should roles be Projection-defined?
- Should profiles define role vocabularies?

Likely direction:

`role` should be required or strongly recommended, but vocabulary should be Projection-defined or profile-defined.

### 0.5.5 Structure namespace

The optional `structure` namespace may record ordering, grouping, navigation, or reconstruction paths.

Open questions:

- Is `structure` required if Section order is already encoded elsewhere?
- Should `structure` support multiple alternative orderings?
- Should `structure` be allowed to reference Sections only, or also Occurrences and Entities?

Likely direction:

Keep `structure` optional in Core.

Do not use it to reintroduce mandatory Relation.

### 0.5.6 Status and versioning

IdeaMark documents are operational snapshots.

Open questions:

- Should status apply only at document level?
- Should object-level status be allowed but optional?
- How should regeneration be tracked without requiring global identity stability?

Likely direction:

Part 3 should define document-level status first and allow object-level status as optional extension.

Possible document metadata:

```yaml
meta:
  spec_version:
  document_id:
  status:
  generated_at:
  generator:
  source_revision:
  projection_revision:
```

### 0.5.7 Multi-source and multi-projection handling

Part 3 should clarify that:

- one IdeaMark document may reference multiple Original Sources;
- one IdeaMark document may reference multiple Projections;
- multiple IdeaMark documents may be generated from the same Original Source under different Projections;
- different generated documents may later be searched, compared, or reconstructed together.

Open questions:

- Does Core need explicit generation pair records for Source x Projection combinations?
- How much of this belongs to Part 3 versus Part 4 or Part 5?

Likely direction:

Part 3 should define the conceptual allowance. Part 4 should define representation details.

## 0.6 Part 3 / Part 4 Boundary

Part 3 defines conceptual requirements.

Part 4 defines concrete YAML syntax and validation rules.

Part 3 may use YAML-like examples, but those examples are illustrative unless Part 4 makes them normative.

## 0.7 Part 3 / Part 5 Boundary

Part 3 defines the Core Model produced by Projection-guided Decomposition.

Part 5 defines Projection as a reusable strategy and ecosystem object.

Part 3 should not decide whether a Projection is:

- high quality;
- socially shareable;
- legally appropriate;
- institutionally approved;
- broadly reusable;
- too narrow;
- too broad;
- obsolete;
- worth publishing in a Projection Library.

Those are Projection lifecycle and ecosystem questions.

Part 3 should only require that the Projection Context used for Decomposition can be referenced or recorded sufficiently for later reconstruction.

## 0.8 Recommended Drafting Order

Recommended Part 3 drafting order:

1. Core Model Overview.
2. Model Boundary and Non-goals.
3. Original Source Reference Model.
4. Projection Context and Metadata Model.
5. Decomposition Model.
6. IdeaMark Document Model.
7. Section Model.
8. Occurrence Model.
9. Entity Model.
10. Anchorage and Traceability Model.
11. Status, Versioning, and Regeneration Model.
12. Model Invariants.
13. Core Model Summary.

This order establishes the boundary before individual model objects are finalized.

## 0.9 Questions to Resolve Before Writing Normative YAML

Before Part 4 defines YAML syntax, Part 3 should resolve:

- Which conceptual objects are mandatory in every IdeaMark document?
- Which conceptual objects are optional but Core-defined?
- Which fields are conceptual requirements versus YAML representation choices?
- How strongly every document should preserve source anchors.
- Whether Projection Context must always be explicitly recorded.
- Whether Decomposition should be represented explicitly or only implied by Projection Context and generated structures.
- Whether Entity, Occurrence, and Section identifiers are local, document-level, repository-level, or implementation-defined.
- How to express uncertainty, review status, and regeneration without turning the model into workflow management.
- How to support multi-source documents without requiring a universal source aggregation model.
- How to support non-textual sources without making text offsets the hidden default.
- How to represent local rationale, provenance-like notes, or method notes without implying full reversibility of Decomposition.

## 0.10 Summary

Part 3 can now proceed as a specification draft.

The Core Model should be precise enough to support interoperability and validation, but not so prescriptive that it freezes meaning, source media, domain vocabulary, Projection practice, Decomposition workflow, or future intellectual activity.

Its central modeling stance is that IdeaMark documents are produced by Projection-guided Decomposition and preserve Projection-shaped access structures rather than final interpretations.
