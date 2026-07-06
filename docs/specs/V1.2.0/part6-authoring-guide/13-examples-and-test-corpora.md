# 13. Examples and Test Corpora

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 13.1 Purpose

Examples and test corpora help authors, AI systems, validators, formatters, migration tools, and reviewers learn what useful IdeaMark Documents look like.

They should demonstrate both syntax and authoring judgment.

Part 4 normalized samples provide implementation-oriented YAML examples.

Part 6 explains how such samples can be used for authoring practice and quality evaluation.

## 13.2 Samples Are More Than Syntax

A sample is not only a valid YAML file.

A good sample demonstrates:

- Projection-shaped decomposition;
- useful Section boundaries;
- reusable Entity material;
- clear Occurrence roles;
- adequate traceability;
- appropriate omission;
- optional structure ordering when useful;
- inspectable working-artifact status.

A syntactically valid sample may still be a weak authoring example.

## 13.3 Sample Categories

A mature sample corpus may include multiple categories:

```text
valid/
invalid/
warnings/
migration/
profiles/
roundtrip/
retrieval/
```

The initial Part 4 samples are positive examples and conformance-suite seeds.

Future corpora may add invalid and warning cases to test validators and authoring tools.

## 13.4 Same-source Different-Projection Samples

Same-source different-Projection samples are especially important.

They demonstrate that Projection changes decomposition.

Examples include:

- heapq performance vs heapq API design;
- recipe cooking execution vs recipe ingredient substitution;
- RFC design rationale vs migration planning;
- image visual inspection vs object cataloging;
- report evidence extraction vs policy planning.

If two different Projections produce indistinguishable samples, either the source is simple or the Projection/application is not shaping authoring strongly enough.

## 13.5 Negative and Warning Samples

Negative and warning samples are useful for tools and authoring education.

Possible examples:

- missing required namespace;
- duplicate IDs;
- unresolved Occurrence entity reference;
- keyed-map legacy structure where array-based representation is required;
- hidden placeholder;
- weak anchor precision under a strict profile;
- source flattening;
- summary-only Entities;
- Projection drift.

Some of these are Core errors.

Others are authoring warnings or profile-specific issues.

The corpus should distinguish them clearly.

## 13.6 Migration Samples

Migration samples help tools convert older or exploratory forms into Part 4 representation.

For example:

```yaml
sections:
  SEC-001:
    title: Example
```

may migrate to:

```yaml
sections:
  - id: SEC-001
    title: Example
```

Migration samples should include:

- input fixture;
- expected output fixture;
- expected warnings;
- known loss or ambiguity;
- migration rationale.

## 13.7 Retrieval Samples

Retrieval samples should pair documents with intended retrieval scenarios.

A retrieval sample may define:

- user query or future activity;
- expected Sections;
- expected Entities;
- expected Occurrence roles;
- source regions that should be revisited;
- expected activation expression type;
- acceptable alternative outputs.

This helps evaluate whether the document supports reuse rather than only syntax.

## 13.8 Sample Metadata

Sample corpora may benefit from a manifest.

A manifest can record:

- sample ID;
- path;
- source domain;
- Projection pattern;
- expected validation result;
- covered features;
- profile requirements;
- migration role;
- retrieval scenarios;
- known limitations.

The Part 4 samples directory includes an initial manifest seed.

## 13.9 Human-AI Use of Samples

Humans can use samples to learn authoring judgment.

AI systems can use samples as few-shot guidance, test fixtures, or regression examples.

Tools can use samples for validation and formatting tests.

Reviewers can use samples to compare whether a new document follows established authoring patterns.

Sample use should remain transparent: the sample should be inspectable as an IdeaMark Document, not only embedded in a prompt.

## 13.10 Corpus Evolution

A sample corpus should evolve with implementation experience.

As CLI, POR, validators, and retrieval experiments produce results, the corpus should collect:

- successful examples;
- failed examples;
- ambiguous cases;
- migration edge cases;
- domain profile examples;
- authoring anti-patterns;
- retrieval evaluation fixtures.

The corpus should be treated as design infrastructure, not as decoration.

## 13.11 Authoring Checks

Review examples and test corpora with questions such as:

1. Does the sample demonstrate authoring judgment?
2. Is the expected validation result clear?
3. Does the sample cover a useful feature or failure mode?
4. Can humans learn from it?
5. Can tools test against it?
6. Can AI systems use it without hidden context?
7. Does the corpus include same-source different-Projection cases?
8. Are negative, warning, and migration cases clearly separated?
