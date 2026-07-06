# 02 — Original Source Reference Model

**Part:** 3 — Core Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 2.1 Purpose

This section defines the conceptual role of Original Source references in the IdeaMark Core Model.

An IdeaMark document is generated from Original Source material under a Projection Context.

The document does not replace the Original Source.

It preserves structures that help future humans, AI systems, and tools return to relevant source material and reconstruct useful activation expressions.

Therefore, Original Source references and source anchors are central to IdeaMark's traceability model.

## 2.2 Definition

An Original Source is any accessible material that can participate in Projection-guided Human-AI Intellectual Activity.

An Original Source Reference is a document-level or local reference to that material.

It provides enough information for later systems or users to identify, retrieve, inspect, or reopen the source material when needed.

An Original Source Reference is not a claim that the source is universally true, authoritative, complete, or final.

It is a traceable reference to material used or made available for Projection-guided Decomposition and later reconstruction.

## 2.3 Media Independence

Original Sources are not limited to text.

They may include:

- prose documents;
- source code;
- configuration files;
- images;
- audio;
- video;
- datasets;
- database records;
- sensor logs;
- interaction histories;
- chat transcripts;
- generated artifacts;
- diagrams;
- spreadsheets;
- recipes;
- composite source bundles;
- future media that can be made accessible.

Part 3 must not make line numbers, paragraphs, or text offsets the hidden default for all sources.

Text anchors are one case of source anchoring, not the general model.

## 2.4 Accessibility Requirement

A material can be conceptually imagined as a future Original Source only if it can be made accessible to humans, AI systems, or supporting tools.

For practical current workflows, source material must be accessible enough to support:

- observation;
- reference;
- transformation;
- input to Decomposition;
- later retrieval;
- later reconstruction.

For example:

- a text file can be referenced by path, revision, and line ranges;
- a video can be referenced by file identity and time range;
- an image can be referenced by file identity and region;
- a dataset can be referenced by table, row, column, or query;
- a recipe can be referenced by ingredient line or step number;
- a code file can be referenced by repository, path, revision, and symbol or span.

If a material cannot be observed, referenced, transformed, or supplied to a reconstruction process, it may be conceptually interesting but is not practically usable as an Original Source in current IdeaMark workflows.

## 2.5 Original Source Reference Responsibilities

An Original Source Reference should support the following responsibilities:

1. **Identification** — distinguish this source from other sources.
2. **Retrieval** — allow later users or tools to locate or reopen the source where possible.
3. **Revision awareness** — identify which version, revision, timestamp, or snapshot was used when relevant.
4. **Media description** — indicate the type or form of the source material.
5. **Traceability support** — provide a base for source anchors used by Sections, Occurrences, Entities, or metadata.
6. **Composite support** — allow one IdeaMark document to reference multiple sources.
7. **Non-authority stance** — avoid implying that source reference equals universal truth.

Part 3 defines these responsibilities conceptually.

Part 4 may define the concrete YAML fields.

## 2.6 Source Identity

Source identity should be sufficient for later reconstruction, but Core does not require a universal identity system for all source materials.

Possible identity components include:

- local file path;
- URI;
- repository name;
- repository path;
- commit hash or revision;
- document ID;
- content hash;
- dataset ID;
- media file ID;
- timestamp;
- storage locator;
- external catalog ID;
- implementation-defined source ID.

The appropriate identity components depend on source type, storage practice, and implementation profile.

Core only requires that the IdeaMark document can refer to Original Sources consistently enough for traceability and reconstruction.

## 2.7 Source Revision

Original Sources may change over time.

When source revision matters, an Original Source Reference should identify the source version used for Decomposition.

Revision indicators may include:

- Git commit hash;
- version number;
- timestamp;
- content hash;
- immutable object ID;
- dataset snapshot ID;
- document revision ID;
- archival locator;
- implementation-defined revision marker.

A later reconstruction may use:

- the same source revision;
- a newer source revision;
- an archived source snapshot;
- a derived source representation;
- another source judged compatible by implementation or Projection logic.

Part 3 does not prescribe revision resolution algorithms.

It only requires that the model can record source revision information when needed.

## 2.8 Source Anchors

A source anchor is a traceability claim connecting part of an IdeaMark document to part of an Original Source.

A source anchor may be attached to:

- a Section;
- an Occurrence;
- an Entity;
- document metadata;
- local rationale;
- optional structure entries;
- extension objects.

Section-level anchors are the primary expectation because Section functions as a Projection-shaped local source window.

However, more precise anchors may be attached to Occurrences or Entities when useful.

## 2.9 Anchor Forms

Source anchors must be media-independent.

Possible anchor forms include:

```yaml
line_range:
  start: 58
  end: 95
```

```yaml
paragraph_range:
  start: 3
  end: 5
```

```yaml
code_symbol:
  language: python
  symbol: heapq._siftup
```

```yaml
media_time_range:
  start: 00:01:12
  end: 00:02:05
```

```yaml
image_region:
  x: 120
  y: 80
  width: 300
  height: 200
```

```yaml
dataset_fragment:
  table: observations
  rows: [100, 101, 102]
  columns: [timestamp, temperature]
```

```yaml
recipe_fragment:
  ingredients: [miso paste]
  steps: [6]
```

These examples are conceptual.

Part 4 may define specific representation forms.

## 2.10 Exact, Approximate, and Composite Anchors

Not all source anchors can be exact.

Part 3 should allow:

- exact anchors;
- approximate anchors;
- inferred anchors;
- composite anchors;
- tool-specific anchors;
- human-readable anchors;
- machine-resolvable anchors.

A composite anchor may refer to multiple source fragments.

For example, a recipe Section about ingredient substitution may refer to both the ingredient line and the step where the ingredient is used.

A code Section about an optimization decision may refer to both a function implementation and a nearby explanatory comment.

A design RFC Section about migration impact may refer to examples, syntax rules, statistics, and unresolved questions.

## 2.11 Multi-source Documents

One IdeaMark document may reference multiple Original Sources.

This is necessary for cases such as:

- comparing documents;
- synthesizing evidence;
- tracing code and design documentation together;
- combining data and narrative explanation;
- reconstructing activity from multiple media;
- using one IdeaMark document as a source for another.

Part 3 does not require a universal multi-source aggregation model.

It only requires that each source can be referenced and that local anchors can identify which source they refer to.

## 2.12 Original Source and Projection

Original Source material is not decomposed in isolation.

Its relevance depends on Projection Context.

The same Original Source may produce different IdeaMark documents under different Projections.

For example:

- a code file may produce an algorithm-learning document under one Projection and an API-design document under another;
- a database subsystem file may produce a correctness-invariant document under one Projection and a state-machine document under another;
- an RFC may produce a language-design rationale document under one Projection and a migration-impact document under another;
- a recipe may produce a cooking-execution document under one Projection and an ingredient-substitution document under another.

Original Source Reference therefore records what material was available, while Projection Context explains why particular parts became useful.

## 2.13 Original Source and Authority

Referencing an Original Source does not mean Core treats it as universal truth.

An Original Source may be:

- authoritative in a local context;
- partial;
- outdated;
- contested;
- speculative;
- generated;
- erroneous;
- useful only under a specific Projection.

Part 3 does not define source authority ranking.

Authority, trust, quality, legal appropriateness, and social legitimacy belong to Projection practice, domain practice, governance, or implementation policy.

Core only requires traceability.

## 2.14 Original Source as Future IdeaMark Input

An IdeaMark document may itself become an Original Source for later IdeaMark generation.

This recursive possibility does not make IdeaMark a knowledge base.

It means that an IdeaMark document, like any other artifact, can become material for later Projection-guided Decomposition.

When this happens, the later IdeaMark document should reference the earlier document as an Original Source and may also preserve references to the earlier document's own sources if useful.

## 2.15 Conceptual Minimum

At the conceptual level, an Original Source Reference should provide enough information for:

```text
later user or tool
  -> identify source
  -> locate or reopen source when possible
  -> understand source type or medium
  -> resolve source anchors
  -> support reconstruction under a Projection
```

Part 4 may choose concrete fields such as:

```yaml
sources:
  - id:
    type:
    uri:
    revision:
    media_type:
    description:
```

This example is illustrative, not normative for Part 3.

## 2.16 Invariants

Original Source references should preserve the following invariants:

1. An IdeaMark document does not replace Original Source material.
2. Traceability to Original Source material is more important than semantic completeness.
3. Source references should be media-independent.
4. Source anchors are traceability claims, not only text spans.
5. One IdeaMark document may reference multiple Original Sources.
6. The same Original Source may support multiple IdeaMark documents under different Projections.
7. Referencing a source does not imply universal truth or authority.
8. Source revision should be recorded when relevant to reconstruction.
9. An IdeaMark document may itself become an Original Source for later Decomposition.

## 2.17 Summary

Original Source Reference is the Core Model's connection back to the material from which Projection-guided Decomposition begins.

It must be flexible enough for many media types and precise enough to support traceability.

Part 3 defines Original Source Reference conceptually.

Part 4 will define concrete YAML representation.
