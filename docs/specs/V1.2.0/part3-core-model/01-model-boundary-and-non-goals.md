# 01 — Model Boundary and Non-goals

**Part:** 3 — Core Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 1.1 Purpose

This section defines the boundary of the IdeaMark Core Model.

The Core Model exists to define the conceptual structures required for an IdeaMark document to function as a Projection-shaped access structure.

It does not define every activity, algorithm, storage mechanism, validation rule, or authoring process surrounding IdeaMark.

The boundary is necessary because IdeaMark intentionally separates:

- Original Source material;
- Projection Context;
- Decomposition;
- generated access structures;
- later reconstruction;
- activation expression generation;
- Human-AI Intellectual Activity.

Part 3 defines the generated access structures and their conceptual responsibilities.

It does not collapse the entire Human-AI Intellectual Activity process into the document model.

## 1.2 Core Model Scope

Part 3 defines the conceptual responsibilities of:

- IdeaMark Document;
- document metadata;
- Original Source references;
- Projection Context references;
- Decomposition boundary;
- Sections;
- Occurrences;
- Entities;
- source anchors and traceability claims;
- optional structure and ordering information;
- status and versioning at the conceptual level.

Part 3 defines these as model roles, not as final YAML syntax.

Concrete YAML representation belongs to Part 4.

Projection authoring, Projection evaluation, and Projection lifecycle belong primarily to Part 5.

## 1.3 Core Model Non-goals

The Core Model does not define:

- final meaning;
- universal truth;
- universal ontology;
- universal domain vocabulary;
- universal authority ranking;
- universal coordinate system;
- universal taxonomy of intellectual activities;
- a complete theory of interpretation;
- a complete model of human cognition;
- a complete model of AI reasoning;
- a storage engine;
- a retrieval algorithm;
- a ranking algorithm;
- a Decomposition algorithm;
- an authoring workflow;
- a review workflow;
- a governance process;
- Projection quality metrics;
- Projection library membership rules;
- concrete YAML schema details;
- JSON storage layout;
- database indexes;
- user interface behavior.

These may be addressed by later parts, profiles, companion specifications, implementations, Projection libraries, or domain practices.

## 1.4 Meaning Boundary

IdeaMark does not store final meaning.

Meaning is not considered to be contained entirely in an Original Source, Projection, IdeaMark document, or generated explanation by itself.

Meaning becomes observable when expression, interpretation, Situation, and activity meet and produce intellectual, practical, or observational consequence.

Therefore, Part 3 must not define Core objects as final containers of meaning.

A Section is not a meaning unit.

An Occurrence is not a meaning event.

An Entity is not a universal semantic object.

Instead:

```text
Section
  = Projection-shaped local source window

Occurrence
  = role-bearing placement of reusable material within that window

Entity
  = reusable material shaped by Projection and available for later reconstruction
```

These objects help future reconstruction and activation.

They do not complete interpretation by themselves.

## 1.5 Original Source Boundary

An IdeaMark document does not replace Original Source material.

The Original Source remains necessary for non-trivial reconstruction.

The Core Model should therefore prioritize traceability over semantic completeness.

An IdeaMark document may preserve labels, content snippets, role placements, local rationale, and source anchors, but these should not be treated as a full substitute for the Original Source.

Part 3 models how to preserve access to Original Source material, not how to embed all relevant source meaning into the IdeaMark document.

## 1.6 Projection Boundary

Projection shapes Decomposition.

Part 3 requires that the relevant Projection Context can be referenced or recorded sufficiently for later reconstruction.

However, Part 3 does not define:

- how Projections are authored;
- how Projections are evaluated;
- how Projection libraries are governed;
- how Projection compatibility is scored;
- how Projections are selected from a Situation Vector;
- how Projections should be socially or institutionally approved.

Part 3 only needs the Projection Context as a conceptual input to Decomposition and as metadata for later traceability.

Projection as an ecosystem object belongs primarily to Part 5.

## 1.7 Decomposition Boundary

Decomposition is the Projection-guided structuring act that produces an IdeaMark document from Original Source material.

Part 3 defines the conceptual boundary of Decomposition:

```text
Input:  Original Source material x Projection Context
Process: Projection-guided Decomposition
Output: IdeaMark Document
```

Part 3 does not define the algorithm used to perform Decomposition.

Decomposition may be performed by:

- humans;
- LLMs;
- deterministic tools;
- mixed human-AI workflows;
- POR-like large-scale authoring workflows;
- future systems not yet specified.

The generated IdeaMark document may contain local rationale or generation notes, but it is not required to contain a complete reversible record of Decomposition.

## 1.8 Reconstruction Boundary

Part 3 supports reconstruction, but it does not define a reconstruction algorithm.

Reconstruction may involve:

- searching IdeaMark documents;
- selecting relevant Sections;
- following source anchors;
- reopening Original Source material;
- applying the original Projection;
- applying a compatible or different Projection;
- generating activation expressions;
- asking follow-up questions;
- comparing multiple IdeaMark documents.

The Core Model should reduce the cost of these activities.

It should not require that an IdeaMark document alone can reconstruct every useful activation expression.

In most non-trivial cases, reconstruction should return to Original Source material.

## 1.9 Storage and Retrieval Boundary

Part 3 does not define storage architecture.

An implementation may store IdeaMark documents in:

- files;
- Git repositories;
- document databases;
- relational databases;
- vector databases;
- object stores;
- search indexes;
- hybrid systems.

Part 3 also does not define retrieval algorithms.

However, the Core Model should remain suitable for retrieval by preserving:

- document metadata;
- source references;
- Projection references;
- Section-level organization;
- Occurrence roles;
- Entity material;
- source anchors;
- optional ordering and structure.

Part 4 and implementation specifications may define concrete serialization and indexing practices.

## 1.10 Validation Boundary

Part 3 defines conceptual validity.

Part 4 defines representation validity.

For example, Part 3 may state that an Occurrence places Entity material within a Section under a role.

Part 4 may later specify the YAML fields required to represent that relationship.

Part 3 examples may use YAML-like notation for readability, but they are illustrative unless Part 4 adopts them as normative syntax.

## 1.11 Domain Boundary

Core does not define domain vocabularies.

It should not decide that an Entity must be a person, concept, ingredient, state, function, evidence item, or task.

Those interpretations depend on Projection and domain practice.

The same Core structure should support:

- code analysis;
- system design;
- RFC reasoning;
- cooking recipes;
- organizational knowledge;
- research notes;
- datasets;
- future media.

Core defines the role of Entity, Occurrence, and Section in the access structure.

It does not define the domain taxonomy that fills them.

## 1.12 Relation Boundary

Relation is not a required Core namespace in IdeaMark Core v1.2.0 Part 3.

The design experiments did not require a separate Relation object to support reconstruction.

Section grouping, Occurrence roles, Entity material, source anchors, and metadata were sufficient.

Relation-like structures may be useful in some profiles or implementations.

They may be added later as:

- optional extension fields;
- companion specifications;
- Projection-defined structures;
- domain-specific relation vocabularies;
- retrieval graph indexes.

Core must not require Relation as a mandatory object.

## 1.13 Perspective and Provenance Boundary

Perspective and Provenance are not required Core namespaces in Part 3.

The responsibilities previously associated with them are handled by:

- Projection references;
- inline Projection metadata;
- Original Source references;
- source anchors;
- generation notes;
- local rationale;
- tool and timestamp metadata;
- review notes;
- status and versioning information.

More elaborate perspective or provenance systems may be defined by profiles, repositories, institutions, or companion specifications.

Core only requires enough metadata and traceability to support later reconstruction.

## 1.14 Multi-source and Multi-projection Boundary

Part 3 allows:

- one IdeaMark document to reference multiple Original Sources;
- one IdeaMark document to reference multiple Projections;
- multiple IdeaMark documents to be generated from the same Original Source under different Projections;
- multiple IdeaMark documents to be retrieved, compared, or reconstructed together later.

Part 3 does not require a universal source aggregation model or Projection compatibility algorithm.

It only requires that documents can record sufficient source and Projection context for later use.

## 1.15 Boundary Summary

The Core Model should be minimal but sufficient.

It must define enough structure to support:

- Projection-guided Decomposition;
- traceability to Original Sources;
- reusable local source windows;
- role-bearing placement of reusable material;
- future retrieval and reconstruction;
- interoperability across tools and implementations.

It must avoid defining:

- final meaning;
- universal ontology;
- storage architecture;
- retrieval algorithms;
- Projection governance;
- domain vocabulary;
- complete intellectual activity workflows.

This boundary preserves IdeaMark as a Projection-shaped access model rather than a meaning store, knowledge base, or workflow engine.
