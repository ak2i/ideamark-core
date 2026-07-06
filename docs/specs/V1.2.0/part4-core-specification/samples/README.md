# Part 4 Normalized YAML Samples

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft Samples

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
- provide compact examples for authoring tools.

## Sample Files

- [`heapq-performance.ideamark.yaml`](./heapq-performance.ideamark.yaml) — code source / performance engineering Projection.
- [`heapq-api-design.ideamark.yaml`](./heapq-api-design.ideamark.yaml) — same code source / API design Projection.
- [`sqlite-pager-state-machine.ideamark.yaml`](./sqlite-pager-state-machine.ideamark.yaml) — system correctness and state-machine source pattern.
- [`rust-rfc-design-prose.ideamark.yaml`](./rust-rfc-design-prose.ideamark.yaml) — formal RFC design prose source pattern.
- [`recipe-cooking-execution.ideamark.yaml`](./recipe-cooking-execution.ideamark.yaml) — recipe source / cooking execution Projection.
- [`recipe-ingredient-substitution.ideamark.yaml`](./recipe-ingredient-substitution.ideamark.yaml) — same recipe source / ingredient function and substitution Projection.

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
