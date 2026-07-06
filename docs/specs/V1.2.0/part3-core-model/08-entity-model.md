# 08 — Entity Model

**Part:** 3 — Core Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 8.1 Purpose

This section defines the conceptual role of Entity in the IdeaMark Core Model.

An Entity is reusable material shaped by Projection-guided Decomposition.

It is not a universal semantic object, ontology node, final meaning unit, or globally stable knowledge item by default.

Entity exists so that reusable material can be referenced, placed, reviewed, reused, and reconstructed through Occurrences and Sections.

## 8.2 Definition

An Entity is Projection-shaped reusable material.

It is produced by Projection-guided Decomposition and may be placed into Sections through Occurrences.

Conceptually, an Entity may include:

- a local identifier;
- kind or type label;
- content or payload;
- source role or source-derived description;
- source anchors;
- local rationale;
- status or review notes;
- extension metadata.

Part 4 defines concrete YAML representation.

## 8.3 Entity Is Not Final Meaning

An Entity must not be treated as final meaning.

It may contain explanatory text, labels, structured data, or source-derived material, but these are reusable materials for reconstruction.

They do not eliminate the need for Original Source material, Projection Context, Situation, interpretation, or later activation expression generation.

For example, an Entity such as:

```text
The implementation avoids early break in _siftup because comparison costs may dominate.
```

is useful material under a performance-engineering Projection.

It is not a universal final statement about all heap implementations.

## 8.4 Entity and Projection

Projection shapes what becomes an Entity.

The same source fragment may produce different Entities under different Projections.

For example:

- under a Cooking Execution Projection, miso paste may become part of a heat-control step;
- under an Ingredient Function Projection, miso paste may become a seasoning and body component;
- under a Dietary Constraint Projection, miso paste may become a soy-based or sodium-related constraint;
- under a Shopping Projection, miso paste may become a shopping item.

These Entities are not necessarily the same object.

They are Projection-shaped reusable materials.

## 8.5 Entity and Occurrence

Entities become useful in context through Occurrences.

An Occurrence places Entity material within a Section under a role.

The Entity provides reusable material.

The Occurrence provides situated placement.

The Section provides local source context.

```text
Section
  -> Occurrence
       -> Entity
```

An Entity may be referenced by multiple Occurrences when useful.

However, Core does not require Entity reuse across Occurrences, Sections, documents, or Projections.

## 8.6 Entity and Section

An Entity does not necessarily belong to only one Section.

It may be placed in multiple Sections through multiple Occurrences.

However, the meaning-like function of an Entity is not complete without Section and Occurrence context.

A standalone Entity may be searchable or reviewable, but reconstruction usually requires the local Section window and the Occurrence role.

## 8.7 Entity Kind

An Entity may have a kind or type label.

The kind helps later users and tools understand what kind of reusable material it is.

Possible kinds include:

- concept;
- rule;
- step;
- task;
- invariant;
- state;
- transition;
- evidence;
- rationale;
- example;
- ingredient;
- ingredient function;
- constraint;
- caution;
- design choice;
- API contract;
- migration impact;
- teaching concept;
- domain-specific material.

Core does not define a universal Entity kind vocabulary.

Kinds should be Projection-defined, profile-defined, domain-defined, or implementation-defined.

## 8.8 Entity Content

Entity content is the reusable material carried by the Entity.

It may be:

- text;
- structured data;
- reference to external material;
- source-derived phrase;
- normalized label;
- code symbol;
- media reference;
- dataset reference;
- short explanation;
- profile-defined payload.

Entity content should be useful for reconstruction.

It should not pretend to replace the Original Source or store final meaning.

Part 4 or profiles may define allowed content forms.

## 8.9 Entity Payload Boundary

Entity content may need to be explanatory enough to support reconstruction.

However, too much explanation may turn Entity into a mini-summary or meaning store.

A useful boundary is:

```text
Entity content may preserve Projection-shaped reusable material,
but it should not claim to be a complete final interpretation independent of Original Source and Projection.
```

Good Entity content helps answer:

```text
What reusable material is being placed or referenced?
```

It should not try to answer every future question by itself.

## 8.10 Entity Identity

An Entity should have an identifier within the IdeaMark document.

Core treats Entity IDs primarily as reference labels.

Core does not require:

- global Entity identity;
- cross-document identity stability;
- ontology membership;
- canonical naming;
- universal equivalence across Projections.

Implementations, profiles, or libraries may define stronger identity systems when needed.

For Core, local identity is sufficient if Occurrences can reference Entities within the document.

## 8.11 Entity Reuse

Entity reuse is allowed but not required.

The same Entity may be referenced by multiple Occurrences.

This can be useful when the same material appears in multiple Section contexts.

However, forcing reuse may introduce artificial identity claims.

It may be better to create Projection-specific or Section-specific Entities when the reusable material differs by role or context.

Core should allow both patterns.

## 8.12 Entity and Source Anchor

An Entity may have a source anchor.

Entity-level anchors are useful when the reusable material is directly derived from a specific source fragment.

However, Section-level anchors may be sufficient in many cases.

Core should allow:

- unanchored Entities within anchored Sections;
- Entities with direct anchors;
- Entities with multiple anchors;
- Entities with approximate or inferred anchors;
- Entities whose source traceability is mediated through Occurrences.

A document with no traceability from Entities, Occurrences, or Sections to Original Source material is weak as an IdeaMark document.

## 8.13 Entity and Inference

Entities may be directly sourced or inferred.

For example:

- a code comment may directly state a performance rationale;
- a recipe step may directly state a heat-control action;
- a design RFC may directly state an alternative;
- an ingredient function may be inferred from culinary knowledge and recipe context;
- a migration impact may be inferred from a proposed syntax change.

Inferred Entities should preserve enough context, anchors, and rationale to support review.

Core does not prohibit inference.

However, inferred Entities must remain Projection-shaped reusable material, not final meaning.

## 8.14 Entity Granularity

Entity granularity is Projection-dependent.

An Entity should be small enough to be reusable and large enough to remain meaningful for reconstruction.

Too-large Entities may become summaries.

Too-small Entities may lose useful context and force excessive reconstruction work.

Examples:

- under a performance Projection, one Entity may represent a cost driver;
- under a state-machine Projection, one Entity may represent a state or transition;
- under a recipe substitution Projection, one Entity may represent an ingredient function;
- under an RFC evidence Projection, one Entity may represent an evidence limitation.

Core does not define universal Entity granularity.

Projection libraries, profiles, or implementations may define guidance.

## 8.15 Entity Completeness

An Entity is not required to capture all possible meanings or uses of a source fragment.

It only needs to preserve reusable material under a Projection.

Other Projections may generate other Entities from the same source material.

A document may be valid even if it contains only a subset of possible Entities.

Completeness should be interpreted relative to Projection and document status.

## 8.16 Multi-source Entities

An Entity may be derived from multiple source fragments or sources.

For example:

- a design rationale may combine a motivation paragraph and a detailed-design rule;
- a performance material may combine code and benchmark comments;
- a recipe substitution material may combine ingredient list and step usage;
- a research material may combine dataset rows and narrative interpretation.

A multi-source Entity should preserve enough traceability to support later review.

## 8.17 Entity Status and Review

Entities may have review or status information if a profile or implementation requires it.

Core does not require object-level status.

Document-level status should be defined first.

Entity-level status may be useful when:

- generated Entities require human review;
- inferred Entities need approval;
- deprecated material should remain traceable;
- regeneration changes Entity payloads;
- profile-specific validation requires object status.

## 8.18 Weak or Invalid Entities

An Entity may be weak if it:

- stores final interpretation without traceability;
- has no usable content or reference;
- has no way to be placed through Occurrences;
- claims universal identity without basis;
- lacks Projection-shaped purpose;
- cannot be reviewed or reconstructed through source context;
- duplicates source text without reuse function;
- becomes a summary that replaces Original Source material.

Part 4 or profiles may define validation levels.

Part 3 identifies these conceptual risks.

## 8.19 Conceptual Example

The following shape is illustrative:

```yaml
entities:
  IE-004:
    kind: implementation_rationale
    content: |
      The implementation deliberately avoids an early break in _siftup because comparison savings depend on workload and comparison cost.
    source_role: optimization_rationale
    source_anchor:
      source: SRC-heapq-py
      line_ranges:
        - start: 63
          end: 75
```

This example is not normative YAML.

Part 4 defines concrete syntax.

## 8.20 Invariants

An Entity should preserve the following invariants:

1. An Entity is produced by Projection-guided Decomposition.
2. An Entity is Projection-shaped reusable material.
3. An Entity is not final meaning.
4. An Entity is not a universal ontology object by default.
5. Entity identity is local unless a profile defines stronger identity rules.
6. Entity kind vocabulary is not Core-defined.
7. Entity content should support reconstruction without replacing Original Source material.
8. An Entity becomes locally useful through Occurrence placement in a Section.
9. Entity reuse is allowed but not required.
10. An Entity may be directly sourced or inferred.
11. Entity granularity is Projection-dependent.

## 8.21 Summary

Entity is the Core Model's reusable material object.

It allows Decomposition to preserve material that can be placed, referenced, reviewed, and reused.

A good Entity helps later humans, AI systems, or tools reconstruct useful activity, but it does not claim to contain final meaning by itself.
