# 10. Projection Profile

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## Purpose

This chapter defines the role of a Projection Profile.

A Projection Profile is a concrete or semi-concrete way to express Projection responsibilities for tools, documents, libraries, or authoring workflows.

Part 5 defines what Projection is responsible for.

A Projection Profile defines how some or all of those responsibilities are represented in a reusable form.

## Profile Boundary

A Projection Profile is not necessarily the same as an IdeaMark Core YAML profile.

An IdeaMark document may reference a Projection Profile, embed a small Projection fragment, or point to a separate Projection document.

A Projection may also exist outside an IdeaMark document in a library, repository, organizational policy store, tool configuration, or authoring environment.

Therefore, a Projection Profile SHOULD distinguish:

- Projection-as-document;
- Projection-as-library-entry;
- Projection-as-inline-fragment;
- Projection-as-authoring-parameter;
- Projection-as-runtime-selection;
- Projection-as-private-local-context.

A single ecosystem may support more than one representation.

## Minimum Profile Responsibilities

A minimally useful Projection Profile SHOULD support:

1. **identity** — a way to identify the Projection or fragment;
2. **version awareness** — a way to distinguish revisions;
3. **reuse intent** — what future activity the Projection supports;
4. **boundary** — what Situation assumptions are included or excluded;
5. **decomposition guidance** — how source material should be structured;
6. **retrieval and matching guidance** — how later candidates should be found or judged;
7. **reconstruction guidance** — how selected material should become an activation expression;
8. **evaluation criteria** — how success or failure should be reviewed;
9. **privacy and sharing policy** — whether the Projection may be exposed or only referenced.

A lightweight experimental Profile MAY omit some of these fields if the omission is explicit.

## Suggested Profile Areas

A Projection Profile MAY include areas such as:

```text
projection
  identity
  lifecycle
  intended_reuse
  audience
  situation_boundary
  requirement_bundle
  source_coverage_policy
  section_strategy
  entity_strategy
  occurrence_strategy
  traceability_strategy
  retrieval_intent
  matching_criteria
  filtering_policy
  reconstruction_targets
  evaluation_criteria
  compatibility_notes
  privacy_policy
  examples
```

This list is illustrative, not a required schema.

Part 4 or companion specifications may convert some of these areas into concrete YAML or JSON fields.

## Inline Projection Fragments

An IdeaMark document MAY include inline Projection fragments when a full external Projection is unavailable or unnecessary.

Inline fragments are useful for:

- exploratory authoring;
- one-off generation;
- recording local rationale;
- preserving a generation note;
- explaining a compatibility assumption;
- documenting reconstruction expectations.

Inline fragments SHOULD NOT pretend to be complete when they are only local notes.

A Profile SHOULD provide a way to distinguish complete Projections from partial Projection notes.

## External Projection References

An IdeaMark document MAY reference external Projections.

External references are useful when:

- a Projection is reused across many documents;
- a Projection is governed by an organization or library;
- a Projection contains private details;
- versioning matters;
- compatibility rules are maintained outside the document;
- tools need a stable identifier for retrieval or reconstruction.

A reference SHOULD preserve enough information for later users or tools to resolve, review, or at least identify the Projection that shaped Decomposition.

## Private Projection Resolution

A Profile MAY support private Projection resolution.

In this pattern, a document records an opaque or partial Projection reference, while authorized tools or users can resolve the full Projection in a private context.

This supports reuse without forcing sensitive requirements into public documents.

However, if a Projection is not fully visible, the document SHOULD avoid making strong public claims about compatibility or reconstruction that cannot be reviewed.

## Profile and Doc CLI

A Projection Profile MAY be exposed through Doc CLI-style describe and validate mechanisms.

For example, a tool may expose:

- authoring guidance;
- required parameters;
- supported Projection fields;
- supported compatibility classes;
- validation diagnostics;
- routing and language capabilities.

Part 5 does not require a specific CLI.

However, Projection-capable tools SHOULD make their supported Profile responsibilities discoverable when they are used in multi-tool environments.

## Profile Non-goal

A Projection Profile should not become a universal domain ontology.

It should represent the reusable strategy needed for Decomposition, retrieval, matching, filtering, and reconstruction.

Domain vocabularies may be referenced by a Profile, but they should not be confused with Projection itself.
