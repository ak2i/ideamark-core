# 00 — Projection Philosophy

**Part:** 5 — Projection Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 0.1 Purpose

This section defines the philosophical role of Projection in IdeaMark Core.

Projection is the constraint-like strategy that makes IdeaMark possible.

It connects the open-ended nature of Situation and Human-AI Intellectual Activity to the finite structures that IdeaMark documents can preserve.

Part 5 should not treat Projection as merely a prompt, field set, schema, or document template.

Projection is the reusable strategy that shapes how Original Source material is decomposed, searched, matched, and reconstructed.

## 0.2 Why Projection Is Needed

Situation is effectively unbounded.

A Situation may include human purpose, organizational context, emotional state, domain knowledge, task constraints, available tools, source accessibility, cultural assumptions, risk, timing, and future use.

IdeaMark cannot directly preserve or process the whole Situation.

Therefore, a Projection is needed.

A Projection is a finite constraint-like expression derived from Situation or Situation Vector that makes Decomposition and reconstruction tractable.

```text
Situation / Situation Vector
        ↓
Human, LLM, tool, or mixed interpretation
        ↓
Projection
        ↓
Projection-guided Decomposition and reconstruction
```

This derivation is not a simple deterministic mapping.

It is an intellectual act.

Humans, LLMs, tools, organizations, or communities may create Projections.

## 0.3 Projection as Constraint

Projection should be understood as a constraint set rather than merely a data object.

It constrains:

- what source material is relevant;
- what may be ignored;
- how material should be decomposed;
- how Sections should be shaped;
- what Occurrence roles matter;
- what Entity material should preserve;
- what granularity is useful;
- what future reconstruction should support;
- what activation expressions may become useful.

These constraints do not store meaning.

They shape the conditions under which meaning may later be activated.

## 0.4 Projection as Reusable Strategy

A Projection is reusable.

A Projection may be used across:

- multiple Original Sources;
- multiple IdeaMark documents;
- multiple Decomposition runs;
- multiple users;
- multiple organizations;
- multiple future reconstruction activities.

A Projection may be personal, local, organizational, public, experimental, domain-specific, or library-managed.

Reusability does not require universality.

A narrow Projection may be highly reusable inside a particular domain or activity.

## 0.5 Projection as Transformation Key

Projection functions as a transformation key across several phases.

```text
Decomposition Key
  -> shapes what is preserved, ignored, split, grouped, or emphasized

Retrieval Key
  -> helps find relevant IdeaMark documents and structures

Matching and Filtering Key
  -> helps judge whether existing structures are usable

Reconstruction Key
  -> helps generate activation expressions from sources and structures
```

This makes Projection broader than a generation prompt.

A prompt may be one expression of a Projection for a particular LLM run.

The Projection itself is more durable and reusable.

## 0.6 Projection and Meaning

Projection does not store final meaning.

Meaning becomes observable when expression, interpretation, Situation, and activity produce intellectual, practical, or observational consequence.

Projection shapes the path toward that activation.

It helps determine what source material and access structures should be preserved so later meaning activation becomes possible or cheaper.

Projection is therefore a catalyst, not a meaning container.

## 0.7 Projection and Original Source

Original Source material is not decomposed in isolation.

Projection determines how source material becomes useful.

The same Original Source may produce different IdeaMark documents under different Projections.

For example:

- a code file may be decomposed for performance engineering, API design, or teaching;
- an RFC may be decomposed for rationale, migration impact, or evidence review;
- a recipe may be decomposed for cooking execution, substitution, dietary constraints, or shopping preparation.

Projection does not change the Original Source.

It changes what is preserved from it and how later access is structured.

## 0.8 Projection and Part 3 Core Objects

Part 3 defines:

```text
Section
  = Projection-shaped local source window

Occurrence
  = role-bearing placement of reusable material within that window

Entity
  = reusable material shaped by Projection and available for later reconstruction
```

This means Projection shapes all three central Core objects.

Projection shapes Section boundaries, Occurrence roles, Entity kinds, Entity payload boundaries, source anchors, coverage, non-goals, and reconstruction expectations.

Part 5 explains the Projection side of that relationship.

## 0.9 Projection Metadata

Because Projections are reusable, they must be findable.

Part 5 should therefore distinguish:

```text
Projection
  = constraint-like reusable strategy

Projection Document
  = artifact that preserves the body of a Projection

Projection Metadata
  = index information used to find, compare, select, reference, and reuse Projections
```

The Core does not need to standardize every possible detail of Projection content.

It does need enough metadata conventions to allow humans, AI systems, and tools to find appropriate Projections.

## 0.10 Projection Library

A Projection Library is a reuse infrastructure for Projections.

It may collect, version, describe, classify, compare, deprecate, or recommend Projections.

A Projection Library may be personal, organizational, domain-specific, public, or implementation-specific.

Part 5 should describe Projection Libraries without turning them into universal governance systems.

## 0.11 Projection and Capability

A major purpose of Projection is to improve capability.

When useful Projections are preserved, indexed, shared, and reused, future humans and AI systems can perform knowledge work with lower interpretation cost.

This is not because meaning is stored.

It is because reusable constraints and source access structures make reconstruction easier.

Projection is therefore a way to accumulate reusable intellectual strategy.

## 0.12 Summary

Projection is the bridge between unbounded Situation and finite reusable IdeaMark structures.

It is best understood as:

```text
Projection
  = constraint-like reusable knowledge-reuse strategy
  = transformation key for decomposition, retrieval, matching, and reconstruction
```

Part 5 defines Projection, Projection Metadata, Projection Documents, and Projection Libraries so Part 4 can later represent them without reducing Projection to a prompt or freezing it into a universal ontology.
