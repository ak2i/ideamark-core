# 16. Normative Examples

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 16.1 Purpose

This chapter provides small normative examples for validator, formatter, migration, and authoring implementation.

Examples are intentionally minimal.

Profiles may define richer examples.

## 16.2 Minimal Valid Document

This is a minimal valid Core document in Core mode:

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example-minimal
  status: draft
sources: []
sections: []
occurrences: []
entities: []
```

A Core validator MUST accept this document shape.

A profile MAY reject it as incomplete.

## 16.3 One Source, Section, Occurrence, and Entity

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example-basic
  status: draft
sources:
  - id: src-001
    type: document
    title: Example Source
    uri: ./example-source.md
sections:
  - id: sec-001
    title: Example local source window
    anchors:
      - source: src-001
        type: line_range
        ranges:
          - start: 1
            end: 10
        precision: exact
    occurrences:
      - occ-001
occurrences:
  - id: occ-001
    entity: ent-001
    role: evidence
    status: active
entities:
  - id: ent-001
    kind: claim
    content: Example reusable material extracted from the source window.
```

This example demonstrates the primary reconstruction chain:

```text
Section -> Occurrence -> Entity
```

and the primary traceability chain:

```text
Section anchor -> Source
```

## 16.4 Multiple Sources

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example-multiple-sources
  status: draft
sources:
  - id: src-001
    type: document
    title: Source A
    uri: ./source-a.md
  - id: src-002
    type: web_page
    title: Source B
    uri: https://example.org/source-b
sections:
  - id: sec-001
    title: Multi-source comparison window
    anchors:
      - source: src-001
        type: line_range
        ranges:
          - start: 5
            end: 12
      - source: src-002
        type: heading_path
        path:
          - Background
    occurrences:
      - occ-001
      - occ-002
occurrences:
  - id: occ-001
    entity: ent-001
    role: evidence
  - id: occ-002
    entity: ent-002
    role: counterpoint
entities:
  - id: ent-001
    content: Reusable material from Source A.
  - id: ent-002
    content: Reusable material from Source B.
```

## 16.5 Projection References

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example-projection-reference
  status: generated
  projections:
    - role: generation
      ref: projection://example/source-extraction/v1
      version: v1
    - role: reconstruction_reference
      ref: projection://example/reconstruction/v1
sources: []
sections: []
occurrences: []
entities: []
```

Projection references are metadata.

They do not make Projection internals part of Core.

## 16.6 Structured Entity Payload

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example-payload
  status: draft
sources: []
sections:
  - id: sec-001
    occurrences:
      - occ-001
occurrences:
  - id: occ-001
    entity: ent-001
    role: observation
entities:
  - id: ent-001
    kind: structured_observation
    payload:
      metric: latency
      value: 120
      unit: ms
```

This example is valid because Entity reusable material may be carried by `payload` rather than `content`.

## 16.7 Extension Namespace

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example-extension
  status: draft
  profiles:
    - example.org/review-profile-v1
sources: []
sections: []
occurrences: []
entities:
  - id: ent-001
    content: Example reusable material.
    x-example-org:
      review_state: pending
extensions:
  example.org/review:
    reviewer_role: domain-specialist
```

Core mode validators SHOULD preserve extension data.

Strict mode MAY require the profile to be available.

## 16.8 Optional Structure

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example-structure
  status: draft
sources: []
sections:
  - id: sec-002
    occurrences: []
  - id: sec-001
    occurrences: []
occurrences: []
entities: []
structure:
  sections:
    - sec-001
    - sec-002
```

This example demonstrates that explicit structure order may differ from physical array order.

## 16.9 Invalid: Missing Required Namespace

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: invalid-missing-entities
  status: draft
sources: []
sections: []
occurrences: []
```

This is invalid because `entities` is missing.

## 16.10 Invalid: Unresolved Occurrence Entity Reference

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: invalid-unresolved-entity
  status: draft
sources: []
sections:
  - id: sec-001
    occurrences:
      - occ-001
occurrences:
  - id: occ-001
    entity: ent-missing
    role: evidence
entities: []
```

This is invalid because `occurrences[].entity` references a missing Entity.

## 16.11 Invalid: Duplicate Entity IDs

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: invalid-duplicate-entity
  status: draft
sources: []
sections: []
occurrences: []
entities:
  - id: ent-001
    content: First material.
  - id: ent-001
    content: Second material.
```

This is invalid because Entity IDs must be unique within `entities`.

## 16.12 Invalid: Anchor Missing Source

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: invalid-anchor-source
  status: draft
sources: []
sections:
  - id: sec-001
    anchors:
      - source: src-missing
        type: line_range
    occurrences: []
occurrences: []
entities: []
```

This is invalid because the anchor references a missing Source.
