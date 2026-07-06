# 00 — Part 5 Drafting Approach

**Part:** 5 — Projection Model  
**Status:** Drafting Approach  
**Version:** IdeaMark Core v1.2.0

## 1. Purpose

This note defines how Part 5 should be drafted.

Part 5 should define Projection before Part 4 defines YAML representation.

The purpose is to prevent Part 4 from prematurely freezing fields such as `meta.projections`, `role`, `kind`, `coverage`, or `compatibility` before the Projection model is conceptually clear.

## 2. Does Part 5 Need Discussion?

Yes, but the discussion should be focused.

Part 3 required broad experiments because the Core objects themselves were unstable.

Part 5 starts from a clearer foundation:

```text
Section
  = Projection-shaped local source window

Occurrence
  = role-bearing placement of reusable material within that window

Entity
  = reusable material shaped by Projection and available for later reconstruction
```

Therefore, Part 5 does not need another long domain experiment phase.

It needs a focused conceptual definition of Projection.

## 3. Recommended Starting Point

Part 5 should begin from the boundary question:

> What is a Projection, and what is it not?

This should be discussed before defining fields.

If Projection is defined too narrowly, it becomes just a prompt.

If Projection is defined too broadly, it becomes Situation, worldview, ontology, governance, or workflow.

The correct target is between those extremes.

## 4. Working Position

A Projection should be treated as a reusable knowledge-reuse strategy.

It is a transformation key used across multiple phases:

```text
Decomposition Key
  -> shapes what is preserved from Original Source material

Retrieval Key
  -> helps find relevant IdeaMark documents and structures

Matching and Filtering Key
  -> helps judge whether existing structures are usable

Reconstruction Key
  -> helps generate activation expressions from source material and IdeaMark structures
```

This definition should guide Part 5.

## 5. First Discussion Axis: Boundary

The first discussion should separate Projection from adjacent concepts.

Projection is not:

- final meaning;
- full Situation;
- a prompt only;
- a schema only;
- a workflow only;
- a domain ontology;
- a governance approval;
- a retrieval algorithm;
- a user persona by itself;
- a document template by itself.

Projection may refer to or contain elements that look like these, but it should remain a reusable strategy for shaping decomposition and reconstruction.

## 6. Second Discussion Axis: Minimum Content

After boundary, Part 5 should discuss minimum Projection content.

A candidate minimal Projection may include:

```yaml
projection:
  id:
  purpose:
  intended_activity:
  focus:
  non_goals:
  source_selection:
  section_guidance:
  occurrence_role_guidance:
  entity_guidance:
  reconstruction_guidance:
```

This is illustrative, not Part 4 YAML.

The key question is not field syntax.

The key question is:

> What must be preserved for a Projection to be reusable?

## 7. Third Discussion Axis: Projection and Core Object Shaping

Part 5 must explain how Projection shapes Part 3 objects.

Projection shapes:

- Section boundaries;
- Section granularity;
- Occurrence role vocabulary;
- Entity kinds;
- Entity payload boundaries;
- source selection;
- coverage and non-goals;
- reconstruction expectations.

This is the strongest reason Part 5 should precede Part 4.

## 8. Fourth Discussion Axis: Generation and Reconstruction

Part 5 must clarify that generation Projection and reconstruction Projection may differ.

A reconstruction Projection may be:

- identical to the generation Projection;
- a newer version;
- narrower;
- broader;
- partially compatible;
- only source-pointer compatible;
- incompatible, requiring new Decomposition.

Part 5 should define this conceptually without forcing a compatibility scoring algorithm.

## 9. Fifth Discussion Axis: Projection Library

Part 5 should also define Projection Library, but carefully.

Projection Library should be treated as reusable strategy infrastructure, not universal governance.

A Projection Library may provide:

- reusable Projection definitions;
- versioned Projection entries;
- role vocabularies;
- examples;
- compatibility notes;
- deprecation/supersession metadata;
- domain-specific profiles.

Part 5 should not define a universal institutional approval process.

## 10. What Can Be Drafted Without More Discussion?

The following can be drafted immediately:

- Projection Model Overview;
- Projection Boundary and Non-goals;
- Projection as Transformation Key;
- Relationship to Part 3;
- Why Part 5 precedes Part 4.

These are already implied by the Part 3 theoretical review.

## 11. What Needs Discussion Before Normative Drafting?

The following should be discussed before becoming too normative:

1. Minimal required Projection fields.
2. Whether `intended_activity` is required or optional.
3. Whether Projection should define role vocabulary directly.
4. Whether Entity kind guidance belongs in Projection or profile.
5. Whether coverage/non-goals should be required.
6. How to express compatibility without algorithmic scoring.
7. Whether Projection Library is part of Core or a companion ecosystem concept.

## 12. Recommended Drafting Sequence

Part 5 should proceed in this order:

1. Boundary and non-goals.
2. Working definition.
3. Projection as transformation key.
4. Projection content model.
5. Projection and Core object shaping.
6. Generation and reconstruction Projections.
7. Compatibility.
8. Projection Library.
9. Status and versioning.
10. Invariants and summary.

## 13. Immediate Next Step

The next file should be:

```text
01-projection-boundary-and-non-goals.md
```

This should define what Projection is not before defining fields.

Once the boundary is stable, `02-projection-definition.md` can define Projection positively.

## 14. Summary

Part 5 needs discussion, but not broad empirical validation.

The right first discussion is the Projection boundary.

The main risk is defining Projection either too narrowly as a prompt or too broadly as Situation, ontology, workflow, or governance.

The target is:

```text
Projection = reusable knowledge-reuse strategy / transformation key
```

This target should guide all subsequent Part 5 drafting.
