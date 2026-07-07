# 20. Skeleton Graph YAML Extension

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 20.1 Purpose

This chapter defines a recommended YAML representation for optional **Skeleton Graphs** in IdeaMark Core v1.2.0 documents.

Skeleton Graphs support retrieval-oriented structural matching before full reconstruction.

They are optional Core-adjacent structures. They do not replace the required namespaces `meta`, `sources`, `sections`, `occurrences`, and `entities`.

## 20.2 Top-level Namespace

An IdeaMark document MAY include a top-level `skeletons` namespace.

```yaml
skeletons:
  - id: skel-001
    role: retrieval
    projection: projection://example-projection/v1
    nodes: []
    links: []
```

When present, `skeletons` SHOULD be an array of Skeleton Graph objects.

Core mode validators SHOULD preserve `skeletons` during round-trip formatting.

Core mode validators MAY warn when the namespace is present but malformed.

Strict profile mode MAY require or reject `skeletons` according to profile rules.

## 20.3 Skeleton Graph Object

A Skeleton Graph object SHOULD use the following shape:

```yaml
skeletons:
  - id: skel-001
    role: retrieval
    projection: projection://example-projection/v1
    status: draft
    nodes:
      - id: skn-001
        ref:
          kind: section
          id: SEC-001
        slot: preserved_effect_or_function
    links:
      - id: skl-001
        from: skn-001
        to: skn-002
        type: constraint
```

### Fields

- `id` — graph identifier; SHOULD be unique within the document.
- `role` — graph purpose, such as `retrieval`, `generation_trace`, `compatibility`, `review`, or profile-defined values.
- `projection` — optional Projection reference that shaped or is expected to consume the graph.
- `status` — optional lifecycle state such as `draft`, `review`, `accepted`, or profile-defined values.
- `nodes` — array of Skeleton Node objects.
- `links` — array of Skeleton Link objects.
- `notes` — optional human-readable note.
- extension fields — allowed and SHOULD be preserved.

## 20.4 Skeleton Node Object

A Skeleton Node object SHOULD use the following shape:

```yaml
nodes:
  - id: skn-001
    ref:
      kind: section
      id: SEC-dashi-function
    slot: preserved_effect_or_function
    required: true
    status: accepted
```

### Fields

- `id` — node identifier; SHOULD be unique within the Skeleton Graph.
- `ref` — optional reference to an IdeaMark object.
- `slot` — optional domain-reduced activity slot label.
- `required` — optional boolean indicating whether a matching graph should contain this slot.
- `status` — optional node review state.
- `notes` — optional human-readable note.

### `ref` Shape

```yaml
ref:
  kind: section | occurrence | entity | source | anchor | extension
  id: <object-id>
```

`kind` MAY use profile-defined values.

`id` SHOULD refer to an object in the same document unless the profile allows external graph references.

## 20.5 Skeleton Link Object

A Skeleton Link object SHOULD use the following shape:

```yaml
links:
  - id: skl-001
    from: skn-001
    to: skn-002
    type: constraint
    required: true
```

### Fields

- `id` — link identifier; SHOULD be unique within the Skeleton Graph.
- `from` — source Skeleton Node ID.
- `to` — target Skeleton Node ID.
- `type` — Skeleton Link type.
- `required` — optional boolean indicating whether a matching graph should contain this link.
- `weight` — optional numeric hint for matching or ranking.
- `notes` — optional human-readable note.

## 20.6 Recommended Skeleton Link Types

Core recommends but does not close the following link vocabulary:

| Type | Description |
|---|---|
| `sequence` | Nodes participate in an ordered composition. |
| `dependency` | One node is needed to use or evaluate another. |
| `constraint` | One node limits, bounds, or conditions another. |
| `alternative` | Nodes represent selectable or substitutable options. |
| `parallel` | Nodes coexist without required order. |
| `conflict` | Nodes are incompatible or mutually blocking in the activity structure. |
| `aggregation` | Nodes combine into a larger activity unit. |
| `specialization` | One node narrows or instantiates another. |
| `confirmation` | One node supplies a check, signal, or review point for another. |

Unknown link types MUST NOT cause Core-mode validation failure.

Profiles MAY define closed vocabularies.

## 20.7 Example: Recipe Substitution

```yaml
skeletons:
  - id: skel-recipe-substitution-001
    role: retrieval
    projection: projection://recipe-ingredient-function-substitution-v0
    nodes:
      - id: skn-blocked-element
        ref:
          kind: occurrence
          id: OCC-bonito-function
        slot: unavailable_or_blocked_element
      - id: skn-preserved-function
        ref:
          kind: occurrence
          id: OCC-dashi-substitution-target
        slot: preserved_effect_or_function
      - id: skn-alternative-space
        ref:
          kind: section
          id: SEC-dashi-function
        slot: alternative_space
      - id: skn-confirmation
        slot: confirmation_signal
        status: underspecified
    links:
      - id: skl-001
        from: skn-blocked-element
        to: skn-preserved-function
        type: constraint
      - id: skl-002
        from: skn-preserved-function
        to: skn-alternative-space
        type: dependency
      - id: skl-003
        from: skn-alternative-space
        to: skn-confirmation
        type: confirmation
```

This graph does not state that bonito flakes semantically cause dashi.

It states that the matched material participates in an activity pattern for finding alternatives while preserving a function or effect.

## 20.8 Example: Heapq Performance

```yaml
skeletons:
  - id: skel-heapq-performance-001
    role: retrieval
    projection: projection://code-design-performance-heapq-v0
    nodes:
      - id: skn-boundary
        ref:
          kind: occurrence
          id: OCC-001
        slot: preserved_invariant_or_boundary
      - id: skn-design-choice
        ref:
          kind: occurrence
          id: OCC-002
        slot: chosen_operational_form
      - id: skn-restoration
        ref:
          kind: occurrence
          id: OCC-003
        slot: restoration_or_recovery_strategy
    links:
      - id: skl-001
        from: skn-boundary
        to: skn-design-choice
        type: constraint
      - id: skl-002
        from: skn-design-choice
        to: skn-restoration
        type: dependency
```

This allows a use-side Projection to retrieve implementation material that explains how a design choice preserves a constraint or invariant without searching for the exact source terms.

## 20.9 Validation Guidance

Core-mode validators SHOULD check only basic shape when implemented:

- `skeletons` is an array when present;
- each Skeleton Graph has an `id` when possible;
- `nodes` and `links` are arrays when present;
- `links[].from` and `links[].to` refer to node IDs within the same Skeleton Graph when enough information is available.

Core-mode validators SHOULD warn, not fail, for unknown slots, roles, statuses, or link types.

Strict profile validators MAY add stronger rules.

## 20.10 Compatibility

The `skeletons` namespace is additive.

Older v1.2.0 Core documents without `skeletons` remain valid.

Tools that do not understand `skeletons` SHOULD preserve it as an unknown top-level namespace according to extension preservation rules.

Tools that do understand `skeletons` may use it for retrieval-oriented indexing, graph pattern matching, compatibility explanation, and reconstruction candidate selection.
