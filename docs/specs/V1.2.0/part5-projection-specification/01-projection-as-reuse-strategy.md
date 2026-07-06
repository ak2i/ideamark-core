# 1. Projection as Reuse Strategy

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## Purpose

This chapter defines Projection as a reuse strategy.

IdeaMark does not preserve knowledge as a final meaning object.

It preserves reusable access structures that help future humans and AI systems return to Original Sources and reconstruct useful activation expressions.

Projection is the strategy that makes this reuse intentional.

## Reuse Target

A Projection SHOULD identify what kind of future reuse it is trying to support.

The target may include:

- answering questions;
- generating plans;
- supporting review;
- preparing decisions;
- explaining procedures;
- comparing alternatives;
- detecting risks;
- teaching a learner;
- reconstructing domain guidance for a different audience;
- producing machine-actionable inputs for another tool.

A Projection does not need to support every possible reuse.

A narrower Projection may be more valuable than a broad one when it reduces interpretation cost for a specific repeated activity.

## Reuse Unit

A Projection SHOULD clarify what should become reusable.

Depending on the activity, reusable material may be:

- a concept;
- a procedural step;
- a condition;
- an exception;
- a risk pattern;
- an evidence item;
- a decision criterion;
- a source window;
- a relation-like dependency;
- an example;
- a contrast;
- a reconstruction instruction.

The reusable unit is not universal.

Part 3 defines Entity as Projection-shaped reusable material, not as a global semantic atom.

Therefore, the Projection is responsible for explaining which kind of reusable unit matters for the intended activity.

## Reuse Horizon

A Projection MAY define a reuse horizon.

The reuse horizon describes how far away the expected reuse may be from the generating Situation.

Examples include:

- immediate use in the current session;
- reuse by the same user later;
- reuse by another member of the same organization;
- reuse across departments;
- reuse across domains;
- reuse by public readers;
- reuse by future AI systems or tools.

A longer reuse horizon usually requires stronger traceability, clearer metadata, and more conservative assumptions.

A short reuse horizon may allow lighter authoring if the local context remains available.

## Interpretation Cost Reduction

A Projection SHOULD reduce interpretation cost.

Interpretation cost includes the effort required to understand why a source is relevant, what part should be used, what assumptions shaped the access structure, and how the material can be reconstructed safely.

A Projection reduces this cost by making repeated choices explicit enough to reuse:

- what to include;
- what to ignore;
- how to split material;
- how to group material;
- what source anchors matter;
- which roles and statuses are useful;
- what compatibility means;
- which reconstruction forms are expected.

## Reuse Without Final Meaning

Projection-guided reuse does not require a single stored meaning.

The same IdeaMark document may support different reconstructions under different Projections when their assumptions are compatible enough.

The same Original Source may be decomposed differently under multiple Projections, producing multiple valid IdeaMark documents.

This is not duplication by mistake.

It is a deliberate mechanism for supporting plural reuse without forcing a universal interpretation.

## Minimum Useful Projection

A minimum useful Projection SHOULD state:

1. the intended reuse activity;
2. the audience or interpreter assumptions;
3. the reusable unit strategy;
4. the source coverage policy;
5. the reconstruction expectation;
6. at least one quality criterion.

A Projection MAY be informal or incomplete during exploration.

However, a Projection that cannot explain its reuse intent is difficult to compare, improve, share, or govern.
