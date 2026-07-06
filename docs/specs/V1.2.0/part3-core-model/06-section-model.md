# 06 — Section Model

**Part:** 3 — Core Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 6.1 Purpose

This section defines the conceptual role of Section in the IdeaMark Core Model.

A Section is the primary local access unit of an IdeaMark document.

It groups or points to Original Source material under a Projection-shaped local context so that later reconstruction can begin from a bounded, traceable window.

A Section is not a source heading, document chapter, topic label, final interpretation, or meaning unit.

## 6.2 Definition

A Section is a Projection-shaped local source window.

It is produced by Projection-guided Decomposition and exists to make some part, combination, or view of Original Source material useful for later retrieval, reconstruction, and activation expression generation.

A Section may contain or reference:

- a local identifier;
- title or label;
- source anchors;
- Occurrence references;
- local rationale;
- ordering or grouping information;
- status or review notes;
- extension metadata.

Part 4 defines concrete YAML representation.

## 6.3 Section as Local Source Window

A Section should be understood as a bounded window over source material.

The boundary is shaped by Projection.

It may correspond to:

- a single source span;
- multiple source spans;
- a source heading;
- a fragment inside a heading;
- a source region that crosses headings;
- a code symbol and nearby comments;
- a recipe ingredient line and related step;
- a media time range;
- an image region;
- a dataset fragment;
- a composite of multiple sources.

The Section boundary is determined by expected reconstruction usefulness, not by source layout alone.

## 6.4 Section Is Not a Source Heading

A Section may align with a source heading, but it is not defined by source headings.

For example:

- in an RFC, one Projection may create Sections around design rationale, while another creates Sections around migration impact;
- in source code, one Projection may create Sections around performance decisions, while another creates Sections around API design;
- in a recipe, one Projection may create Sections around execution order, while another creates Sections around ingredient function;
- in a database subsystem, one Projection may create Sections around correctness invariants, while another creates Sections around state transitions.

Therefore, copying the Original Source outline is not sufficient to define Sections.

## 6.5 Section and Projection

Projection determines what a Section is useful for.

A Section should preserve local source context that is useful under the generation Projection.

Different Projections over the same Original Source may produce different Section sets.

The same source fragment may participate in multiple Sections across different generated documents or within a multi-Projection document.

A Section should therefore be interpreted relative to:

- document metadata;
- Original Source references;
- generation Projection Context;
- source anchors;
- contained Occurrences;
- later reconstruction use.

## 6.6 Section and Decomposition

A Section is a Decomposition product.

It is not assumed to exist in the Original Source before Decomposition.

Decomposition may create a Section by:

- selecting a contiguous source fragment;
- grouping non-contiguous fragments;
- combining source material across media;
- organizing material by Projection focus;
- grouping Occurrences that support a future reconstruction activity;
- preserving a source window for later investigation.

Part 3 does not prescribe how Section boundaries are determined algorithmically.

## 6.7 Section and Occurrence

A Section contains or references Occurrences.

An Occurrence is a role-bearing placement of Entity material within a Section.

The Section provides the local context in which the Occurrence role is meaningful.

Without Section context, an Occurrence may lose its reconstruction function.

For example, the same recipe ingredient may be placed in:

- an execution Section as a timed cooking step;
- a substitution Section as an ingredient function;
- a dietary Section as an allergen or constraint flag.

The Section determines the local window in which the placement should be interpreted.

## 6.8 Section and Entity

A Section does not directly have to contain all Entity material.

It may reference Occurrences, and those Occurrences may reference Entities.

This separation allows Entity-like material to appear in different Section contexts under different roles.

However, Core does not require global Entity reuse.

Entity identity may remain local to the document or implementation-defined scope.

## 6.9 Section and Source Anchor

A Section should normally preserve traceability to Original Source material.

Section-level anchoring is the primary Core expectation because a Section is a local source window.

A Section source anchor may be:

- exact;
- approximate;
- composite;
- inferred;
- tool-specific;
- human-readable;
- machine-resolvable.

A Section may have multiple anchors.

A Section may also be anchored indirectly through Occurrences or Entities when appropriate, but lack of any traceability weakens its Core function.

## 6.10 Section and Local Rationale

A Section may include local rationale.

Local rationale may explain:

- why the source material was grouped;
- why this window is useful under the Projection;
- how the Section should support future reconstruction;
- why the anchor is approximate;
- why certain related source material was omitted;
- what kind of activation expression the Section may support.

Local rationale is not required by Core unless a profile requires it.

However, it can improve review, debugging, and reuse.

## 6.11 Section and Structure

The optional `structure` area may record ordering or grouping of Sections.

Section order may matter when:

- reconstruction should follow a teaching sequence;
- procedural execution order matters;
- design rationale builds on earlier material;
- state transitions must be navigated in order;
- review workflows need a stable document order.

Part 3 does not require that Section order represent source order.

Section order may be Projection-shaped.

## 6.12 Section Identity

A Section should have an identifier within the IdeaMark document.

Core does not require Section identity to be globally stable across documents, repositories, or regenerations.

A Section ID is primarily a reference label.

Implementations or profiles may define stronger identity rules when needed.

Regeneration may preserve, change, split, merge, or remove Section IDs.

Status and revision metadata may help compare regenerated documents.

## 6.13 Section Granularity

Section granularity is Projection-dependent.

A Section should be large enough to preserve useful local context and small enough to support efficient retrieval and reconstruction.

Too-large Sections may become unhelpful containers.

Too-small Sections may lose context and force later reconstruction to repeat too much work.

Core does not define universal granularity rules.

Projection libraries, authoring profiles, or implementations may define granularity guidance.

## 6.14 Section Completeness

A Section is not required to completely represent all source material related to its topic.

It only needs to preserve a useful local source window under the Projection.

A Section may be partial, draft, or exploratory.

However, a Section that lacks traceability, Occurrences, or useful local context may fail to function as a Core Section.

## 6.15 Multi-source Sections

A Section may refer to multiple Original Sources.

This may be necessary when:

- a code implementation and design document are used together;
- data and prose evidence are combined;
- two documents are compared;
- an image and caption are interpreted together;
- a recipe step and ingredient list are combined;
- an earlier IdeaMark document is used with its source material.

A multi-source Section should preserve enough anchor information to distinguish which material came from which source.

## 6.16 Multi-projection Sections

A Section is usually shaped by a generation Projection.

However, in a multi-Projection document, different Sections may be shaped by different Projection Contexts.

A Section may therefore need local Projection metadata or reference to document-level Projection entries.

Part 3 allows this conceptually.

Part 4 may define representation details.

## 6.17 Weak or Invalid Sections

A Section may be weak if it:

- has no clear Projection-shaped purpose;
- merely copies a source heading without reuse function;
- lacks traceability to source material;
- contains no Occurrences or useful local material;
- stores final interpretation without source return path;
- cannot support later retrieval or reconstruction.

Part 4 or profiles may define validation levels.

Part 3 identifies these conceptual risks.

## 6.18 Conceptual Example

The following shape is illustrative:

```yaml
sections:
  SEC-001:
    title: Comparison-cost-aware sift strategy
    source_anchor:
      source: SRC-heapq-py
      line_ranges:
        - start: 58
          end: 95
    occurrences:
      - OCC-004
      - OCC-005
      - OCC-006
    rationale: |
      This Section groups source commentary and implementation material useful for reconstructing a performance-engineering explanation.
```

This example is not normative YAML.

Part 4 defines concrete syntax.

## 6.19 Invariants

A Section should preserve the following invariants:

1. A Section is produced by Projection-guided Decomposition.
2. A Section is a Projection-shaped local source window.
3. A Section is not necessarily a source heading or document chapter.
4. A Section should support traceability to Original Source material.
5. A Section provides local context for Occurrence roles.
6. A Section may combine multiple source fragments or sources.
7. Section order is Projection-shaped and need not match source order.
8. Section identity is local unless a profile defines stronger identity rules.
9. A Section does not store final meaning.
10. A Section should reduce the cost of later reconstruction.

## 6.20 Summary

Section is the Core Model's local source-window object.

It is the primary structure that lets IdeaMark preserve Projection-shaped access without becoming a summary or knowledge base.

A good Section helps later humans, AI systems, or tools reopen the right source material under the right Projection-shaped context.
