# 16. Authoring Guide Review Notes

**Version:** IdeaMark Core v1.2.0  
**Status:** Review Note

## 16.1 Purpose

This note records the first whole-part review of Part 6 after drafting the Authoring Guide chapters.

It is not a normative chapter.

It records current alignment, review conclusions, and follow-up items for later passes.

## 16.2 Overall Review Result

Part 6 is structurally complete as a first draft.

It covers:

- authoring stance;
- authoring principles;
- Projection selection;
- source reading;
- reusable intellectual structure identification;
- Entity modeling;
- Occurrence modeling;
- Section organization;
- anchorage and traceability;
- human-AI collaborative authoring;
- validation and correction loops;
- retrieval-oriented evaluation;
- regeneration and versioning;
- examples and test corpora;
- common mistakes;
- non-goals.

The guide is ready for terminology review, example review, and alignment with Part 4 samples.

## 16.3 Core Authoring Thesis

The current Part 6 draft is organized around the following thesis:

```text
IdeaMark authoring is the ongoing activity of improving an IdeaMark Document so that knowledge becomes more reusable under one or more Projections.
```

This thesis supports the following design positions:

- IdeaMark authoring is knowledge reuse design, not generic summarization.
- IdeaMark Documents may be working artifacts, not only final completed artifacts.
- Section, Occurrence, and Entity are functional authoring objects.
- Projection shapes what is noticed, omitted, decomposed, and reused.
- Human and AI roles are intentionally not fixed by the specification.
- POR is an authoring method, not a Core requirement.
- Retrieval-oriented evaluation is the primary quality lens for authoring.

## 16.4 Alignment with Part 3

Part 6 aligns with Part 3 by treating:

- Section as a Projection-shaped local source window and practical local activity unit;
- Occurrence as a role-bearing placement of reusable material within a Section;
- Entity as Projection-shaped reusable material;
- optional relations as useful but not required for initial authoring;
- incompleteness as acceptable when visible.

Part 6 adds practical authoring language without redefining the Core Model.

## 16.5 Alignment with Part 4

Part 6 refers to Part 4 as the source of concrete YAML representation and Core conformance.

Part 6 does not define required YAML fields, validation errors, or serialization rules.

YAML examples in Part 6 should remain compatible with the Part 4 array-based object representation.

Future review should check all examples against Part 4 once the CLI validator is available.

## 16.6 Alignment with Part 5

Part 6 treats Projection as the authoring lens for reuse.

It explains how authors use, sketch, or select Projections without attempting to complete a full theory of Projection quality.

Projection quality remains an important future topic, but Part 6 intentionally defers its full treatment until more implementation and corpus evidence exists.

## 16.7 Mermaid Diagram Convention

Part 6 uses Mermaid diagrams in Markdown code blocks.

This is consistent with the desired authoring workflow because Mermaid diagrams are:

- reviewable as plain text;
- renderable on GitHub;
- easy to diff;
- portable across documentation tools.

Future diagram additions should continue using Mermaid unless a specific companion artifact requires another format.

## 16.8 Non-normative Boundary

Part 6 is guidance, not Core conformance.

Review should ensure that Part 6 does not accidentally introduce mandatory requirements that belong in Part 4.

Potentially normative language should be checked carefully.

In general:

- `should` may express guidance;
- `must` should be avoided unless explicitly referring to Part 4 or another normative source;
- domain-specific requirements should move to profiles;
- CLI behavior should move to CLI contracts;
- POR behavior should move to POR-specific design documents.

## 16.9 Sample and Corpus Alignment

Part 6 now treats examples and corpora as design infrastructure.

The Part 4 normalized samples and manifest are the initial implementation-oriented sample set.

Future work should expand samples into:

- valid cases;
- invalid cases;
- warning cases;
- migration fixtures;
- retrieval scenarios;
- profile-specific examples;
- round-trip formatter fixtures.

This should happen after the CLI validator and formatter begin to stabilize.

## 16.10 Open Review Items

The following items should be reviewed in later passes:

1. Confirm terminology consistency across Part 3, Part 4, Part 5, and Part 6.
2. Check that every Part 6 YAML example is compatible with Part 4 syntax.
3. Decide whether `local activity unit` should appear in Part 3 terminology or remain Part 6 explanatory language.
4. Decide whether the term `Knowledge Reuse Design` should appear in Part 1 or Part 2 as a higher-level framing concept.
5. Review whether the treatment of non-text Entity material needs additional Part 4 representation examples.
6. Add retrieval scenario fixtures once CLI or POR experiments generate real examples.
7. Add invalid and warning samples after validator diagnostics are defined.
8. Confirm that Part 6 does not over-specify POR.
9. Confirm that Part 6 does not define profile rules prematurely.
10. Review all Mermaid diagrams after GitHub rendering.

## 16.11 Recommended Next Step

The recommended next step is not to expand Part 6 further immediately.

Instead, the next useful work is:

1. align Part 6 terminology with Part 3 and Part 5;
2. verify Part 4 samples against the current Part 4 requirements;
3. begin CLI-oriented validator and formatter planning;
4. use implementation feedback to refine samples, warning cases, and migration fixtures.

Part 6 should remain stable enough for now to support implementation planning.
