# IdeaMark Core Specification v1.1.0 (edit-v0.5)

## 0-4 (unchanged from edit-v0.4)

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
