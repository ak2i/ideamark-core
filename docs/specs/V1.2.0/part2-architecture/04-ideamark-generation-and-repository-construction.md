# 4. IdeaMark Generation and Repository Construction

**Part:** 2 — Architecture of Human-AI Co-evolution  
**Status:** Draft Rev002  
**Type:** Informative / Reference Architecture

IdeaMark generation transforms an Original Source and a Projection into an IdeaMark document or document set.

Repository construction makes those IdeaMark documents available for future reconstruction.

This section describes architectural responsibilities, not required implementation mechanisms.

## 4.1 Purpose

The purpose of IdeaMark generation is to create reusable access structures that help future humans and AI systems return to Original Sources and reconstruct intellectual activity under a Projection.

The purpose of repository construction is to make those access structures discoverable and reusable.

Neither generation nor repository construction turns IdeaMark into the final authority for meaning.

An Original Source is treated as authority for the Projection-guided generation and reconstruction activity, but IdeaMark Core does not declare the source universally authoritative, true, complete, or final.

## 4.2 Generation as Source-Projection Transformation

The basic generation pattern is:

```text
Original Source
        x
Projection
        ↓
IdeaMark Document
```

The Original Source provides the material basis for construction.

The Projection defines how that material should become reusable for a future class of intellectual activities.

The generated IdeaMark document records reusable structures shaped by that Projection.

This transformation may be performed by humans, AI systems, deterministic tools, templates, review workflows, or combinations of these.

Part 2 does not prescribe the generation method.

## 4.3 Repository as Availability Layer

An IdeaMark repository is any mechanism that makes IdeaMark documents available for future use.

It may be a file directory, database, document store, object store, search system, application memory, local cache, version-controlled repository, or another implementation-specific mechanism.

Part 2 does not define a required repository technology.

The architectural role of the repository is to preserve availability, traceability, and reuse of generated IdeaMark documents.

```text
IdeaMark Documents
        ↓
Repository / Availability Mechanism
        ↓
Retrieval, Regeneration, Review, or Reconstruction
```

The repository should be understood as an architectural responsibility, not as a mandatory product component.

## 4.4 Repository Responsibilities

A repository may support responsibilities such as:

- storing or referencing IdeaMark documents;
- associating documents with Original Sources;
- associating documents with Projections;
- supporting retrieval or lookup;
- preserving versions;
- allowing multiple documents for the same source;
- allowing multiple documents for the same Projection;
- recording generation status;
- supporting review status;
- enabling regeneration;
- preserving traceability.

These responsibilities may be distributed across multiple systems.

IdeaMark Core should not require that they all be implemented in a single database or service.

## 4.5 Multiple Documents for One Source

The same Original Source may have multiple IdeaMark documents.

This may occur because:

- different Projections were applied;
- different versions of a Projection were applied;
- different generation methods were used;
- a document was regenerated after review;
- a temporary exploratory document was preserved;
- different organizations require different access structures;
- historical versions remain useful.

Multiple IdeaMark documents for one source are not necessarily duplicates.

They may represent different access strategies for different reconstruction purposes.

## 4.6 Multiple Sources for One Reconstruction Activity

A single reconstruction activity may require multiple Original Sources.

An implementation may therefore retrieve or generate multiple IdeaMark documents and then guide the user or AI system back to several source materials.

```text
Current Situation
        ↓
Projection
        ↓
IdeaMark Documents from Multiple Sources
        ↓
Original Source Set
        ↓
Reconstruction
```

Part 2 does not define how such source sets are ranked, merged, clustered, or presented.

It only recognizes that reconstruction often requires more than one source.

## 4.7 Document Status and Review

Generated IdeaMark documents may have different operational statuses.

For example, a document may be:

- temporary;
- provisional;
- reviewed;
- accepted for organizational use;
- deprecated;
- superseded;
- archived;
- regenerated.

Part 2 does not define the status vocabulary.

Later parts or implementations may define concrete fields and rules.

The architectural point is that generated IdeaMark documents are operational artifacts whose reliability, review status, and intended use may vary.

## 4.8 Repository Construction and Original Source Access

Repository construction should preserve the ability to return to Original Sources.

If an IdeaMark document is stored without sufficient source traceability, it may still be readable, but it becomes weaker as a reconstruction aid.

The repository should therefore support source access where possible.

This may involve direct links, source identifiers, content hashes, file references, citation metadata, offsets, archival references, or other implementation-specific mechanisms.

Part 2 does not define the required mechanism.

## 4.9 Repository Construction and Projection Access

Repository construction should also preserve the connection between generated IdeaMark documents and the Projections that shaped them.

Without Projection traceability, future users may not understand what kind of reuse the document was designed to support.

A generated IdeaMark document may become misleading if interpreted under assumptions that differ significantly from its Projection.

This does not mean a document can only be used with its original Projection.

It means that knowing the original Projection helps future humans and AI systems evaluate how the document should be reused, adapted, or regenerated.

## 4.10 Regeneration and Coexistence

Repository construction should allow for regeneration and coexistence.

Regeneration may produce a new IdeaMark document from the same source and Projection.

Coexistence may preserve multiple documents for different Projections, versions, review states, or use cases.

```text
Source S + Projection P v1 → IdeaMark A
Source S + Projection P v2 → IdeaMark B
Source S + Projection Q    → IdeaMark C
```

In this example, A, B, and C may all remain useful.

The repository should not assume that only one canonical IdeaMark document can exist for a source.

## 4.11 Non-goals

This section does not define:

- a repository database schema;
- a storage engine;
- a search index;
- a vector index;
- a file naming convention;
- a synchronization protocol;
- a review workflow;
- a governance model;
- a ranking algorithm;
- a persistence requirement for temporary documents.

These may be defined by implementations, companion specifications, or organizational practices.

## 4.12 Design Rationale

IdeaMark generation and repository construction are separated from meaning reconstruction so that documents can remain operational access structures.

The repository makes reusable structures available.

The reconstruction process later uses those structures to return to Original Sources and interpret them under a current Situation and Projection.

This separation prevents the repository from becoming a final knowledge store and keeps Original Sources available as the material basis for Projection-guided reconstruction.

It also reduces interpretation cost because later participants can inspect which source and Projection shaped a document rather than treating the document as an opaque result.

## 4.13 Summary

IdeaMark generation creates access structures from Original Sources and Projections.

Repository construction makes those access structures available for future reconstruction.

A repository may support many implementation forms, but its architectural role is to preserve availability, traceability, Projection context, and the possibility of regeneration or coexistence.
