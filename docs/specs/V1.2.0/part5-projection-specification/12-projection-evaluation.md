# 12. Projection Evaluation

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## Purpose

This chapter defines conceptual evaluation dimensions for Projections.

Projection evaluation asks whether a Projection helps humans, AI systems, and tools produce, find, match, filter, and reconstruct useful access structures with lower interpretation cost.

Evaluation is not a universal truth test.

A Projection may be good for one Situation class, audience, risk level, or reconstruction target and poor for another.

## Evaluation Boundary

Part 5 defines evaluation responsibilities and dimensions.

It does not define:

- a universal score;
- a required benchmark;
- a required review workflow;
- a required statistical method;
- a required AI judge;
- a required governance process.

Projection Libraries, tools, organizations, or companion specifications MAY define stricter evaluation methods.

## Core Evaluation Question

The central evaluation question is:

```text
Does this Projection reduce the cost and risk of later intellectual activity
by guiding Decomposition, retrieval, matching, filtering, and reconstruction
in a reusable and inspectable way?
```

This question should be interpreted relative to the intended reuse context.

## Interpretation Cost Reduction

A Projection SHOULD be evaluated by whether it reduces interpretation cost.

Interpretation cost includes the effort required to:

- decide which source material matters;
- understand why a structure was generated;
- return to Original Source material;
- judge whether a candidate is compatible;
- adapt material for a new audience or Situation;
- detect missing assumptions;
- explain reconstruction decisions;
- review risk and responsibility.

A Projection that creates more structure than necessary may increase interpretation cost.

A Projection that creates too little structure may reduce authoring cost but increase future reconstruction cost.

## Decomposition Quality

A Projection MAY be evaluated by Decomposition quality.

Useful questions include:

- Does it guide source coverage clearly?
- Does it produce reusable Section boundaries?
- Does it produce reusable Entity boundaries?
- Does it preserve role-bearing Occurrences that matter for later use?
- Does it avoid accidental summarization?
- Does it preserve uncertainty and exclusion rules when important?
- Does it preserve enough traceability to return to source?

Decomposition quality should be evaluated relative to the Projection's intended future reuse, not against a universal extraction ideal.

## Retrieval and Matching Quality

A Projection MAY be evaluated by retrieval and matching quality.

Useful questions include:

- Can future users or tools find relevant documents or sources?
- Are irrelevant candidates filtered out?
- Can compatibility be explained?
- Are partial matches useful rather than noisy?
- Are analogical matches reviewed carefully enough?
- Are unknown matches distinguished from compatible matches?
- Do version changes preserve or document compatibility?

Retrieval success alone is not sufficient.

A Projection that retrieves many candidates but cannot explain compatibility may still increase interpretation cost.

## Reconstruction Quality

A Projection MAY be evaluated by reconstruction quality.

Useful questions include:

- Does reconstruction produce an expression appropriate for the audience and activity?
- Are source-critical constraints preserved?
- Are uncertainties visible enough?
- Are transformation assumptions explicit?
- Does the expression avoid implying unsupported authority?
- Can a user or tool return to sufficient source material?
- Does the Projection allow reconstruction to fail when necessary?

A Projection should be rewarded for safe refusal or partial reconstruction when full reconstruction is not supported.

## Traceability Quality

Traceability is a central quality dimension.

A Projection may be weak if it produces attractive reconstructions that cannot be traced back to Original Sources.

Traceability quality may consider:

- anchor precision;
- source accessibility;
- source revision awareness;
- composite source handling;
- confidence or uncertainty notes;
- relationship between generated structures and source fragments;
- ability to support later review.

The required traceability level depends on risk and reuse horizon.

## Transfer and Adaptation Quality

Some Projections are valuable because they support transfer across domains, roles, audiences, or media.

Transfer quality may consider:

- whether functional structure is preserved;
- whether domain-specific constraints are not silently lost;
- whether analogies are bounded;
- whether adaptation risks are visible;
- whether the target audience receives enough prerequisite context;
- whether review is required when transfer is uncertain.

A Projection that enables cross-domain reuse should not hide the fact that transfer is occurring.

## Lifecycle Quality

A Projection MAY be evaluated as a maintained asset.

Lifecycle quality may consider:

- version clarity;
- status clarity;
- deprecation behavior;
- feedback capture;
- compatibility notes;
- library discoverability;
- privacy and sharing policy;
- review history;
- examples of successful and failed use.

A Projection that works once may be useful.

A Projection that can be improved through feedback becomes an intellectual asset.

## Evaluation Evidence

Evaluation may use many evidence forms, including:

- human review notes;
- reconstruction outcomes;
- retrieval logs;
- matching explanations;
- failed reconstruction cases;
- user feedback;
- comparison with earlier Projection versions;
- source review results;
- downstream task success;
- library reuse statistics.

Part 5 does not require that such evidence be stored inside the Projection itself.

However, Projection Libraries SHOULD preserve evaluation evidence when it improves future selection, compatibility, or governance.

## Evaluation Non-goal

Projection evaluation should not force all Projections to become public, formal, or expert-authored.

Exploratory Projections are valuable.

Private Projections are valuable.

AI-generated Projections are allowed.

The evaluation requirement is proportional: the higher the reuse horizon, risk, and sharing level, the stronger the expected evaluation should be.
