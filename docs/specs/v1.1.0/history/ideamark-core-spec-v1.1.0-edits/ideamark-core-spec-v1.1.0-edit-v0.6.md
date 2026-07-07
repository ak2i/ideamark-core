# IdeaMark Core Specification v1.1.0 (edit-v0.6)

## 0-5 (unchanged from edit-v0.5)

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
