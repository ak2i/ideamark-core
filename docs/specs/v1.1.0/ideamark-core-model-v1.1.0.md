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
