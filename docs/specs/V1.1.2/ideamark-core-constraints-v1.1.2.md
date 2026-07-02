# IdeaMark Core Constraints v1.1.2

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

- occurrence.entity MUST refer to an existing entity when single-Entity shorthand is used
- every occurrence.entity_roles[].entity MUST refer to an existing entity when multi-Entity form is used
- section.occurrences MUST refer to existing occurrences
- relations.from MUST refer to a valid target
- relations.to MUST refer to a valid target

Invalid references MUST be treated as errors.

For relations.from / relations.to, a bare identifier is resolved against the entity namespace first, then the section namespace. An identifier present in both namespaces is ambiguous: implementations SHOULD emit a warning, and authors SHOULD disambiguate using a typed reference form.

Reference integrity intentionally excludes perspective_ref. A bare perspective_ref that does not resolve within the document SHOULD be reported as a warning, never as an error (see Core Spec §2.4).

Reference integrity applies to references within the containing document only. A reference qualified with another document's doc_id (Core Spec §9.2) is opaque to validation: reusing an element id from another document is a normal case, never an error.

---

### 7.5 Identifier Uniqueness

The following identifiers MUST be unique within their namespace:

- entity_id
- occurrence_id
- section_id
- relation_id
- perspective_id

Canonical v1.1.2 registries are ordered lists of ID-bearing records. Therefore, every entity, occurrence, section, relation, and perspective record MUST define `id`.

Mapping-style registries from v1.1.1 MAY be accepted as compatibility input by tooling, but canonical output SHOULD use list-style registries.

Duplicate identifiers MUST fail validation.

---

### 7.6 Structural Completeness

Each occurrence MUST define either the single-Entity shorthand:

```yaml
entity
role
```

or the canonical multi-Entity form:

```yaml
entity_roles
role
```

`entity_roles` MUST be a non-empty array when present.

Each `entity_roles[]` item MUST define:

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

atomicity_basis is an enumeration: `interpretive | lexical | structural`.

A value outside this enumeration MUST be reported as a warning, not an error. The value is preserved (§7.17); Core assigns it no semantics.

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
- entity_roles
- occurrences

Single values MUST be normalized as single-element arrays.

A value that cannot be normalized to an array (e.g. a mapping) MUST be treated as an error.

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

Errors protect structural processability; warnings flag deviations in interpretive metadata.

#### Errors

- invalid references
- duplicate identifiers
- missing required fields
- missing record id in list-style registries
- missing payload
- payload without body/ref/cache
- ref without uri
- multi-value fields that cannot be normalized (§7.13)

#### Warnings

- missing media_type
- missing captured_at
- missing optional fields
- unused entities
- ambiguous relation references
- unresolved perspective references
- unknown atomicity_basis values (§7.11)

Implementations MAY add further hygiene warnings (§7.17); such warnings are outside the Core list above.

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

---

### 7.20 v1.1.2 Registry Representation

Core registries SHOULD be represented as ordered lists of ID-bearing records:

```yaml
entities:
  - id: ENT-001
    kind: instrument
    payload:
      body: "..."

occurrences:
  - id: OCC-001
    entity: ENT-001
    role: evidence

sections:
  - id: SEC-001
    occurrences:
      - OCC-001
```

Implementations MUST construct internal ID indexes for validation and processing.

Mapping-style v1.1.1 registries MAY be accepted as compatibility input, but v1.1.2 canonical output SHOULD use list-style registries.

### 7.21 Occurrence Compatibility

The following single-Entity shorthand remains valid:

```yaml
occurrences:
  - id: OCC-001
    entity: ENT-001
    role: evidence
```

It is equivalent to:

```yaml
occurrences:
  - id: OCC-001
    role: evidence
    entity_roles:
      - entity: ENT-001
        role: evidence
```

Processors MAY normalize shorthand into `entity_roles`.

