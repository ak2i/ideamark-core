# 15. Skeleton Family Library Boundary

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 15.1 Purpose

This chapter defines the boundary between IdeaMark Core, Projection, and **Skeleton Family**.

A Skeleton Family is a reusable family of Intellectual Activity Skeleton patterns.

It may group related Skeleton Graphs that share an activity-composition pattern across domains, Projections, or source types.

Skeleton Family is useful for retrieval scalability and Projection reuse, but it is not part of the required IdeaMark Core model.

## 15.2 Core Boundary

IdeaMark Core may define:

- optional document-side `skeletons`;
- Skeleton Graphs;
- Skeleton Nodes;
- Skeleton Links;
- references from Skeleton Nodes to Sections, Occurrences, Entities, anchors, or placeholders;
- preservation and validation expectations for document-side Skeleton Graph shape.

IdeaMark Core should not define:

- a closed catalog of Skeleton Families;
- universal Skeleton Family IDs;
- universal activity taxonomies;
- universal slot semantics;
- universal cross-domain analogy rules;
- governance rules for Projection or Skeleton Family libraries.

Core stores and exchanges graph-shaped access structures.

Core does not decide the global meaning, classification, or social value of those structures.

## 15.3 Skeleton Family Definition

A Skeleton Family is an external or Projection-side reusable pattern that describes a family of compatible or analogically related Skeleton Graphs.

Example family:

```yaml
skeleton_family:
  id: skeleton-family://preserve-required-effect-under-change/v0
  title: Preserve Required Effect Under Change
  purpose: >
    Support retrieval for activities where an element, design, measure, or
    current state is unavailable, constrained, risky, or problematic, while a
    required effect, invariant, boundary, or condition must be preserved.
  canonical_slots:
    - constrained_or_unavailable_element
    - preserved_effect_or_boundary
    - alternative_or_operational_form
    - confirmation_or_review_signal
  common_links:
    - type: constraint
    - type: dependency
    - type: confirmation
```

This family may include recipe substitution, invariant-constrained software design, crash-recovery planning, compatibility-preserving language design, disaster response intervention, or other domain-specific Projections.

The family is a reusable intellectual activity pattern, not a Core vocabulary.

## 15.4 Relationship to Projection Library

Skeleton Families may be managed in several ways:

1. inside a Projection Library;
2. in a separate Skeleton Family Library linked from Projection definitions;
3. in an organization-specific or domain-specific library;
4. as inline experimental notes during early Projection design.

The recommended long-term model is:

```text
Projection Library
  -> references Skeleton Family Library entries
  -> defines Projection-specific required_skeletons
  -> maps family slots to Projection-specific slots
  -> defines matching, filtering, reconstruction, and review policy
```

This allows many Projections to share one Skeleton Family while still retaining their own requirements.

## 15.5 Many-to-many Relationship

Projection and Skeleton Family have a many-to-many relationship.

One Projection may use multiple Skeleton Families.

Example:

```yaml
projection:
  id: projection://software-architecture-review/v0
  uses_skeleton_families:
    - skeleton-family://compatibility-preserving-change/v0
    - skeleton-family://invariant-constrained-design/v0
    - skeleton-family://failure-recovery/v0
    - skeleton-family://resource-allocation-under-constraint/v0
```

One Skeleton Family may be used by many Projections.

Example:

```yaml
skeleton_family:
  id: skeleton-family://compatibility-preserving-change/v0
  used_by:
    - projection://rust-rfc-design-rationale/v0
    - projection://python-pep-compatibility-review/v0
    - projection://api-migration-planning/v0
    - projection://database-schema-evolution/v0
```

Part 5 does not require either direction to be materialized in Core documents.

## 15.6 Projection-side Mapping

A Projection may map a Skeleton Family's canonical slots to its own Projection-specific slots.

Example:

```yaml
projection:
  id: projection://recipe-ingredient-function-substitution-v0
  uses_skeleton_families:
    - ref: skeleton-family://preserve-required-effect-under-change/v0
      slot_mapping:
        constrained_or_unavailable_element: unavailable_or_blocked_element
        preserved_effect_or_boundary: preserved_effect_or_function
        alternative_or_operational_form: alternative_space
        confirmation_or_review_signal: confirmation_signal
```

Another Projection may map the same family differently:

```yaml
projection:
  id: projection://system-correctness-state-machine-v0
  uses_skeleton_families:
    - ref: skeleton-family://preserve-required-effect-under-change/v0
      slot_mapping:
        constrained_or_unavailable_element: constrained_or_risky_element
        preserved_effect_or_boundary: preserved_invariant_or_boundary
        alternative_or_operational_form: chosen_operational_form
        confirmation_or_review_signal: confirmation_signal
```

This keeps Core free from universal slot semantics while still making cross-Projection retrieval possible.

## 15.7 Document-side Reference

An IdeaMark document MAY reference a Skeleton Family in metadata or Skeleton Graph fields when useful.

Example:

```yaml
skeletons:
  - id: SKEL-example
    role: retrieval
    family:
      ref: skeleton-family://preserve-required-effect-under-change/v0
      mapping_profile: projection-local
    nodes: []
    links: []
```

This reference is informative unless a profile makes it normative.

Core validators SHOULD preserve the reference.

Core validators SHOULD NOT require the referenced family to be known.

## 15.8 Retrieval Role

Skeleton Family can support retrieval scalability by narrowing the search space before graph matching.

Conceptual path:

```text
Use-side Situation or query
  -> select or infer Projection
  -> identify relevant Skeleton Families
  -> select required_skeleton patterns
  -> match document-side Skeleton Graphs
  -> return candidate Sections / Occurrences / Entities / anchors
  -> reconstruct or fail responsibly
```

Skeleton Family is therefore a retrieval index design asset.

It is not the retrieval algorithm itself.

## 15.9 Governance and Growth

Skeleton Families should be allowed to grow outside Core.

They may be:

- experimental;
- local to a project;
- private to an organization;
- shared in an open library;
- specialized for a domain;
- generalized across domains;
- versioned and deprecated over time.

A mature ecosystem may treat Skeleton Families as reusable intellectual activity assets.

However, Core should remain stable even as families evolve.

## 15.10 Non-goals

Skeleton Family definitions should not become:

- a universal ontology;
- a universal process language;
- a fixed taxonomy of all intellectual activity;
- a substitute for Projection design;
- a substitute for domain expertise;
- a replacement for source anchors;
- a guarantee that analogical transfer is safe.

They are external reusable patterns for organizing retrieval and Projection reuse.

## 15.11 Summary

Skeleton Graph is a Core-adjacent document structure.

Skeleton Family is an external reusable pattern asset.

Projection is the bridge between them.

```text
IdeaMark Core
  defines document-side Skeleton Graph shape

Skeleton Family Library
  defines reusable activity pattern families

Projection Library
  maps Skeleton Families to concrete Projection requirements

IdeaMark Document
  may record Skeleton Graphs and optional references to external families
```

This boundary allows IdeaMark Core to remain small while giving the ecosystem room to grow reusable intellectual activity patterns outside Core.
