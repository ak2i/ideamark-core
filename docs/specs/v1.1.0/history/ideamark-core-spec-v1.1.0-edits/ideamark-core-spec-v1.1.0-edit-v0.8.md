# IdeaMark Core Specification v1.1.0 (edit-v0.8)

## 0-7 (unchanged from edit-v0.7)

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
