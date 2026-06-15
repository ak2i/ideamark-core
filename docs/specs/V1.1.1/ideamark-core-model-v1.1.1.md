# IdeaMark Core Model v1.1.1 (Revised)

## 3. Entity

### 3.1 Positioning

Entity is the fundamental unit of reusable meaning-boundary anchoring in IdeaMark.

Entity does not own meaning itself.

Meaning is not preserved inside an Entity.

Instead:

> Entity defines the boundary of a reusable trace of meaning-making.

Entity represents a stabilized extraction from prior intellectual activity.

Entity is independent from the representation format of the knowledge it references.

---

### 3.2 Redefinition of Atomicity

Entity remains the minimal reusable unit under a given interpretive intention.

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

### 3.5 Entity Schema

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
        selector: string

      cache:
        body: string
        captured_at: datetime
        source_hash: string

    atomicity_basis: interpretive | lexical | structural
    perspective_scope: [perspective_ref, ...]
```

---

### 3.6 Entity Identity

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

## 4. Occurrence

### 4.1 Positioning

Occurrence is the activation of an Entity within a specific intellectual activity.

Occurrence does not merely record appearance.

Instead:

> Occurrence records how an Entity functioned within a meaning-making process.

Examples:

- claim
- evidence
- observation
- assumption
- constraint
- objective

The same Entity MAY participate in multiple Occurrences with different roles.

---

### 4.2 Occurrence as Reuse Trace

Entity represents a reusable boundary.

Occurrence represents a contextualized use of that boundary.

Therefore:

> Occurrence is a trace of knowledge use, not merely a reference to an Entity.

---

## 5. Section

### 5.1 Positioning

Section groups Occurrences into an interpretable unit.

A Section represents a local interpretive context.

Sections provide the structure through which readers perform new projections.

---

## 6. Perspective Scope

### 6.1 Positioning

Perspective is not meaning itself.

Perspective records reusable clues regarding interpretive direction.

Perspective is therefore understood as:

> A trace of projection.

---

### 6.2 Perspective Scope

```yaml
perspective_scope:
  - perspective_ref
```

Perspective scope records the projection traces used when stabilizing an Entity boundary.

It is:

- not a semantic restriction
- not the only valid interpretation
- not a guarantee of future meaning

It is extraction provenance.

---

## 7. Meaning Emergence

Meaning emerges through the interaction of:

- Entity
- Occurrence
- Section
- Perspective
- Relations

Entity alone is only a potential carrier of reusable structure.

Meaning is generated when an interpreter performs projection.

---

## 8. Summary Statement

> IdeaMark organizes reusable traces of intellectual activity rather than preserving meaning itself.

> Entity defines reusable boundaries.
> Occurrence records contextual use.
> Perspective preserves projection traces.
> Meaning emerges through future interpretation.
