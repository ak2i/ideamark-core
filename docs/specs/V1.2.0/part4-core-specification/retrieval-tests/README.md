# Part 4 Retrieval Test Suite

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft Test Suite Seed

## Purpose

This directory contains retrieval-oriented tests for IdeaMark Core v1.2.0 samples.

The tests evaluate whether documents can be retrieved through **Intellectual Activity Skeleton Graph** structure rather than through exact keywords, domain labels, or full-document LLM inspection.

These tests are not Core validators.

They seed future CLI, POR, library, and conformance-suite behavior for:

- Skeleton Graph extraction;
- required Skeleton matching;
- partial match reporting;
- missing slot visibility;
- candidate Section / Occurrence / Entity selection;
- reconstruction boundary checks.

## Test Flow

```text
Use-side Projection
  -> required_skeleton
  -> candidate IdeaMark samples
  -> document-side skeletons
  -> match class
  -> matched slots and links
  -> expected candidate structures
  -> reconstruction policy
```

## Test Files

- [`function-preserving-alternative-selection.yaml`](./function-preserving-alternative-selection.yaml)
  - tests keyword-independent retrieval for replacement / substitution activity composition.
- [`invariant-constrained-design-selection.yaml`](./invariant-constrained-design-selection.yaml)
  - tests retrieval for implementation material where a design choice is constrained by an invariant and requires restoration.
- [`cross-domain-skeleton-analogy.yaml`](./cross-domain-skeleton-analogy.yaml)
  - tests whether cross-domain analogical matches can be identified and marked as review-required.

## Expected Runner Behavior

A future runner may implement commands such as:

```text
ideamark retrieve test docs/specs/V1.2.0/part4-core-specification/retrieval-tests
ideamark retrieve explain <test-id>
```

This directory does not require those commands.

The test definitions are intended to be readable by humans and easy to convert into CLI test fixtures later.
