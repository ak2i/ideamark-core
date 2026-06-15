# IdeaMark Core Constraints v1.1.1

## 7. Validation / Constraints

### 7.1 Positioning

Validation defines the structural integrity of an IdeaMark document.

IdeaMark validates structure, not meaning.

Therefore:

> Validation constrains structure without constraining interpretation.

---

### 7.2 Design Principle: Minimal Constraint

Only constraints required for:

- consistency
- interpretability
- processability

are enforced.

Meaning-related constraints are intentionally excluded.

---

### 7.3 Required Elements

An IdeaMark document MUST include:

- entities
- occurrences
- sections

Relations and perspectives remain OPTIONAL.

---

### 7.4 Reference Integrity

All internal references MUST be valid.

- occurrence.entity MUST refer to an existing entity
- section.occurrences MUST refer to existing occurrences
- relations.from MUST refer to a valid target
- relations.to MUST refer to a valid target

Invalid references MUST be treated as errors.

---

### 7.5 Identifier Uniqueness

The following identifiers MUST be unique within their namespace:

- entity_id
- occurrence_id
- section_id
- relation_id
- perspective_id

Duplicate identifiers MUST fail validation.

---

### 7.6 Structural Completeness

Each occurrence MUST define:

```yaml
entity
role
```

Each section MUST define:

```yaml
occurrences
```

with a non-empty array.

---

### 7.7 Entity Payload Requirements

Each entity MUST define:

```yaml
payload
```

The payload MUST contain at least one of:

```yaml
payload.body
payload.ref
payload.cache
```

The following are valid:

```yaml
body
```

```yaml
ref
```

```yaml
cache
```

```yaml
body + ref
```

```yaml
ref + cache
```

```yaml
body + ref + cache
```

The following is invalid:

```yaml
payload: {}
```

---

### 7.8 Payload Format Requirements

If present:

```yaml
payload:
  format:
```

the following recommendations apply:

| Field | Requirement |
|---------|---------|
| media_type | SHOULD |
| profile | MAY |
| version | MAY |
| definition_ref | MAY |

Example:

```yaml
format:
  media_type: text/markdown
  profile: GCP-knowledge-catalog-okf
  version: "1.0"
  definition_ref: https://...
```

---

### 7.9 Payload Reference Requirements

If:

```yaml
payload:
  ref:
```

is present,

then:

```yaml
ref.uri
```

MUST be present.

Optional:

```yaml
ref.selector
```

Example:

```yaml
ref:
  uri: ./knowledge/example.okf.md
  selector: "#claim-001"
```

Selector semantics are profile-dependent and outside Core validation scope.

---

### 7.10 Payload Cache Requirements

If:

```yaml
payload:
  cache:
```

is present,

the following recommendations apply:

| Field | Requirement |
|---------|---------|
| body | SHOULD |
| captured_at | SHOULD |
| source_hash | MAY |

Example:

```yaml
cache:
  body: ...
  captured_at: 2026-06-16T00:00:00+09:00
  source_hash: sha256:...
```

---

### 7.11 Default Handling

If optional fields are omitted:

- perspective MAY remain undefined
- atomicity_basis defaults to interpretive
- discourse_frame MAY be omitted
- anchorage MAY be omitted
- profile MAY be omitted
- definition_ref MAY be omitted

---

### 7.12 Type Flexibility

The following remain intentionally unconstrained:

- entity.kind
- occurrence.role
- relation.type
- anchorage.view
- anchorage.phase
- payload.format.profile

Implementations MAY introduce controlled vocabularies.

Core validation MUST NOT require them.

---

### 7.13 Multi-Value Fields

The following MUST be arrays if present:

- perspectives
- perspective_scope
- anchorage.view
- anchorage.phase

Single values MUST be normalized as single-element arrays.

---

### 7.14 Empty Structures

The following MUST NOT be empty:

- entities
- occurrences
- sections

The following MAY be empty or absent:

- relations
- perspectives

---

### 7.15 Error vs Warning

#### Errors

- invalid references
- duplicate identifiers
- missing required fields
- missing payload
- payload without body/ref/cache
- ref without uri

#### Warnings

- missing media_type
- missing captured_at
- missing optional fields
- unused entities
- unused sections

---

### 7.16 Payload Validation Boundary

Core validation validates:

- YAML structure
- references
- completeness

Core validation does NOT validate:

- payload meaning
- payload correctness
- payload profile semantics
- external resource existence
- URI reachability
- selector interpretation

Therefore:

> Payload processing belongs to profile-specific tooling, not IdeaMark Core.

---

### 7.17 Implementation Freedom

Implementations MAY:

- infer optional fields
- enrich metadata
- normalize structures

However they MUST preserve traceability.

---

### 7.18 Forward Compatibility

Unknown fields MUST be ignored.

Unknown payload profiles MUST NOT invalidate a document.

Implementations SHOULD preserve unsupported payload metadata.

---

### 7.19 Summary Statement

> Validation guarantees structural integrity while preserving payload independence, interpretive flexibility, and future extensibility.
