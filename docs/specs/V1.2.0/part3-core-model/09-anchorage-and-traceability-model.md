# 09 — Anchorage and Traceability Model

**Part:** 3 — Core Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 9.1 Purpose

This section defines anchorage and traceability in the IdeaMark Core Model.

An IdeaMark document does not replace Original Source material.

It must therefore preserve enough traceability for later humans, AI systems, and tools to return to relevant Original Source material during reconstruction.

Anchorage is the Core Model mechanism for expressing that traceability.

## 9.2 Definition

An anchor is a traceability claim connecting an IdeaMark structure to Original Source material.

An anchor may identify source material exactly, approximately, indirectly, or through implementation-defined locators.

Anchorage is not limited to text spans or line ranges.

A text line range is only one possible anchor form.

## 9.3 Traceability Responsibility

Traceability is a Core responsibility because IdeaMark is a source-mediated access structure.

An IdeaMark document should help later reconstruction answer:

```text
Which Original Source material should be reopened, inspected, or transformed?
```

Traceability is more important than semantic completeness.

A document that contains well-written Entities but cannot return to Original Source material is weak as an IdeaMark document.

## 9.4 Anchor Targets

Anchors may connect to many kinds of Original Source material, including:

- text spans;
- paragraphs;
- source headings;
- code spans;
- code symbols;
- repository paths;
- commit revisions;
- media time ranges;
- audio segments;
- video segments;
- image regions;
- dataset rows;
- dataset columns;
- database query results;
- spreadsheet cells or ranges;
- recipe ingredients;
- recipe steps;
- conversation turns;
- sensor log ranges;
- composite source fragments;
- generated artifacts;
- earlier IdeaMark documents.

Core must remain media-independent.

## 9.5 Anchor Attachment Points

Anchors may be attached to different parts of an IdeaMark document.

Possible attachment points include:

- document metadata;
- Original Source references;
- Sections;
- Occurrences;
- Entities;
- local rationale;
- optional structure entries;
- extension objects.

Section-level anchors are the primary Core expectation because a Section is a Projection-shaped local source window.

Occurrence-level and Entity-level anchors may provide more precise traceability when useful.

## 9.6 Section-level Anchors

A Section should normally have source anchorage.

Because a Section is a local source window, its anchor identifies the source material that the window opens.

A Section-level anchor may refer to:

- one source fragment;
- multiple source fragments;
- one source object;
- multiple source objects;
- an approximate source region;
- a logical source unit;
- a composite of heterogeneous media fragments.

A Section without any source traceability may still exist in a draft or speculative document, but it is weak as a Core Section.

## 9.7 Occurrence-level Anchors

An Occurrence may have source anchorage.

Occurrence-level anchorage is useful when the role-bearing placement depends on a specific source fragment.

For example:

- a performance rationale may point to a specific code comment;
- a state transition may point to a state diagram line;
- a recipe timing constraint may point to a specific step;
- an RFC migration impact may point to a syntax example;
- a dataset-derived claim may point to specific rows or columns.

Occurrence-level anchors are not always required if the Section anchor provides sufficient source context.

## 9.8 Entity-level Anchors

An Entity may have source anchorage.

Entity-level anchorage is useful when the reusable material is directly derived from source material.

For example:

- a design rule copied or normalized from a specification;
- a code symbol extracted from source;
- an ingredient function inferred from recipe text;
- an evidence item derived from a report paragraph;
- a dataset feature derived from a table column.

Entity-level anchorage should not imply that the Entity stores final meaning.

It only indicates where the reusable material can be traced.

## 9.9 Metadata-level Anchors

Metadata may contain source-level or document-level anchors.

These may identify:

- source files;
- repository revisions;
- dataset snapshots;
- document versions;
- media file identifiers;
- generation source bundles;
- parent IdeaMark documents.

Metadata-level anchors provide global context.

Local anchors on Sections, Occurrences, or Entities provide more precise reconstruction paths.

## 9.10 Exact Anchors

An exact anchor identifies a source fragment precisely enough for deterministic retrieval or inspection.

Examples include:

```yaml
line_range:
  start: 58
  end: 95
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
spreadsheet_range:
  sheet: Q1
  range: B2:D20
```

Exact anchors are valuable when source media and tools support them.

Core should not require all anchors to be exact.

## 9.11 Approximate Anchors

An approximate anchor identifies a source region without claiming exact boundaries.

Approximate anchors may be needed when:

- source media lacks stable offsets;
- OCR or transcription is uncertain;
- the source is a conversation or stream;
- source fragments are inferred;
- a human author only knows an approximate location;
- the document is draft or exploratory.

Approximate anchors should be marked or described when possible.

Approximation is preferable to losing traceability entirely.

## 9.12 Composite Anchors

A composite anchor refers to multiple source fragments.

Composite anchors are important because Projection-shaped Sections often combine source material that is not contiguous.

Examples:

- a code implementation and a nearby design comment;
- an RFC summary, detailed design, and unresolved question;
- a recipe ingredient line and its later cooking step;
- a dataset column and a report paragraph;
- an image region and a caption;
- multiple documents used for comparison.

Composite anchors should preserve the identity of each referenced source fragment.

## 9.13 Inferred Anchors

Some structures are inferred from source material rather than directly copied.

An inferred anchor records the source material that supports or motivates the inference.

For example:

- an ingredient function inferred from recipe steps;
- a migration impact inferred from an RFC syntax change;
- a performance concern inferred from implementation comments;
- a risk flag inferred from multiple evidence fragments.

Inferred anchors should not present inference as final meaning.

They should preserve enough traceability for later review.

## 9.14 Tool-specific Anchors

Some anchors may depend on specific tools or storage systems.

Examples include:

- database record IDs;
- search index offsets;
- vector store chunk IDs;
- document processing node IDs;
- OCR bounding boxes;
- media transcript IDs;
- GitHub blob references;
- implementation-specific source locators.

Core should allow tool-specific anchors as extensions or profile-defined forms.

However, tool-specific anchors should be accompanied by human-readable or source-reference context when practical.

## 9.15 Anchor Stability

Anchors may become stale when sources change.

For example:

- line numbers may shift;
- documents may be edited;
- media may be re-encoded;
- datasets may be regenerated;
- repository paths may change;
- web resources may disappear.

Source revision metadata improves anchor stability.

When possible, anchors should be tied to immutable or versioned source references.

Part 3 does not define anchor repair algorithms.

## 9.16 Anchor and Source Revision

Anchors should be interpreted relative to source revision.

A line range in one revision may not refer to the same material in another revision.

Therefore, document metadata or source references should record revision information when needed.

Possible revision indicators include:

- commit hash;
- content hash;
- timestamp;
- version number;
- dataset snapshot ID;
- document revision ID;
- archival locator;
- implementation-defined revision marker.

## 9.17 Anchor and Reconstruction

Anchors support reconstruction by enabling later users or tools to return to source material.

During reconstruction, a system may:

- search IdeaMark metadata;
- select relevant Sections;
- follow Section anchors;
- inspect Occurrence roles;
- inspect Entity material;
- reopen source fragments;
- generate an activation expression under a Projection.

Anchors do not themselves perform reconstruction.

They preserve the return path.

## 9.18 Anchor and Review

Anchors support review.

A reviewer may use anchors to check:

- whether a Section source window is appropriate;
- whether an Occurrence role is supported;
- whether an Entity payload overstates the source;
- whether inferred material is justified;
- whether source revision has changed;
- whether a regenerated document preserves expected traceability.

Poor anchorage makes review difficult.

## 9.19 Anchor and Authority

Anchoring to a source does not mean the source is true or authoritative.

An anchor only claims traceability.

Authority, trust, correctness, safety, legal appropriateness, and institutional legitimacy are outside Part 3 Core.

They may be handled by Projection practice, review, governance, domain policy, or implementation metadata.

## 9.20 Weak or Invalid Anchors

An anchor may be weak if it:

- cannot identify the source;
- refers to unstable material without revision context;
- is too broad to support reconstruction;
- is too vague to support review;
- points to inaccessible material;
- uses a tool-specific locator with no explanation;
- claims exactness where only approximation is available.

Part 4 or profiles may define validation levels.

Part 3 identifies these conceptual risks.

## 9.21 Conceptual Example

The following shape is illustrative:

```yaml
sections:
  SEC-FUNC-002:
    title: Miso as seasoning and body
    source_anchor:
      source: SRC-recipe-miso-soup-sketch-001
      anchor_type: composite
      fragments:
        - recipe_fragment:
            ingredients: [miso paste]
        - recipe_fragment:
            steps: [6]
    occurrences:
      - OCC-FUNC-004
      - OCC-FUNC-005
```

This example is not normative YAML.

Part 4 defines concrete syntax.

## 9.22 Invariants

Anchorage and traceability should preserve the following invariants:

1. An anchor is a traceability claim to Original Source material.
2. An anchor is not limited to text spans or line ranges.
3. Section-level anchorage is the primary Core expectation.
4. Occurrence-level and Entity-level anchorage may provide precision.
5. Anchors may be exact, approximate, composite, inferred, or tool-specific.
6. Anchors should be interpreted relative to source revision when relevant.
7. Anchoring does not imply universal truth or authority.
8. Anchors support reconstruction and review by preserving source return paths.
9. A document without traceability is weak as an IdeaMark document.
10. Anchor representation details belong to Part 4 or profiles.

## 9.23 Summary

Anchorage is the Core Model's traceability mechanism.

It preserves the ability to return from IdeaMark structures to Original Source material.

A good anchor helps future humans, AI systems, and tools reopen the right source material under the right Projection-shaped context without forcing Core to become text-only, source-replacing, or meaning-storing.
