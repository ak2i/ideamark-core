# 0. Specification Overview

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 0.1 Purpose

This document begins the normative Core Specification for IdeaMark Core v1.2.0.

Part 4 defines the serialized document representation that IdeaMark-compatible tools may emit, validate, exchange, normalize, migrate, and preserve.

Part 4 is intentionally narrower than the full IdeaMark concept.

It specifies the minimum interoperable access-structure format for:

- document metadata;
- Original Source references;
- Sections;
- Occurrences;
- Entities;
- references among those objects;
- validation behavior;
- extension preservation;
- compatibility and migration.

## 0.2 Normative Language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as normative requirement levels within this specification.

This specification uses those terms to distinguish:

- Core interoperability requirements;
- recommended authoring and tooling behavior;
- optional extension points;
- profile-specific behavior that is outside the Core.

## 0.3 Core Serialization Goal

An IdeaMark Core document is a reusable access-structure artifact.

It is not required to store final meaning, final interpretation, complete workflow state, or domain-specific ontology.

A conforming Core document MUST make it possible for tools and future readers to identify:

- which document is being processed;
- which Core version it targets;
- which Original Sources are referenced;
- how source windows are represented as Sections;
- how reusable material is represented as Entities;
- how role-bearing placements are represented as Occurrences;
- how references among those objects are resolved;
- which data is Core and which data is extension or profile-defined.

## 0.4 Core Object Model Boundary

The normative Core objects in v1.2.0 are:

- `meta`
- `sources`
- `sections`
- `occurrences`
- `entities`

These required namespaces encode the minimum access structure.

Part 4 does not make `relations`, `perspectives`, `provenance`, runtime session state, authoring engine internals, or Projection Library internals required Core objects.

Those concepts MAY appear as optional namespaces, extension data, profile-defined structures, or companion specifications.

## 0.5 Relationship to Part 3 and Part 5

Part 4 encodes the conceptual responsibilities defined in Part 3.

It also preserves the Projection boundary clarified in Part 5.

In particular:

- Core MAY record Projection references and limited Projection-related metadata;
- Core MUST NOT define the full Projection content model;
- Core MUST remain usable without requiring a Projection Library implementation;
- Core documents MAY be generated under different Projections from the same Original Source;
- Core validation MUST validate document structure, not the intellectual quality of a Projection.

## 0.6 Document Format Boundary

Part 4 defines document representation, not authoring process.

Authoring engines may use CLI workflows, visual editors, AI agents, progressive processors, batch converters, IDE integrations, or companion systems.

Those engines MAY maintain internal state, intermediate representations, caches, review queues, prompt plans, or scheduling state.

Such internal state MUST NOT be required for Core document validity.

## 0.7 Serialization Format

YAML is the primary human-authored serialization format for IdeaMark Core v1.2.0.

Tools MAY provide a JSON-equivalent normalized representation.

When converting between YAML and JSON-equivalent forms, tools SHOULD preserve Core objects, extension fields, and unknown namespaces unless a strict validation or normalization mode explicitly rejects them.

For interoperability:

- YAML mappings MUST be parseable as ordinary YAML mappings;
- YAML sequences MUST be parseable as ordinary YAML sequences;
- advanced YAML features that make round-trip processing ambiguous SHOULD NOT be used;
- semantic ordering SHOULD be represented explicitly rather than relying only on incidental map order.

## 0.8 Conformance Levels

This specification defines two initial validation levels.

### Core mode

Core mode validates required Core structure and required Core fields.

Core mode:

- MUST reject malformed YAML;
- MUST reject missing required Core namespaces;
- MUST reject unresolved required references;
- SHOULD warn about unknown top-level namespaces unless declared as extensions;
- SHOULD preserve unknown fields and namespaces during round-trip formatting.

### Strict mode

Strict mode is intended for controlled pipelines, tests, exchange contracts, and profile enforcement.

Strict mode MAY reject:

- unknown top-level namespaces;
- unknown object fields;
- unknown vocabulary values;
- placeholder objects;
- extension data that is not declared by a profile.

Strict mode MUST NOT silently reinterpret invalid data as valid Core data.

## 0.9 Non-goals of Part 4

Part 4 does not define:

- final meaning;
- Projection content modeling;
- Projection evaluation;
- retrieval ranking;
- storage engines;
- UI behavior;
- authoring workflow;
- chunking or OCR algorithms;
- LLM prompt orchestration;
- runtime session state;
- domain-specific vocabularies;
- global ontology governance.

## 0.10 Initial Specification Shape

The remaining chapters define the following normative areas:

1. document structure;
2. required top-level namespaces;
3. common object requirements;
4. metadata and Projection references;
5. Original Source references;
6. source anchors and traceability;
7. Sections;
8. Occurrences;
9. Entities;
10. structure and ordering;
11. status, versioning, and regeneration metadata;
12. optional extensions;
13. validation rules;
14. compatibility and migration;
15. serialization requirements;
16. normative examples;
17. non-goals.
