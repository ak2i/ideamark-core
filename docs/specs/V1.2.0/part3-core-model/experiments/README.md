# Part 3 Design Experiments

**Part:** 3 — Core Model  
**Status:** Supporting Design Materials

> Note: YAML fragments in this directory are exploratory design artifacts. They may predate the Part 4 array-based object representation and are not normative IdeaMark Core v1.2.0 examples. Use Part 4 normalized samples for implementation-oriented YAML.

This directory contains exploratory design experiments used to test the Part 3 Core Model.

These files are evidence and design history, not normative specification text.

They were used to evaluate whether Section, Occurrence, and Entity can serve as functional Core Model objects across different Original Source types and Projections.

## Non-normative YAML Note

See [Non-normative YAML Note](./00-non-normative-yaml-note.md) for how to interpret exploratory YAML fragments in this directory.

## Experiments

2. [Code Original Source Experiment](./02-code-original-source-experiment.md)
3. [Heapq Performance Candidate IdeaMark Experiment](./03-heapq-performance-candidate.md)
4. [Heapq Cross-Projection Reconstruction Test](./04-heapq-cross-projection-reconstruction.md)
5. [Heapq JSON and MongoDB Search Simulation](./05-heapq-json-mongodb-search-simulation.md)
6. [Heapq Multi-Projection Generation Test](./06-heapq-multi-projection-generation.md)
7. [SQLite Pager Original Source Test](./07-sqlite-pager-original-source-test.md)
8. [Rust RFC Original Source Test](./08-rust-rfc-original-source-test.md)
9. [SQLite Pager Multi-Projection Candidate Test](./09-sqlite-pager-multi-projection-candidates.md)
10. [Rust RFC Multi-Projection Candidate Test](./10-rust-rfc-multi-projection-candidates.md)
11. [Recipe Original Source Test](./11-recipe-original-source-test.md)
12. [Recipe Multi-Projection Candidate Test](./12-recipe-multi-projection-candidates.md)

## Relationship to Core Specification

The main Part 3 specification files remain in the parent directory.

Experiment files may contain provisional structures, candidate YAML-like examples, rejected alternatives, and superseded terminology.

When terminology differs, the parent Part 3 specification and Part 5 Projection Specification take precedence.

For implementation-oriented YAML examples, use the normalized samples under:

```text
docs/specs/V1.2.0/part4-core-specification/samples/
```
