# IdeaMark Core Specification v1.2.0 (Draft)

## 1. Purpose

IdeaMark Core is **not a knowledge representation format**.

It is a structural representation of **Intellectual Activities** that
enables humans and AI to rediscover, reinterpret and reuse original
sources under new situations.

Meaning is **not stored** inside IdeaMark. Meaning is reconstructed
later by combining:

-   Original Sources
-   Projection
-   Current Situation
-   Interpreter (Human or AI)

Original sources remain the authoritative source of meaning.

------------------------------------------------------------------------

## 2. Core Principles

1.  Separate structure from meaning.
2.  Preserve reusable intellectual activity instead of fixed
    interpretation.
3.  Projection determines how intellectual activities are extracted.
4.  Original sources remain authoritative.
5.  IdeaMark cooperates with LLMs rather than replacing them.
6.  IdeaMark documents are replaceable snapshots, not immutable
    knowledge artifacts.

------------------------------------------------------------------------

## 3. Conceptual Model

    Original Sources
            │
            ▼
     Projection
            │
            ▼
       IdeaMark
     (Intellectual Activity Index)
            │
            ▼
     Retrieval
            │
            ▼
     Original Sources
            │
            ▼
     Human / AI
            │
            ▼
     Meaning Reconstruction

------------------------------------------------------------------------

## 4. Core Components

### Entity

Reusable reasoning component.

### Occurrence

Reusable reasoning episode describing how one or more Entities
participate together within an intellectual activity.

### Section

A local coordinate frame inside the intellectual activity represented by
a Projection.

Sections organize reasoning episodes rather than document chapters.

### Anchorage

Coordinates describing where a Section belongs within the local
intellectual activity.

Core defines only the representation mechanism. Coordinate vocabularies
are intentionally external and Projection-dependent.

### Projection

A reusable Knowledge Accessibility Strategy.

Projection determines:

-   reusable entities
-   entity granularity
-   reasoning episodes
-   section organization
-   retrieval objectives

Projection is an independent reusable intellectual asset.

------------------------------------------------------------------------

## 5. Original Sources

IdeaMark never replaces original sources.

Entities SHOULD reference original material through payload references
whenever possible.

------------------------------------------------------------------------

## 6. Lifecycle

IdeaMark documents are operational snapshots.

Implementations MAY:

-   regenerate
-   replace
-   coexist
-   version

IdeaMark documents according to changes in source material, projections
and organizational needs.

------------------------------------------------------------------------

## 7. AI Collaboration

IdeaMark assumes AI-assisted use.

Typical workflow:

Situation → Projection → Temporary IdeaMark → Retrieval → Original
Sources → LLM → Situation-specific guidance

Small on-device LLMs and large cloud LLMs benefit equally because
IdeaMark reduces the search space while preserving traceability to
original sources.

------------------------------------------------------------------------

## 8. Design Goals

-   Intellectual Activity representation
-   Projection-driven authoring
-   Payload-agnostic architecture
-   Human/AI collaborative retrieval
-   Cross-domain knowledge accessibility
-   Replaceable operational indexes
-   Long-term interoperability
