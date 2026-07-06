# 07 — Occurrence Model

**Part:** 3 — Core Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 7.1 Purpose

This section defines the conceptual role of Occurrence in the IdeaMark Core Model.

An Occurrence connects reusable Entity material to a Section under a role.

It explains how material participates in a Projection-shaped local source window.

An Occurrence is not merely a textual occurrence, source appearance, event, instance, or observation.

## 7.2 Definition

An Occurrence is a role-bearing placement of reusable material within a Section.

It is produced by Projection-guided Decomposition.

Conceptually, an Occurrence may include or reference:

- a local identifier;
- an Entity reference;
- a Section context;
- a role;
- local rationale;
- source anchors;
- ordering information;
- status or review notes;
- extension metadata.

Part 4 defines concrete YAML representation.

## 7.3 Occurrence as Placement

Occurrence should be understood as placement rather than mere appearance.

An Entity-like material may be present in the Original Source, but it becomes useful in an IdeaMark document when Decomposition places it into a Section with a role.

For example, the same recipe fragment involving miso paste may be placed as:

- a heat-control rule under a Cooking Execution Projection;
- a seasoning function under an Ingredient Function Projection;
- a soy-based dietary constraint under a Dietary Constraint Projection.

The source fragment may be similar, but the Occurrence is different because the role and Section context are different.

## 7.4 Occurrence and Section

An Occurrence belongs to or is interpreted within a Section.

The Section provides the Projection-shaped local source window that makes the Occurrence role meaningful.

Without Section context, an Occurrence may lose its reconstruction purpose.

For example:

```text
Entity material: remove kombu before boiling
```

In a Cooking Execution Section, this may occur as a timing constraint.

In a Beginner Teaching Section, it may occur as a mistake-prevention explanation.

In an Ingredient Function Section, it may be less central or omitted.

The Occurrence role is meaningful only within the local source window.

## 7.5 Occurrence and Entity

An Occurrence references or uses Entity material.

The Entity provides reusable material.

The Occurrence provides situated role and placement.

This separation allows the same material to participate in different Sections or Projections without requiring universal Entity identity.

For example, an Entity such as:

```text
miso paste provides saltiness, fermented aroma, and body
```

may be placed as:

- a substitution constraint;
- a dietary caution;
- a teaching concept;
- a shopping-list item context.

Each placement may be a different Occurrence.

## 7.6 Occurrence and Projection

Projection determines which placements are useful.

A role that is meaningful under one Projection may be irrelevant under another.

For example:

- in a performance-engineering Projection, an Occurrence may play the role `supports_design_choice`;
- in an API-design Projection, similar material may play the role `frames_api_contract`;
- in a migration-impact Projection, it may play the role `identifies_breaking_behavior`;
- in a cooking-execution Projection, it may play the role `prevents_execution_error`.

Core does not define a universal role vocabulary.

Roles are shaped by Projection, profile, domain practice, or implementation convention.

## 7.7 Occurrence Role

The role of an Occurrence describes how Entity material participates in the Section.

The role should support reconstruction.

It may indicate that the Entity material functions as:

- evidence;
- constraint;
- rationale;
- step;
- caution;
- example;
- definition;
- state;
- transition;
- ingredient function;
- teaching concept;
- migration impact;
- review target;
- another Projection-defined placement type.

Part 3 does not prescribe role names.

A profile or Projection library may define role vocabularies.

## 7.8 Required Role Semantics

Even if Core does not define a universal vocabulary, an Occurrence role should be meaningful enough for later reconstruction.

A weak role such as `related` may be insufficient unless the Section, Entity, or rationale clarifies how it is related.

A useful role helps a later user or tool answer:

```text
How does this Entity material participate in this Section under this Projection?
```

## 7.9 Occurrence and Source Anchor

An Occurrence may have a source anchor.

Occurrence-level anchors are useful when the placement depends on a specific source fragment.

However, Section-level anchors are often sufficient because the Section is the local source window.

Core should allow anchors at multiple levels:

- Section-level anchors for local source windows;
- Occurrence-level anchors for precise placements;
- Entity-level anchors for reusable material origins;
- metadata-level anchors for document-level traceability.

A lack of Occurrence-level anchor does not necessarily invalidate an Occurrence if the Section provides sufficient traceability.

## 7.10 Occurrence and Local Rationale

An Occurrence may include local rationale.

Local rationale may explain:

- why the Entity material was placed in the Section;
- why the role was assigned;
- how the placement supports future reconstruction;
- why the placement is inferred rather than directly sourced;
- how the placement relates to the Projection Context;
- why similar material was omitted or placed elsewhere.

Local rationale is optional unless required by a profile.

It can improve review, debugging, and reuse.

## 7.11 Occurrence and Inference

An Occurrence may be directly sourced or inferred.

For example:

- a code comment directly states an implementation rationale;
- a recipe step directly states an execution order;
- a state diagram directly shows a transition;
- an ingredient function may be inferred from culinary knowledge and the recipe context;
- a migration impact may be inferred from a syntax change and example.

Inferred Occurrences should preserve traceability and, where useful, local rationale.

Core does not prohibit inference.

However, inferred placements should not be presented as final meaning independent of Original Source and Projection.

## 7.12 Occurrence and Ordering

Occurrences may be ordered within a Section.

Ordering may be useful when:

- steps must be executed in sequence;
- reasoning builds from definition to evidence;
- state transitions must be followed;
- teaching material has a progression;
- reconstruction requires a stable ordering.

Occurrence order does not have to match source order.

It may be Projection-shaped.

Part 4 may define how ordering is represented.

## 7.13 Occurrence Identity

An Occurrence should have an identifier within the IdeaMark document.

Core does not require Occurrence identity to be globally stable across documents, repositories, or regenerations.

An Occurrence ID is primarily a reference label.

Regeneration may preserve, change, split, merge, or remove Occurrence IDs.

Profiles or implementations may define stronger identity rules.

## 7.14 Occurrence Granularity

Occurrence granularity is Projection-dependent.

An Occurrence should be specific enough to make the role useful, but not so small that local context is lost.

For example:

- a performance-engineering Section may have separate Occurrences for cost driver, implementation rationale, and empirical support;
- a recipe execution Section may have separate Occurrences for step, timing constraint, and heat-control rule;
- an RFC migration Section may have separate Occurrences for breaking behavior, migration mechanism, and impact evidence.

Core does not define universal Occurrence granularity.

Projection libraries, profiles, or implementations may define guidance.

## 7.15 Occurrence Completeness

An Occurrence is not required to capture every possible role of an Entity or source fragment.

It only records a useful placement under a Projection.

Other Projections may create different Occurrences from the same source material.

A document may be valid even if it contains only a subset of possible Occurrences.

Completeness should be interpreted relative to Projection and document status.

## 7.16 Multi-source Occurrences

An Occurrence may depend on multiple source fragments or multiple sources.

For example:

- an implementation rationale may depend on a code block and a comment;
- a design claim may depend on a motivation paragraph and a statistics table;
- a recipe substitution rule may depend on both ingredient list and cooking step;
- a research conclusion may depend on multiple data records.

A multi-source Occurrence should preserve enough anchor information to support later review and reconstruction.

## 7.17 Weak or Invalid Occurrences

An Occurrence may be weak if it:

- has no role;
- references no Entity material;
- has no Section context;
- cannot be traced directly or indirectly to Original Source material;
- stores final interpretation without reconstruction context;
- uses vague placement labels that do not support future use;
- cannot be reviewed or interpreted under the document's Projection Context.

Part 4 or profiles may define validation levels.

Part 3 identifies these conceptual risks.

## 7.18 Conceptual Example

The following shape is illustrative:

```yaml
occurrences:
  OCC-004:
    entity: IE-004
    role: explains_non_textbook_choice
    rationale: |
      This placement records why the implementation avoids an apparent early-exit optimization under the performance-engineering Projection.
    source_anchor:
      source: SRC-heapq-py
      line_ranges:
        - start: 63
          end: 75
```

This example is not normative YAML.

Part 4 defines concrete syntax.

## 7.19 Invariants

An Occurrence should preserve the following invariants:

1. An Occurrence is produced by Projection-guided Decomposition.
2. An Occurrence is a role-bearing placement of Entity material within a Section.
3. An Occurrence is not merely a textual occurrence or source appearance.
4. An Occurrence role is meaningful relative to Section and Projection Context.
5. Core does not define a universal role vocabulary.
6. An Occurrence may be directly sourced or inferred.
7. Occurrence ordering may be Projection-shaped and need not match source order.
8. Occurrence identity is local unless a profile defines stronger identity rules.
9. An Occurrence does not store final meaning.
10. An Occurrence should support later reconstruction or review.

## 7.20 Summary

Occurrence is the Core Model's placement object.

It explains how reusable Entity material participates in a Projection-shaped Section.

A good Occurrence gives later humans, AI systems, or tools enough role information to understand why the material matters in that local source window and how it may support reconstruction.
