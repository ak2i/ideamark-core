# 00 — Core Model Overview

**Part:** 3 — Core Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 0.1 Purpose of the Core Model

The IdeaMark Core Model defines the conceptual objects needed for an IdeaMark document to function as a reusable access structure.

An IdeaMark document is produced by Projection-guided Decomposition of Original Source material.

It is not a knowledge base, a summary, a semantic ontology, or a container of final meaning.

Its purpose is to help future humans and AI systems return to relevant Original Source material, understand the Projection-shaped structure that was generated, and create activation expressions that can support Human-AI Intellectual Activity.

The Core Model therefore defines the minimum conceptual roles needed for:

- traceability to Original Sources;
- Projection-shaped organization;
- reusable material placement;
- reconstruction support;
- interoperability across authoring and retrieval tools.

## 0.2 Core Flow

The Core Model assumes the following conceptual flow:

```text
Original Source material
        x
Projection Context
        ↓
Projection-guided Decomposition
        ↓
IdeaMark Document
        ↓
Sections / Occurrences / Entities
        ↓
Later retrieval, reconstruction, and activation expression generation
```

This flow does not prescribe an algorithm.

It only defines the conceptual boundary of the model.

Decomposition may be performed by humans, LLMs, tools, POR-like workflows, or mixed processes.

## 0.3 Original Source

An Original Source is any accessible material that can participate in Projection-guided Human-AI Intellectual Activity.

Original Sources may include:

- documents;
- source code;
- images;
- audio;
- video;
- datasets;
- sensor logs;
- conversations;
- generated artifacts;
- composite materials;
- future media that can be made accessible to humans, AI systems, or tools.

The Core Model does not restrict Original Sources to text.

However, practical use requires accessibility.

If source material cannot be observed, referenced, transformed, or supplied to a reconstruction process, it cannot function as a practical Original Source in current IdeaMark workflows.

## 0.4 Projection Context

A Projection Context is the reuse strategy that shapes Decomposition.

It determines what is useful to preserve, how the Original Source is locally organized, what material becomes reusable, and what future reconstruction activity should be supported.

Projection Context is not the same as final meaning.

It is also not merely a prompt.

A Projection may encode purpose, audience, focus, exclusions, assumptions, intended activities, or compatibility information.

Part 3 does not define Projection authoring, evaluation, lifecycle, or governance.

Those belong primarily to Part 5.

Part 3 only requires that the Projection Context relevant to generation can be referenced or recorded sufficiently for later traceability and reconstruction.

## 0.5 Decomposition

Decomposition is the Projection-guided structuring act that produces an IdeaMark document from Original Source material.

```text
Input:  Original Source material x Projection Context
Process: Projection-guided Decomposition
Output: IdeaMark Document
```

Decomposition is not general extraction.

The same Original Source may produce different IdeaMark documents under different Projections.

The output of Decomposition is the IdeaMark document as a whole.

The generated document may include metadata, Sections, Occurrences, Entities, source anchors, status information, ordering information, and local rationale.

Decomposition is not assumed to be reversible.

An IdeaMark document may explain why some structures were generated, but it is not required to contain a complete inverse mapping of the Decomposition process.

## 0.6 IdeaMark Document

An IdeaMark document is an operational access-structure artifact.

It is generated from one or more Original Sources under one or more Projection Contexts.

It may later be used to:

- retrieve or reopen Original Source material;
- understand what Projection shaped the generated structure;
- select relevant Sections, Occurrences, or Entities;
- support reconstruction under the original Projection or a compatible Projection;
- generate activation expressions for future Human-AI Intellectual Activity.

An IdeaMark document is an operational snapshot.

It is not a universal representation of the Original Source.

Multiple valid IdeaMark documents may be generated from the same Original Source under different Projections.

An IdeaMark document may itself become an Original Source for later IdeaMark generation.

## 0.7 Core Objects

The required Core Model objects for Part 3 are:

```text
meta
sections
occurrences
entities
```

The Core Model may also define optional document-level structures such as:

```text
structure
status
traceability information
local rationale
```

The central structural objects are Section, Occurrence, and Entity.

They are defined functionally:

```text
Section
  = Projection-shaped local source window

Occurrence
  = role-bearing placement of reusable material within that window

Entity
  = reusable material shaped by Projection and available for later reconstruction
```

These names are historical and descriptive.

They should not be read as domain-specific semantic categories.

## 0.8 Section

A Section is a Projection-shaped local source window.

It is a bounded local context created by Decomposition so that future reconstruction can reopen or reason about a useful part of the Original Source.

A Section is not necessarily:

- a source heading;
- a chapter;
- a topic;
- a workflow step;
- a document section;
- a final unit of meaning.

A Section may group source fragments, Occurrences, local rationale, ordering information, and source anchors.

The same Original Source may produce different Section structures under different Projections.

## 0.9 Occurrence

An Occurrence is a role-bearing placement of reusable Entity material within a Section.

It explains how an Entity participates in a local source window under a Projection.

An Occurrence is not necessarily:

- a textual occurrence;
- an event;
- an observation;
- a source span;
- an instance of a universal concept.

The same Entity-like material may be placed differently under different Projections.

For example, in a recipe source, miso paste may occur as:

- a heat-control step under a Cooking Execution Projection;
- a seasoning and body component under an Ingredient Function Projection;
- a soy-based dietary constraint under a Dietary Constraint Projection.

The source fragment may be similar, but the Occurrence role changes.

## 0.10 Entity

An Entity is reusable material shaped by Projection.

It may represent a concept, object, task, ingredient, rule, function, evidence item, state, transition, decision, or other material depending on Projection and domain practice.

Core does not require universal Entity identity.

Entity IDs should be treated primarily as reference labels within an IdeaMark document or implementation-defined scope.

An Entity must not be treated as final meaning.

Entity content may be explanatory enough to support reconstruction, but it remains Projection-shaped reusable material, not a substitute for Original Source material.

## 0.11 Metadata

The `meta` area records document-level context needed for traceability and reconstruction.

It may include:

- document identity;
- spec version;
- status;
- Original Source references;
- Projection references;
- inline Projection material;
- generation information;
- timestamps;
- source revisions;
- projection revisions;
- generator or tool information;
- review notes.

Perspective and Provenance are not required Core Model objects in Part 3.

Their practical responsibilities are handled through metadata, source references, projection references, source anchors, generation notes, and local rationale.

## 0.12 Source Anchors and Traceability

Traceability is a Core responsibility.

An IdeaMark document should preserve enough traceability for later humans, AI systems, or tools to return to relevant Original Source material.

A source anchor is a traceability claim.

It may refer to:

- a line range;
- a paragraph;
- a code span;
- a document heading;
- an ingredient line;
- a recipe step;
- a media time range;
- an image region;
- a dataset row or column;
- a composite source fragment;
- an approximate or tool-specific source position.

Text line ranges are only one implementation case.

Core should remain media-independent.

## 0.13 Structure

The optional `structure` area may record document-level ordering, grouping, navigation, or reconstruction paths.

It should not be used to reintroduce Relation as a mandatory Core object.

Ordering and grouping may be sufficient for many reconstruction tasks.

Relation-like structures may be added later as an extension, profile, or companion specification.

## 0.14 Relation, Perspective, and Provenance

Relation is not required as a Core object in v1.2.0 Part 3.

The design experiments did not require a separate Relation namespace.

Section grouping, Occurrence roles, Entity material, source anchors, metadata, and ordering were sufficient to support reconstruction.

Perspective and Provenance are also not required as separate Core namespaces.

They may appear as metadata patterns, extension fields, authoring notes, or companion specifications when needed.

## 0.15 Core Invariants

The Core Model should preserve the following invariants:

1. An IdeaMark document is produced by Projection-guided Decomposition.
2. An IdeaMark document does not store final meaning.
3. An IdeaMark document does not replace Original Source material.
4. A Section is a Projection-shaped local source window.
5. An Occurrence is a role-bearing placement within a Section.
6. An Entity is Projection-shaped reusable material.
7. Traceability to Original Source material is more important than semantic completeness.
8. Multiple valid IdeaMark documents may exist for the same Original Source.
9. Multiple Projections and multiple Original Sources may participate in one document or in related documents.
10. Core defines model roles, not universal domain vocabularies.
11. Core does not prescribe Decomposition algorithms, retrieval algorithms, or storage architecture.

## 0.16 Relationship to Part 4

Part 3 defines conceptual requirements.

Part 4 defines concrete YAML representation and validation rules.

Therefore, examples in Part 3 may use YAML-like notation for readability, but they are not normative YAML syntax unless Part 4 adopts them.

## 0.17 Relationship to Part 5

Part 5 defines Projection as a reusable strategy and ecosystem object.

Part 3 only requires that the Projection Context used for Decomposition can be referenced or recorded sufficiently for later reconstruction.

Part 3 does not decide whether a Projection is high quality, broadly reusable, socially appropriate, legally safe, or ready for inclusion in a Projection Library.

## 0.18 Summary

Part 3 defines IdeaMark Core as a Projection-shaped access model.

Its central objects are:

```text
IdeaMark Document
  -> meta
  -> sections
  -> occurrences
  -> entities
  -> optional structure and traceability information
```

The model should remain minimal while supporting reusable access, source traceability, reconstruction, and future Human-AI Intellectual Activity.
