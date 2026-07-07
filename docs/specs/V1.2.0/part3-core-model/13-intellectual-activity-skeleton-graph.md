# 13 — Intellectual Activity Skeleton Graph Model

**Part:** 3 — Core Model  
**Status:** Specification Draft  
**Version:** IdeaMark Core v1.2.0

## 13.1 Purpose

This chapter defines the conceptual role of **Intellectual Activity Skeletons**, **Skeleton Graphs**, and **Skeleton Links** in IdeaMark Core.

The purpose is to clarify how IdeaMark can support retrieval before reconstruction.

A valid IdeaMark document can support reconstruction through Sections, Occurrences, Entities, source anchors, and Projection references. However, large-scale retrieval also needs a lower-cost structure for finding candidate documents, Sections, or source windows without relying only on keywords, domain labels, or full LLM inspection.

Skeleton Graphs provide that retrieval-oriented structure.

## 13.2 Intellectual Activity Skeleton

An **Intellectual Activity Skeleton** is the domain-reduced composition pattern of a future Human-AI Intellectual Activity.

It is not a domain taxonomy, workflow ontology, final meaning, or universal list of verbs.

It represents the reusable compositional shape left after a Projection-guided Decomposition removes as much domain-specific expression as practical while preserving the structure needed for later activity.

Examples of domain-specific expressions that may share a similar Skeleton include:

- replacing an unavailable ingredient while preserving flavor function;
- replacing an unavailable algorithm while preserving performance or API constraints;
- replacing an unavailable disaster-response measure while preserving protective effect;
- changing a communication strategy while preserving audience activation.

The domain-specific words differ, but the reusable activity composition may involve similar slots such as:

- a blocked or unavailable element;
- an effect, function, constraint, or condition to preserve;
- an alternative space;
- compatibility boundaries;
- confirmation or review signals.

## 13.3 Skeleton Graph

A **Skeleton Graph** is an explicit graph representation of an Intellectual Activity Skeleton.

A Skeleton Graph consists of:

- **Skeleton Nodes**: references to IdeaMark structures or Projection-side requirement slots;
- **Skeleton Links**: compositional links between nodes;
- optional graph-level metadata such as purpose, Projection reference, status, matching hints, or review notes.

A Skeleton Graph is not required for minimum Core reconstruction.

An IdeaMark document MAY include Skeleton Graphs when retrieval-oriented matching, filtering, comparison, or compatibility evaluation would benefit from precomputed structure.

## 13.4 Skeleton Node

A Skeleton Node is an activity-composition node.

In an IdeaMark document, a node may reference:

- a Section;
- an Occurrence;
- an Entity;
- an anchor or source window;
- a profile-defined object;
- a placeholder slot when the document is incomplete.

In a Projection, a node may represent a required, optional, excluded, or preferred activity slot.

A node SHOULD avoid domain-specific naming when the purpose is cross-domain retrieval.

A node MAY include a human-readable label or note for review, but matching SHOULD NOT depend only on that label.

## 13.5 Skeleton Link

A **Skeleton Link** is a compositional edge in a Skeleton Graph.

Skeleton Links are not semantic Relations.

They do not assert universal meaning such as "A causes B" or "A proves B".

They describe how one node participates with another node in the composition of an Intellectual Activity Skeleton.

Recommended initial link types include:

- `sequence` — nodes participate in an ordered composition;
- `dependency` — one node is needed to use or evaluate another;
- `constraint` — one node limits, bounds, or conditions another;
- `alternative` — nodes represent selectable or substitutable options;
- `parallel` — nodes coexist without required order;
- `conflict` — nodes are incompatible or mutually blocking in the activity structure;
- `aggregation` — nodes combine into a larger activity unit;
- `specialization` — one node narrows or instantiates another;
- `confirmation` — one node supplies a check, signal, or review point for another.

These are recommended structural operators, not a closed universal vocabulary.

Profiles and Projection Libraries MAY define stricter or domain-specific Skeleton Link vocabularies.

## 13.6 Difference from Relation

Earlier Relation-like designs connected Entities or Sections through semantic labels.

Skeleton Links serve a different purpose.

```text
Relation-like edge:
  A supports B
  A causes B
  A explains B

Skeleton Link:
  node A participates with node B as part of an activity composition pattern
```

This distinction preserves the v1.2.0 stance that semantic Relation is not a required Core namespace while allowing retrieval-oriented graph patterns to be represented as optional Core-adjacent structure.

## 13.7 Retrieval Role

Skeleton Graphs are primarily retrieval-oriented.

They allow a system to compare:

```text
Projection-required Skeleton Graph
        against
IdeaMark-recorded Skeleton Graphs
```

This supports candidate selection before expensive reconstruction.

A system may use Skeleton Graphs for:

- graph pattern matching;
- partial graph matching;
- compatibility filtering;
- analogical transfer detection;
- retrieval explanation;
- identifying missing activity slots;
- selecting Sections and source anchors for reconstruction.

Part 3 does not define a matching algorithm.

## 13.8 Reconstruction Role

Skeleton Graphs do not replace Sections, Occurrences, Entities, anchors, or Original Sources.

After retrieval selects candidate structures, reconstruction should still use:

- Projection guidance;
- matched Sections;
- role-bearing Occurrences;
- reusable Entities;
- source anchors;
- Original Source material;
- review and compatibility constraints.

Skeleton Graphs reduce the cost of finding promising material. They do not contain the final activation expression.

## 13.9 Domain Boundary

Core SHOULD NOT require a universal domain dictionary.

Domain may still appear in Projection descriptions, Original Source descriptions, local notes, or operational storage boundaries.

However, Skeleton Graphs are intended to help remove domain-specific expression when it would otherwise block reuse.

Decomposition may use domain knowledge to produce a domain-reduced Skeleton Graph.

Reconstruction may use a new Situation or domain context to reinstantiate the retrieved Skeleton into an activation expression.

## 13.10 Conceptual Minimum

Skeleton Graph support should remain optional in Core v1.2.0.

The conceptual minimum remains:

```text
meta
sources
sections
occurrences
entities
```

When present, Skeleton Graphs provide an additional retrieval layer:

```text
skeletons
  nodes
  links
```

This layer is Core-adjacent and retrieval-oriented.

It SHOULD be preserved by tools that round-trip IdeaMark documents.

It MAY be validated more strictly by profiles, Projection Libraries, or retrieval-oriented conformance suites.
