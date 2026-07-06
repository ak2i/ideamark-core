# 19. Open Review Issues

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft Review Note

## 19.1 Purpose

This note records open review issues and recently resolved design decisions for Part 4.

Part 4 is already at an initial draft-complete state.

The remaining work is not mainly to add missing chapters, but to decide which draft rules should be frozen for v1.2.0, which should remain profile-defined, and which should move outside Core.

This file is intentionally a review-control document, not a normative chapter.

Normative requirements should be reflected in the relevant Part 4 chapters after review decisions are accepted.

## 19.2 Issue Categories

Review items are classified as:

- **Resolved for v1.2.0** — accepted design decisions that should be treated as the current Part 4 direction.
- **Must decide before v1.2.0 freeze** — unresolved issues that affect Core conformance.
- **Can remain profile-defined** — items that should not be frozen in Core.
- **Move to Part 5** — Projection-specific concerns.
- **Move to IdeaMark CLI** — implementation-specific CLI behavior.
- **Move to Part 6 / Authoring Guide** — authoring practice, granularity guidance, and examples.
- **Future version candidate** — useful but not required for v1.2.0.

## 19.3 Resolved for v1.2.0

### 19.3.1 Array-based object representation

**Decision:** Adopt array-based object representation as the normative v1.2.0 shape.

The required object namespaces use arrays of objects with explicit `id` fields:

```yaml
sources:
  - id: src-001
sections:
  - id: sec-001
occurrences:
  - id: occ-001
entities:
  - id: ent-001
```

Keyed-map forms may appear in older drafts, Part 3 experiments, v1.1.x material, or implementation-internal representations, but they are not the normative Part 4 shape.

Migration tools SHOULD convert keyed maps into arrays while preserving the original keys as `id` values.

Rationale:

- works better with YAML/JSON interchange;
- avoids object identity being hidden in mapping keys;
- supports stable ordering;
- is friendlier to LLM generation and patch-based editing;
- makes object shape uniform across Sources, Sections, Occurrences, and Entities.

### 19.3.2 Placeholder objects in Core mode

**Decision:** Allow placeholder objects in Core mode, but report warnings.

Placeholder objects may intentionally appear in draft, template, partial generation, staged authoring, multi-perspective exploration, or missing-information workflows.

IdeaMark Documents may be used as an expression system in multi-faceted situations, so absence can itself be intentional.

However, missing fields may also indicate authoring mistakes.

Therefore, Core mode SHOULD warn rather than reject placeholders.

Strict mode and profiles MAY reject placeholders.

Examples of placeholder-like structures:

```yaml
entities:
  - id: ent-placeholder
    status: draft
```

```yaml
occurrences:
  - id: occ-placeholder
    status: draft
```

```yaml
sections:
  - id: sec-placeholder
    occurrences: []
```

Rationale:

- supports partial and staged authoring;
- preserves intentional incompleteness;
- avoids over-constraining IdeaMark as only a finalized exchange format;
- still alerts tools and authors through warnings.

### 19.3.3 `meta.projections.inline`

**Decision:** Allow `meta.projections.inline` when it is valid YAML/structured data, but do not inspect or validate its internal Projection semantics in Core.

Part 4 validators may validate that inline data is parseable and structurally representable as YAML data, but they MUST NOT treat inline Projection content as a full Core-defined Projection schema.

Example:

```yaml
meta:
  projections:
    - role: generation
      ref: projection://example/projection/v1
      inline:
        purpose: explain professional cooking guidance for household use
        audience: non-specialist
```

Rationale:

- small inline Projection notes are useful for local traceability;
- Part 4 should not require all Projection data to be externally addressable;
- Part 4 must not become the Projection content model;
- Part 5 remains responsible for Projection specification.

### 19.3.4 `structure` namespace

**Decision:** Keep `structure` optional in Core v1.2.0.

`structure` may provide document-level Section ordering, grouping, or alternate view metadata, but the required Core namespaces remain:

- `meta`
- `sources`
- `sections`
- `occurrences`
- `entities`

Core documents without `structure` may still be valid.

When `structure.sections` exists, tools SHOULD treat it as explicit document-level Section order.

Rationale:

- minimal Core should not require an extra namespace when Sections and Occurrences already carry local ordering;
- simple documents do not need explicit global structure;
- complex reconstruction or alternate-view documents can opt in;
- profiles may require `structure` when needed.

### 19.3.5 Recommended vocabularies remain open

**Decision:** Keep recommended vocabularies open in Core mode.

Core mode SHOULD warn on unknown values where useful, but SHOULD NOT reject them solely because they are not in the recommended vocabulary.

This applies to values such as:

- document status;
- object status;
- source type;
- anchor type;
- anchor precision;
- Occurrence role;
- Entity kind;
- Projection role.

Rationale:

- Part 3 experiments show that roles and kinds are Projection-shaped and domain-shaped;
- closed vocabularies would push domain language into Core;
- profiles and strict validation can define closed vocabularies when needed;
- Core must remain reusable across technical, procedural, policy, culinary, design, and future domains.

## 19.4 Must Decide Before v1.2.0 Freeze

### 19.4.1 Whether resolved decisions are reflected consistently across all chapters

**Status:** Open.

The decisions in section 19.3 should be checked against all Part 4 chapters.

Expected consistency checks:

- array-based object representation is consistently normative;
- placeholder warnings are consistently described in Sections, Occurrences, Entities, Sources, and Validation;
- inline Projection content is permitted but not semantically validated;
- `structure` remains optional everywhere;
- recommended vocabularies remain open in Core mode.

Likely affected chapters:

- `01-document-structure.md`
- `03-common-object-requirements.md`
- `04-metadata-and-projection-references.md`
- `10-structure-and-ordering.md`
- `13-validation-rules.md`
- `14-compatibility-and-migration.md`
- `16-normative-examples.md`

### 19.4.2 Whether `meta.projections.inline` needs size or scope guidance

**Status:** Open.

Decision 19.3.3 allows inline Projection data if YAML-structured, but Part 4 may still need guidance that inline data should not be used to store a complete reusable Projection Library entry.

Possible resolution:

- keep validation permissive;
- add non-normative guidance that large reusable Projection definitions should move to Part 5 Projection documents or Projection Library storage;
- do not define a hard size limit in Core.

### 19.4.3 Whether anchor `role` or `purpose` should be mentioned in examples

**Status:** Open.

Part 4 now allows optional anchor `role` and `purpose`.

Normative examples should probably include at least one anchor with `role` or `purpose`, especially for code-source or recipe-source examples.

Possible resolution:

- add one small example to `16-normative-examples.md`;
- keep anchor `role` and `purpose` optional.

### 19.4.4 Whether legacy migration examples are sufficient

**Status:** Open.

Part 3 experiments and older v1.x material may use:

- keyed maps;
- `original_sources` under `meta`;
- singular `anchor`;
- `line_ranges` instead of `ranges`;
- `anchor_type` instead of anchor `role` or `purpose`;
- `ref_id` instead of `ref` in Projection references.

Part 4 should decide how much of this belongs in `14-compatibility-and-migration.md`.

Possible resolution:

- add a compact migration examples section;
- leave detailed migration implementation to tools.

## 19.5 Can Remain Profile-defined

### 19.5.1 Closed role and kind vocabularies

Core should not define closed role or kind vocabularies.

Profiles MAY define them.

Examples:

- a code-analysis profile may define implementation-rationale roles;
- a recipe profile may define ingredient-function roles;
- an audit profile may define evidence and claim roles;
- a policy profile may define issue, measure, risk, and outcome roles.

### 19.5.2 Source-specific anchor types

Core should keep the common anchor vocabulary open.

Profiles MAY define source-specific anchor types such as:

- `ingredient_line`
- `recipe_step`
- `code_comment_block`
- `function_body`
- `rfc_section`
- `dataset_partition`
- `sensor_time_window`

### 19.5.3 Strict completeness rules

Core mode allows incomplete and placeholder-like documents with warnings.

Profiles MAY require:

- at least one Source;
- every Section to have anchors;
- every Section to contain Occurrences;
- every Occurrence to be referenced by exactly one Section;
- every Entity to be referenced by at least one Occurrence;
- every Entity to contain `content`, `payload`, or `ref`;
- exact anchors rather than approximate or inferred anchors.

### 19.5.4 Domain payload schemas

Entity `payload` remains open in Core.

Profiles MAY define payload schemas for specific domains.

Core validators should preserve payloads without attempting domain validation.

## 19.6 Move to Part 5

### 19.6.1 Projection content model

Part 4 may record Projection references and inline data.

Part 4 should not define the full Projection content model.

Part 5 should define:

- Projection identity;
- Projection purpose;
- Projection scope;
- Projection compatibility;
- Projection lifecycle;
- Projection Library conventions;
- Projection evaluation or review concepts where appropriate.

### 19.6.2 Projection compatibility

Whether two Projections are compatible, comparable, substitutable, or reusable together is outside Part 4.

Part 4 only records metadata that may help future reconstruction.

### 19.6.3 Projection Library governance

Versioning, naming, publishing, sharing, and governance of reusable Projections should remain outside Core document serialization.

## 19.7 Move to IdeaMark CLI

### 19.7.1 Diagnostic codes

Part 4 should define validation requirements and severity expectations, but not concrete CLI diagnostic codes.

IdeaMark CLI should define codes such as:

- required namespace missing;
- duplicate ID;
- unresolved reference;
- unknown status;
- placeholder object;
- malformed anchor.

### 19.7.2 CLI command behavior

Part 4 should not define:

- command names;
- flags;
- stdout/stderr behavior;
- JSON diagnostic schema;
- exit code mapping;
- formatter options;
- strict/profile mode flags.

Those belong to the IdeaMark CLI repository or CLI contract.

### 19.7.3 Formatter behavior beyond Core preservation

Part 4 may require that tools preserve Core and extension data, but exact formatter behavior should be CLI-specific.

Examples:

- canonical sort order;
- quote style;
- line wrapping;
- comment preservation strategy;
- destructive normalization flags.

## 19.8 Move to Part 6 / Authoring Guide

### 19.8.1 Entity granularity guidance

Part 4 should not validate whether an Entity is too large, too explanatory, or too summary-like.

Authoring guidance should explain how to choose Entity boundaries under different Projections.

Part 3 experiments showed that Entity content may become mini-summaries.

This is an authoring and Projection design problem, not a Core validation problem.

### 19.8.2 Section design patterns

Part 4 defines Section shape.

Part 6 should explain how to choose Sections for different activities:

- code reasoning;
- recipe execution;
- ingredient substitution;
- RFC interpretation;
- policy analysis;
- field operations;
- planning and decision support.

### 19.8.3 Projection-shaped sample authoring

Part 6 should include practical guidance for turning one Original Source into different IdeaMark Documents under different Projections.

The recipe test is a strong candidate for this because it clearly shows different decompositions from the same source.

## 19.9 Future Version Candidates

### 19.9.1 Optional relation profile

Part 4 keeps `relations` optional.

A future companion specification may define a relation profile for use cases that need explicit graph structures.

Examples:

- evidence graphs;
- dependency graphs;
- causal models;
- argument maps;
- policy measure chains.

### 19.9.2 Profile declaration schema

Part 4 allows `meta.profiles`, but does not define a complete profile schema.

A future version may define:

- profile identifiers;
- profile discovery;
- required namespaces;
- validation mode declarations;
- closed vocabularies;
- payload schemas;
- extension namespace declarations.

### 19.9.3 Stronger source verification

Core anchors are traceability claims.

Future profiles or tools may define stronger verification:

- source content hash;
- source availability check;
- anchor text verification;
- OCR confidence;
- source license validation;
- audit-grade citation validation.

### 19.9.4 Canonical JSON representation

Part 4 allows JSON-equivalent representation, but does not define a canonical JSON format.

A future version or companion tool spec may define canonical JSON for storage, hashing, tests, or interop.

## 19.10 Current Freeze Candidate Summary

The following decisions are current freeze candidates for IdeaMark Core v1.2.0 Part 4:

1. Use array-based object representation as normative.
2. Keep required Core namespaces as `meta`, `sources`, `sections`, `occurrences`, and `entities`.
3. Keep `structure` optional.
4. Keep `relations`, `perspectives`, and `provenance` optional or profile-defined.
5. Allow placeholder objects in Core mode with warnings.
6. Allow `meta.projections.inline` without Core semantic validation of Projection internals.
7. Keep recommended vocabularies open in Core mode.
8. Keep CLI diagnostic codes and command behavior outside Part 4.
9. Keep Entity granularity and authoring practices outside Part 4.
10. Treat Part 3 samples as conformance review material and future regression tests for the Core document model.
