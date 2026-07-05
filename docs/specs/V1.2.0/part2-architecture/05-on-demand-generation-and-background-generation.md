# 5. On-demand Generation and Background Generation

**Part:** 2 — Architecture of Human-AI Co-evolution  
**Status:** Draft Rev002  
**Type:** Informative / Reference Architecture

IdeaMark documents may be generated before they are needed, at the moment they are needed, or temporarily during reconstruction.

Part 2 does not require one generation mode.

Different systems may combine modes according to source volume, Projection stability, cost, latency, review requirements, and organizational practice.

## 5.1 Purpose

This section explains how generation timing affects the architecture.

The purpose is not to define a job scheduler, database strategy, cache policy, or performance model.

The purpose is to clarify that IdeaMark generation may occur at different points in the reconstruction ecosystem while preserving the same architectural role: creating reusable access structures that help humans and AI systems return to Original Sources under a Projection.

## 5.2 Background Generation

Background generation creates IdeaMark documents before a specific reconstruction request occurs.

```text
Original Source Collection
        x
Projection Library
        ↓
Scheduled or Prioritized Generation
        ↓
IdeaMark Document Set
```

Background generation may be useful when:

- source collections are stable;
- Projections are known in advance;
- low-latency retrieval is important;
- human review is required before use;
- organizational standards define common Projections;
- repeated use is expected.

Background generation may reduce reconstruction latency because access structures already exist when needed.

However, it may also create documents that are never used.

Part 2 does not prescribe whether this trade-off is worthwhile.

## 5.3 Prioritized Background Generation

Full background generation may be expensive when there are many sources and many Projections.

A system may therefore prioritize generation.

Prioritization may consider:

- source importance;
- source recency;
- source authority within a domain or Projection-guided construction;
- Projection demand;
- user role;
- organizational policy;
- expected retrieval frequency;
- review capacity;
- cost constraints;
- risk level.

Prioritization is an implementation concern.

The architectural concern is that generation can be partial while still supporting later reconstruction.

## 5.4 On-demand Generation

On-demand generation creates an IdeaMark document when a reconstruction activity requires it.

```text
Current Situation
        ↓
Projection Selection or Generation
        ↓
Missing or Insufficient IdeaMark Document
        ↓
On-demand Generation
        ↓
Original Source Access and Reconstruction
```

On-demand generation may be useful when:

- the current Situation is novel;
- a needed Projection did not exist previously;
- the source collection is too large for full pre-generation;
- source material changes frequently;
- exploratory reconstruction is more important than persistence;
- the system wants to avoid generating unused documents.

On-demand generation may increase latency, but it can improve adaptability.

Part 2 does not define latency requirements.

## 5.5 Temporary Generation

Temporary generation creates an IdeaMark document or document-like structure for short-term use.

It may be used within a single conversation, analysis session, experiment, or workflow.

A temporary IdeaMark document may be discarded, preserved, reviewed, or promoted into a repository.

Temporary generation is useful when the system or user is still exploring which Projection or structure is useful.

It allows IdeaMark-style reconstruction support without requiring immediate long-term persistence.

## 5.6 Regeneration

Regeneration creates a new IdeaMark document for a source-projection combination that already has an earlier document.

Regeneration may occur because:

- the Original Source changed;
- the Projection changed;
- a better generation method became available;
- human review identified problems;
- retrieval logs showed poor access behavior;
- new reconstruction requirements emerged;
- previous documents were too broad, too narrow, or misleading.

Regeneration does not automatically invalidate earlier documents.

Earlier documents may remain useful for historical comparison, previous Projections, reproducibility, or different reconstruction activities.

## 5.7 Hybrid Generation

Many implementations may combine generation modes.

For example:

- common Projections may be generated in the background;
- rare Projections may be generated on demand;
- exploratory Projections may be temporary;
- reviewed documents may be preserved;
- low-quality generated documents may be replaced;
- high-value sources may receive deeper generation and review.

Hybrid generation is expected.

IdeaMark Core should not assume a single generation strategy.

## 5.8 Generation Timing and Projection Evolution

Projection evolution affects generation timing.

If a Projection library changes, some previously generated IdeaMark documents may need regeneration.

If a new Projection is created during reconstruction, on-demand or temporary generation may be appropriate.

If a Projection becomes organizationally important, background generation may become worthwhile.

Thus generation timing is not fixed.

It may change as Projections mature, usage patterns change, and the human-AI ecosystem evolves.

## 5.9 Generation Timing and Source Authority

Regardless of generation timing, an IdeaMark document is not itself the authority for meaning.

The relevant Original Source remains the material basis to which reconstruction should remain traceable for the selected Projection.

A background-generated IdeaMark document is not more authoritative simply because it already exists.

An on-demand-generated document is not less useful simply because it was created during a request.

A temporary document is not final, but it may still support useful reconstruction if it preserves source access and Projection context.

The architectural value of a generated document depends on its ability to support traceable reconstruction, not on its generation timing alone.

## 5.10 Non-goals

This section does not define:

- scheduling mechanisms;
- queue architecture;
- batch processing frameworks;
- cache policies;
- cost models;
- persistence rules;
- latency targets;
- invalidation protocols;
- background worker designs;
- model orchestration strategies.

These are implementation concerns.

## 5.11 Design Rationale

IdeaMark documents are operational snapshots.

Because sources, Projections, users, AI systems, and reconstruction needs evolve, generation timing should remain flexible.

A rigid requirement to precompute everything would make IdeaMark unnecessarily expensive.

A rigid requirement to generate everything on demand would make some review and low-latency use cases difficult.

The architecture therefore allows multiple generation modes while keeping the purpose constant: support future reconstruction from Original Sources through Projection.

This flexibility also controls interpretation cost across the lifecycle: systems may spend cost earlier for review and latency, later for adaptability, or temporarily for exploration.

## 5.12 Summary

IdeaMark generation may be background, prioritized, on-demand, temporary, regenerative, or hybrid.

These modes are implementation choices.

The Core architectural concern is that generated IdeaMark documents remain reusable access structures that support traceable reconstruction under current Situations and Projections.
