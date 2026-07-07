# 18. Retrieval Test Suite

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 18.1 Purpose

This chapter defines a practical test-suite pattern for evaluating whether IdeaMark documents support retrieval through Intellectual Activity Skeletons.

The goal is to test whether candidate materials can be found by activity-composition structure rather than by exact keywords, domain labels, or full-document LLM inspection.

This chapter is informative guidance. It does not define a required Core validator behavior.

## 18.2 Retrieval Test Boundary

A Retrieval Test Suite should evaluate the path:

```text
Use-side Projection
  -> required_skeleton
  -> candidate IdeaMark documents
  -> document-side skeletons
  -> Skeleton Graph match
  -> matched Sections / Occurrences / Entities / anchors
  -> Reconstruction task
  -> Activation expression or responsible failure
```

The test should separate retrieval success from reconstruction success.

A candidate can retrieve successfully but still fail reconstruction because source anchors, authority, compatibility, safety, or missing slots are insufficient.

## 18.3 Test Case Shape

A retrieval test case SHOULD include:

```yaml
retrieval_test:
  id: rt-001
  name: function_preserving_alternative_without_source_keyword
  purpose: Test retrieval by Skeleton Graph rather than source keyword.
  use_side_projection:
    ref: projection://function-preserving-alternative-selection/v0
    required_skeleton:
      nodes:
        - id: qn-blocked-element
          slot: unavailable_or_blocked_element
          required: true
        - id: qn-preserved-function
          slot: preserved_effect_or_function
          required: true
        - id: qn-alternative-space
          slot: alternative_space
          required: true
        - id: qn-confirmation
          slot: confirmation_signal
          required: false
      links:
        - from: qn-blocked-element
          to: qn-preserved-function
          type: constraint
          required: true
        - from: qn-preserved-function
          to: qn-alternative-space
          type: dependency
          required: true
        - from: qn-alternative-space
          to: qn-confirmation
          type: confirmation
          required: false
  candidate_set:
    - ideamark://sample/recipe-substitution
    - ideamark://sample/heapq-performance
  expected_retrieval:
    matches:
      - document: ideamark://sample/recipe-substitution
        match_class: partial
        matched_slots:
          - unavailable_or_blocked_element
          - preserved_effect_or_function
          - alternative_space
        missing_slots:
          - confirmation_signal
        expected_sections:
          - SEC-dashi-function
    non_matches: []
  expected_reconstruction:
    policy: warning_or_review_required
```

Implementations may represent tests in YAML, JSON, Markdown, a database, or a dedicated conformance runner.

## 18.4 Required Test Dimensions

A useful Retrieval Test Suite should test at least four dimensions.

### 18.4.1 Keyword-independent Retrieval

The test should avoid using source-specific terms when the target claim is structural.

Example:

```text
Use "replace unavailable component while preserving required effect"
not "bonito flakes".
```

### 18.4.2 Section Candidate Quality

The test should verify that matched Skeleton Nodes lead to reconstructable Sections, Occurrences, Entities, or anchors.

A Skeleton Graph match that cannot return to source-backed structures is weak.

### 18.4.3 Missing Slot Visibility

The test should verify that missing slots are surfaced.

A partial match should not be silently treated as complete.

### 18.4.4 Reconstruction Boundary

The test should verify that reconstruction uses retrieved material responsibly and does not invent unsupported domain-specific conclusions.

## 18.5 Recipe Substitution Test Pattern

A recipe substitution test can evaluate whether a document can be retrieved without knowing the term `bonito flakes`.

### Use-side intent

```text
Find source-backed material useful for replacing an unavailable component while preserving a required effect or function.
```

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

### Expected Candidate

The recipe substitution document should match if it contains:

- a node for the unavailable or blocked component;
- a node for the function or effect to preserve;
- a node for the alternative space;
- links showing constraint and dependency;
- a visible missing or underspecified confirmation slot if the source does not provide verification material.

### Failure Conditions

The test should fail or warn if:

- retrieval requires the literal ingredient name;
- the matched document only contains a keyword match and no Skeleton Graph structure;
- the confirmation requirement is hidden;
- reconstruction says only "remove the ingredient" without preserving the functional role;
- reconstruction invents a replacement outside the source without marking external knowledge.

## 18.6 Heapq Performance Test Pattern

A heapq performance test can evaluate whether implementation material can be retrieved by invariant-constrained design structure rather than exact API or code terms.

### Use-side intent

```text
Find implementation material where a design choice is constrained by an invariant and requires a restoration strategy.
```

### Required Skeleton

```text
preserved_invariant_or_boundary
  --constraint-->
chosen_operational_form
  --dependency-->
restoration_or_recovery_strategy
```

### Expected Candidate

The heapq performance document should match if it contains:

- a node for the invariant or performance boundary;
- a node for the operational design choice;
- a node for restoration or recovery strategy;
- a constraint link from boundary to design choice;
- a dependency link from design choice to restoration strategy.

### Failure Conditions

The test should fail or warn if:

- retrieval requires the exact word `heap` or `siftdown`;
- the design choice is retrieved without the invariant boundary;
- reconstruction ignores restoration strategy;
- source anchors do not allow the user to inspect the implementation material.

## 18.7 Cross-domain Skeleton Test Pattern

A cross-domain test can evaluate whether two documents from different domains share an activity-composition pattern.

Example:

```text
Recipe substitution:
  unavailable ingredient -> preserve flavor function -> alternative space -> confirmation

Software implementation:
  unavailable naive operation -> preserve invariant/performance boundary -> alternative design -> benchmark or restoration check

Disaster policy:
  unavailable measure -> preserve protective effect -> alternative intervention -> evaluation signal
```

The test does not require these documents to be interchangeable.

It only tests whether analogical retrieval can identify structurally compatible candidates and mark domain transfer as review-required when appropriate.

## 18.8 Evaluation Output

A retrieval test runner or human reviewer should produce an output such as:

```yaml
result:
  test_id: rt-001
  retrieval:
    status: partial_match
    matched_documents:
      - ideamark://sample/recipe-substitution
    matched_slots:
      - unavailable_or_blocked_element
      - preserved_effect_or_function
      - alternative_space
    missing_slots:
      - confirmation_signal
    warnings:
      - confirmation_missing
  reconstruction:
    status: supported_with_warning
    required_review:
      - external_substitution_candidates
```

## 18.9 Quality Signals

Positive signals include:

- retrieval succeeds without exact source keywords;
- matched Skeleton Nodes lead to traceable source-backed structures;
- missing slots are visible;
- reconstruction uses the matched structure;
- analogical matches are marked as such rather than treated as exact domain matches.

Negative signals include:

- retrieval only works through keywords;
- Skeleton slots are too generic to filter candidates;
- link types are used as semantic claims;
- candidates match but cannot support source return;
- partial matches are treated as complete;
- reconstruction invents unsupported material.

## 18.10 Relationship to CLI

A future IdeaMark CLI may implement commands such as:

```text
ideamark skeleton validate
ideamark retrieve test
ideamark retrieve explain
ideamark reconstruct test
```

This chapter does not require those commands.

It defines the test logic that future CLI, POR, or library implementations can use.
