# 12 — Core Model Summary

**Part:** 3 — Core Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 12.1 Purpose

This section summarizes the IdeaMark Core Model defined in Part 3.

Part 3 translates the philosophical stance of Part 1 and the architectural stance of Part 2 into a conceptual model for IdeaMark documents.

The model is intentionally minimal.

It defines the structural roles needed to support Projection-guided access, traceability, reconstruction, and future Human-AI Intellectual Activity without storing final meaning.

## 12.2 Core Definition

An IdeaMark document is a Projection-shaped access structure produced by Decomposition of Original Source material under Projection Context.

```text
Original Source material
        x
Projection Context
        ↓
Projection-guided Decomposition
        ↓
IdeaMark Document
```

The document preserves structures that help later humans, AI systems, and tools return to relevant Original Source material and generate activation expressions.

It is not a knowledge base, summary, ontology, source replacement, or final interpretation.

## 12.3 Central Objects

The central Core Model objects are:

```text
meta
sections
occurrences
entities
```

Optional or profile-defined structures may include:

```text
structure
status
local rationale
review notes
extension fields
```

The central structural interpretation is:

```text
Section
  = Projection-shaped local source window

Occurrence
  = role-bearing placement of reusable material within that window

Entity
  = reusable material shaped by Projection and available for later reconstruction
```

## 12.4 Original Source

Original Source material is any accessible material that can participate in Projection-guided Human-AI Intellectual Activity.

Original Sources may include text, code, images, audio, video, datasets, sensor logs, conversations, generated artifacts, composite materials, or future accessible media.

An IdeaMark document does not replace Original Source material.

It preserves traceable access paths back to source material.

## 12.5 Projection Context

Projection Context shapes Decomposition.

It determines what material is useful, how local source windows are created, what reusable material becomes Entity-like, and what Occurrence roles matter.

Part 3 does not define Projection authoring, evaluation, governance, lifecycle, or library membership.

Those belong primarily to Part 5 or to profiles and implementations.

## 12.6 Decomposition

Decomposition is the Projection-guided structuring act that produces an IdeaMark document.

It is not general extraction.

It is not final meaning extraction.

It is not required to be fully reversible.

Decomposition may be performed by humans, AI systems, tools, POR-like workflows, or mixed processes.

Part 3 defines the conceptual products and invariants of Decomposition, not its algorithm.

## 12.7 IdeaMark Document

An IdeaMark document is an operational snapshot.

It records a Projection-guided structuring result at a particular time, from particular source material, under particular context.

Multiple valid IdeaMark documents may exist for the same Original Source.

Different Projections may produce different valid documents.

Regenerated documents may coexist with earlier documents.

## 12.8 Section

A Section is a Projection-shaped local source window.

It is the primary local access unit of the document.

It may align with a source heading, but it is not defined by source headings.

It should preserve a useful local context for later reconstruction.

Section-level anchorage is the primary Core expectation.

## 12.9 Occurrence

An Occurrence is a role-bearing placement of Entity material within a Section.

It explains how reusable material participates in a local source window under a Projection.

It is not merely a textual occurrence or source appearance.

Occurrence roles are not universal Core vocabulary.

They are shaped by Projection, profile, domain practice, or implementation convention.

## 12.10 Entity

An Entity is Projection-shaped reusable material.

It is not final meaning, a universal semantic object, or an ontology node by default.

Entity identity is local unless a profile defines stronger identity rules.

An Entity becomes locally useful through Occurrence placement in Section context.

## 12.11 Anchorage and Traceability

Anchorage is the Core Model's traceability mechanism.

An anchor is a traceability claim connecting an IdeaMark structure to Original Source material.

Anchors are not limited to line ranges or text spans.

They may be exact, approximate, composite, inferred, or tool-specific.

Traceability is more important than semantic completeness.

## 12.12 Status, Versioning, and Regeneration

Status and versioning keep IdeaMark operational.

They support review, comparison, regeneration, deprecation, supersession, and reuse.

Status is operational metadata, not truth.

Regeneration may produce a different valid document rather than correcting an earlier document toward one final representation.

Core does not require stable IDs across regeneration.

## 12.13 Non-required Core Namespaces

Part 3 v1.2.0 does not require the following as Core namespaces:

- Relation;
- Perspective;
- Provenance.

Relation-like structures may be added as extensions, profiles, companion specifications, or implementation indexes.

Perspective and Provenance responsibilities are handled through metadata, Projection references, source references, anchors, generation notes, local rationale, status, and profile-defined extensions.

## 12.14 Minimal Conceptual Shape

The minimal conceptual shape of an IdeaMark document is:

```text
IdeaMark Document
  meta
    sources
    projections
    status/version context
  sections
    Section = Projection-shaped local source window
  occurrences
    Occurrence = role-bearing placement within Section
  entities
    Entity = Projection-shaped reusable material
```

A YAML-like illustrative shape is:

```yaml
meta:
  document_id:
  spec_version:
  status:
  sources:
  projections:

sections:
  SEC-001:
    source_anchor:
    occurrences:
      - OCC-001

occurrences:
  OCC-001:
    entity: IE-001
    role:

entities:
  IE-001:
    kind:
    content:
```

This is illustrative.

Part 4 defines normative YAML representation.

## 12.15 Core Success Condition

The Core Model succeeds when an IdeaMark document helps a later user or tool:

```text
identify the document
  -> identify relevant Original Sources
  -> identify relevant Projection Context
  -> select useful Sections
  -> inspect Occurrence roles
  -> use Entity material
  -> follow anchors back to source material
  -> reconstruct useful activation expressions
  -> support Human-AI Intellectual Activity
```

The document is not expected to complete this activity by itself.

It is expected to reduce the cost of beginning it.

## 12.16 Final Summary

IdeaMark Core v1.2.0 Part 3 defines a minimal model for Projection-shaped access structures.

It preserves a disciplined separation between:

- source material;
- Projection;
- Decomposition;
- generated access structures;
- reconstruction;
- meaning activation.

The model is centered on:

```text
Section = Projection-shaped local source window
Occurrence = role-bearing placement within that window
Entity = Projection-shaped reusable material
```

This structure allows IdeaMark to support reusable knowledge work without pretending that meaning can be fully stored, extracted, or finalized inside the document itself.
