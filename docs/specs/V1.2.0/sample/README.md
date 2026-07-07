# IdeaMark Core v1.2.0 Sample Library

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft Sample Library  
**Scope:** External samples for CLI, POR, retrieval, and reconstruction development

## Purpose

This directory contains sample **Skeleton Families** and **Projections** for IdeaMark Core v1.2.0 implementation work.

These files are intentionally placed outside the strict Core specification chapters.

They are not normative Core definitions.

They are sample library assets for:

- IdeaMark CLI parser and validator development;
- Projection loader development;
- Skeleton Family loader development;
- POR generation experiments;
- retrieval test expansion;
- reconstruction test expansion;
- sample-driven implementation design.

## Directory Contents

```text
sample/
  README.md
  manifest.yaml
  skeleton-families.yaml
  projections.yaml
```

## Design Boundary

IdeaMark Core v1.2.0 defines the document-side structures that can record optional Skeleton Graphs.

This sample library defines reusable external patterns that may be used by Projection Libraries or implementation tools.

```text
Core Spec
  defines document structures

sample/skeleton-families.yaml
  provides example external Skeleton Family definitions

sample/projections.yaml
  provides example Projection definitions and mappings

CLI / POR
  may load these files as fixtures, examples, or initial library data
```

## Recommended CLI Uses

Initial CLI commands may use this directory for tests such as:

```text
ideamark sample list
ideamark projection list --library docs/specs/V1.2.0/sample/projections.yaml
ideamark skeleton-family list --library docs/specs/V1.2.0/sample/skeleton-families.yaml
ideamark projection validate docs/specs/V1.2.0/sample/projections.yaml
ideamark skeleton-family validate docs/specs/V1.2.0/sample/skeleton-families.yaml
ideamark retrieve test docs/specs/V1.2.0/part4-core-specification/retrieval-tests
```

These commands are suggestions for implementation design, not required by Core.

## Recommended POR Uses

POR experiments may use these samples to test whether an engine can:

1. load a Projection;
2. resolve referenced Skeleton Families;
3. map family canonical slots to Projection-specific slots;
4. decompose a source into Sections, Occurrences, and Entities;
5. emit a document-side Skeleton Graph;
6. expose missing slots and warnings;
7. support retrieval-oriented evaluation.

## Sample Scale

The library starts with:

- 8 Skeleton Families;
- 24 Projection samples.

This is large enough to test many-to-many mapping behavior without pretending to be a mature ontology or complete Projection ecosystem.

## Non-normative Status

The content in this directory may change faster than the Core specification.

It should be treated as sample implementation material.

A mature ecosystem may later move these assets into dedicated repositories such as:

- `ideamark-projection-library`;
- `ideamark-skeleton-family-library`;
- organization-specific internal libraries.
