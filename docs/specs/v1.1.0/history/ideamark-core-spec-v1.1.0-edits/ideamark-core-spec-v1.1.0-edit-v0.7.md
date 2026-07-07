# IdeaMark Core Specification v1.1.0 (edit-v0.7)

## 0-6 (unchanged from edit-v0.6)

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
