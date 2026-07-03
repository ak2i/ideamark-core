# IdeaMark Core v1.2.0

## Part 1 --- Philosophy (Draft)

> **Status:** Draft for discussion
>
> This document defines the philosophy and design rationale of IdeaMark
> Core. It intentionally does not define the YAML syntax or validation
> rules.

# 1. What IdeaMark Is

IdeaMark is **not** a knowledge representation format.

IdeaMark is a structural representation of **Intellectual Activities**.

Its purpose is to help humans and AI rediscover, reinterpret, and reuse
intellectual activities recorded in original sources under new
situations.

IdeaMark stores neither truth nor meaning.

Instead, it stores reusable structural traces that guide future
interpreters toward the original sources from which meaning can be
reconstructed.

Original sources remain the authoritative foundation.

------------------------------------------------------------------------

# 2. Motivation

Previous generations of information systems focused on different
problems.

-   Expert systems attempted to preserve explicit knowledge and derive
    answers.
-   Web search made documents discoverable through indexing.
-   Embedding-based retrieval improved semantic similarity.
-   LLMs enabled flexible interpretation and language generation.

IdeaMark addresses a different problem:

> How can intellectual activities performed in one context become
> reusable in another context by people or AI with different
> backgrounds?

------------------------------------------------------------------------

# 3. Core Principles

## Principle 1 --- Separate Structure from Meaning

Meaning depends on:

-   original sources
-   interpreter
-   situation
-   purpose

Therefore IdeaMark represents reusable structures rather than fixed
interpretations.

### Design Rationale

Meaning changes as contexts change. Structural traces are more stable
than interpretations.

------------------------------------------------------------------------

## Principle 2 --- Original Sources Remain Authoritative

IdeaMark never replaces original sources.

Entities should reference original material whenever possible.

### Design Rationale

The source document is the only authoritative basis from which new
interpretations can be reconstructed.

------------------------------------------------------------------------

## Principle 3 --- Projection Defines Accessibility

Projection specifies how intellectual activities are extracted for
future reuse.

Projection is not a truth model.

Projection is a **Knowledge Accessibility Strategy**.

### Design Rationale

Different users, organizations, and situations require different entry
points into the same original source.

------------------------------------------------------------------------

## Principle 4 --- Reuse Intellectual Activities

IdeaMark focuses on reusable reasoning components, reasoning episodes,
and intellectual activity structures.

### Design Rationale

The objective is not to preserve answers but to preserve reusable ways
of thinking.

------------------------------------------------------------------------

## Principle 5 --- Cooperate with AI

IdeaMark assumes AI-assisted retrieval and explanation.

LLMs reconstruct situation-specific explanations after relevant
intellectual activities and original sources have been retrieved.

### Design Rationale

IdeaMark reduces search complexity. LLMs reconstruct meaning.

The two systems complement each other.

------------------------------------------------------------------------

## Principle 6 --- Operational Rather than Immutable

IdeaMark documents are operational snapshots.

They may be regenerated, replaced, versioned, or coexist according to
changes in source material, projections, and organizational needs.

### Design Rationale

Knowledge environments evolve continuously. Reusable indexes should
evolve as well.

------------------------------------------------------------------------

# 4. Non-goals

IdeaMark does not aim to:

-   preserve meaning
-   replace original documents
-   define universal ontologies
-   standardize domain vocabularies
-   replace LLMs
-   prescribe a single Projection

------------------------------------------------------------------------

# 5. Future Direction

Projection specifications, coordinate models, authoring methods, and
retrieval architectures are intentionally developed as separate
specifications.

This separation allows both IdeaMark and Projection ecosystems to evolve
independently while remaining interoperable.

------------------------------------------------------------------------

# Closing Statement

IdeaMark is designed as an intellectual activity infrastructure.

Its purpose is not to preserve a single interpretation of knowledge, but
to enable humans and AI to repeatedly rediscover, reinterpret, and reuse
intellectual activities through authoritative original sources.
