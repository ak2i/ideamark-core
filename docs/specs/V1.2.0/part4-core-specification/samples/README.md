# Part 4 Normalized YAML Samples

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft Samples / Conformance Suite Seed

## Purpose

This directory contains normalized YAML samples that follow the Part 4 array-based object representation.

These samples are derived from the Part 3 design experiments, but they are not the original experiment records.

The Part 3 experiment files remain design-history artifacts.

These Part 4 samples are intended to help:

- implement parsers;
- implement validators;
- implement formatters;
- test migration behavior;
- compare Projection-shaped decompositions;
- provide compact examples for authoring tools;
- seed a future IdeaMark Core conformance suite.

## Sample Files

- [`heapq-performance.ideamark.yaml`](./heapq-performance.ideamark.yaml) — code source / performance engineering Projection.
- [`heapq-api-design.ideamark.yaml`](./heapq-api-design.ideamark.yaml) — same code source / API design Projection.
- [`sqlite-pager-state-machine.ideamark.yaml`](./sqlite-pager-state-machine.ideamark.yaml) — system correctness and state-machine source pattern.
- [`rust-rfc-design-prose.ideamark.yaml`](./rust-rfc-design-prose.ideamark.yaml) — formal RFC design prose source pattern.
- [`recipe-cooking-execution.ideamark.yaml`](./recipe-cooking-execution.ideamark.yaml) — recipe source / cooking execution Projection.
- [`recipe-ingredient-substitution.ideamark.yaml`](./recipe-ingredient-substitution.ideamark.yaml) — same recipe source / ingredient function and substitution Projection.

## Suggested Conformance Uses

Implementations may use these samples to test:

- YAML parsing;
- required top-level namespace detection;
- array-based object handling;
- object ID uniqueness;
- Section → Occurrence → Entity reference resolution;
- Source anchor resolution;
- optional `structure.sections` ordering;
- open role and kind vocabularies;
- round-trip preservation;
- formatter stability;
- migration comparison from Part 3 keyed-map examples.

## Sample Classification

The current samples are positive examples.

They are expected to be valid under Core mode unless a later Part 4 change explicitly updates the sample set.

Future sample groups may include:

```text
valid/
invalid/
warnings/
migration/
profiles/
roundtrip/
```

This directory intentionally starts flat to keep early drafting and inspection simple.

## Normative Scope

These files are samples, not independent normative chapters.

They should conform to the Part 4 Core Specification draft, especially:

- required top-level namespaces;
- array-based object representation;
- explicit object IDs;
- Section → Occurrence → Entity reconstruction path;
- Source anchors through `anchors` arrays;
- optional `structure` ordering;
- open role and kind vocabularies.

Validator behavior should be based on Part 4 chapters, not on this README alone.
