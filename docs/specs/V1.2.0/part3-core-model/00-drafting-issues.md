# Part 3 Drafting Issues

**Part:** 3 — Core Model  
**Status:** Planning Draft  
**Type:** Drafting Notes / Editorial Planning

This document identifies the major issues that should be resolved while drafting Part 3.

Part 3 should translate the philosophy of Part 1 and the architecture of Part 2 into a conceptual model.

It should not prematurely define YAML syntax.

## 0.1 Central Drafting Question

The central question for Part 3 is:

> What minimal conceptual objects must IdeaMark Core define so that future humans and AI systems can reconstruct useful interpretations from Original Sources through Projections without storing final meaning?

This question should guide all modeling choices.

## 0.2 Model Orientation

Part 3 should model:

- reusable access structures;
- traceability to Original Sources;
- Projection-shaped structure;
- Decomposition as the bridge between Original Source and Core Model structures;
- document-level identity and context;
- relationships among Entities, Occurrences, Sections, Relations, Perspectives, and Anchorage;
- status, versioning, and regeneration responsibilities;
- invariants that preserve reconstruction usefulness.

Part 3 should avoid modeling:

- final meaning;
- universal truth;
- universal authority ranking;
- universal ontology;
- universal domain vocabulary;
- universal coordinate system;
- complete intellectual activity content;
- Projection quality evaluation;
- Projection library governance;
- implementation storage or retrieval design.

## 0.3 Required Conceptual Objects

The following conceptual objects appear necessary for Part 3:

1. **Original Source Reference** — a traceable reference to source material used as the basis for Projection-guided generation or reconstruction.
2. **Projection Context** — the reuse strategy or Projection identity that shaped the IdeaMark document.
3. **Decomposition** — the Projection-guided modeling act that transforms Original Source material into Core Model structures.
4. **IdeaMark Document** — an operational access-structure artifact generated from Original Source(s) under Projection Context.
5. **Entity** — a Projection-shaped structural component produced by Decomposition.
6. **Occurrence** — an activation, appearance, evidence instance, or situated use produced or recognized by Decomposition.
7. **Section** — a local organizational frame for reconstruction produced or organized by Decomposition.
8. **Relation** — a structural link useful for reconstruction.
9. **Perspective** — a record of interpretive or Projection-related context, without becoming final meaning.
10. **Provenance** — information about how and why the document or object was produced, reviewed, or regenerated.
11. **Anchorage** — a claim connecting model objects to source positions, spans, fragments, contexts, or other traceable anchors.
12. **Status and Versioning** — operational state of documents and model objects across regeneration, coexistence, review, and deprecation.

The exact YAML form of these concepts belongs to Part 4.

## 0.4 Key Modeling Tensions

### 0.4.1 Decomposition: General Extraction or Projection-guided Modeling?

Decomposition must not be defined as general extraction from an Original Source.

A Projection-independent IdeaMark document may be technically possible, but it is not the intended model because it does not encode a useful reuse strategy.

Drafting issue:

- How should Part 3 define Decomposition without turning it into an algorithm?
- How should Decomposition depend on Projection Context while remaining independent from any particular authoring workflow?
- How should Part 3 explain that Situation Vector informs Projection generation but is not directly embedded as an unbounded input to Decomposition?
- How should Decomposition avoid evaluating Projection quality?

Likely direction:

Decomposition should be defined as the Projection-guided modeling act that produces Entity, Occurrence, Section, Relation, Anchorage, and related structures from Original Source material.

Part 3 should define Decomposition outputs and invariants, while leaving Projection quality, Projection lifecycle, and Projection library governance to Part 5.

### 0.4.2 Entity: Meaning Unit or Decomposition Component?

Entity must not be defined as a final semantic object or as a globally stable knowledge unit.

It should be defined as a structural component produced by Projection-guided Decomposition.

Drafting issue:

- How much semantic description may an Entity contain before it begins to look like fixed meaning?
- Should Entity identity be stable across Projections, or should Projection-specific Entities be allowed by default?
- How should Entity reuse across multiple IdeaMark documents be described conceptually without requiring global ontology management?
- How should Part 3 explain that an Entity may be useful alone, but often becomes useful only with Occurrences, Sections, Relations, and Anchorage?

Likely direction:

Entity should be treated as a Projection-shaped structural component. Reusability is a desirable property, not the definition of Entity. Core should not require universal Entity identity.

### 0.4.3 Occurrence: Textual Appearance or Intellectual Activation?

Occurrence must not be reduced to text span occurrence.

An Occurrence may be a source appearance, evidence instance, event, observation, activation, use, or situated manifestation relevant under a Projection.

Drafting issue:

- Should Occurrence require source anchorage?
- Can an Occurrence be inferred from multiple source fragments?
- How should non-textual occurrences be modeled conceptually?

Likely direction:

Occurrence should be a Projection-shaped instance or activation connected to source material through Anchorage where possible.

### 0.4.4 Section: Source Structure or Reconstruction Frame?

Section must not merely reproduce source headings.

A Section should organize future reconstruction according to Projection and expected intellectual activity.

Drafting issue:

- How much freedom should Section have relative to the Original Source structure?
- Can one Section combine material from multiple Original Sources?
- Can multiple Section structures coexist for the same source under different Projections?

Likely direction:

Section should be treated as a local coordinate frame for reconstruction.

### 0.4.5 Relation: Semantic Claim or Navigation Aid?

Relation should support reconstruction but should not become a universal ontology edge.

Drafting issue:

- Are Relations claims about the world, claims about source structure, or claims about reuse?
- Should relation types be Core-defined or Projection-defined?
- How should uncertainty or contested relations be handled?

Likely direction:

Core should define Relation as a structural link with optional typing, leaving relation vocabularies largely to Projection, domain practice, or later specifications.

### 0.4.6 Perspective: Projection Record or Interpretive Context?

Perspective may record why a document or object was generated in a particular way.

However, it must not become a container for final interpretation.

Drafting issue:

- Should Projection be represented as a Perspective, linked from Perspective, or modeled separately?
- What minimal Perspective information is necessary for reconstruction?
- How should multiple Perspectives coexist?

Likely direction:

Perspective should record interpretive and Projection-related context sufficient for later users to understand the access strategy, without defining a universal viewpoint taxonomy.

### 0.4.7 Anchorage: Exact Span or Traceability Claim?

Anchorage should preserve the ability to return to Original Sources.

However, source media may be text, image, video, sensor stream, conversation, dataset, code, or future forms.

Drafting issue:

- Should Core define anchorage abstractly rather than text-offset-first?
- What kinds of anchors are required for interoperability?
- How should approximate, indirect, or multi-source anchorage be represented conceptually?

Likely direction:

Anchorage should be a generalized traceability claim, with text spans as one implementation case.

### 0.4.8 Status and Versioning: Document-level or Object-level?

IdeaMark documents are operational snapshots.

Drafting issue:

- Should status apply only to documents or also to Entities, Occurrences, Sections, and Relations?
- How should regeneration preserve traceability without requiring global identity stability?
- How should coexistence of multiple documents be explained conceptually?

Likely direction:

Part 3 should define document-level status first and allow object-level status as an optional extension or later specification concern.

## 0.5 Part 3 / Part 5 Boundary

Part 3 defines the Core Model produced by Projection-guided Decomposition.

Part 5 defines Projection as a reusable strategy and ecosystem object.

Part 3 should not decide whether a Projection is:

- high quality;
- socially shareable;
- legally appropriate;
- institutionally approved;
- broadly reusable;
- too narrow;
- too broad;
- obsolete;
- worth publishing in a Projection Library.

Those are Projection lifecycle and ecosystem questions.

Part 3 should only require that the Projection Context used for Decomposition can be referenced or recorded sufficiently for later reconstruction.

## 0.6 Cross-cutting Design Constraints

Part 3 should preserve the following constraints from Part 1 and Part 2:

1. **No final meaning inside Core.**
2. **Original Source is authority only in Projection-guided context, not universal truth.**
3. **Projection shapes the model but is not reduced to a prompt.**
4. **IdeaMark documents are operational snapshots.**
5. **Multiple valid models may exist for the same source.**
6. **Traceability is more important than semantic completeness.**
7. **Interpretation cost reduction is a design rationale.**
8. **Human-AI Intellectual Activity remains open and not enumerated.**
9. **The Core should define model roles, not domain vocabularies.**
10. **Future media and source types must remain possible.**
11. **Decomposition should be Projection-guided, not general extraction.**
12. **Entity ID should be treated primarily as a reference label, not a universal identity claim.**

## 0.7 Recommended Drafting Order

Recommended Part 3 drafting order:

1. Core Model Overview.
2. Model Boundary and Non-goals.
3. Original Source Reference Model.
4. Projection Context Model.
5. Decomposition Model.
6. IdeaMark Document Model.
7. Entity / Occurrence / Section models.
8. Relation / Perspective / Provenance models.
9. Anchorage and Traceability Model.
10. Status, Versioning, and Regeneration Model.
11. Model Invariants.
12. Core Model Summary.

This order establishes the boundary before individual model objects are defined.

## 0.8 Questions to Resolve Before Writing Normative YAML

Before Part 4 defines YAML syntax, Part 3 should resolve:

- Which conceptual objects are mandatory in every IdeaMark document?
- Which conceptual objects are optional but Core-defined?
- Which fields are conceptual requirements versus YAML representation choices?
- How strongly must every object be anchored to Original Sources?
- Whether Projection Context must always be explicitly recorded.
- Whether Decomposition should be represented explicitly or only implied by Projection Context and generated structures.
- Whether Entity, Occurrence, and Section identifiers are local, document-level, repository-level, or implementation-defined.
- Whether relation types belong to Core or Projection.
- How to express uncertainty, review status, and regeneration without turning the model into workflow management.
- How to support multi-source documents without requiring a universal source aggregation model.
- How to support non-textual sources without making text offsets the hidden default.

## 0.9 Summary

Part 3 should make IdeaMark Core precise enough to support interoperability and validation, but not so prescriptive that it freezes meaning, source media, domain vocabulary, Projection practice, or future intellectual activity.

The Core Model should be the bridge between the philosophy of separation and the later YAML specification.

Its central modeling stance is that IdeaMark documents are produced by Projection-guided Decomposition, not by general source extraction.
