# 10. Structure and Ordering

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 10.1 Purpose

`structure` is an optional namespace for explicit document-level ordering, grouping, and reconstruction hints.

It exists because array order alone is useful for authoring but should not be the only way to express reconstruction order when ordering matters.

`structure` does not define final meaning.

`structure` does not replace Sections, Occurrences, or Entities.

## 10.2 Optional Namespace

`structure` is OPTIONAL in Core v1.2.0.

A document without `structure` MAY still be valid.

When `structure` is absent, tools MAY use the order of `sections[]` as authoring order.

When `structure.sections` is present, it SHOULD be treated as the explicit document-level Section order.

## 10.3 Recommended Shape

Example:

```yaml
structure:
  sections:
    - sec-001
    - sec-002
    - sec-003
```

`structure` SHOULD be a mapping.

`structure.sections` SHOULD be an array of Section IDs.

Each ID in `structure.sections` SHOULD resolve to an existing Section.

## 10.4 Section Ordering

`structure.sections` defines the recommended document-level Section sequence.

This sequence MAY differ from the physical array order of `sections[]`.

Formatters SHOULD NOT reorder `sections[]` solely to match `structure.sections` unless a canonical formatting mode is explicitly requested.

Validators SHOULD warn when `structure.sections` references missing Sections.

Validators SHOULD warn when a Section exists but is omitted from `structure.sections`, unless a profile declares partial ordering.

## 10.5 Occurrence Ordering

Occurrence order within a Section SHOULD be expressed by `sections[].occurrences`.

Example:

```yaml
sections:
  - id: sec-001
    occurrences:
      - occ-001
      - occ-002
```

`structure` SHOULD NOT duplicate all Section-local Occurrence ordering unless a profile requires an alternate reconstruction view.

## 10.6 Grouping

`structure` MAY include grouping metadata.

Example:

```yaml
structure:
  groups:
    - id: group-001
      title: Background sections
      sections:
        - sec-001
        - sec-002
```

Grouping semantics are profile-defined unless a later specification defines them.

Core validators SHOULD preserve grouping data.

Core validators SHOULD NOT require grouping data for Core reconstruction.

## 10.7 Alternate Views

Profiles MAY define alternate ordering or view structures.

Example:

```yaml
structure:
  views:
    - id: view-review
      title: Review order
      sections:
        - sec-003
        - sec-001
```

Core does not define semantics for alternate views beyond preserving the data and validating resolvable references when possible.

## 10.8 Ordering Boundary

`structure` provides ordering and grouping.

It MUST NOT be required to carry:

- Projection content;
- retrieval ranking;
- UI layout;
- workflow state;
- authoring engine scheduling;
- final interpretation logic.

Profiles MAY define UI-oriented structure, but that is outside minimum Core.

## 10.9 Validation Requirements

A Core validator SHOULD check, when `structure` is present:

- `structure` is a mapping;
- `structure.sections`, if present, is an array;
- each `structure.sections[]` item is a string;
- each `structure.sections[]` item resolves to an existing Section ID.

A Core validator SHOULD warn when:

- `structure.sections` omits existing Sections;
- `structure.sections` contains duplicate Section IDs;
- grouping references missing Sections;
- alternate view references are malformed.

Strict mode MAY promote warnings to errors.
