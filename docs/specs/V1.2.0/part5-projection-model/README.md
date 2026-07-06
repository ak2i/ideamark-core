# Part 5 — Projection Model

**Version:** IdeaMark Core v1.2.0  
**Status:** Planning Draft

Part 5 defines Projection as a reusable strategy object for IdeaMark Core.

Part 5 should be drafted before Part 4 because the concrete YAML representation of IdeaMark documents depends on how Projection is defined, referenced, versioned, and reused.

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

However, Part 4 cannot safely finalize fields such as `meta.projections`, role vocabularies, Entity kinds, coverage notes, or compatibility hints until Part 5 clarifies what Projection means.

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
- how Projection differs from prompt, perspective, schema, workflow, and ontology;
- what minimum information a Projection should preserve;
- how a Projection shapes Decomposition;
- how a Projection shapes Sections, Occurrences, and Entities;
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
- a complete theory of all human interpretation.

Part 5 may define conceptual requirements that Part 4 later serializes.

## Working Definition

A Projection is a reusable knowledge-reuse strategy that shapes how Original Source material is decomposed, searched, matched, and reconstructed for future Human-AI Intellectual Activity.

It is not merely a prompt.

It is also not final meaning.

A Projection may include purpose, focus, audience, assumptions, non-goals, granularity guidance, role vocabulary, Entity kind guidance, source-selection rules, coverage expectations, and reconstruction intent.

## Projection as Transformation Key

Projection should be understood as a reusable transformation key.

It can function as:

```text
Decomposition Key
  -> what to extract or preserve from Original Source material

Retrieval Key
  -> what generated documents or structures are relevant later

Matching and Filtering Key
  -> how to judge whether existing IdeaMark structures are useful

Reconstruction Key
  -> how to generate activation expressions from sources and structures
```

This makes Projection broader than a generation prompt.

## Draft Sections

0. [Projection Model Overview](./00-projection-model-overview.md) *(planned)*
1. [Projection Boundary and Non-goals](./01-projection-boundary-and-non-goals.md) *(planned)*
2. [Projection Definition](./02-projection-definition.md) *(planned)*
3. [Projection Content Model](./03-projection-content-model.md) *(planned)*
4. [Projection and Decomposition](./04-projection-and-decomposition.md) *(planned)*
5. [Projection and Core Object Shaping](./05-projection-and-core-object-shaping.md) *(planned)*
6. [Generation and Reconstruction Projections](./06-generation-and-reconstruction-projections.md) *(planned)*
7. [Projection Compatibility](./07-projection-compatibility.md) *(planned)*
8. [Projection Libraries](./08-projection-libraries.md) *(planned)*
9. [Projection Status and Versioning](./09-projection-status-versioning.md) *(planned)*
10. [Projection Governance Boundary](./10-projection-governance-boundary.md) *(planned)*
11. [Projection Model Invariants](./11-projection-model-invariants.md) *(planned)*
12. [Projection Model Summary](./12-projection-model-summary.md) *(planned)*

## Immediate Drafting Questions

Part 5 should begin by answering:

1. What minimum fields make a Projection reusable?
2. Which Projection content belongs in Core versus profiles?
3. How much role vocabulary should a Projection define?
4. How should Projection compatibility be described without forcing an algorithm?
5. How should Projection Library be described without turning Part 5 into governance policy?
6. How should Part 5 prepare Part 4 to represent Projection references and inline Projection material?

## Relationship to Part 3

Part 3 treats Projection Context as an input to Decomposition and metadata for reconstruction.

Part 5 defines Projection itself.

Part 3 should not be retrofitted to contain Projection internals.

Part 4 should wait until Part 5 clarifies the Projection model.
