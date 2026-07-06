# 2. Index Construction Layer

**Part:** 2 — Architecture of Human-AI Co-evolution  
**Status:** Draft Rev002  
**Type:** Informative / Reference Architecture

The Index Construction Layer creates IdeaMark documents from Original Sources and Projections.

In this layer, index means an access structure for future reconstruction.

It does not mean a database index, search engine index, vector index, storage layout, or implementation-specific optimization mechanism.

## 2.1 Purpose

The purpose of the Index Construction Layer is to produce IdeaMark documents that can later help humans and AI systems return to relevant Original Sources and reconstruct intellectual activity under a Projection.

The layer does not attempt to preserve final meaning.

It creates reusable structural traces that can support later interpretation.

```text
Original Source
        x
Projection
        ↓
IdeaMark Document
        ↓
Future Reconstruction Support
```

An IdeaMark document generated in this layer should be understood as a reconstruction aid.

It is not a replacement for the Original Source.

## 2.2 Inputs

The primary inputs of this layer are:

1. Original Sources treated as authority for the selected Projection-guided construction;
2. one or more Projections;
3. optional contextual information needed for generation;
4. optional authoring or review policies.

Original Sources may include documents, reports, transcripts, datasets, conversations, code, logs, diagrams, images, sensor streams, or other materials from which future intellectual activity may be reconstructed.

Projection defines what kind of reuse matters.

For example, a Projection may focus on field operations, policy design, education, engineering design, investment analysis, safety review, research synthesis, or another future intellectual activity.

The same Original Source may therefore produce different IdeaMark documents under different Projections.

## 2.3 Output

The output of the Index Construction Layer is an IdeaMark document or document set.

The output may contain structures such as entities, occurrences, sections, relations, source references, or other structures defined in later parts of the specification.

Part 2 does not define the exact YAML representation of these structures.

That belongs to later Core Model and Core Specification parts.

The architectural requirement is that the output can support future reconstruction by connecting a current Situation and Projection back to relevant Original Sources.

## 2.4 Source-Projection Pairing

The basic construction pattern is source-projection pairing.

```text
Source S
Projection P
        ↓
IdeaMark(S, P)
```

This notation means that the generated IdeaMark document is shaped by both the source and the Projection.

It does not mean that every implementation must precompute all source-projection combinations.

For a large source collection and a large Projection library, full precomputation may be unnecessary, expensive, or inappropriate.

An implementation may instead prioritize, defer, cache, regenerate, or generate on demand.

## 2.5 Projection Determines Reusable Structure

Projection determines what counts as reusable for the intended reconstruction activity.

It may influence:

- entity boundaries;
- occurrence boundaries;
- section organization;
- relation selection;
- source reference granularity;
- retrieval objectives;
- ignored material;
- preferred explanation paths;
- expected future interpreters.

This is why two IdeaMark documents generated from the same source may both be valid while having different structures.

They are not competing truth claims.

They are different access structures for different reconstruction purposes.

## 2.6 Generation Modes

The Index Construction Layer may operate in multiple modes.

### 2.6.1 Background Generation

A system may generate IdeaMark documents before any specific user request.

This may be useful when sources and Projections are stable enough that pre-generation improves later access.

### 2.6.2 Prioritized Generation

A system may generate IdeaMark documents first for high-value sources, high-demand Projections, or known organizational needs.

This may be useful when full generation is too costly.

### 2.6.3 On-demand Generation

A system may generate an IdeaMark document only when a reconstruction request requires a source-projection combination that does not yet exist.

This may be useful when source collections, Projections, or user needs change frequently.

### 2.6.4 Temporary Generation

A system may generate a temporary IdeaMark document for a single session, workflow, or experiment.

This may be useful for exploratory use where persistence is not yet justified.

These modes are implementation choices.

IdeaMark Core does not require one mode over another.

## 2.7 Traceability Responsibility

The Index Construction Layer should preserve traceability to Original Sources whenever possible.

Traceability supports later reconstruction because future interpreters must be able to return to the original material.

Without traceability, an IdeaMark document risks becoming a detached summary or unsupported interpretation.

Traceability may be represented by source references, payload references, citations, offsets, identifiers, or implementation-specific links.

Part 2 does not define the final representation of traceability fields.

It only identifies traceability as an architectural responsibility.

## 2.8 Review and Regeneration

IdeaMark documents are operational snapshots.

They may be reviewed, replaced, versioned, regenerated, or allowed to coexist.

Regeneration may be appropriate when:

- an Original Source changes;
- a Projection changes;
- the intended reconstruction activity changes;
- better generation methods become available;
- human review identifies weak structures;
- retrieval behavior reveals missing or misleading access paths.

Coexistence may be appropriate when multiple Projections or historical versions remain useful.

The Index Construction Layer should therefore not assume that one generated IdeaMark document is the final representation of a source.

## 2.9 Non-goals

The Index Construction Layer does not define:

- database indexing;
- vector indexing;
- storage schemas;
- file formats beyond the later Core Specification;
- job queue design;
- cache invalidation rules;
- model selection;
- generation algorithms;
- user interface behavior;
- governance rules for approving Projections.

Those concerns may be important in implementations, but they are outside the scope of Part 2.

## 2.10 Design Rationale

The Index Construction Layer exists because future reconstruction is easier when prior intellectual activities have been made accessible in advance or at the moment of need.

However, the layer must not collapse access into interpretation.

The generated IdeaMark document should help future humans and AI systems find relevant Original Sources and reconstruct meaning under a Projection.

It should not claim to be the meaning itself.

This keeps IdeaMark aligned with the Part 2 principles of separating access from interpretation, treating Projection as reuse strategy, and treating Original Source as authority for a Projection-guided construction rather than as universal truth.

## 2.11 Summary

The Index Construction Layer creates IdeaMark documents from Original Sources and Projections.

These documents are index-like because they function as reusable access structures.

They help future humans and AI systems find relevant Original Sources and reconstruct intellectual activity under current Situations and Projections.

They do not define storage-level indexing, final meaning, or required implementation architecture.
