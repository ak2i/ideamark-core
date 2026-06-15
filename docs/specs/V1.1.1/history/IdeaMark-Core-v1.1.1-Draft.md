# IdeaMark Core Specification v1.1.1 (Draft)

## Purpose of v1.1.1

This version refines the Entity model to support payload-agnostic knowledge representation and external knowledge formats such as OKF, TPCG, Markdown, JSON, YAML, and future formats.

Core principle:

> Entity defines meaning-boundary metadata.
> Payload provides representational material.

---

## 1. Entity Payload Model

### 1.1 Design Goal

IdeaMark Core SHALL NOT depend on a specific content representation.

Entities MAY carry:

- embedded content
- referenced content
- cached snapshots

The meaning structure remains independent from payload format.

---

### 1.2 Payload Schema

```yaml
entities:
  IE-001:
    kind: claim

    payload:
      format:
        media_type: text/markdown
        profile: GCP-knowledge-catalog-okf
        version: "1.0"
        definition_ref: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md

      body: |
        Example embedded content.

      ref:
        uri: ./knowledge/example.okf.md

      cache:
        body: |
          Snapshot copy.
        captured_at: 2026-06-16T00:00:00+09:00
        source_hash: sha256:example
```

---

## 2. Payload Components

### 2.1 format

Describes the representation format.

```yaml
format:
  media_type: text/markdown
  profile: GCP-knowledge-catalog-okf
  version: "1.0"
  definition_ref: https://...
```

#### media_type

Identifies the syntactic container.

Examples:

- text/plain
- text/markdown
- application/json
- application/yaml

#### profile

Identifies the semantic document format.

Examples:

- GCP-knowledge-catalog-okf
- tpcg
- ideamark
- profit-model-catalog

Profile vocabularies are intentionally open.

#### version

Optional format version.

#### definition_ref

Reference to the defining specification.

The referenced resource MAY be:

- specification document
- RFC
- Git repository document
- schema repository
- standards document

---

### 2.2 body

Embedded payload content.

Used when:

- fully self-contained documents are desired
- LLM context expansion is needed
- snapshot portability is required

---

### 2.3 ref

Reference to the canonical payload source.

```yaml
ref:
  uri: ./knowledge/example.okf.md
```

The referenced resource SHOULD be treated as the authoritative source when present.

---

### 2.4 cache

Snapshot copy of externally referenced content.

```yaml
cache:
  body: ...
  captured_at: ...
  source_hash: ...
```

Purpose:

- offline processing
- reproducibility
- auditability
- snapshot preservation

---

## 3. Canonical Resolution Rules

When multiple payload representations are present:

1. ref is the canonical source.
2. cache is a captured snapshot.
3. body is an embedded representation.

Implementations MAY choose local optimization strategies, but SHOULD preserve traceability.

---

## 4. Entity Identity Clarification

Entity identity is independent of payload identity.

Therefore:

- identical payloads MAY correspond to different entities
- different payloads MAY correspond to equivalent entities

Entity boundaries are determined by:

- Perspective
- Extraction policy (POR)
- Intended reuse

not by payload location.

---

## 5. Core Positioning Update

IdeaMark Core is redefined as:

> A payload-agnostic meaning-structure framework.

IdeaMark does not standardize the knowledge representation itself.

Instead, it standardizes:

- Entity
- Occurrence
- Section
- Perspective
- Relations

through which knowledge representations can be organized, interpreted, retrieved, and recomposed.

---

## 6. Compatibility

### Backward Compatibility

Previous:

```yaml
content: "..."
```

Recommended migration:

```yaml
payload:
  format:
    media_type: text/plain
  body: "..."
```

### Forward Compatibility

Unknown payload profiles MUST NOT invalidate a document.

Implementations SHOULD ignore unsupported profile-specific details while preserving payload metadata.

---

## Summary

v1.1.1 introduces:

- content → payload transition
- payload body / ref / cache model
- profile-based format identification
- definition_ref for specification traceability
- payload-agnostic Core positioning

This change strengthens IdeaMark's role as a reusable knowledge-structure layer capable of organizing heterogeneous knowledge representations.
