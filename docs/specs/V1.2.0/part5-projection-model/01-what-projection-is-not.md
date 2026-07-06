# 01 — What Projection Is Not

**Part:** 5 — Projection Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 1.1 Purpose

This section defines the boundary of Projection by clarifying what Projection is not.

Projection is central to IdeaMark Core, but it should not absorb every adjacent concept.

If Projection is too narrow, it collapses into a prompt.

If Projection is too broad, it becomes Situation, ontology, workflow, governance, or worldview.

Part 5 should keep Projection in the middle:

```text
Projection = constraint-like reusable knowledge-reuse strategy
```

## 1.2 Projection Is Not Final Meaning

Projection does not store final meaning.

It shapes how source material may later participate in meaning activation.

Meaning becomes observable through expression, interpretation, Situation, and activity.

Projection helps prepare conditions for that activity, but it does not complete interpretation by itself.

A Projection may guide what should be preserved, ignored, emphasized, or reconstructed.

It should not claim to contain the final meaning of an Original Source.

## 1.3 Projection Is Not Situation

Projection is derived from Situation or Situation Vector, but it is not the whole Situation.

Situation is open-ended and effectively unbounded.

Projection is finite enough to guide Decomposition and reconstruction.

```text
Situation / Situation Vector
  -> interpreted by human, LLM, tool, or mixed process
  -> Projection
```

This derivation is not a simple mapping.

Projection creation may involve judgment, abstraction, omission, emphasis, and strategy.

Projection should therefore not attempt to encode the full Situation.

## 1.4 Projection Is Not a Prompt Only

A prompt may express a Projection for a particular AI interaction.

However, Projection is more durable than a prompt.

A Projection may be reused across:

- Decomposition;
- retrieval;
- matching;
- filtering;
- reconstruction;
- activation expression generation;
- library search;
- review and regeneration.

A prompt is often a single operational instruction.

A Projection is a reusable strategy that can be expressed through many prompts, documents, tools, or workflows.

## 1.5 Projection Is Not a Schema Only

A schema defines structural validity.

A Projection defines reuse strategy.

A Projection may influence which fields, roles, kinds, or structures are useful, but it is not merely a validation schema.

For example, a Projection may say that a recipe should be decomposed by ingredient function and substitution constraints.

A schema may later define how such results are serialized.

The Projection shapes the intellectual decomposition.

The schema validates representation.

## 1.6 Projection Is Not a Workflow Only

A workflow defines process steps.

A Projection defines constraints and strategy for source interpretation and reuse.

A workflow may use a Projection.

A Projection may include workflow hints.

But Projection should not be reduced to a sequence of operational steps.

Different workflows may implement the same Projection.

The same Projection may be used by a human, LLM, batch process, POR-like pipeline, or interactive tool.

## 1.7 Projection Is Not an Ontology

An ontology defines concepts and relations in a domain.

Projection does not define a universal domain model.

A Projection may include or reference domain vocabulary.

It may guide Entity kinds or Occurrence roles.

However, it should not require IdeaMark Core to adopt a universal ontology.

Projection is about how to reuse knowledge under a purpose, not about permanently defining what the world contains.

## 1.8 Projection Is Not a Perspective Object

Projection may include viewpoint-like information such as purpose, audience, focus, or assumptions.

However, Projection is more operational than a passive perspective.

It actively shapes Decomposition, retrieval, matching, and reconstruction.

Perspective-like information may appear inside Projection Metadata or Projection Document content.

But Projection should not be reduced to a viewpoint label.

## 1.9 Projection Is Not Provenance

Provenance records how something was produced, sourced, reviewed, or modified.

Projection shapes what should be produced and how it may later be reused.

Projection Metadata may include provenance-like information, such as author, version, generator, or review status.

However, Projection itself is not provenance.

## 1.10 Projection Is Not Governance

Projection governance may decide whether a Projection is approved, deprecated, recommended, public, internal, or institutionally endorsed.

Projection itself is the reusable strategy.

Governance is a management layer around Projections.

Part 5 should support governance metadata and library practices without defining one universal governance process.

## 1.11 Projection Is Not a Universal Role Vocabulary

Projection may define role vocabulary for Occurrences.

However, Part 5 should not impose one universal role vocabulary for all IdeaMark documents.

Role vocabularies should be Projection-defined, profile-defined, domain-defined, or library-defined.

Core should allow many role vocabularies to coexist.

## 1.12 Projection Is Not a Universal Entity Kind Taxonomy

Projection may guide Entity kinds.

However, Projection Model should not define one universal Entity kind taxonomy.

Entity kinds depend on domain, Projection, activity, and library practice.

A performance-engineering Projection, recipe-substitution Projection, and migration-impact Projection may need very different Entity kinds.

## 1.13 Projection Is Not a Retrieval Algorithm

Projection can function as a retrieval key.

However, it is not itself a retrieval algorithm.

A Projection may guide search, filtering, matching, and ranking.

Implementations may use different algorithms to apply it.

Part 5 should not prescribe retrieval algorithms.

## 1.14 Projection Is Not a Compatibility Algorithm

Projection compatibility matters.

However, Projection itself is not a compatibility scoring algorithm.

Part 5 may define conceptual compatibility types such as exact, partial, functional, source-pointer, or incompatible.

Implementations may define scoring or matching methods.

Core should not force one universal algorithm.

## 1.15 Projection Is Not a Document Template Only

A template shapes document output.

A Projection shapes decomposition and reconstruction strategy.

A Projection may include template-like guidance.

However, it should not be reduced to output formatting.

Two Projections might produce the same surface template while preserving very different reusable materials.

## 1.16 Projection Is Not a User Persona Only

Audience or user persona may be part of Projection.

But a Projection is not merely a persona.

It must shape source selection, decomposition, roles, entities, reconstruction, or reuse.

A persona without reuse strategy is insufficient as a Projection.

## 1.17 Projection Is Not a Tag Set Only

Projection Metadata may include tags.

Tags help search and indexing.

However, a tag set is not enough to define a Projection.

A Projection must constrain how source material should be reused.

Tags may help find a Projection, but they do not replace its strategy.

## 1.18 Projection Is Not Required to Be Universal

A Projection may be narrow.

It may be designed for:

- one person;
- one organization;
- one domain;
- one source type;
- one recurring task;
- one experimental workflow.

Reusability does not mean universal applicability.

Part 5 should allow narrow but useful Projections.

## 1.19 Projection Is Not Required to Be Human-authored

A Projection may be created by:

- a human;
- an LLM;
- a tool;
- an organization;
- a community;
- a mixed human-AI process.

Part 5 should not require human-only authorship.

However, metadata should make authorship, generation, review, or status traceable when relevant.

## 1.20 Summary

Projection should not be reduced to any adjacent object.

It is not final meaning, Situation, prompt, schema, workflow, ontology, perspective, provenance, governance, role vocabulary, Entity taxonomy, retrieval algorithm, compatibility algorithm, template, persona, or tag set.

It may interact with all of these.

The correct Core target remains:

```text
Projection
  = constraint-like reusable knowledge-reuse strategy
  = transformation key for decomposition, retrieval, matching, and reconstruction
```
