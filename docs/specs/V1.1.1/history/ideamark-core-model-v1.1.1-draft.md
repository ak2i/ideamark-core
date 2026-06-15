# IdeaMark Core Model v1.1.1

## 3. Entity

### 3.1 Positioning

Entity is the fundamental unit of meaning anchoring in IdeaMark.

Entity does not own meaning itself.

Instead:

> Entity defines the boundary under which meaning may emerge and be reused.

Entity is independent from the representation format of the knowledge it references.

---

### 3.2 Redefinition of Atomicity

Entity remains the minimal meaningful unit under a given interpretive intention.

Atomicity is determined by:

- Perspective
- Extraction policy (POR)
- Intended reuse

and not by representation format.

---

### 3.3 Atomicity Basis

```yaml
atomicity_basis: interpretive | lexical | structural
```

Default:

```yaml
atomicity_basis: interpretive
```

---

### 3.4 Payload-Agnostic Entity

IdeaMark Core is payload-agnostic.

Entities MAY reference:

- plain text
- markdown
- OKF
- TPCG
- JSON
- YAML
- future formats

The representation format does not affect Entity identity.

---

### 3.5 Entity Schema (v1.1.1)

```yaml
entities:
  {entity_id}:
    kind: string

    payload:
      format:
        media_type: string
        profile: string
        version: string
        definition_ref: uri

      body: string

      ref:
        uri: string

      cache:
        body: string
        captured_at: datetime
        source_hash: string

    atomicity_basis: interpretive | lexical | structural
    perspective_scope: [perspective_ref, ...]
```

---

### 3.6 Payload Model

#### 3.6.1 format

Describes the representation format.

```yaml
format:
  media_type: text/markdown
  profile: GCP-knowledge-catalog-okf
  version: "1.0"
  definition_ref: https://...
```

##### media_type

Identifies the syntactic container.

Examples:

- text/plain
- text/markdown
- application/json
- application/yaml

##### profile

Identifies the semantic document format.

Examples:

- GCP-knowledge-catalog-okf
- tpcg
- ideamark
- profit-model-catalog

##### version

Optional format version.

##### definition_ref

Reference to the defining specification.

---

#### 3.6.2 body

Embedded payload representation.

Used when:

- self-contained documents are preferred
- LLM context expansion is required
- portability is desired

---

#### 3.6.3 ref

Reference to the canonical payload source.

```yaml
ref:
  uri: ./knowledge/example.okf.md
```

When present, the referenced resource SHOULD be treated as the authoritative source.

---

#### 3.6.4 cache

Snapshot copy of externally referenced content.

```yaml
cache:
  body: ...
  captured_at: ...
  source_hash: ...
```

Purpose:

- reproducibility
- offline processing
- auditability
- snapshot preservation

---

### 3.7 Canonical Resolution Rules

When multiple payload representations are present:

1. ref is canonical.
2. cache is a captured snapshot.
3. body is an embedded representation.

Implementations MAY optimize locally but SHOULD preserve traceability.

---

### 3.8 Perspective Scope

```yaml
perspective_scope:
  - perspective_ref
```

Perspective scope records the interpretive conditions under which the entity boundary was stabilized.

It is:

- not a semantic restriction
- not the only valid interpretation

It is extraction provenance.

---

### 3.9 Entity Identity and Payload Identity

Entity identity is independent from payload identity.

Therefore:

- identical payloads MAY produce different entities
- different payloads MAY represent equivalent entities

Entity identity is determined by:

- interpretation boundary
- perspective conditions
- intended reuse

not by payload location.

---

### 3.10 Entity Granularity Trade-off

| Granularity | Effect |
|------------|--------|
| Fine | higher recomposability |
| Coarse | higher semantic cohesion |

IdeaMark does not enforce a fixed granularity.

---

### 3.11 Entity and Meaning Emergence

Meaning emerges through the interaction of:

- Entity
- Occurrence
- Section
- Perspective
- Relations

Entity alone is only a potential carrier of meaning.

---

### 3.12 Summary Statement

> Entity defines a reusable meaning boundary while remaining independent from the representation format of the underlying knowledge payload.
