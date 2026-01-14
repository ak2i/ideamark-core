
# IdeaMark Sample Document Structure Guide

This document explains the **complete structure and vocabulary** used in the IdeaMark sample demonstrated across:
- UK (Public Right of Way)
- Japan (Kanagawa / Fuji-Hakone-Izu)
- Australia (Uluru)
- USA (National Parks)

The goal is to show **how an IdeaMark document is composed**, what each concept means, and how it enables reuse of past Problem–Solution patterns.

---

## 1. Core Philosophy

- **IdeaMark does not store meaning**
- Meaning emerges when **humans or AIs read through Sections and Views**
- The system stores:
  - Structure
  - Context
  - Relationships
  - Decision traces

---

## 2. Top-Level Document Structure

```
IdeaMark Document
├─ Meta
├─ Sections[]
└─ (Optional) Pattern Registry
```

---

## 3. Meta Section

Defines global intent and scope.

**Typical vocabulary:**
- intent
- domain
- timeframe
- authoring_context
- pattern_registry

---

## 4. Section

A **Section** is the primary unit of meaning emergence.

### SectionMeta Vocabulary

- view: background | problem | vision | solution | case_analysis | problem_reframing | solution_reinterpretation
- phase: conceptualization | design_evaluation
- rhetorical_mode: enumeration | contrast | structural_comparison | mapping
- default_atomic_assumption
- intent
- anchor_problem
- anchor_pattern

---

## 5. Occurrence

An **Occurrence** represents one appearance of an IdeaEntity within a Section.

### Occurrence Vocabulary

- role:
  - observation
  - contrast
  - motivation
  - problem_core
  - tension
  - historical_pattern
  - design_choice
  - reframed_problem
  - solution_cluster
  - missing_solution
- emphasis
- instantiates
- addresses
- omits
- link_to:
  - and
  - but
  - therefore
  - implies
  - observed_as
  - can_be_addressed_by

---

## 6. IdeaEntity

**IdeaEntity is the only conceptual unit that exists.**

### IdeaEntity Vocabulary

- id
- payload
- children
- note
- reusable_as
- pros
- cons

Atomicity is contextual, not inherent.

---

## 7. Pattern Entity

A **Pattern** is a reusable IdeaEntity representing a generalized Problem–Solution structure.

### Pattern Components

- Problem Structure
- Historical Manifestations
- Solution Strategy Space
- Trade-offs & Risks
- Decision Axes

---

## 8. Case Sections

Each case is represented as:

```
Section: Case Study – <Region>
├─ Problem
└─ Solution
```

---

## 9. Meta-Comparison Section

Extracts shared structure and reframed problems.

Vocabulary:
- problem_reframing
- structural_comparison
- reframed_problem

---

## 10. Pattern Instantiation Map

Maps:
- Case → Strategy
- Case → Omissions
- Case → Risks

---

## 11. Why This Structure Works

- Past cases become reusable design components
- Solutions are positioned, not copied
- New problems are interpreted faster
- AI agents can reason structurally

---

## 12. Summary

IdeaMark enables structural reuse of experience and view-dependent meaning emergence.