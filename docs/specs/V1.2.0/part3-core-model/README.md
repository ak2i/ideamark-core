# Part 3 — Core Model

**Version:** IdeaMark Core v1.2.0  
**Status:** Initial Specification Draft Complete

Part 3 defines the conceptual model of IdeaMark Core.

Part 1 explains why IdeaMark exists.

Part 2 explains the reference architecture for Human-AI Intellectual Activity and reconstruction.

Part 3 explains what conceptual objects IdeaMark Core needs in order to function as reusable access structures without storing final meaning.

## Scope

Part 3 is conceptual.

It defines model roles, boundaries, constraints, and invariants before YAML representation is specified in Part 4.

Part 3 should not define:

- concrete YAML syntax;
- validation schema details;
- storage architecture;
- retrieval algorithms;
- Projection authoring workflows;
- Projection quality evaluation;
- Projection library governance;
- universal domain vocabularies;
- universal coordinate systems;
- universal authority rankings;
- a taxonomy of all intellectual activities.

Those belong to later parts, companion specifications, implementations, Projections, or domain practices.

## Core Modeling Stance

IdeaMark generation is not a general extraction task performed on an Original Source in isolation.

An IdeaMark document becomes useful when Original Source material is decomposed under a Projection for expected future retrieval, reconstruction, and meaning activation.

Projection-independent decomposition may be technically possible, but it is not the intended Core model.

Without Projection, an IdeaMark document risks becoming a detached catalog or dictionary-like artifact rather than a living access structure for Human-AI Intellectual Activity.

Part 3 therefore treats Decomposition as the conceptual bridge between Original Source, Projection, optional runtime context, and the generated structures of an IdeaMark document.

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
Sections / Occurrences / Entities
```

Part 3 does not evaluate whether a Projection is good, legitimate, widely shareable, or socially valuable.

Part 3 only defines how a Projection-guided Decomposition can produce Core Model structures that remain traceable and reusable.

Projection evaluation, Projection lifecycle, Projection library formation, and Projection governance belong primarily to Part 5.

## Meaning Activation Stance

IdeaMark does not store meaning.

Meaning is not treated as something contained in an Original Source, Projection, IdeaMark document, or generated explanation by itself.

Meaning becomes observable when expression, interpretation, Situation, and activity meet and produce some intellectual, practical, or observational consequence.

The purpose of IdeaMark is therefore not to retrieve knowledge as a finished object.

Its purpose is to preserve structures that help future humans and AI systems return to the right Original Source material and generate activation expressions under a Projection.

In this sense, an IdeaMark document is not merely an index of Original Sources.

It is a reusable structural snapshot that helps gather, order, and expose the materials from which an activation expression may be generated.

Such an expression may be text, diagram, image, interaction, explanation, question, warning, plan, sensory representation, or another medium appropriate to the future Situation.

Part 3 does not define how activation expressions are generated.

It only defines the Core Model structures that make such generation and reconstruction traceable, reusable, and less costly.

## Original Source Stance

An Original Source is not limited to a text document or fixed media object.

Anything may be treated as an Original Source if, when viewed through a Projection, it can participate as a component of Human-AI Intellectual Activity.

This may include documents, images, audio, video, source code, datasets, sensor logs, interaction histories, generated artifacts, streams, composites, or future media not yet supported by current tools.

However, practical use requires accessibility.

For an Original Source to be usable in current IdeaMark workflows, humans, AI systems, or supporting tools must be able to observe, reference, transform, or input it sufficiently for Decomposition and later reconstruction.

Something that cannot yet be observed by humans, supplied to AI systems, or converted into an accessible representation may be conceptually eligible as a future Original Source, but it is not practically usable in current IdeaMark authoring or reconstruction.

Part 3 therefore defines Original Source Reference in a media-independent way while preserving the practical requirement that source material must be accessible enough to support traceability and reconstruction.

## Decomposition Stance

Decomposition is the Projection-guided structuring act that produces an IdeaMark document from Original Source material.

Its role is to make later retrieval, reconstruction, and meaning activation possible by producing Core Model structures that are useful under an intended or anticipated Projection.

Decomposition may be performed by humans, AI systems, tools, or larger authoring processes such as Progressive Occurrence Resolution.

Part 3 does not prescribe the algorithm or workflow by which Decomposition is performed.

In particular, Decomposition is not assumed to be fully reconstructable from the generated IdeaMark document.

The generated IdeaMark document may preserve local rationale, generation notes, method notes, or explanatory traces that help later users understand why particular structures were produced.

However, such notes are partial explanations, not a complete inverse mapping of the Decomposition process.

For Part 3, the most important responsibility is that the Decomposition boundary remains clear:

```text
Input:  Original Source material x Projection x optional runtime context
Process: Projection-guided Decomposition
Output: IdeaMark Document
```

The output of Decomposition is the IdeaMark document as a whole.

Therefore, any Core Model structure in the document may be a Decomposition product, including Sections, Occurrences, Entities, document-level metadata, traceability information, status information, and other document-level structures.

Decomposition does not judge the universal truth of Original Sources or the quality, legitimacy, or social value of a Projection.

It only determines what structures are produced under the given Original Source, Projection, and any applicable runtime context so that later Human-AI Intellectual Activity can begin from a traceable access structure.

## Refined Core Object Interpretation

The Part 3 design experiments support retaining Section, Occurrence, and Entity as the central Core Model objects.

They must be defined functionally, not semantically.

```text
Section
  = Projection-shaped local source window

Occurrence
  = role-bearing placement of reusable material within that window

Entity
  = reusable material shaped by Projection and available for later reconstruction
```

This interpretation was tested across:

- algorithm implementation code;
- system correctness and state-machine code;
- formal RFC design prose;
- everyday recipe procedure.

Across these sources, the same pattern appeared:

```text
Original Source + Projection
  -> Projection-shaped Sections
  -> role-bearing Occurrences
  -> Projection-shaped reusable Entities
  -> lower-cost return to Original Source
  -> future activation expression
```

## Structural Catalyst Stance

The Core Model does not attempt to encode meaning.

Its purpose is to preserve enough reusable structure so that Projection-guided Human-AI Intellectual Activity can efficiently return to Original Sources and reconstruct useful activation expressions.

The three-layer structural pattern of Section, Occurrence, and Entity should therefore be understood primarily as a structural catalyst rather than as a fixed semantic taxonomy.

Their names are historical and descriptive.

A Section does not have to mean a document section, workflow step, chapter, topic, or decision unit.

In Core, a Section is a Projection-shaped local source window: a bounded local context created by Decomposition so later reconstruction can reopen a useful part of the Original Source.

An Occurrence does not have to mean a textual occurrence, event, instance, or observation.

In Core, an Occurrence is a role-bearing placement of Entity material within a Section. It explains how reusable material participates in that local source window under the generation Projection.

An Entity does not have to mean a concept, object, actor, term, or knowledge unit.

In Core, an Entity is Projection-shaped reusable material. It may be reused, referenced, placed, or reinterpreted, but it is not a universal meaning unit or global ontology object.

Those domain-specific interpretations belong to Projection, authoring practice, domain practice, or reconstruction activity.

Section, Occurrence, and Entity are useful because they can be separated from both Original Source and Projection while still functioning as keys that help future humans and AI systems reactivate meaning under a Projection.

## Metadata Stance

Perspective and Provenance are not treated as required Core Model objects in Part 3.

Their earlier responsibilities are folded into document-level metadata, source references, projection references, source anchors, local rationale, and generation notes.

The metadata area may record references to Projections, inline Projection definitions, Original Source references, generation notes, local rationale conventions, tool information, timestamps, review notes, or other information useful for traceability and reconstruction.

This keeps the Core Model focused on reusable structural catalysts rather than broad interpretive metadata categories.

For example, an IdeaMark document may record multiple Projections as metadata:

```yaml
meta:
  projections:
    - role: generation
      ref_id: projection://cooking-functional-substitution/v1
    - role: reconstruction_reference
      ref_id: projection://household-cooking/v1
    - role: inline_note
      inline_yaml: |
        purpose: explain professional cooking guidance for household use
        audience: non-specialist
```

A single IdeaMark document may be generated from multiple Projection x Original Source combinations.

Conversely, multiple IdeaMark documents generated from different Projection x Original Source combinations may later be retrieved, compared, or reconstructed together.

Part 3 only requires that the relevant Projection and source references can be recorded sufficiently for later reconstruction.

It does not require Perspective or Provenance to exist as separate namespaces.

## Traceability Stance

Traceability is more important than semantic completeness.

An IdeaMark document should preserve enough traceability to allow later humans, AI systems, or tools to return to relevant Original Source material.

Traceability should be modeled as a source anchor or traceability claim, not as a text-span-only mechanism.

A source anchor may refer to:

- line ranges;
- paragraphs;
- code spans;
- ingredient lines;
- recipe steps;
- media time ranges;
- image regions;
- dataset rows or columns;
- composite source fragments;
- approximate or tool-specific source positions.

Exact anchors are useful when available, but the Core Model must remain media-independent.

## Relation Stance

Relation is not a required Core Model object for v1.2.0 Part 3.

The experiments did not require a separate Relation namespace.

Ordering, Section grouping, Occurrence roles, Entity payloads, source anchors, and document-level metadata were sufficient to support reconstruction.

Relation-like structures may be added later as an optional extension, profile, or companion specification, but they should not be mandatory for the Core Model.

## IdeaMark Document Stance

An IdeaMark document is an operational access-structure artifact produced by Projection-guided Decomposition.

It is not the final result of intellectual activity.

It is an intermediate reusable structure that helps future intellectual activity begin more effectively.

An IdeaMark document may be used to retrieve Original Sources, understand which Projection shaped the decomposition, reconstruct relevant structures, and generate expressions that can activate meaning for humans or AI systems under a future Situation.

An IdeaMark document may also become an Original Source for later IdeaMark generation when it can participate as a component of future Human-AI Intellectual Activity.

This recursive possibility does not make IdeaMark a knowledge base.

It means that IdeaMark documents, like other artifacts, can become material for later Projection-guided reconstruction.

## Core Specification Sections

0. [Core Model Overview](./00-core-model-overview.md) *(drafted)*
1. [Model Boundary and Non-goals](./01-model-boundary-and-non-goals.md) *(drafted)*
2. [Original Source Reference Model](./02-original-source-reference-model.md) *(drafted)*
3. [Projection and Metadata Model](./03-projection-and-metadata-model.md) *(drafted)*
4. [Decomposition Model](./04-decomposition-model.md) *(drafted)*
5. [IdeaMark Document Model](./05-ideamark-document-model.md) *(drafted)*
6. [Section Model](./06-section-model.md) *(drafted)*
7. [Occurrence Model](./07-occurrence-model.md) *(drafted)*
8. [Entity Model](./08-entity-model.md) *(drafted)*
9. [Anchorage and Traceability Model](./09-anchorage-and-traceability-model.md) *(drafted)*
10. [Status, Versioning, and Regeneration Model](./10-status-versioning-and-regeneration-model.md) *(drafted)*
11. [Model Invariants](./11-model-invariants.md) *(drafted)*
12. [Core Model Summary](./12-core-model-summary.md) *(drafted)*

## Supporting Design Materials

The Part 3 directory separates specification text from design materials.

Drafting notes are maintained under [`drafting-notes/`](./drafting-notes/):

- [Part 3 Drafting Issues](./drafting-notes/00-drafting-issues.md)
- [IdeaMark Document Constraints](./drafting-notes/01-ideamark-document-constraints.md)
- [Part 3 Readiness Assessment](./drafting-notes/13-part3-readiness-assessment.md)

Design experiments are maintained under [`experiments/`](./experiments/):

- [Code Original Source Experiment](./experiments/02-code-original-source-experiment.md)
- [Heapq Performance Candidate IdeaMark Experiment](./experiments/03-heapq-performance-candidate.md)
- [Heapq Cross-Projection Reconstruction Test](./experiments/04-heapq-cross-projection-reconstruction.md)
- [Heapq JSON and MongoDB Search Simulation](./experiments/05-heapq-json-mongodb-search-simulation.md)
- [Heapq Multi-Projection Generation Test](./experiments/06-heapq-multi-projection-generation.md)
- [SQLite Pager Original Source Test](./experiments/07-sqlite-pager-original-source-test.md)
- [Rust RFC Original Source Test](./experiments/08-rust-rfc-original-source-test.md)
- [SQLite Pager Multi-Projection Candidate Test](./experiments/09-sqlite-pager-multi-projection-candidates.md)
- [Rust RFC Multi-Projection Candidate Test](./experiments/10-rust-rfc-multi-projection-candidates.md)
- [Recipe Original Source Test](./experiments/11-recipe-original-source-test.md)
- [Recipe Multi-Projection Candidate Test](./experiments/12-recipe-multi-projection-candidates.md)

## Review Status

The initial Part 3 draft is complete enough for consistency review and transition planning toward Part 4.

Remaining work should focus on:

- reducing duplication across chapters;
- aligning normative language levels;
- deciding which conceptual requirements become concrete YAML requirements in Part 4;
- preparing example documents and validation profiles.

## Reading Notes

Part 3 should be read after Part 1 and Part 2.

The key design constraint is that the Core Model must define enough structure to support reusable access, traceability, reconstruction, and interoperability while avoiding the temptation to encode final meaning.

Part 3 should therefore model **Projection-shaped access structures**, not final interpretations and not Projection-independent extraction results.
