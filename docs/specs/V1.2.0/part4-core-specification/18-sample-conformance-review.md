# 18. Sample Conformance Review

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft Review Note

## 18.1 Purpose

This note reviews selected Part 3 design experiments against the Part 4 Core Specification draft.

The purpose is not to define CLI behavior.

The purpose is to test whether the Part 4 YAML representation can express the structures that Part 3 found useful without over-constraining implementation-specific tools such as IdeaMark CLI.

This review should help identify:

- places where Part 4 is too strict;
- places where Part 4 is too loose;
- migration implications from earlier IdeaMark-like shapes;
- whether the required namespaces are sufficient;
- whether optional namespaces should remain optional;
- whether sample documents can be rewritten into conforming v1.2.0 YAML.

## 18.2 Reviewed Part 3 Samples

This initial review focuses on two representative Part 3 experiment families.

### Heapq performance candidate

The heapq performance candidate is a manual IdeaMark-like document generated from CPython `Lib/heapq.py` under a Performance Engineering Projection.

It is useful because it contains concrete Sections, Occurrences, Entities, source anchors, roles, rationale, and explicit structure ordering.

It was explicitly not intended to define final YAML syntax, making it a good migration and conformance test.

### Recipe multi-projection test

The recipe test explores whether Section / Occurrence / Entity still work outside technical domains.

It is useful because the same recipe sketch is expected to produce different Section and Entity shapes under cooking execution, ingredient substitution, shopping, beginner teaching, and dietary constraint Projections.

This makes it a good test for whether Part 4 remains Projection-shaped rather than domain-specific.

## 18.3 Review Method

For each sample, this review asks:

1. Can the sample be represented using the required namespaces `meta`, `sources`, `sections`, `occurrences`, and `entities`?
2. Can the sample use the Part 4 array-based object shape?
3. Can source references and source anchors be represented without text-span-only assumptions?
4. Can Projection context be represented in `meta.projections` without making Projection internals part of Core?
5. Can Occurrence roles carry the needed local function without requiring a separate `relations` namespace?
6. Are optional `structure`, extension fields, and profile-defined vocabularies sufficient?
7. Does the conversion reveal missing or ambiguous Part 4 rules?

## 18.4 Heapq Candidate: Original Shape

The Part 3 heapq candidate used the following broad shape:

```yaml
meta:
  experiment_id: part3-heapq-performance-001
  status: exploratory
  original_sources:
    - id: SRC-heapq-py
      repository: python/cpython
      path: Lib/heapq.py
      ref: main
      source_type: public_source_code
  projections:
    - role: generation
      id: code-design-performance-heapq-v0
      purpose: extract implementation and performance reasoning from source code
sections:
  SEC-001:
    title: Heap invariant as performance boundary
    anchor:
      source: SRC-heapq-py
      line_ranges:
        - start: 3
          end: 32
    occurrences:
      - OCC-001
entities:
  IE-001:
    kind: structural_principle
    content: A heap is represented as an array constrained by an invariant.
occurrences:
  OCC-001:
    entity: IE-001
    role: establishes_performance_boundary
```

This shape is conceptually close to Part 4, but it differs from the Part 4 draft in several serialization decisions.

## 18.5 Heapq Candidate: Conformance Findings

### 18.5.1 Required namespaces

The sample already contains the conceptual equivalents of:

- `meta`
- source references through `meta.original_sources`
- `sections`
- `occurrences`
- `entities`
- `structure`

Part 4 requires `sources` as a top-level namespace, so the sample should move `meta.original_sources` to `sources`.

Finding: **Part 4 can represent the sample, but migration requires source extraction from metadata into `sources`.**

### 18.5.2 Array-based object shape

The sample uses keyed maps for Sections, Occurrences, and Entities.

Part 4 uses arrays of objects with explicit `id` fields.

Finding: **The sample is migratable but not directly conforming.**

Recommended migration:

```yaml
sections:
  SEC-001:
    title: Heap invariant as performance boundary
```

becomes:

```yaml
sections:
  - id: sec-001
    title: Heap invariant as performance boundary
```

The original ID may be preserved exactly or normalized to the recommended lower-case prefix.

Preserving the original ID is safer for migration.

### 18.5.3 Source anchors

The sample uses a singular `anchor` field with `line_ranges` and `anchor_type`.

Part 4 uses an `anchors` array with anchor objects.

Finding: **Part 4's anchor model can represent the sample more uniformly.**

Recommended migration:

```yaml
anchor:
  source: SRC-heapq-py
  line_ranges:
    - start: 3
      end: 32
  anchor_type: source_context
```

becomes:

```yaml
anchors:
  - source: SRC-heapq-py
    type: line_range
    ranges:
      - start: 3
        end: 32
    precision: exact
    role: source_context
```

Open issue: Part 4 currently defines `type` as anchor kind but does not define a standard field for the old `anchor_type` role-like value.

Recommendation: keep such values as extension fields or add a recommended optional field such as `role` or `purpose` on anchor objects.

### 18.5.4 Projection metadata

The sample includes a rich inline Projection-like object under `meta.projections`.

Part 4 allows Projection references and limited inline notes, but intentionally does not define full Projection internals.

Finding: **The sample validates the need for `meta.projections`, but also shows why Part 4 should keep inline Projection fragments limited.**

Recommended migration:

```yaml
meta:
  projections:
    - role: generation
      ref: projection://code-design-performance-heapq-v0
      inline:
        purpose: extract implementation and performance reasoning from source code
        audience:
          - software engineer
          - LLM code assistant
```

For reusable or governed Projections, the full Projection should move to Part 5 style Projection documents or a Projection Library.

### 18.5.5 Occurrence roles

The sample uses highly specific roles such as:

- `establishes_performance_boundary`
- `frames_api_design`
- `explains_non_textbook_choice`
- `identifies_cost_driver`
- `supports_design_choice`

Part 4 allows open role vocabularies in Core mode.

Finding: **This supports keeping Occurrence role vocabulary open in Core mode.**

If Part 4 required a closed role vocabulary, the heapq sample would either lose precision or require many domain-specific additions to Core.

### 18.5.6 Relation namespace

The Part 3 heapq review concluded that no separate Relation object was needed for that experiment.

Ordering, Section grouping, role, local rationale, and source anchors were sufficient.

Finding: **This supports Part 4's decision to keep `relations` optional.**

### 18.5.7 Entity content risk

The Part 3 review noted that Entity `content` fields may become mini-summaries.

Part 4 allows `content`, `payload`, or `ref` but does not judge Entity granularity.

Finding: **This remains a conceptual and authoring-guide issue, not a Core validation issue.**

Part 4 should not attempt to validate whether an Entity is too explanatory.

Part 6 or Projection profiles may define granularity guidance.

## 18.6 Heapq Candidate: Part 4 Rewrite Sketch

The following sketch shows the heapq sample in a Part 4-conforming style.

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: part3-heapq-performance-001
  status: draft
  projections:
    - role: generation
      ref: projection://code-design-performance-heapq-v0
      inline:
        purpose: extract implementation and performance reasoning from source code
        audience:
          - software engineer
          - LLM code assistant
sources:
  - id: SRC-heapq-py
    type: code_file
    title: CPython heapq.py
    uri: https://github.com/python/cpython/blob/main/Lib/heapq.py
    revision: main
sections:
  - id: SEC-001
    title: Heap invariant as performance boundary
    anchors:
      - source: SRC-heapq-py
        type: line_range
        ranges:
          - start: 3
            end: 32
          - start: 41
            end: 76
        precision: exact
        role: source_context
    occurrences:
      - OCC-001
      - OCC-002
      - OCC-003
occurrences:
  - id: OCC-001
    entity: IE-001
    role: establishes_performance_boundary
    rationale: The heap invariant defines what must be preserved by every operation.
  - id: OCC-002
    entity: IE-002
    role: frames_api_design
    rationale: The API design constrains how users reason about heap behavior as a normal Python list.
  - id: OCC-003
    entity: IE-003
    role: explains_restoration_strategy
entities:
  - id: IE-001
    kind: structural_principle
    content: A heap is represented as an array constrained by an invariant that keeps the smallest item at index 0.
  - id: IE-002
    kind: design_choice
    content: CPython's heap API uses 0-based indexing and exposes a min-heap interface to behave naturally as a Python list.
  - id: IE-003
    kind: algorithmic_operation
    content: Removing the root is handled by moving a lower-level item into the root and percolating it down until the invariant is restored.
structure:
  sections:
    - SEC-001
```

This sketch is not intended as the final heapq sample document.

It demonstrates that the Part 4 shape can represent the Part 3 candidate with predictable migration rules.

## 18.7 Recipe Test: Conformance Findings

The recipe test is more valuable as a multi-Projection shape test than as a concrete YAML migration test.

It demonstrates that the same source material may produce different Sections and Entities under different Projections.

### 18.7.1 Required namespaces

The recipe test can be represented using the required Part 4 namespaces:

- `meta` records document identity and Projection references;
- `sources` records the recipe sketch or actual recipe source;
- `sections` records Projection-shaped local source windows;
- `occurrences` records practical roles within those windows;
- `entities` records reusable material such as cooking steps, ingredient functions, shopping items, cautions, or coaching prompts.

Finding: **The required namespace set is sufficient for the recipe tests.**

### 18.7.2 Projection-shaped Sections

The recipe test strongly supports the Part 4 definition of Section as a Projection-shaped local source window.

For the same recipe source:

- cooking execution yields procedural Sections;
- ingredient substitution yields functional ingredient Sections;
- shopping/prep yields procurement and preparation Sections;
- beginner teaching yields explanation and mistake-prevention Sections;
- dietary constraint yields risk and adaptation Sections.

Finding: **Part 4 should keep Section independent from source headings.**

### 18.7.3 Entity kind openness

The recipe test expects Entity kinds such as:

- `cooking_step`
- `timing_constraint`
- `heat_control_rule`
- `ingredient_function`
- `substitution_target`
- `shopping_item`
- `prep_task`
- `beginner_explanation`
- `dietary_constraint_flag`
- `adaptation_target`

Part 4 keeps Entity `kind` recommended but not mandatory and leaves the vocabulary open in Core mode.

Finding: **The recipe test strongly supports open Entity kind vocabularies in Core mode.**

A closed Core Entity taxonomy would push too much domain-specific vocabulary into Core.

### 18.7.4 Occurrence role without Relation

The recipe test asks whether practical use can be represented without a separate Relation object.

For example, the same ingredient may appear as:

- a cooking item;
- a substitution target;
- a shopping item;
- a dietary constraint flag.

Part 4 can express this through different Occurrences referencing the same or similar Entities under different Sections.

Finding: **Occurrence role plus Section context is sufficient for the initial recipe tests.**

`relations` should remain optional.

### 18.7.5 Source anchor flexibility

Recipes may need anchors to ingredient lines, step numbers, inferred contexts, or grouped source regions.

Part 4's anchor model supports line ranges, paragraphs, heading paths, approximate anchors, and extension fields.

Finding: **The Part 4 anchor model is flexible enough, but recipe profiles may need recipe-specific anchor types.**

Possible profile-defined anchor types:

- `ingredient_line`
- `recipe_step`
- `ingredient_group`
- `procedure_group`

These should not be required in Core.

## 18.8 Recipe Test: Part 4 Rewrite Sketch

The following sketch shows how the recipe source could be represented for the Ingredient Function / Substitution Projection.

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: recipe-substitution-sample-001
  status: draft
  projections:
    - role: generation
      ref: projection://recipe-ingredient-function-substitution-v0
      inline:
        purpose: identify ingredient functions and support substitution decisions
sources:
  - id: SRC-recipe-sample-001
    type: document
    title: Simple miso soup with tofu and wakame recipe sketch
    media_type: text/plain
sections:
  - id: SEC-dashi-function
    title: Dashi ingredients as umami system
    anchors:
      - source: SRC-recipe-sample-001
        type: heading_path
        path:
          - Ingredients
        precision: inferred
      - source: SRC-recipe-sample-001
        type: heading_path
        path:
          - Steps
        precision: inferred
    occurrences:
      - OCC-kombu-function
      - OCC-bonito-function
      - OCC-dashi-substitution-target
occurrences:
  - id: OCC-kombu-function
    entity: IE-kombu-function
    role: identifies_ingredient_function
  - id: OCC-bonito-function
    entity: IE-bonito-function
    role: identifies_ingredient_function
  - id: OCC-dashi-substitution-target
    entity: IE-dashi-substitution-target
    role: marks_substitution_target
entities:
  - id: IE-kombu-function
    kind: ingredient_function
    content: Kombu contributes glutamate-rich umami.
  - id: IE-bonito-function
    kind: ingredient_function
    content: Bonito flakes contribute smoky and savory flavor.
  - id: IE-dashi-substitution-target
    kind: substitution_target
    content: Dashi can be approximated by another broth that supplies savory depth.
```

This sketch shows that Part 4 can represent a non-technical, practical, Projection-shaped decomposition without adding recipe concepts to Core.

## 18.9 Cross-sample Findings

### 18.9.1 Required namespaces are sufficient

Both heapq and recipe tests fit the required namespaces.

No additional required namespace is needed for the current sample set.

### 18.9.2 `relations` should remain optional

Both tests support reconstruction using:

- Section ordering;
- Occurrence roles;
- Entity reuse;
- source anchors;
- metadata Projection references;
- optional structure ordering.

Neither test requires `relations` as a Core namespace.

### 18.9.3 Open vocabularies are necessary

Both tests rely on domain- or Projection-shaped vocabularies.

Core should not freeze:

- Occurrence role vocabulary;
- Entity kind vocabulary;
- recipe-specific anchor types;
- code-specific role values.

Part 4's warning-based Core mode is appropriate.

### 18.9.4 Anchor role/purpose may need clarification

The heapq sample used `anchor_type` to express why a source region was selected.

Part 4 currently uses `type` to identify anchor kind such as `line_range`.

This creates a possible missing field for the anchor's local purpose.

Recommendation:

- keep `type` as the anchor mechanism;
- add a recommended optional anchor field such as `role` or `purpose`;
- do not make it mandatory.

### 18.9.5 Placeholder policy should remain permissive in Core mode

Part 3 samples include planning-stage and expected-shape examples, especially in the recipe test.

These are valuable during drafting and Projection evaluation.

Part 4 should continue to allow placeholder objects in Core mode with warnings.

Strict mode and profiles can reject them.

### 18.9.6 CLI mapping belongs outside Core

This review confirms that Part 4 should define validation requirements but should not define IdeaMark CLI diagnostic codes, command behavior, or CLI output schema.

Those belong in the IdeaMark CLI repository or a CLI-specific contract.

Part 4 should remain a document-format specification.

## 18.10 Recommended Follow-up Changes to Part 4

This review suggests only small Part 4 refinements:

1. In the Source Anchors chapter, mention optional anchor `role` or `purpose` for source-region function.
2. In Compatibility and Migration, explicitly mention migration from singular `anchor` to array `anchors`.
3. In Normative Examples, consider adding one code-source example and one recipe-source example later.
4. In Validation Rules, keep unknown role/kind values as warnings in Core mode.
5. Do not add CLI diagnostic mapping to Part 4.

## 18.11 Review Conclusion

The Part 3 samples are broadly compatible with the Part 4 draft.

The main changes required are serialization-level migrations:

- keyed maps to arrays;
- `original_sources` to `sources`;
- singular `anchor` to `anchors`;
- legacy anchor fields to common anchor shape;
- rich inline Projection data to `meta.projections` reference or limited inline note.

The samples support the major Part 4 design decisions:

- required Core namespaces are sufficient;
- array-based object shape is workable;
- Section / Occurrence / Entity remain useful;
- `relations`, `perspectives`, and `provenance` can remain optional;
- open vocabularies are necessary;
- Part 4 should not define CLI implementation behavior.
