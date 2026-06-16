# IdeaMark Core

**IdeaMark Core** is a framework for making traces of intellectual activity reusable across contexts.

It is designed for situations where useful knowledge exists in conversations, reports, observations, plans, essays, analyses, or structured documents, but cannot be easily reused because its meaning depends on context, perspective, and later interpretation.

IdeaMark does not try to store meaning itself.

Instead, it preserves reusable structures that help future readers, tools, or AI systems generate meaning again.

> Meaning is not stored in text itself.  
> Meaning emerges through structured interpretation.

## Why IdeaMark?

Many knowledge-management approaches assume that knowledge can be captured as stable content.

In practice, the same text, claim, observation, or plan may mean different things depending on:

- who reads it
- why it is being reused
- which perspective is applied
- which surrounding context is active
- which downstream task is being performed

IdeaMark addresses this by separating representation from reusable meaning structure.

Rather than forcing all knowledge into one universal representation format, IdeaMark provides a core structure for organizing reusable traces of meaning-making.

## What IdeaMark Core Provides

IdeaMark Core defines a small set of structural concepts:

| Concept | Purpose |
|---|---|
| **Entity** | Defines the boundary of a reusable trace of meaning-making |
| **Occurrence** | Records how an Entity was used in a specific intellectual activity |
| **Section** | Groups Occurrences into a local interpretation boundary |
| **Perspective** | Records reusable clues about interpretive direction |
| **Relations** | Connect IdeaMark units into a graph structure |
| **Constraints** | Validate structural integrity without validating meaning |

These concepts allow prior intellectual activity to be retrieved, reinterpreted, recomposed, and projected into new contexts.

## What IdeaMark Is Not

IdeaMark Core is **not**:

- a command-line tool
- a GUI application
- a server framework
- a database
- a validator implementation
- a universal knowledge-representation format
- a replacement for domain-specific formats such as OKF, TPCG, JSON, YAML, or Markdown

This repository provides specifications, philosophy, examples, and official templates only.

Executable tools and application-specific processors should live in separate repositories.

## Core Idea

IdeaMark is based on a simple but important shift:

```text
Reality → Projection → Log → IdeaMark Structure → Projection → New Meaning
```

A document is treated as a log of prior meaning-making activity, not as knowledge itself.

IdeaMark extracts and organizes reusable structural traces from that log. Later, another reader, tool, or AI system can use those traces to perform a new projection and generate new meaning in a different context.

## Payload-Agnostic by Design

IdeaMark Core is payload-agnostic.

An Entity may point to or contain many kinds of payloads, including:

- plain text
- Markdown
- YAML
- JSON
- OKF
- TPCG
- external documents
- future formats

IdeaMark Core does not define the semantics of those payloads.

It defines the structure around them: boundaries, activations, interpretation contexts, perspectives, and relations.

## Repository Contents

This repository is intended to contain:

- Core specifications
- Design philosophy
- Core model definitions
- Structural constraints
- Official examples
- Official template library
- Application and usage notes

The current active specification is **IdeaMark Core v1.1.1**.

## Start Here

Read the v1.1.1 documents in this order:

1. [`ideamark-core-philosophy-v1.1.1.md`](docs/specs/V1.1.1/ideamark-core-philosophy-v1.1.1.md)  
   Explains the design hypothesis: meaning is emergent, not stored.

2. [`ideamark-core-model-v1.1.1.md`](docs/specs/V1.1.1/ideamark-core-model-v1.1.1.md)  
   Defines Entity, Occurrence, Section, Perspective, and Relations.

3. [`ideamark-core-constraints-v1.1.1.md`](docs/specs/V1.1.1/ideamark-core-constraints-v1.1.1.md)  
   Defines structural validation boundaries and required constraints.

4. [`ideamark-core-spec-v1.1.1.md`](docs/specs/V1.1.1/ideamark-core-spec-v1.1.1.md)  
   Provides the integrated Core Specification.

## Minimal Example

```yaml
entities:
  E1:
    kind: claim
    payload:
      body: "Meaning is not stored directly in text."
    atomicity_basis: interpretive

occurrences:
  O1:
    entity: E1
    role: claim

sections:
  S1:
    title: "Core hypothesis"
    occurrences: [O1]
```

This example does not attempt to encode the full meaning of the claim.

It identifies a reusable Entity, records its Occurrence as a claim, and places it inside a Section that provides an interpretation boundary.

## Validation Philosophy

IdeaMark Core validates structure, not meaning.

Core validation checks things such as:

- required structures exist
- references are valid
- identifiers are unique
- occurrences define `entity` and `role`
- sections contain non-empty `occurrences`
- entities define a usable `payload`

Core validation does not check:

- whether a claim is true
- whether a payload is semantically correct
- whether an external URI is reachable
- whether a selector is meaningful for a payload profile
- whether future readers will derive the same meaning

This is intentional. IdeaMark constrains interpretation enough to support reuse, while preserving flexibility for future projection.

## Design Status

IdeaMark Core v1.1.1 is an active design-stage specification.

The v1.1.x series emphasizes:

- representation independence
- payload-agnostic structure
- controlled divergence of interpretation
- reusable traces of intellectual activity
- separation of meaning boundary, contextual activation, and interpretive direction

Formal migration rules are outside the current Core specification and are considered tooling concerns.

## License

See the repository license file for licensing terms.
