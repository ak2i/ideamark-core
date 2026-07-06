# 13. Progressive Authoring Engines and POR Boundary

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## Purpose

This chapter defines the boundary between Projection Specification and progressive authoring engines.

IdeaMark Core assumes that very large Original Sources may require stateful, progressive, and tool-assisted Decomposition.

However, Core does not define the internal algorithm of such engines.

## Progressive Authoring Engine

A progressive authoring engine is a stateful system that incrementally constructs IdeaMark structures from large, streaming, composite, or difficult Original Sources.

Such sources may include:

- large PDFs;
- long videos;
- audio streams;
- source code repositories;
- large datasets;
- multi-document corpora;
- interaction logs;
- continuously updated sources;
- mixed-media source collections.

A progressive authoring engine may revisit earlier decisions as more context becomes available.

It may use LLMs, parsers, chunking, source indexing, intermediate representations, session state, review loops, or other implementation-specific mechanisms.

## Progressive Occurrence Resolution

Progressive Occurrence Resolution, abbreviated as POR in the IdeaMark ecosystem, is a planned or companion mechanism for progressive construction of IdeaMark structures.

POR is intended for large Original Sources, stream input, LLM-assisted extraction, backward reinterpretation, stateful session management, and progressive evaluation.

Part 5 recognizes that such a mechanism may exist.

Part 5 does not define the POR algorithm, internal representation, session state, orchestration behavior, or context-force reinterpretation rules.

Those responsibilities belong to the IdeaMark-POR repository or another companion specification.

## Projection Input to Progressive Engines

A progressive authoring engine MAY consume a Projection.

The Projection may guide:

- chunk selection;
- source window formation;
- candidate Occurrence generation;
- Entity boundary decisions;
- Section strategy;
- backward reinterpretation priorities;
- uncertainty handling;
- review priorities;
- compatibility notes;
- reconstruction-oriented metadata.

However, the engine's internal scheduling, state transitions, and orchestration remain outside Part 5.

## Core Boundary

IdeaMark Core should assume only the following:

1. Decomposition may be performed by humans, AI systems, tools, workflows, or progressive authoring engines.
2. Large Original Sources may require incremental and stateful Decomposition.
3. Progressive engines may revise earlier candidate structures when later context changes interpretation.
4. The final or intermediate outputs should be representable as IdeaMark documents or compatible structures when they cross the Core boundary.
5. Projection can guide such engines, but Core does not prescribe their internal operation.

## CLI Boundary

IdeaMark CLI is expected to remain a stateless document operation tool.

A CLI may validate, describe, inspect, format, compare, or transform documents.

It should not be required to hold progressive session state in order to conform to Core.

A progressive engine may call CLI operations, emit documents for CLI validation, or consume CLI-described profiles.

This does not make the CLI responsible for progressive authoring state.

## Projection Specification Boundary

Part 5 defines Projection responsibilities that progressive authoring engines may use.

It does not require that a Projection contain engine-specific implementation details.

A Projection may include engine hints when useful, but such hints should be clearly separated from reusable Projection responsibilities.

For example:

- source coverage policy is a Projection responsibility;
- chunk scheduling algorithm is an engine responsibility;
- traceability expectation is a Projection responsibility;
- source-anchor extraction implementation is an engine responsibility;
- reconstruction target is a Projection responsibility;
- prompt orchestration strategy is an engine responsibility.

## Backward Reinterpretation

Progressive authoring engines may perform backward reinterpretation.

Backward reinterpretation means that later source context, later model output, or later human review changes the interpretation of earlier candidate structures.

Core can allow statuses, revision metadata, regeneration notes, or replacement relationships to record the result.

Core does not define how the reinterpretation is triggered, scheduled, or resolved internally.

## Companion Specification Relationship

A POR specification or implementation may define:

- progressive source ingestion;
- chunking and scheduling;
- internal intermediate representation;
- session state;
- LLM orchestration;
- context-force mechanisms;
- candidate Occurrence lifecycle;
- backward reinterpretation;
- review queues;
- output emission;
- integration with CLI validation.

Those are companion responsibilities.

Part 5 should remain compatible with them while avoiding dependency on one specific POR implementation.

## Naming Note

Within the IdeaMark ecosystem, POR should be reserved for Progressive Occurrence Resolution unless explicitly redefined by a different repository or specification.

Part 5 should not use POR to mean Projection-Oriented Reuse, Projection-Oriented Reconstruction, or Projection Optimization Routine.

Projection lifecycle and improvement should instead be described with terms such as Projection Evaluation, Projection Lifecycle, Projection Evolution, Projection Engineering, or Projection Library Management.
