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
