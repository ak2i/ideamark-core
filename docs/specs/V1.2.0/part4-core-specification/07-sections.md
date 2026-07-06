# 7. Sections

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 7.1 Purpose

A Section represents a Projection-shaped local source window.

A Section is the primary local coordinate frame in which Occurrences are ordered and interpreted for reconstruction.

A Section is not necessarily:

- an Original Source heading;
- a source chapter;
- a topic;
- a semantic unit;
- a summary unit;
- a final meaning container.

## 7.2 Required Shape

`sections` MUST be an array.

Each item in `sections` MUST be a mapping object.

Each Section object MUST contain an `id` field.

Example:

```yaml
sections:
  - id: sec-001
    title: Example local source window
    occurrences:
      - occ-001
      - occ-002
```

## 7.3 Required Fields

| Field | Type | Requirement |
| --- | --- | --- |
| `id` | string | MUST |

A validator MUST reject a Section whose `id` is missing, null, empty, or non-string.

A validator MUST reject duplicate Section IDs within `sections`.

## 7.4 Recommended Fields

| Field | Type | Meaning |
| --- | --- | --- |
| `title` | string | Human-readable section title or label |
| `description` | string | Human-readable explanation |
| `anchors` | array | Source anchors for the local source window |
| `occurrences` | array | Ordered Occurrence references |
| `status` | string | Section lifecycle state |
| `note` / `notes` | string or array | Human-readable notes |

A Section SHOULD include `occurrences` unless it is a placeholder, draft fragment, or template section.

A Section SHOULD include `anchors` when it represents a known source window.

## 7.5 Occurrence Ordering

`sections[].occurrences` defines the ordered Occurrence sequence within a Section.

Example:

```yaml
sections:
  - id: sec-001
    occurrences:
      - occ-001
      - occ-002
      - occ-003
```

The order of IDs in this array SHOULD be treated as the primary reconstruction order for that Section.

Array order in the top-level `occurrences` namespace MAY be authoring order, but Section-level occurrence order is more specific for reconstruction.

A validator MUST reject unresolved Occurrence references in `sections[].occurrences`.

## 7.6 Empty Occurrence Lists

A Section MAY have an empty `occurrences` array during drafting, template authoring, partial generation, or staged authoring.

Example:

```yaml
sections:
  - id: sec-placeholder
    title: Placeholder Section
    occurrences: []
```

Core mode validators SHOULD accept empty occurrence lists.

Validators MAY warn when a non-placeholder Section has no Occurrences.

Strict mode or profiles MAY require non-empty occurrence lists.

## 7.7 Section Anchors

A Section SHOULD use `anchors` when the Section corresponds to one or more source regions.

Example:

```yaml
sections:
  - id: sec-001
    anchors:
      - source: src-001
        type: line_range
        ranges:
          - start: 10
            end: 25
        precision: exact
    occurrences:
      - occ-001
```

Section anchors identify the local source window used by that Section.

A Section may have multiple anchors when it is constructed from multiple source regions.

## 7.8 Section Without Source Anchor

A Section MAY omit anchors.

This is valid for:

- authored documents without external sources;
- synthetic or planning documents;
- early drafts;
- template sections;
- sections whose source traceability is intentionally omitted;
- sections that organize already extracted Occurrences.

Profiles MAY require Section anchors for traceable extraction documents.

## 7.9 Section Status

A Section MAY include `status`.

Recommended Section status values are:

- `active`
- `draft`
- `provisional`
- `deprecated`
- `superseded`
- `rejected`

Core mode validators SHOULD warn on unknown status values.

Strict mode MAY reject unknown status values unless declared by a profile.

## 7.10 Section Identity and Stability

A Section ID SHOULD remain stable while the local source window or structural role remains substantially the same.

Editing Section title, notes, order, or Occurrence membership SHOULD NOT automatically require changing the Section ID.

A Section ID MAY change when:

- the Section is split;
- multiple Sections are merged;
- its source window is substantially redefined;
- a migration tool cannot preserve identity safely.

## 7.11 Sections and Source Headings

A Section MAY correspond to a source heading, but this is not required.

A Section may be:

- smaller than a source heading;
- larger than a source heading;
- composed from multiple non-contiguous source regions;
- shaped by a Projection rather than by source document structure;
- created without a direct source heading.

Tools MUST NOT assume that Section title equals source heading.

## 7.12 Sections and Meaning

A Section provides a local coordinate frame.

It does not itself guarantee a final interpretation.

Meaning is reconstructed from the relationship among:

- the Section's source anchors;
- its ordered Occurrences;
- the referenced Entities;
- Projection context recorded in metadata;
- optional profile or extension data.

## 7.13 Cross-section Reuse

The same Entity MAY appear through multiple Occurrences in different Sections.

A Section MUST reference Occurrences, not Entities directly, when it needs role-bearing placement.

This preserves the distinction:

```text
Entity = reusable material
Occurrence = role-bearing placement
Section = local coordinate frame
```

## 7.14 Section Extension Fields

Sections MAY include extension fields.

Example:

```yaml
sections:
  - id: sec-001
    title: Example Section
    occurrences:
      - occ-001
    x-example-org:
      review_priority: high
```

Core mode validators SHOULD preserve extension fields.

Strict mode MAY reject undeclared extension fields.

## 7.15 Validation Requirements

A Core validator MUST check:

- `sections` exists;
- `sections` is an array;
- every Section is a mapping object;
- every Section has a valid `id`;
- Section IDs are unique within `sections`;
- if `occurrences` exists, it is an array;
- every reference in `sections[].occurrences` resolves to an existing Occurrence ID;
- if `anchors` exists, it satisfies common anchor requirements.

A Core validator SHOULD warn when:

- a Section has no title, description, anchors, or Occurrences;
- a non-placeholder Section has an empty Occurrence list;
- a Section references the same Occurrence more than once;
- a Section has unknown status;
- extension fields are undeclared.

Strict mode MAY promote warnings to errors.
