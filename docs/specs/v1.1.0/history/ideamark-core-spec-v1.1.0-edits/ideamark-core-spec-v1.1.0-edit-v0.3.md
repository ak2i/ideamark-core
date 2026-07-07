# IdeaMark Core Specification v1.1.0 (edit-v0.3)

## 0. Version Positioning

This document is an editing draft of IdeaMark Core Specification v1.1.0.

- Target: Establish the philosophical and conceptual foundation
- Scope: Core Philosophy + Perspective + Entity
- Status: editing draft (edit-v0.3)

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
