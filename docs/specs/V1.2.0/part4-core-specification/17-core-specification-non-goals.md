# 17. Core Specification Non-goals

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 17.1 Purpose

This chapter records what Part 4 intentionally does not define.

The non-goals protect IdeaMark Core from becoming too broad, too implementation-specific, or too tied to one authoring method.

## 17.2 Meaning Is Not Stored as Final State

Part 4 does not define a format for storing final meaning.

IdeaMark Core preserves access structures that allow meaning to be regenerated, reviewed, compared, or reused in future contexts.

Entities, Occurrences, Sections, Sources, and metadata provide reconstruction support.

They do not guarantee a final interpretation.

## 17.3 Projection Internals Are Not Core

Part 4 may record Projection references and limited inline Projection notes.

Part 4 does not define:

- Projection content model;
- Projection evaluation;
- Projection compatibility rules;
- Projection lifecycle;
- Projection Library governance;
- Projection authoring workflows.

Those belong primarily to Part 5 or companion specifications.

## 17.4 Authoring Engine Internals Are Not Core

Part 4 defines the document representation that authoring engines may emit, validate, exchange, normalize, or migrate.

Part 4 does not define how those documents are produced.

It does not define:

- chunk scheduling;
- OCR or preprocessing pipelines;
- internal intermediate representation;
- prompt orchestration;
- LLM call planning;
- review queues;
- approval workflows;
- session state;
- cache state;
- progressive reinterpretation;
- engine-specific recovery behavior.

## 17.5 Retrieval and Ranking Are Not Core

Part 4 does not define retrieval algorithms, ranking models, embedding strategies, search indexes, vector databases, graph traversal, or recommendation behavior.

Core documents may support retrieval by making access structure explicit.

The retrieval system itself is outside Core.

## 17.6 Storage Engines Are Not Core

Part 4 does not define database schema, storage engines, indexing architecture, sharding, caching, object storage, or repository layout.

Implementations may store IdeaMark Core documents in files, databases, object stores, repositories, or derived indexes.

They remain conforming if they can emit and validate the Core document representation.

## 17.7 UI and Workflow Are Not Core

Part 4 does not define visual layout, editor behavior, review screens, user permissions, workflow stages, or collaboration UX.

Profiles or applications may define those behaviors.

Core validation does not require them.

## 17.8 Domain Vocabularies Are Not Core

Part 4 does not define universal domain vocabularies.

It provides recommended starting vocabularies for statuses, source types, anchor types, roles, and Entity kinds.

Profiles, Projections, and domains may define more precise vocabularies.

Core mode generally warns rather than fails on unknown vocabulary values unless a required structural rule is violated.

## 17.9 Intellectual Quality Is Not Core Validation

Part 4 validation does not judge:

- truth;
- usefulness;
- completeness;
- quality of extraction;
- quality of Projection;
- adequacy of Entity granularity;
- correctness of interpretation;
- domain validity;
- citation sufficiency beyond structural source references.

Those evaluations belong to review processes, profiles, Projection evaluation, domain tools, or human judgment.

## 17.10 Security and Access Control Are Not Core

Part 4 may preserve access-related metadata as source metadata or extension data.

Part 4 does not define authentication, authorization, encryption, redaction, audit policy, or permission enforcement.

Systems handling sensitive documents must implement those concerns outside the Core document format.

## 17.11 Non-goal Summary

IdeaMark Core v1.2.0 Part 4 is a document serialization specification.

It defines the interoperable access-structure representation.

It intentionally does not define the full intellectual, operational, runtime, storage, retrieval, security, or user-interface environment around that representation.
