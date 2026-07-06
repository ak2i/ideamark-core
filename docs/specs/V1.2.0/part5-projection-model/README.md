# Part 5 — Projection Model

**Version:** IdeaMark Core v1.2.0  
**Status:** Specification Drafting

Part 5 defines Projection as a constraint-like reusable strategy for IdeaMark Core.

Part 5 should be drafted before Part 4 because the concrete YAML representation of IdeaMark documents depends on how Projection is defined, referenced, indexed, versioned, and reused.

## Why Part 5 Precedes Part 4

Part 3 defines the Core Model:

```text
Section
  = Projection-shaped local source window

Occurrence
  = role-bearing placement of reusable material within that window

Entity
  = reusable material shaped by Projection and available for later reconstruction
```

This makes Projection central to the entire model.

Part 4 will eventually define concrete YAML syntax.

However, Part 4 cannot safely finalize fields such as `meta.projections`, role vocabularies, Entity kinds, coverage notes, indexing metadata, or compatibility hints until Part 5 clarifies what Projection means and what metadata is needed to find and use Projections.

Therefore, the practical drafting order is:

```text
Part 1 — Meaning and philosophy
Part 2 — Human-AI Intellectual Activity architecture
Part 3 — Core Model
Part 5 — Projection Model
Part 4 — YAML Representation and Validation
```

## Part 5 Scope

Part 5 should define:

- what a Projection is;
- how Projection differs from prompt, perspective, schema, workflow, ontology, and governance;
- how Projection is derived from Situation or Situation Vector by humans, LLMs, tools, or mixed processes;
- what Projection metadata is needed for search, selection, reuse, and interoperability;
- how Projection Documents may preserve the body of a reusable Projection;
- how Projection Metadata may index Projection Documents;
- how Projection shapes Decomposition;
- how Projection shapes Sections, Occurrences, and Entities;
- how generation Projection and reconstruction Projection relate;
- how Projection compatibility should be understood conceptually;
- how Projection versions, libraries, and reuse should be handled;
- what belongs to Projection governance versus Core specification.

## Part 5 Non-goals

Part 5 should not define:

- concrete YAML syntax for IdeaMark documents;
- final Part 4 validation rules;
- storage architecture;
- retrieval algorithms;
- social approval processes for all Projection libraries;
- universal domain vocabularies;
- universal role vocabularies;
- universal Entity kind taxonomies;
- a complete theory of all human interpretation;
- a deterministic mapping from Situation Vector to Projection.

Part 5 may define conceptual requirements that Part 4 later serializes.

## Working Definition

A Projection is a constraint-like reusable knowledge-reuse strategy that shapes how Original Source material is decomposed, searched, matched, and reconstructed for future Human-AI Intellectual Activity.

A Projection may be created from Situation or Situation Vector, but it is not a simple deterministic mapping from Situation.

Projection creation may be performed by humans, LLMs, tools, organizations, communities, or mixed processes.

Projection is not merely a prompt.

It is also not final meaning.

A Projection may include purpose, focus, audience, assumptions, non-goals, granularity guidance, role vocabulary, Entity kind guidance, source-selection rules, coverage expectations, and reconstruction intent.

## Projection as Constraint and Transformation Key

Projection should be understood as a reusable constraint set and transformation key.

It can function as:

```text
Decomposition Key
  -> what to preserve, ignore, split, group, or emphasize from Original Source material

Retrieval Key
  -> what generated documents, Sections, Occurrences, or Entities are relevant later

Matching and Filtering Key
  -> how to judge whether existing IdeaMark structures are usable for a new activity

Reconstruction Key
  -> how to generate activation expressions from sources and structures
```

This makes Projection broader than a generation prompt and more operational than an abstract perspective.

## Projection Metadata and Projection Document

Part 5 should distinguish Projection itself from the metadata used to find and use it.

A Projection Document may preserve the body of a reusable Projection.

Projection Metadata may index that Projection so humans, AI systems, tools, and libraries can find, compare, select, and reference it.

IdeaMark documents may usually reference Projection Metadata or a Projection Document by ID.

Inline Projection material should also be allowed for experiments, local use, or self-contained documents.

The important Core question is not only:

```text
What is inside a Projection?
```

It is also:

```text
What metadata is needed so the right Projection can be found and reused?
```

## Draft Sections

0. [Projection Philosophy](./00-projection-philosophy.md) *(planned)*
1. [What Projection Is Not](./01-what-projection-is-not.md) *(planned)*
2. [Projection Definition](./02-projection-definition.md) *(planned)*
3. [Projection Metadata](./03-projection-metadata.md) *(planned)*
4. [Projection Document](./04-projection-document.md) *(planned)*
5. [Projection as Constraint and Transformation Key](./05-projection-as-constraint-and-transformation-key.md) *(planned)*
6. [Projection and Core Object Shaping](./06-projection-and-core-object-shaping.md) *(planned)*
7. [Generation and Reconstruction Projections](./07-generation-and-reconstruction-projections.md) *(planned)*
8. [Projection Compatibility](./08-projection-compatibility.md) *(planned)*
9. [Projection Library](./09-projection-library.md) *(planned)*
10. [Projection Lifecycle, Status, and Versioning](./10-projection-lifecycle-status-and-versioning.md) *(planned)*
11. [Projection Governance Boundary](./11-projection-governance-boundary.md) *(planned)*
12. [Projection Model Invariants](./12-projection-model-invariants.md) *(planned)*
13. [Projection Model Summary](./13-projection-model-summary.md) *(planned)*

## Immediate Drafting Questions

Part 5 should begin by answering:

1. What kind of constraint is a Projection?
2. What distinguishes Projection from Situation, prompt, ontology, workflow, schema, and governance?
3. What metadata is needed to find and choose an existing Projection?
4. What belongs in Projection Metadata versus Projection Document?
5. Which Projection content belongs in Core versus profiles?
6. How much role vocabulary should a Projection define?
7. How should Projection compatibility be described without forcing an algorithm?
8. How should Projection Library be described without turning Part 5 into governance policy?
9. How should Part 5 prepare Part 4 to represent Projection references and inline Projection material?

## Relationship to Part 3

Part 3 treats Projection Context as an input to Decomposition and metadata for reconstruction.

Part 5 defines Projection, Projection Metadata, Projection Documents, and Projection Libraries conceptually.

Part 3 should not be retrofitted to contain Projection internals.

Part 4 should wait until Part 5 clarifies the Projection model.
