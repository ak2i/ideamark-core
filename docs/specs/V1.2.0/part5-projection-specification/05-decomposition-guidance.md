# 5. Projection and Decomposition Guidance

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## Purpose

This chapter defines how Projection guides Decomposition.

Part 3 defines Decomposition as the Projection-guided structuring act that produces an IdeaMark document from Original Source material.

Part 5 defines what a Projection may say in order to guide that act.

## Decomposition Responsibility

A Projection SHOULD guide the authoring process enough that another human, AI system, or tool can understand why the resulting IdeaMark document was shaped as it was.

This does not require a fully deterministic algorithm.

It does require explicit enough guidance to make Decomposition inspectable and improvable.

## Source Coverage Policy

A Projection SHOULD define a source coverage policy.

The policy may specify:

- whether the whole source should be considered;
- whether only a named section, time range, region, table, or fragment should be used;
- whether examples should be included or ignored;
- whether background material should be included;
- whether contradictions should be preserved;
- whether uncertainty should be represented;
- whether missing information should be recorded.

Source coverage policy prevents accidental summarization from replacing Projection-guided Decomposition.

## Section Strategy

A Projection MAY define a Section strategy.

A Section strategy describes how local source windows should be formed.

Examples include:

- section by source heading;
- section by task phase;
- section by decision point;
- section by risk category;
- section by evidence cluster;
- section by temporal episode;
- section by reconstruction need;
- section by user capability level.

Part 3 defines Section functionally as a Projection-shaped local source window.

Part 5 allows the Projection to explain which local windows are useful for the intended reuse.

## Entity Strategy

A Projection SHOULD define an Entity strategy when reusable material boundaries matter.

The strategy may specify:

- what counts as reusable material;
- how small or large reusable material should be;
- when to split material;
- when to preserve a composite;
- how to handle examples;
- how to handle exceptions;
- how to handle implicit assumptions;
- how to handle definitions, procedures, evidence, constraints, and decisions.

An Entity strategy is not a universal ontology.

It is a Projection-specific boundary rule for reuse.

## Occurrence Strategy

A Projection MAY define an Occurrence strategy.

The strategy may specify:

- which roles are useful;
- how role-bearing placements should be assigned;
- whether role vocabulary should be strict or open;
- how status should be used;
- when a placement should be provisional;
- how attribution or generation notes should be recorded;
- how the same reusable material may appear in multiple Sections.

Occurrence strategy is important when the same Entity material plays different roles in different local windows.

## Traceability Strategy

A Projection SHOULD define traceability expectations.

It may specify the preferred source anchors, such as:

- line range;
- paragraph;
- heading;
- media time range;
- image region;
- table row or column;
- code span;
- dataset fragment;
- approximate source region;
- composite anchor.

Exact anchors are useful when available, but Projection should not require text-only anchoring when the Original Source is not text.

## Ignoring Material

A Projection SHOULD make important exclusion rules explicit.

Ignoring source material is often as consequential as selecting it.

A Projection may ignore material because it is outside scope, not reusable for the intended activity, too uncertain, too domain-specific, private, redundant, outdated, or better handled by another Projection.

When exclusion may surprise future users, the reason SHOULD be recorded.

## Decomposition Quality

A Projection MAY define Decomposition quality criteria.

Examples include:

- source traceability is sufficient;
- reusable material is not over-compressed;
- boundaries are consistent with the intended future search;
- uncertainties are not hidden;
- reconstruction-critical constraints are preserved;
- ignored material is justifiably outside scope;
- Section grouping supports future access;
- authoring notes explain important judgment calls.

These criteria are not Core validation rules.

They are Projection-side authoring and review criteria.
