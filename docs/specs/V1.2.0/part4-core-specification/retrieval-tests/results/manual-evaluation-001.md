# Manual Evaluation 001 — Initial Skeleton Retrieval Tests

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft Evaluation Result  
**Date:** 2026-07-07

## Purpose

This note records the first manual evaluation of the Retrieval Test Suite against the current Part 4 normalized samples.

The purpose is to determine whether the new optional `skeletons` namespace can support candidate retrieval through Intellectual Activity Skeleton Graphs.

This is not an automated CLI result.

It is a human-readable baseline for future automated test runner development.

## Evaluated Samples

| Sample | Skeleton Graph Coverage | Notes |
|---|---:|---|
| `sample-recipe-ingredient-substitution` | present | Contains `SKEL-function-preserving-alternative`. |
| `sample-heapq-performance` | present | Contains `SKEL-invariant-constrained-design`. |
| `sample-recipe-cooking-execution` | not yet present | Expected non-match for the first retrieval tests. |
| `sample-heapq-api-design` | not yet present | Expected non-match for the first retrieval tests. |
| `sample-sqlite-pager-state-machine` | not yet present | Future Skeleton Graph target. |
| `sample-rust-rfc-design-prose` | not yet present | Future Skeleton Graph target. |

## Test 1 — Function-preserving Alternative Selection

**Test file:** `function-preserving-alternative-selection.yaml`

### Required Skeleton

```text
unavailable_or_blocked_element
  --constraint-->
preserved_effect_or_function
  --dependency-->
alternative_space
  --confirmation-->
confirmation_signal
```

### Manual Result

| Candidate | Result | Reason |
|---|---|---|
| `sample-recipe-ingredient-substitution` | partial match | Contains the required blocked element, preserved function, alternative space, and required links. Confirmation is visible but underspecified. |
| `sample-heapq-performance` | analogical partial | Contains structurally similar boundary/design/restoration/confirmation pattern, but slot labels and domain differ. |
| `sample-recipe-cooking-execution` | non-match | No Skeleton Graph currently present; execution Projection does not model function-preserving alternatives. |
| `sample-heapq-api-design` | non-match | No Skeleton Graph currently present; API design sample is not expected to contain the required alternative-selection graph. |

### Evaluation

Result: **passes initial manual expectation**.

The recipe sample can be retrieved without requiring literal source keywords such as `bonito flakes`.

The missing `confirmation_signal` is visible as an underspecified node rather than hidden.

The heapq sample is correctly treated as analogical rather than exact.

## Test 2 — Invariant-constrained Design Selection

**Test file:** `invariant-constrained-design-selection.yaml`

### Required Skeleton

```text
preserved_invariant_or_boundary
  --constraint-->
chosen_operational_form
  --dependency-->
restoration_or_recovery_strategy
  --confirmation-->
confirmation_signal
```

### Manual Result

| Candidate | Result | Reason |
|---|---|---|
| `sample-heapq-performance` | compatible match | Contains the required boundary, operational form, restoration strategy, confirmation signal, and required links. |
| `sample-recipe-ingredient-substitution` | analogical partial | Contains related function-preserving alternative pattern, but not the same design/invariant Skeleton. |
| `sample-heapq-api-design` | non-match | No Skeleton Graph currently present; same source alone is not enough. |
| `sample-rust-rfc-design-prose` | non-match / future candidate | No Skeleton Graph currently present; future compatibility-preserving design Skeleton may make it a candidate. |

### Evaluation

Result: **passes initial manual expectation**.

The heapq performance sample is retrieved by Skeleton structure, not exact code terms.

The recipe sample is visible only as an analogical candidate and requires domain transfer review.

Same-source API design material is not retrieved merely because it shares CPython `heapq.py`.

## Test 3 — Cross-domain Skeleton Analogy

**Test file:** `cross-domain-skeleton-analogy.yaml`

### Skeleton Family

```text
change / constraint / unavailability
  -> preserve required effect or boundary
  -> choose alternative or operational form
  -> confirm, monitor, or review
```

### Manual Result

| Candidate | Result | Reason |
|---|---|---|
| `sample-recipe-ingredient-substitution` | analogical partial | Provides function-preserving alternative pattern, but confirmation is underspecified. |
| `sample-heapq-performance` | analogical compatible | Provides boundary-constrained design and restoration with confirmation support. |
| `sample-sqlite-pager-state-machine` | possible future match | No Skeleton Graph currently present; expected to become relevant after adding correctness/recovery Skeleton. |
| `sample-rust-rfc-design-prose` | possible future match | No Skeleton Graph currently present; expected to become relevant after adding compatibility-preserving design Skeleton. |

### Evaluation

Result: **passes initial manual expectation with limited sample coverage**.

The test distinguishes analogical retrieval from exact reuse.

It also exposes the next required sample work: add Skeleton Graphs to SQLite Pager and Rust RFC samples.

## Findings

### Finding 1 — Skeleton Graphs enable keyword-independent candidate retrieval

The recipe substitution sample can be retrieved by the required activity slots without using source-specific terms.

This supports the design claim that IdeaMark retrieval can operate over Intellectual Activity Skeletons rather than only over source vocabulary.

### Finding 2 — Skeleton Graphs support analogical but bounded cross-domain retrieval

Recipe and heapq can be related structurally without treating them as interchangeable.

The tests require review boundaries for analogical matches.

This supports the design claim that Skeleton Graphs can support cross-domain exploration without unsafe direct transfer.

### Finding 3 — Same source is not sufficient for retrieval

The heapq API design sample is not retrieved by the invariant-constrained test merely because it shares the same source domain or source file.

This supports the design claim that Projection-shaped Skeleton structure matters more than source identity alone.

### Finding 4 — Missing slots are valuable

The underspecified `confirmation_signal` in the recipe sample is useful.

It shows that partial matches can remain usable while preserving warnings for reconstruction.

### Finding 5 — Current coverage is too small

Only two samples currently contain Skeleton Graphs.

The next evaluation pass should add Skeleton Graphs to:

- `sample-sqlite-pager-state-machine`;
- `sample-rust-rfc-design-prose`;
- optionally `sample-recipe-cooking-execution` for a negative/contrast graph.

## Decision

The initial manual evaluation supports continuing with the Skeleton Graph approach in v1.2.0.

The concept should remain optional in Core, but retrieval-oriented samples and tests should continue to expand.

## Recommended Next Work

1. Add a correctness/recovery Skeleton Graph to the SQLite Pager sample.
2. Add a compatibility-preserving design Skeleton Graph to the Rust RFC sample.
3. Re-run cross-domain analogy evaluation after those additions.
4. Draft a minimal pseudo-runner algorithm for Skeleton Graph matching.
5. Later, implement a CLI test runner once IdeaMark CLI development begins.
