# IdeaMark Core

**IdeaMark is a framework for reusing how people think, not just what they wrote.**

IdeaMark Core provides the structural foundation for making intellectual activity reusable across contexts.

It is built around one central idea:

> Do not try to store meaning itself.  
> Preserve the structure that allows meaning to be generated again.

IdeaMark is for conversations, reports, observations, plans, essays, analyses, structured documents, and other artifacts where useful knowledge exists, but cannot be reused reliably because its meaning depends on context, perspective, and later interpretation.

## The Problem

Most knowledge-management systems treat knowledge as if it were stable content.

They usually try to capture, classify, summarize, embed, or retrieve pieces of information.

That works for many tasks, but it breaks down when the important part is not the text itself, but the intellectual activity behind it:

- why a claim mattered
- how an observation was used
- what perspective made an idea relevant
- which context made a statement meaningful
- how one discussion can be reprojected into another domain
- how prior thinking can be recomposed into a new plan, policy, design, or argument

In these cases, simply storing text is not enough.

The same statement can function as evidence, a hypothesis, a constraint, a risk, or a design principle depending on how it is activated in a later context.

## The IdeaMark Approach

IdeaMark treats documents as **logs of meaning-making activity**, not as containers of fixed meaning.

Its basic model is:

```text
Reality → Projection → Log → IdeaMark Structure → Projection → New Meaning
```

A prior conversation, report, or analysis is treated as a trace of intellectual activity. IdeaMark extracts reusable structure from that trace so that a future reader, tool, or AI system can perform a new projection and generate meaning again.

In other words, IdeaMark is not primarily about preserving knowledge.

It is about making prior meaning-making reusable.

## What Makes IdeaMark Different

IdeaMark separates concerns that are often mixed together:

| Concern | IdeaMark Treatment |
|---|---|
| Representation | Stored externally as payload: Markdown, YAML, JSON, OKF, TPCG, text, etc. |
| Meaning | Not stored directly; emerges through interpretation |
| Entity | Boundary of a reusable trace of meaning-making |
| Occurrence | How an Entity functioned in a specific intellectual activity |
| Section | Local interpretation boundary for reading Occurrences together |
| Perspective | Reusable trace of projection / interpretive direction |
| Relations | Graph structure connecting reusable units |
| Constraints | Structural validation without semantic enforcement |

This separation allows IdeaMark to support:

- perspective-dependent retrieval
- cross-domain reuse
- recomposition of prior thinking
- structured synthesis from conversations or reports
- reuse of heterogeneous payload formats
- AI-assisted interpretation without forcing a single knowledge schema

## What IdeaMark Core Provides

IdeaMark Core defines the minimum common structure for reusable intellectual traces:

### Entity

An Entity defines the boundary of a reusable trace of meaning-making.

It does not own meaning itself. Its identity is independent from the payload it references or contains.

### Occurrence

An Occurrence records how an Entity was used in a specific intellectual activity.

The same Entity may appear as a claim, evidence, observation, assumption, objective, constraint, risk, or another role depending on context.

### Section

A Section groups Occurrences into a local interpretation boundary.

It defines how a set of Occurrences should be read together.

### Perspective

A Perspective records reusable clues about interpretive direction.

It is not meaning itself and does not guarantee that future readers will derive the same meaning.

### Relations

Relations connect IdeaMark units into a graph structure.

They support reuse, comparison, synthesis, decomposition, and recomposition.

### Constraints

Constraints validate structural integrity without validating meaning.

IdeaMark Core checks that the structure is processable while leaving interpretation open.

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

Payload-specific meaning, correctness, URI reachability, selector semantics, and profile validation belong to external tools or domain-specific profiles.

IdeaMark defines the reusable structure around payloads: boundaries, activations, interpretation contexts, perspectives, and relations.

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

## Example Use Cases

IdeaMark may be useful for:

- converting research discussions into reusable structured traces
- turning reports or observations into recomposable planning material
- organizing policy, design, or business discussions across perspectives
- reusing prior conversations as inputs for new documents
- connecting domain-specific payloads such as OKF or TPCG without merging their schemas
- building AI workflows that separate extraction, interpretation, and final expression

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
