# 7. Projection-guided Reconstruction

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## Purpose

This chapter defines how Projection guides reconstruction.

Reconstruction is the use-side process of transforming retrieved IdeaMark structures and Original Source material into an activation expression for a future Human-AI Intellectual Activity.

The activation expression may be a text, answer, plan, question, warning, diagram, table, code fragment, checklist, interface state, or another medium.

Skeleton Graphs may support reconstruction indirectly by reducing the cost of selecting relevant candidate structures before reconstruction begins.

## Reconstruction Is Not Stored Meaning

Reconstruction does not simply read stored meaning out of an IdeaMark document.

The IdeaMark document provides reusable access structures.

The Projection provides the strategy for deciding what to retrieve, how to return to source, what to adapt, what to exclude, and how to express the result.

When Skeleton Graphs are present, they provide an additional retrieval-oriented access layer. They help identify which Sections, Occurrences, Entities, and source anchors may contain activity-composition material needed by the use-side Projection.

Meaning becomes active only when the reconstructed expression participates in a Situation and activity.

## Reconstruction Pipeline

A Projection-guided reconstruction pipeline may be understood as:

```text
Use-side Projection
  -> retrieval intent and required_skeleton
  -> candidate IdeaMark Skeleton Graphs
  -> matched Sections / Occurrences / Entities / anchors
  -> Original Source return
  -> Projection-guided adaptation
  -> activation expression
```

This pipeline is conceptual.

Part 5 does not require a specific retrieval engine, graph database, ranking function, or expression generator.

The important boundary is that Skeleton Graph matching selects candidate materials, while reconstruction transforms those materials into an expression.

## Reconstruction Target

A Projection SHOULD define the intended reconstruction target when it materially affects retrieval or Decomposition.

The target may specify:

- audience;
- capability level;
- role;
- medium;
- language;
- depth;
- acceptable uncertainty;
- required source visibility;
- actionability;
- review requirement;
- output structure;
- downstream tool compatibility.

A Projection may support multiple reconstruction targets.

When targets conflict, the Projection SHOULD describe how they are selected or prioritized.

## Source Return

Projection-guided reconstruction SHOULD preserve the ability to return to Original Source material when practical.

Depending on the target, reconstruction may expose source anchors directly, summarize them, hide them behind a review action, or use them only internally.

A high-risk reconstruction target may require stronger source visibility.

A low-risk exploratory target may allow looser source return.

The Projection should make such expectations explicit.

Skeleton Graphs do not remove the need for source return.

A matched Skeleton Node should ultimately lead, directly or indirectly, to Sections, Occurrences, Entities, source anchors, or source windows that support reconstruction.

## Adaptation

A Projection MAY define adaptation rules.

Adaptation may change:

- terminology;
- abstraction level;
- examples;
- ordering;
- granularity;
- medium;
- tone;
- warning level;
- prerequisite explanation;
- action format;
- domain mapping.

Adaptation should not silently remove reconstruction-critical constraints.

When adaptation could distort the source or exceed compatibility, the Projection SHOULD require review, warning, or exclusion.

A Skeleton Graph match may indicate that analogical transfer is possible, but it does not by itself authorize domain transfer. The use-side Projection should decide whether the target Situation permits such transfer.

## Reconstruction Quality

A Projection MAY define reconstruction quality criteria.

Examples include:

- the expression is appropriate for the audience;
- source-critical constraints are preserved;
- uncertainty is visible enough;
- the expression does not imply unsupported authority;
- the output is actionable for the intended activity;
- the output remains traceable to sufficient source material;
- differences between generation Projection and use-side Projection are handled explicitly;
- matched Skeleton slots are used consistently;
- missing Skeleton slots are surfaced when they affect safety, completeness, or actionability;
- known mismatch risks are surfaced.

These criteria are not universal truth tests.

They are Projection-specific quality criteria for the intended reuse activity.

## Reconstruction Failure

A Projection SHOULD allow reconstruction to fail.

Failure is preferable to producing an unsuitable expression when compatibility, traceability, authority, permission, source coverage, or Skeleton Graph completeness is insufficient.

Failure may result in:

- a request for more source material;
- a request for a different Projection;
- a warning-only expression;
- a partial answer;
- a human review task;
- a recommendation not to use the candidate material.

The ability to say that reconstruction is not supported is part of responsible Projection design.

A Skeleton Graph partial match should not be hidden. Missing required slots, unsafe links, or insufficient anchors should be visible to reconstruction and review.

## Feedback

Reconstruction may produce feedback for Projection improvement.

Feedback may indicate:

- missing reusable units;
- missing Skeleton slots;
- weak or noisy Skeleton Links;
- poor source anchors;
- ambiguous roles;
- excessive or insufficient granularity;
- bad matching criteria;
- incompatible audience assumptions;
- useful analogical transfer;
- recurring reconstruction failures.

Projection Libraries SHOULD preserve useful feedback when it can improve future Projection versions.
