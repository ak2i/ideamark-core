# IdeaMark Core Specification v1.1.0 (edit-v0.2)

## 0. Version Positioning

This document is an editing draft of IdeaMark Core Specification v1.1.0.

- Target: Establish the philosophical and conceptual foundation
- Scope: Core Philosophy + Perspective
- Status: editing draft (edit-v0.2)

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
