# IdeaMark Core

**IdeaMark is a framework for reusing how people think, not just what they wrote.**

IdeaMark Core provides the structural foundation for making intellectual activity reusable across contexts.

It is built around one central idea:

> Do not try to store meaning itself.  
> Preserve the access structures that allow meaning to be generated again.

IdeaMark is for conversations, reports, observations, plans, essays, analyses, design records, structured documents, source-code discussions, and other artifacts where useful knowledge exists, but cannot be reused reliably because its meaning depends on context, perspective, source material, and later interpretation.

The current active specification is **IdeaMark Core v1.2.0**.

## The Problem

Most knowledge-management systems treat knowledge as if it were stable content.

They usually try to capture, classify, summarize, embed, or retrieve pieces of information.

That works for many tasks, but it breaks down when the important part is not the text itself, but the intellectual activity behind it:

- why a claim mattered
- how an observation was used
- what source material supported it
- what Projection made it relevant
- which context made a statement meaningful
- how one discussion can be reprojected into another domain
- how prior thinking can be reconstructed into a new plan, policy, design, explanation, or argument

In these cases, simply storing text is not enough.

The same statement can function as evidence, a hypothesis, a constraint, a risk, an implementation rationale, or a design principle depending on how it is activated in a later context.

## The IdeaMark Approach

IdeaMark treats documents as **reusable access structures for meaning-making activity**, not as containers of fixed meaning.

Its basic model is:

```text
Original Source material
        x
Projection
        x
runtime context when applicable
        ↓
Projection-guided Decomposition
        ↓
IdeaMark Document
        ↓
retrieval / matching / reconstruction
        ↓
future activation expression
```

An Original Source may be a document, conversation, dataset, source-code file, image, audio, video, log, generated artifact, composite source, or future media type. IdeaMark does not replace that source.

Instead, an IdeaMark document records how source material was decomposed under a Projection so that a future human, AI system, or tool can return to the right source material and reconstruct a useful expression for a new Situation.

In other words, IdeaMark is not primarily about preserving knowledge as finished content.

It is about making prior meaning-making reusable.

## What Makes IdeaMark Different

IdeaMark separates concerns that are often mixed together:

| Concern | IdeaMark Core v1.2.0 Treatment |
|---|---|
| Original Source | Treated as authoritative material for a given Projection, not copied into Core as final meaning. |
| Meaning | Not stored directly; meaning is activated later through interpretation and use. |
| Projection | External but interoperable reuse strategy that guides Decomposition, retrieval, matching, filtering, and reconstruction. |
| Decomposition | Projection-guided structuring act that produces an IdeaMark document from Original Source material. |
| Entity | Reusable intellectual structure identified under a Projection. |
| Occurrence | How an Entity functions in a Section or local intellectual context. |
| Section | Local access boundary that gathers Occurrences and anchors them to source material. |
| Source anchors | Traceability links from IdeaMark structures back to Original Sources. |
| Core validation | Structural conformance without semantic enforcement. |
| Runtime / workflow | Allowed as traceability metadata when useful, but not required as Core state. |

This separation allows IdeaMark to support:

- Projection-dependent retrieval
- cross-domain reuse
- reconstruction of prior thinking
- structured synthesis from conversations or reports
- reusable access to heterogeneous Original Sources
- comparison of different decompositions of the same source
- AI-assisted interpretation without forcing a single knowledge schema
- reduction of interpretation cost across repeated intellectual work

## What IdeaMark Core Provides

IdeaMark Core v1.2.0 defines the minimum interoperable structure for reusable intellectual access structures.

The required Core namespaces are:

### `meta`

Document-level metadata, including specification version, document identity, status, title, and Projection references or inline Projection notes.

### `sources`

References to Original Sources used for Decomposition and later reconstruction.

Sources are not treated as subordinate copies. They remain the authority that IdeaMark structures point back to.

### `sections`

Local access boundaries that gather Occurrences and may contain source anchors.

A Section helps future readers, tools, or AI systems know which pieces should be read together for a particular reconstruction task.

### `occurrences`

Records of how Entities function in specific local contexts.

The same Entity may appear as evidence, rationale, constraint, risk, premise, design choice, implementation note, or another role depending on the Section and Projection.

### `entities`

Reusable intellectual structures identified through Projection-guided Decomposition.

Entities do not own final meaning. They preserve reusable boundaries and content traces that can support later activation.

## Projection

Projection is a central concept in IdeaMark Core v1.2.0.

A Projection is not merely a prompt parameter. It is a reusable intellectual asset that can guide:

1. **Decomposition** — how Original Source material is structured into IdeaMark Core objects.
2. **Retrieval** — how relevant IdeaMark documents or Original Sources are found.
3. **Matching and filtering** — how full, partial, approximate, compatible, or incompatible reuse is judged.
4. **Reconstruction** — how retrieved material is transformed into a future activation expression.

Projection remains outside the strict Core document model, but Core documents must be able to record which Projection or Projection context guided their generation.

This boundary is intentional. Core remains interoperable, while Projection specifications, libraries, lifecycle rules, evaluation methods, and governance practices can evolve independently.

## Payload- and Source-Agnostic by Design

IdeaMark Core is source- and payload-agnostic.

Original Sources may include:

- plain text
- Markdown
- YAML
- JSON
- OKF
- TPCG
- source code
- datasets
- logs
- external documents
- images, audio, video, or other media
- future formats

IdeaMark Core does not define the full semantics of those sources or payloads.

Payload-specific meaning, correctness, URI reachability, selector semantics, media interpretation, and profile validation belong to external tools, Projection profiles, domain-specific specifications, or companion systems.

IdeaMark defines the reusable access structure around sources: document metadata, source references, source anchors, Sections, Occurrences, Entities, and optional ordering or extension structures.

## What IdeaMark Core Is Not

IdeaMark Core is **not**:

- a command-line tool
- a GUI application
- a server framework
- a database
- a validator implementation
- a universal knowledge-representation format
- a replacement for domain-specific formats such as OKF, TPCG, JSON, YAML, Markdown, or source-code formats
- a Projection library governance system
- a retrieval ranking algorithm
- a Progressive Occurrence Resolution engine

This repository provides specifications, philosophy, examples, and official templates only.

Executable tools, application-specific processors, Projection libraries, retrieval systems, and authoring engines should live in separate repositories or companion projects.

## Repository Contents

This repository is intended to contain:

- Core specifications
- Design philosophy
- Core model definitions
- Structural constraints
- Normative and implementation-oriented examples
- Official template library
- Application and usage notes
- Migration and compatibility notes

## Start Here

Read the v1.2.0 specification library in this order:

1. [`docs/specs/V1.2.0/README.md`](docs/specs/V1.2.0/README.md)  
   Overview of the v1.2.0 specification library and drafting status.

2. [`Part 1 — Philosophy`](docs/specs/V1.2.0/part1-philosophy/README.md)  
   Explains why IdeaMark is an intellectual activity infrastructure rather than a knowledge representation format.

3. [`Part 2 — Architecture of Human-AI Co-evolution`](docs/specs/V1.2.0/part2-architecture/README.md)  
   Describes how humans, AI systems, Projections, IdeaMark documents, retrieval systems, and Original Sources may participate in continuous reconstruction and co-evolution.

4. [`Part 3 — Core Model`](docs/specs/V1.2.0/part3-core-model/README.md)  
   Defines the conceptual model: Projection-guided Decomposition, Original Source stance, Sections, Occurrences, Entities, and meaning activation.

5. [`Part 5 — Projection Specification`](docs/specs/V1.2.0/part5-projection-specification/README.md)  
   Defines Projection as a reusable strategy for Decomposition, retrieval, matching, filtering, and reconstruction.

6. [`Part 4 — Core Specification`](docs/specs/V1.2.0/part4-core-specification/README.md)  
   Defines the normative YAML representation, required fields, compatibility rules, validation constraints, and normalized samples.

7. [`Part 6 — Authoring Guide`](docs/specs/V1.2.0/part6-authoring-guide/README.md)  
   Provides practical guidance for human and AI authoring, review, correction, Projection refinement, and retrieval-oriented evaluation.

## Minimal Example

The following is a compact v1.2.0-style example. It uses the Part 4 array-based representation and the required Core namespaces.

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: minimal-meaning-making-example
  status: draft
  title: Minimal Meaning-Making Example
  projections:
    - role: generation
      inline:
        purpose: preserve a reusable design rationale from a short statement

sources:
  - id: SRC-001
    type: text
    title: Example statement
    inline: "Meaning is not stored directly in text."

sections:
  - id: SEC-core-hypothesis
    title: Core hypothesis
    anchors:
      - source: SRC-001
        type: inline_text
        precision: exact
        role: source_context
    occurrences:
      - OCC-meaning-not-stored

occurrences:
  - id: OCC-meaning-not-stored
    entity: ENT-meaning-not-stored
    role: frames_core_hypothesis
    rationale: The statement is used as a design rationale, not as a universal semantic claim.

entities:
  - id: ENT-meaning-not-stored
    kind: design_principle
    content: Meaning should not be treated as something stored directly in text; reusable structures should support later meaning activation.
```

This example does not attempt to encode the full meaning of the source statement.

It records a source, identifies a reusable Entity, records how that Entity functions as an Occurrence, and places it inside a Section that can be used for later reconstruction.

## Example Use Cases

IdeaMark may be useful for:

- converting research discussions into reusable structured traces
- turning reports or observations into recomposable planning material
- organizing policy, design, or business discussions across Projections
- comparing different decompositions of the same Original Source
- reusing prior conversations as inputs for new documents
- connecting domain-specific payloads such as OKF or TPCG without merging their schemas
- building AI workflows that separate source reading, Projection selection, Decomposition, retrieval, reconstruction, and final expression
- supporting Progressive Occurrence Resolution as a companion authoring method for large, streaming, composite, or difficult sources

## Validation Philosophy

IdeaMark Core validates structure, not final meaning.

Core validation checks things such as:

- required top-level namespaces exist
- required object fields exist
- object IDs are unique where required
- references are valid
- Section → Occurrence → Entity paths can be reconstructed
- source anchors are structurally processable
- serialization follows Core representation rules

Core validation does not check:

- whether a claim is true
- whether a Projection is socially valuable or strategically correct
- whether a payload is semantically correct
- whether an external URI is reachable
- whether a selector is meaningful for a payload profile
- whether a retrieval algorithm will rank results well
- whether future readers will derive the same meaning

This is intentional. IdeaMark constrains structure enough to support reuse, while preserving flexibility for future Projection and reconstruction.

## Design Status

IdeaMark Core v1.2.0 is an active draft specification.

The v1.2.0 series emphasizes:

- Original Source authority
- Projection-guided Decomposition
- reusable access structures
- Human-AI intellectual co-evolution
- interpretation cost reduction
- array-based Core representation
- structural conformance without semantic closure
- separation between Core, Projection, authoring engines, retrieval systems, and runtime workflows

Parts 1 through 6 now have initial drafts. The current focus is review, terminology alignment, Part 4 sample verification, migration planning, and implementation planning for IdeaMark CLI and related authoring tools.

## License

See the repository license file for licensing terms.
