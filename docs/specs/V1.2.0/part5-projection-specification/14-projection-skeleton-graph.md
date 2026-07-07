# 14. Projection Skeleton Graph

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 14.1 Purpose

This chapter defines how a Projection may use an **Intellectual Activity Skeleton Graph** to guide retrieval, matching, filtering, and reconstruction.

A Projection Skeleton Graph describes the activity-composition pattern that a use-side Projection expects candidate IdeaMark documents or Sections to satisfy.

It is not a prompt template, keyword list, domain taxonomy, ranking algorithm, or database schema.

## 14.2 Projection-side Skeleton Role

A Projection may use Skeleton Graphs in three roles:

1. **Decomposition guidance** — suggest which activity slots and links should be extracted from an Original Source.
2. **Retrieval requirement** — describe the graph pattern needed to find candidate IdeaMark structures.
3. **Reconstruction guidance** — describe which matched slots should be revisited and re-expressed for the future Situation.

The same Projection may define multiple Skeleton Graphs for different reconstruction targets, risk levels, audiences, or capability assumptions.

## 14.3 Required Skeleton

A Projection MAY define a `required_skeleton`.

Example:

```yaml
required_skeleton:
  id: req-skel-function-preserving-alternative
  nodes:
    - id: qn-blocked-element
      slot: unavailable_or_blocked_element
      required: true
    - id: qn-preserved-function
      slot: preserved_effect_or_function
      required: true
    - id: qn-alternative-space
      slot: alternative_space
      required: true
    - id: qn-confirmation
      slot: confirmation_signal
      required: false
  links:
    - id: ql-001
      from: qn-blocked-element
      to: qn-preserved-function
      type: constraint
      required: true
    - id: ql-002
      from: qn-preserved-function
      to: qn-alternative-space
      type: dependency
      required: true
    - id: ql-003
      from: qn-alternative-space
      to: qn-confirmation
      type: confirmation
      required: false
```

This graph does not say which domain objects must appear.

It says which domain-reduced activity slots and compositional links are needed for the Projection's intended reuse.

## 14.4 Optional and Excluded Skeletons

A Projection MAY also define:

- `preferred_skeletons` — graph patterns that increase match quality;
- `optional_skeletons` — graph patterns that may be useful but are not required;
- `excluded_skeletons` — graph patterns that should be filtered out or require warning;
- `unsafe_skeletons` — graph patterns that look superficially similar but should not be reconstructed without review.

Example:

```yaml
excluded_skeletons:
  - id: excluded-direct-substitution-without-confirmation
    nodes:
      - id: qn-alternative-space
        slot: alternative_space
      - id: qn-confirmation
        slot: confirmation_signal
    links:
      - from: qn-alternative-space
        to: qn-confirmation
        type: confirmation
        required: false
    rule: missing_confirmation_signal_requires_warning
```

## 14.5 Domain Boundary

Projection Skeleton Graphs SHOULD avoid universal domain labels as primary matching keys.

Domain may still appear in Projection notes, source scope, allowed sources, risk constraints, or reconstruction context.

A Projection may describe domain removal and domain reattachment explicitly:

```yaml
domain_handling:
  decomposition: remove domain-specific surface vocabulary when forming skeleton slots
  retrieval: match on skeleton slots and links before domain-specific terms
  reconstruction: reattach target Situation and domain context during expression generation
```

This makes Domain useful as explanatory context without turning Core retrieval into a universal domain dictionary problem.

## 14.6 Matching Expectations

A Projection SHOULD state whether its Skeleton Graph expectations are:

- exact;
- partial;
- approximate;
- analogical;
- review-required;
- unsafe if incomplete.

Example:

```yaml
matching:
  skeleton_match: partial_allowed
  required_slots:
    - unavailable_or_blocked_element
    - preserved_effect_or_function
    - alternative_space
  review_required_if_missing:
    - confirmation_signal
  analogical_transfer: allowed_with_warning
```

## 14.7 Retrieval Explanation

When practical, systems using Projection Skeleton Graphs SHOULD explain retrieval results in terms of matched and missing slots or links.

Example explanation:

```text
Matched candidate because it contains a blocked-element slot, a preserved-function slot, and an alternative-space slot linked by constraint and dependency links. Confirmation signal is missing, so reconstruction should include a warning or review step.
```

This keeps retrieval explanation tied to the activity composition rather than opaque keyword scores.

## 14.8 Relationship to IdeaMark `skeletons`

Part 4 defines the optional `skeletons` namespace for IdeaMark documents.

Projection-side Skeleton Graphs and document-side Skeleton Graphs use compatible concepts:

```text
Projection required_skeleton
        ↓ graph pattern matching
IdeaMark document skeletons
        ↓ candidate Sections / Occurrences / Entities / anchors
Projection-guided Reconstruction
```

Projection specifications are responsible for declaring which graph patterns matter.

IdeaMark documents are responsible for preserving graph-shaped access structures when such preservation improves retrieval.

## 14.9 Non-goals

Projection Skeleton Graphs do not define:

- a universal ontology of intellectual activity;
- a universal domain taxonomy;
- a mandatory graph database;
- a ranking algorithm;
- a vector embedding strategy;
- an exhaustive workflow language;
- a replacement for Sections, Occurrences, Entities, or source anchors.

They define a reusable structural interface between Projection-guided retrieval and Projection-guided reconstruction.
