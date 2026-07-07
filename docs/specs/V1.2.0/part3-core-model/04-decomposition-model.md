# 04 — Decomposition Model

**Part:** 3 — Core Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 4.1 Purpose

This section defines Decomposition in the IdeaMark Core Model.

Decomposition is the Projection-guided structuring act that produces an IdeaMark document from Original Source material.

It is the conceptual bridge between:

- Original Source material;
- Projection Context;
- generated Sections, Occurrences, and Entities;
- optional Skeleton Graphs;
- later retrieval, reconstruction, and meaning activation.

Part 3 defines Decomposition conceptually.

It does not define a Decomposition algorithm or workflow.

## 4.2 Definition

Decomposition is the process boundary by which Original Source material is structured under a Projection Context into an IdeaMark document.

```text
Input:  Original Source material x Projection Context
Process: Projection-guided Decomposition
Output: IdeaMark Document
```

The output is the IdeaMark document as a whole.

Sections, Occurrences, Entities, source anchors, metadata, local rationale, status information, optional structure information, and optional Skeleton Graphs may all be products of Decomposition.

## 4.3 Decomposition Is Projection-guided

Decomposition is not general extraction.

The same Original Source may produce different IdeaMark documents under different Projections.

A source code file may yield different structures when decomposed for:

- performance engineering;
- algorithm learning;
- API design;
- data pipeline reuse;
- domain adaptation.

A recipe may yield different structures when decomposed for:

- cooking execution;
- ingredient substitution;
- shopping preparation;
- beginner teaching;
- dietary adaptation.

The Projection Context determines what local source windows are useful, what reusable material should be preserved, what Skeleton Graph patterns may be useful for later retrieval, and what future activity the document should support.

## 4.4 Decomposition Is Not Meaning Extraction

Decomposition does not extract final meaning from the Original Source.

It creates Projection-shaped access structures.

The resulting IdeaMark document should help future systems or users return to Original Source material and generate activation expressions.

It does not eliminate the need for future interpretation.

Therefore, Decomposition should not be understood as:

- summarization;
- semantic parsing into final truth;
- ontology construction;
- universal knowledge extraction;
- source replacement;
- complete interpretation capture;
- universal workflow modeling.

It is the creation of reusable access structure under a Projection.

When Decomposition produces a Skeleton Graph, that graph should be understood as a domain-reduced retrieval aid, not as stored meaning.

## 4.5 Decomposition Product

The Decomposition product is the IdeaMark document.

A generated IdeaMark document may contain:

- metadata;
- Original Source references;
- Projection references;
- Sections;
- Occurrences;
- Entities;
- source anchors;
- optional structure information;
- optional Skeleton Graphs;
- local rationale;
- generation notes;
- status information.

The Core Model objects do not have to be generated independently.

A Section, Occurrence, Entity, or Skeleton Node is meaningful in Core only as part of the generated access structure.

## 4.6 Section Production

Under Decomposition, a Section is produced as a Projection-shaped local source window.

It is a bounded local context that makes some part, combination, or view of Original Source material useful for future reconstruction.

A Section may be created from:

- one source span;
- multiple source spans;
- one source object;
- multiple source objects;
- a source heading;
- a non-heading source fragment;
- inferred grouping across source fragments;
- composite media fragments.

A Section boundary is determined by Projection-guided usefulness, not by source layout alone.

## 4.7 Occurrence Production

Under Decomposition, an Occurrence is produced as a role-bearing placement of Entity material within a Section.

It records how reusable material participates in that local source window under the Projection.

An Occurrence may be produced from:

- direct source appearance;
- inferred use;
- evidence placement;
- procedural placement;
- explanatory placement;
- design-rationale placement;
- constraint placement;
- source-fragment combination.

The same source fragment may produce different Occurrences under different Projections.

The same Entity-like material may appear under different roles in different Sections.

## 4.8 Entity Production

Under Decomposition, an Entity is produced as reusable material shaped by Projection.

An Entity may correspond to:

- a concept;
- an object;
- a step;
- a rule;
- an invariant;
- a state;
- a transition;
- an ingredient;
- a function;
- evidence;
- a decision;
- an example;
- a caution;
- another reusable material type defined by Projection or domain practice.

Core does not require universal Entity identity.

Core also does not require that Entities be meaningful outside the document or Projection context.

An Entity is useful because it can be placed, referenced, reused, or reconstructed.

## 4.9 Skeleton Graph Production

Under Decomposition, a Skeleton Graph may be produced as an optional retrieval-oriented representation of an Intellectual Activity Skeleton.

It records how Sections, Occurrences, Entities, anchors, or placeholder slots participate in an activity-composition pattern.

A Skeleton Graph may be produced when:

- future retrieval should not depend on exact source keywords;
- cross-domain or analogical matching is expected;
- the Projection defines required or preferred activity slots;
- candidate selection needs lower-cost structural filtering before reconstruction;
- missing slots should be visible for review or failure handling.

A Skeleton Graph may contain nodes that reference generated Sections, Occurrences, Entities, source anchors, or profile-defined structures.

A Skeleton Graph may also contain placeholder nodes for slots that the Projection expects but the current source does not satisfy.

Skeleton Graph production should avoid turning domain-specific surface vocabulary into universal Core vocabulary.

The purpose is to preserve activity composition, not to define a domain ontology.

## 4.10 Source Anchor Production

Decomposition may produce source anchors.

A source anchor is a traceability claim connecting generated structures to Original Source material.

Source anchors may be attached to:

- Sections;
- Occurrences;
- Entities;
- metadata;
- structure entries;
- Skeleton Nodes;
- local rationale;
- extension objects.

Section-level anchors are the primary Core expectation because Sections are local source windows.

Occurrence-level and Entity-level anchors may be useful for more precise traceability.

Skeleton Graphs should ultimately lead back to traceable structures when used for reconstruction.

## 4.11 Local Rationale

A generated IdeaMark document may include local rationale.

Local rationale explains why a structure was produced, how it should be used, or how it relates to the Projection Context.

For example, rationale may explain:

- why a source region became a Section;
- why an Entity was placed in a Section through an Occurrence;
- why an Occurrence has a particular role;
- why a Skeleton Node was assigned a particular slot;
- why a Skeleton Link type was selected;
- why a source anchor is approximate;
- why some material was omitted;
- why a Section is useful for a future reconstruction activity.

Local rationale is optional unless required by a profile.

It is not a complete inverse mapping of Decomposition.

## 4.12 Non-reversibility

Decomposition is not assumed to be fully reversible.

Given only an IdeaMark document, a later user or tool may not be able to reconstruct exactly why every Decomposition decision was made.

This is acceptable.

The document should preserve enough structure and traceability to support later retrieval and reconstruction, not a complete record of the generation process.

Generation notes, rationale, tool information, source anchors, and Skeleton Graphs may improve explainability, but they do not make Decomposition fully reversible.

## 4.13 Human, AI, and Tool Decomposition

Decomposition may be performed by:

- a human author;
- an LLM;
- a deterministic program;
- an AI-assisted authoring tool;
- a POR-like batch process;
- a review workflow;
- a mixed human-AI process;
- a future system.

Core does not privilege one authoring mechanism.

Part 3 defines what the generated document must conceptually support, not how it is produced.

## 4.14 Decomposition and POR

POR-like processes may perform large-scale or automated Decomposition.

Part 3 should remain compatible with such processes.

A POR-like process may emit Skeleton Graphs as an intermediate or final retrieval aid, but Core does not require POR to do so.

However, POR is not required by Core.

Core should not prescribe:

- batching strategy;
- source ingestion pipeline;
- model prompts;
- review workflow;
- parallelization method;
- storage architecture;
- regeneration scheduler;
- graph matching implementation.

These belong to implementations or companion specifications.

## 4.15 Decomposition and Review

A generated IdeaMark document may be reviewed, corrected, extended, regenerated, or deprecated.

Review may modify:

- metadata;
- Sections;
- Occurrences;
- Entities;
- anchors;
- Skeleton Graphs;
- rationale;
- structure;
- status.

Part 3 does not define review workflow.

It only requires that the document remain traceable and conceptually coherent after modification.

## 4.16 Decomposition and Multiple Outputs

One Original Source and Projection Context may produce multiple IdeaMark documents.

Multiple Original Sources and Projections may also produce one IdeaMark document.

Valid cases include:

- one source decomposed under several Projections into several documents;
- one source decomposed under several Projections into several Skeleton Graphs;
- one source decomposed under a composite Projection into one document;
- several sources decomposed under one Projection into one document;
- several generated documents later combined or compared;
- an IdeaMark document used as an Original Source for a later document.

Part 3 allows these cases conceptually.

Part 4 may define representation details.

## 4.17 Decomposition Quality

Part 3 does not define Decomposition quality metrics.

It does not decide whether a Decomposition is:

- useful;
- complete;
- fair;
- safe;
- unbiased;
- domain-approved;
- institutionally valid;
- publishable.

Those questions belong to Projection practice, review workflow, governance, or implementation policy.

Part 3 defines structural responsibilities and invariants only.

Skeleton Graph quality is also outside Part 3 Core, though Part 5 and Part 6 may discuss retrieval-oriented evaluation.

## 4.18 Decomposition Failure and Partial Documents

A Decomposition may be partial, exploratory, draft, or failed.

Part 3 should allow documents or structures to carry status metadata indicating their operational state.

A partial document may still be useful if it preserves traceable access structures.

A partial Skeleton Graph may be useful if it exposes missing slots, uncertain links, or review needs.

However, a document that cannot identify its Original Source or Projection Context may fail to function as an IdeaMark document in the Core sense.

## 4.19 Conceptual Minimum

At the conceptual level, Decomposition must produce enough structure for:

```text
later user or tool
  -> identify source material
  -> identify Projection Context
  -> select relevant Sections
  -> inspect role-bearing Occurrences
  -> use Entity material
  -> follow source anchors
  -> return to Original Source material
  -> support reconstruction or activation expression generation
```

When Skeleton Graphs are present, Decomposition may additionally support:

```text
later user or tool
  -> identify use-side Projection Skeleton expectations
  -> match document-side Skeleton Graphs
  -> select candidate Sections / Occurrences / Entities / anchors
  -> explain matched and missing activity slots
  -> support lower-cost retrieval before reconstruction
```

Part 4 may define the concrete minimum YAML representation.

## 4.20 Invariants

Decomposition should preserve the following invariants:

1. Decomposition is Projection-guided.
2. Decomposition is not general extraction.
3. Decomposition does not store final meaning.
4. The output of Decomposition is the IdeaMark document as a whole.
5. Sections are Projection-shaped local source windows.
6. Occurrences are role-bearing placements within Sections.
7. Entities are Projection-shaped reusable material.
8. Source anchors preserve traceability claims.
9. Skeleton Graphs, when present, support retrieval-oriented activity-composition matching.
10. Skeleton Links are not semantic Relations.
11. Decomposition need not be fully reversible.
12. Decomposition algorithm and workflow are outside Core.
13. Multiple valid Decomposition outputs may exist for the same Original Source.
14. Decomposition quality evaluation is outside Part 3 Core.
