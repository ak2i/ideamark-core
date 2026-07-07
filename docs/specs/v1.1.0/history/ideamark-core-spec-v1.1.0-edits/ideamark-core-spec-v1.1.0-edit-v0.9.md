# IdeaMark Core Specification v1.1.0 (edit-v0.4)

## 0. Version Positioning

This document is an editing draft of IdeaMark Core Specification v1.1.0.

- Target: Establish the philosophical and conceptual foundation
- Scope: Core Philosophy + Perspective + Entity + Occurrence
- Status: editing draft (edit-v0.4)

---

## 1. Core Philosophy

### 1.1 Background

Human language is not strictly governed by formal grammar.
Instead, it operates within a loosely bounded expressive space:

- Expression > Grammar
- Meaning emerges dynamically
- Communication remains stable despite freedom

This implies:

> There exists a constrained but flexible "meaning space" in human language.

---

### 1.2 Observation from LLMs

Large Language Models (LLMs) demonstrate that:

- Finite structures can generate seemingly infinite expressions
- Generated language remains "human-like"
- Outputs rarely diverge into meaningless randomness

This suggests:

> LLMs approximate the distribution of acceptable human meaning.

---

### 1.3 Core Hypothesis

IdeaMark is based on the following hypothesis:

> Meaning is not stored in text itself, but emerges through structured interpretation.

---

### 1.4 Design Shift

Previous versions (v1.0.x):

- Meaning = anchorage + role

v1.1.0:

> Meaning = controlled emergence within a structured space

---

### 1.5 Controlled Divergence

IdeaMark introduces the concept of:

> Controlled Divergence Space

This means:

- Meaning can vary (diverge)
- But within controlled boundaries
- Ensuring reusability and coherence

---

### 1.6 Responsibility Separation

Meaning generation is separated into three layers:

| Layer | Responsibility |
|------|---------------|
| LLM | Generate meaning (distribution) |
| Perspective | Direct meaning |
| IdeaMark | Constrain structure |

---

### 1.7 Principle Summary

1. Meaning must not be fully defined
2. Meaning must be directionally guided
3. Structure must constrain interpretation
4. Divergence must be allowed but controlled

---

### 1.8 Formal Model

Text → Entity Candidates → Perspective → Meaning Projection → IdeaMark Structure

---

### 1.9 Key Statement

> IdeaMark does not define meaning.
> It defines the conditions under which meaning can emerge without collapsing into chaos.

---

## 2. Perspective

### 2.1 Positioning

Perspective is a first-class object in IdeaMark v1.1.0.

Perspective does not define meaning itself.
Instead, it provides the directional condition under which meaning is generated.

A Perspective is therefore:

- a guide for interpretation
- a constraint on divergence
- a reusable description of analytical stance

Perspective is introduced in order to make controlled divergence explicit and reusable.

---

### 2.2 Minimal Schema

```yaml
perspectives:
  {perspective_id}:
    description: string
    base: perspective_ref
    modifiers: [string, ...]
```

Field meanings:

- `description` (required): natural-language description of the interpretive direction
- `base` (optional): reference to another perspective used as a base orientation
- `modifiers` (optional): free-form tags or adjustment labels

---

### 2.3 Design Principles

#### 2.3.1 Optional + Default

Perspective is not required for all documents.

Some documents may be created simply to achieve initial IdeaMark transformation,
without explicitly fixing a strong analytical stance.

Therefore:

- Perspective is OPTIONAL at the document level
- A document MAY define `default_perspective`
- When no explicit perspective is given, processing MAY proceed without one

This preserves the ability to "just IdeaMarkify" a source text.

#### 2.3.2 Structured but Non-Enumerated

Perspective vocabularies are not globally fixed.

Implementations MUST NOT reject a perspective merely because its semantic category is unknown.
The role of Perspective is not to enforce a closed taxonomy, but to provide a stable entry point into meaning generation.

#### 2.3.3 LLM-Oriented Description

`description` is intentionally natural language.
It is not merely human-facing documentation.
It also serves as machine-usable guidance for LLM-based interpretation.

Perspective therefore sits at the boundary between:

- formal structure
- human conceptual guidance
- model-oriented prompting

---

### 2.4 Default Perspective

Documents MAY define a default perspective.

```yaml
default_perspective: perspective_ref
```

Semantics:

- used when a Section has no explicit perspective list
- provides the baseline interpretive direction for the document
- does not prevent Sections from overriding or extending it

The default perspective is a convenience mechanism, not a mandatory global lock.

---

### 2.5 Multi-Perspective Sections

A Section MAY carry multiple perspectives.

This reflects the fact that a single section may legitimately be interpreted through more than one directional lens.

Example:

```yaml
sections:
  SEC-001:
    perspectives: ["literary", "political", "historical"]
```

Design meaning:

- Section-level interpretation is often plural
- Perspective pluralization is not an error but a feature
- The goal is controlled plurality, not forced singularity

Recommended interpretation:

- list order MAY be treated as soft priority
- implementations MAY use the first perspective as the default leading orientation
- however, all listed perspectives remain valid

This specification does not require a single primary perspective field.
A simple array is preferred at this stage for openness and editorial simplicity.

---

### 2.6 Perspective Scope

Perspective may exist at three levels:

| Level | Meaning |
|------|---------|
| Document | baseline interpretive direction |
| Section | local interpretive direction |
| Entity (optional) | record of extraction or segmentation basis |

This layered model separates:

- document-wide intention
- local reading frame
- extraction provenance

---

### 2.7 Entity-Level Perspective (Optional)

Entities MAY optionally record the perspective basis under which they were extracted or stabilized.

```yaml
entities:
  IE-001:
    kind: "context"
    content: "..."
    perspective_scope: ["political", "historical"]
```

Meaning of `perspective_scope`:

- not the final meaning of the entity
- not a restriction on future reuse
- a record of which interpretive directions contributed to this entity boundary

This is especially important for POR-like pipelines, where entity boundaries may differ depending on interpretive stance.

Entity-level perspective is therefore best understood as:

> extraction-basis metadata

rather than permanent semantic confinement.

---

### 2.8 Perspective and Reuse

Perspective improves reuse in two ways:

1. It constrains retrieval and synthesis by giving a directional entry point
2. It makes plurality manageable by describing divergence instead of hiding it

Thus Perspective is not merely annotation.
It is part of the retrieval architecture of knowledge reuse.

---

### 2.9 Non-Goals

Perspective is NOT:

- a full ontology of interpretation
- a fixed taxonomy of academic disciplines
- a guarantee of correctness
- a substitute for anchorage or role

Perspective provides direction.
Anchorage and role still provide structural reading and local function.

---

### 2.10 Summary Statement

> Perspective is a reusable, optional, and plural interpretive direction
> that constrains meaning generation without freezing it.

---

## 3. Entity

### 3.1 Positioning

Entity is the fundamental unit of meaning anchoring in IdeaMark.

However, unlike traditional linguistic or lexical units,
Entity is NOT defined by grammatical minimality.

Instead:

> Entity is the minimal unit of meaning under a given interpretive intention.

---

### 3.2 Redefinition of Atomicity

In IdeaMark v1.1.0, atomicity is redefined.

Traditional view:
- atomic = smallest lexical unit (word, morpheme)

IdeaMark view:
- atomic = smallest *meaningful unit under interpretation*

This implies:

- A single word MAY be an Entity
- A phrase MAY be an Entity
- A full sentence MAY be an Entity
- Even a long passage MAY be an Entity

Example:

A long literary sentence may function as a single Entity
if it is referenced as a whole unit of meaning.

---

### 3.3 Atomicity Basis

To make this explicit, Entity MAY define:

```yaml
atomicity_basis: interpretive | lexical | structural
```

Meanings:

- interpretive:
  - boundary determined by meaning intention
  - most common in IdeaMark usage

- lexical:
  - boundary follows lexical units
  - useful for linguistic analysis

- structural:
  - boundary follows document structure (e.g., paragraph, section)
  - useful for ingestion pipelines

If omitted:

- default is `interpretive`

---

### 3.4 Design Principle: Intent-Dependent Segmentation

Entity boundaries are not intrinsic to the text.

They depend on:

- Perspective
- Extraction policy (POR)
- Intended reuse

Therefore:

> The same source text may yield different Entity sets under different conditions.

This is not an error.

It is a core feature of controlled divergence.

---

### 3.5 Entity Schema (Extended)

```yaml
entities:
  {entity_id}:
    kind: string
    content: string
    atomicity_basis: interpretive | lexical | structural
    perspective_scope: [perspective_ref, ...]
```

Field meanings:

- kind:
  classification label (e.g., context, claim, evidence, concept)

- content:
  textual representation of the entity

- atomicity_basis (optional):
  how the boundary of this entity was determined

- perspective_scope (optional):
  interpretive directions that influenced this entity extraction

---

### 3.6 Perspective Scope (Revisited)

`perspective_scope` does NOT mean:

- the only valid interpretation of the entity
- a restriction on reuse

It means:

> "This entity was stabilized under these interpretive directions"

Thus:

- future reuse MAY ignore it
- or MAY use it as a hint for alignment

---

### 3.7 Entity Identity and Stability

Entities are not guaranteed to be globally stable.

Two entities with identical content:

- MAY be considered distinct if extracted under different contexts
- MAY be merged by implementations if deemed equivalent

This specification does not enforce global identity resolution.

---

### 3.8 Entity Granularity Trade-off

There is an inherent trade-off:

| Granularity | Effect |
|------------|--------|
| Fine | higher recomposability, lower semantic cohesion |
| Coarse | higher cohesion, lower recomposability |

IdeaMark does not enforce a fixed point.

Instead:

> Granularity should be chosen based on intended reuse.

---

### 3.9 Entity and Meaning Emergence

Entity does not contain meaning in isolation.

Meaning emerges when:

- Entity
- Occurrence (role)
- Section (anchorage + perspective)

are combined.

Thus:

> Entity is a potential carrier of meaning, not meaning itself.

---

### 3.10 Summary Statement

> Entity is an interpretation-dependent unit of meaning anchoring,
> whose boundaries are defined not by language, but by intent.


---

## 4. Occurrence

### 4.1 Positioning

Occurrence represents the appearance of an Entity within a Section.

If Entity is a potential carrier of meaning,
Occurrence is the activation of that potential within a contextual structure.

Thus:

> Occurrence is where meaning begins to take form.

---

### 4.2 Core Responsibility

Occurrence is responsible for:

- linking Entity to a Section
- defining the functional role of that Entity
- describing how the Entity is expressed in discourse

Occurrence does NOT define interpretive direction (Perspective).

---

### 4.3 Core Schema

```yaml
occurrences:
  {occurrence_id}:
    entity: entity_ref
    role: string
    discourse_frame:
      subjectivity: objective | subjective | mixed
      person: first | second | third | none
      modality: assertive | speculative | interrogative | imperative | expressive
```

---

### 4.4 Role

`role` defines what the Entity is doing in that context.

Typical roles may include:

- claim
- evidence
- context
- mechanism
- example
- definition

Design principle:

> role is functional, not interpretive

This means:

- role describes contribution to structure
- not the perspective under which it is interpreted

---

### 4.5 Discourse Frame

Discourse Frame describes *how* the content is expressed.

It captures linguistic and rhetorical properties
that influence how meaning is perceived.

---

#### 4.5.1 subjectivity

```yaml
subjectivity: objective | subjective | mixed
```

- objective: presented as neutral or factual
- subjective: reflects internal state, opinion, or emotion
- mixed: combination of both

---

#### 4.5.2 person

```yaml
person: first | second | third | none
```

- first: speaker-centered (I, we)
- second: listener-directed (you)
- third: external reference (he, she, they)
- none: impersonal or structural statements

---

#### 4.5.3 modality

```yaml
modality: assertive | speculative | interrogative | imperative | expressive
```

- assertive: stating information
- speculative: uncertain or hypothetical
- interrogative: asking a question
- imperative: giving instruction
- expressive: conveying emotion or attitude

---

### 4.6 Design Principle: Separation of Function and Expression

Occurrence separates:

| Aspect | Field |
|------|------|
| What it does | role |
| How it is expressed | discourse_frame |
| How it is interpreted | Section perspective |

This separation ensures:

- composability
- clarity
- controlled divergence

---

### 4.7 Minimality Principle

All discourse_frame fields are OPTIONAL.

If omitted:

- systems MAY infer them
- or leave them undefined

This allows lightweight usage without losing structural consistency.

---

### 4.8 Occurrence and Meaning Emergence

Meaning begins to stabilize when:

- an Entity is placed into a Section
- with a defined role
- under a discourse frame

Thus:

> Occurrence is the first structural layer where meaning becomes observable.

---

### 4.9 Summary Statement

> Occurrence activates an Entity within a context,
> defining its function and expression, but not its interpretation.

---

## 5. Section

### 5.1 Positioning

Section is the primary unit of contextual interpretation.

If Occurrence activates meaning,
Section stabilizes and frames that meaning.

Thus:

> Section defines "how a set of occurrences should be read together."

---

### 5.2 Core Responsibility

Section is responsible for:

- grouping occurrences into a coherent unit
- providing interpretive direction (via Perspective)
- defining contextual anchoring (anchorage)
- establishing positional structure within the document

---

### 5.3 Core Schema

```yaml
sections:
  {section_id}:
    title: string
    perspectives: [perspective_ref, ...]
    anchorage:
      view: [string, ...]
      phase: [string, ...]
    occurrences: [occurrence_ref, ...]
```

---

### 5.4 Title

`title` is a human-readable label for the section.

It represents:

- the local topic
- the editorial intent
- the relative position in discourse

Unlike anchorage:

> title is descriptive, not structural

---

### 5.5 Perspective (Section-Level)

Section carries the primary interpretive direction.

- MAY have multiple perspectives
- MAY inherit from document default
- MAY be empty

Design principle:

> Section is the main locus of interpretation

---

### 5.6 Anchorage (Extended)

Anchorage defines structural positioning of a Section.

In v1.1.0:

```yaml
anchorage:
  view: [string, ...]
  phase: [string, ...]
```

#### 5.6.1 view

Represents *what aspect of the subject is being addressed*

Examples:

- problem
- solution
- background
- implication
- methodology

#### 5.6.2 phase

Represents *where in a process or timeline this section belongs*

Examples:

- introduction
- analysis
- development
- conclusion
- future

---

### 5.7 Multi-Anchorage Design

Both `view` and `phase` are arrays.

This allows:

- hybrid sections
- overlapping roles
- flexible structuring across domains

Example:

```yaml
anchorage:
  view: ["problem", "context"]
  phase: ["introduction"]
```

Design principle:

> Section positioning is multi-dimensional, not singular

---

### 5.8 Section Ordering

Sections may be ordered implicitly or explicitly.

This specification does NOT enforce a strict ordering mechanism.

However:

- document order MAY imply sequence
- title MAY imply narrative progression

---

### 5.9 Section as Interpretation Boundary

Section acts as a boundary where:

- Perspective applies
- Anchorage applies
- Occurrences are grouped

Thus:

> Section is the smallest unit where interpretation becomes coherent.

---

### 5.10 Relationship to Other Layers

| Layer | Function |
|------|--------|
| Entity | potential meaning |
| Occurrence | activation + function |
| Section | interpretation + grouping |

---

### 5.11 Summary Statement

> Section groups occurrences and defines how they are interpreted,
> providing both structural anchoring and interpretive direction.

---

## 6. Relations

### 6.1 Positioning

Relations define connections between elements in IdeaMark.

If Sections stabilize meaning locally,
Relations enable meaning to extend across boundaries.

Thus:

> Relations form the graph structure of IdeaMark.

---

### 6.2 Core Responsibility

Relations are responsible for:

- connecting Entities across contexts
- linking Sections to each other
- enabling knowledge traversal and recomposition

Relations do NOT define meaning by themselves.
They provide pathways through which meaning can be recombined.

---

### 6.3 Design Principle: Explicit Connectivity

IdeaMark does not assume implicit relationships.

All meaningful cross-structure connections SHOULD be explicitly represented.

This ensures:

- transparency
- traceability
- controllable recomposition

---

### 6.4 Relation Schema

```yaml
relations:
  {relation_id}:
    type: string
    from: reference
    to: reference
```

Where:

- `from` and `to` MAY refer to:
  - entity_ref
  - section_ref

---

### 6.5 Relation Types

Relation types are not globally fixed.

Typical examples include:

- supports
- contradicts
- elaborates
- causes
- refers_to
- parallels

Design principle:

> Relation types are descriptive, not constrained

---

### 6.6 Entity-Level Relations

Entities MAY be connected directly.

Example:

```yaml
relations:
  REL-001:
    type: supports
    from: IE-001
    to: IE-002
```

---

### 6.7 Section-Level Relations

Sections MAY also be connected.

Example:

```yaml
relations:
  REL-002:
    type: elaborates
    from: SEC-001
    to: SEC-002
```

---

### 6.8 Cross-Level Relations

Relations MAY cross levels.

Example:

```yaml
relations:
  REL-003:
    type: contextualizes
    from: IE-003
    to: SEC-002
```

---

### 6.9 Directionality

All relations are directional.

- `from` → `to`

---

### 6.10 Multiplicity

Entities and Sections MAY participate in multiple relations.

This forms a graph (not a tree).

---

### 6.11 Relation and Meaning

Relations do not create meaning alone.

Meaning emerges when:

- Entity
- Occurrence
- Section
- Relations

are combined.

---

### 6.12 Design Principle: Recomposition

Relations enable:

- recombining fragments
- traversing knowledge
- constructing new interpretations

---

### 6.13 Summary Statement

> Relations connect the structured units of IdeaMark,
> enabling knowledge to extend, recombine, and evolve across contexts.

---

## 7. Validation / Constraints

### 7.1 Positioning

Validation defines the structural integrity of an IdeaMark document.

While IdeaMark allows flexible and expressive structures,
a minimal set of constraints is required to ensure:

- consistency
- interpretability
- processability

Thus:

> Validation constrains structure without constraining meaning.

---

### 7.2 Design Principle: Minimal Constraint

IdeaMark adopts a minimal constraint philosophy.

- Only constraints necessary for structural coherence are enforced
- Meaning-related constraints are intentionally avoided

This ensures:

- flexibility across domains
- compatibility with LLM-driven generation
- preservation of controlled divergence

---

### 7.3 Required Elements

An IdeaMark document MUST include:

- entities
- sections
- occurrences

Relations and perspectives are OPTIONAL.

---

### 7.4 Reference Integrity

All references MUST be valid.

- occurrence.entity MUST refer to an existing entity
- section.occurrences MUST refer to existing occurrences
- relations.from / relations.to MUST refer to valid entities or sections

Invalid references MUST be treated as errors.

---

### 7.5 Identifier Uniqueness

All identifiers MUST be unique within their namespace.

- entity_id
- occurrence_id
- section_id
- relation_id

Duplicate identifiers MUST be rejected.

---

### 7.6 Structural Completeness

Each occurrence MUST define:

- entity
- role

discourse_frame is OPTIONAL.

Each section MUST define:

- occurrences (non-empty list)

title, perspectives, and anchorage are OPTIONAL.

---

### 7.7 Default Handling

If optional fields are omitted:

- perspective:
  - MAY fall back to document-level default
  - MAY remain undefined

- atomicity_basis:
  - defaults to "interpretive"

- discourse_frame:
  - MAY be inferred or omitted

- anchorage:
  - MAY be absent without invalidating the document

---

### 7.8 Type Flexibility

The following fields are intentionally unconstrained strings:

- entity.kind
- occurrence.role
- relation.type
- anchorage.view / anchorage.phase

Implementations MAY introduce controlled vocabularies,
but the core specification does not enforce them.

---

### 7.9 Multi-Value Fields

The following fields MUST be arrays if present:

- perspectives
- anchorage.view
- anchorage.phase
- perspective_scope

Single values MUST be represented as single-element arrays.

---

### 7.10 Empty Structures

Empty collections are handled as follows:

- sections MUST NOT be empty
- occurrences MUST NOT be empty
- entities MUST NOT be empty

However:

- relations MAY be empty or absent
- perspectives MAY be empty or absent

---

### 7.11 Error vs Warning

Validation distinguishes between:

#### Errors (MUST fail)

- invalid references
- missing required fields
- duplicate identifiers

#### Warnings (SHOULD notify)

- missing optional fields
- empty optional arrays
- unused entities or sections

---

### 7.12 Implementation Freedom

Implementations MAY:

- infer missing optional fields
- enrich documents with additional metadata
- normalize structures

However:

- they MUST NOT alter the explicit structure without traceability

---

### 7.13 Validation Scope

Validation operates at:

- syntactic level (YAML structure)
- structural level (references, completeness)

Validation does NOT operate at:

- semantic correctness
- logical validity
- factual accuracy

---

### 7.14 Summary Statement

> Validation ensures that IdeaMark documents remain structurally sound,
> while preserving maximum freedom for meaning generation and interpretation.

---

## 8. Compatibility / Migration

### 8.1 Positioning

This section defines how IdeaMark v1.1.0 relates to previous versions (v1.0.x),
and how existing documents can be migrated.

Thus:

> Compatibility preserves continuity, while migration enables evolution.

---

### 8.2 Versioning Policy

IdeaMark follows semantic versioning principles:

- MAJOR: incompatible structural changes
- MINOR: backward-compatible feature additions
- PATCH: clarifications or minor fixes

v1.1.0 introduces conceptual and structural extensions,
but aims to remain partially compatible with v1.0.x.

---

### 8.3 Compatibility Overview

| Feature | v1.0.x | v1.1.0 |
|--------|--------|--------|
| Entity | ✔ | ✔ (extended) |
| Occurrence.role | ✔ | ✔ |
| Section.anchorage | single | multi (array) |
| Perspective | implicit | explicit |
| Relations | optional | expanded |
| discourse_frame | ✖ | ✔ |

---

### 8.4 Backward Compatibility

v1.0.x documents MAY be interpreted as valid v1.1.0 documents if:

- missing fields are treated as defaults
- single-value fields are promoted to arrays where needed

Example:

```yaml
anchorage:
  view: "problem"
```

becomes:

```yaml
anchorage:
  view: ["problem"]
```

---

### 8.5 Migration Strategy

Migration from v1.0.x to v1.1.0 SHOULD follow:

#### Step 1: Structural normalization

- convert scalar fields to arrays where required
- ensure identifiers and references are valid

#### Step 2: Optional enrichment

- add perspectives if meaningful
- add discourse_frame if available
- add atomicity_basis where useful

#### Step 3: Graph enrichment (optional)

- introduce relations between entities or sections

---

### 8.6 Non-Breaking Changes

The following changes are designed to be non-breaking:

- addition of optional fields
- expansion of anchorage to arrays
- introduction of discourse_frame

Existing documents remain interpretable without modification.

---

### 8.7 Breaking Considerations

Potential incompatibilities:

- systems expecting scalar anchorage fields
- strict schema validators not supporting arrays
- tooling assuming fixed vocabularies

Implementations SHOULD update parsers accordingly.

---

### 8.8 Default Interpretation of Legacy Documents

When interpreting v1.0.x documents:

- perspective: assumed undefined
- atomicity_basis: assumed interpretive
- discourse_frame: assumed absent

This ensures consistent behavior under v1.1.0.

---

### 8.9 Forward Compatibility

v1.1.0 is designed to allow future extensions:

- additional discourse_frame fields
- richer relation types
- extended anchorage dimensions

Implementations SHOULD ignore unknown fields gracefully.

---

### 8.10 Tooling Implications

Tools SHOULD:

- support both v1.0.x and v1.1.0 inputs
- provide migration utilities
- expose validation warnings for legacy structures

---

### 8.11 Summary Statement

> IdeaMark v1.1.0 extends the expressive and structural capabilities
> of the framework while preserving compatibility pathways for existing documents.
