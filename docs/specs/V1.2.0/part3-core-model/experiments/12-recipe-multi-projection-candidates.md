# Recipe Multi-Projection Candidate Test

**Part:** 3 — Core Model  
**Status:** Design Experiment  
**Type:** Non-technical Multi-Projection Candidate IdeaMark-like Documents

This document generates two small candidate IdeaMark-like structures from the same recipe sketch under different generation Projections.

The purpose is to test whether Section / Occurrence / Entity remains useful in a non-technical domain where the Original Source is practical everyday knowledge rather than code or formal design prose.

## 1. Original Source

```yaml
original_sources:
  - id: SRC-recipe-miso-soup-sketch-001
    source_type: cooking_recipe
    media_type: text
    status: test_fixture
```

Source sketch:

```text
Dish: Simple miso soup with tofu and wakame

Ingredients:
- water
- kombu
- bonito flakes
- miso paste
- tofu
- dried wakame
- green onion

Steps:
1. Soak kombu in water, then heat gently.
2. Remove kombu before boiling.
3. Add bonito flakes, simmer briefly, then strain to make dashi.
4. Rehydrate wakame and cut tofu.
5. Warm the dashi and add tofu and wakame.
6. Turn off heat and dissolve miso paste into the soup.
7. Serve with sliced green onion.
```

This source is intentionally simple.

The test is whether different Projections generate different reusable access structures from the same ordinary recipe.

## 2. Candidate A — Cooking Execution Projection

```yaml
meta:
  experiment_id: recipe-cooking-execution-candidate-001
  status: exploratory
  projections:
    - role: generation
      id: recipe-cooking-execution-v0
      purpose: help a cook execute the recipe successfully as written
      focus:
        - ordered steps
        - timing dependencies
        - heat control
        - ingredient readiness
        - serving sequence
```

### 2.1 Candidate Structure

```yaml
sections:
  SEC-EXEC-001:
    title: Prepare dashi base in safe order
    anchor:
      source: SRC-recipe-miso-soup-sketch-001
      source_fragments:
        - ingredients: [water, kombu, bonito flakes]
        - steps: [1, 2, 3]
      anchor_type: procedural_step_group
    occurrences:
      - OCC-EXEC-001
      - OCC-EXEC-002
      - OCC-EXEC-003

  SEC-EXEC-002:
    title: Prepare add-ins before final assembly
    anchor:
      source: SRC-recipe-miso-soup-sketch-001
      source_fragments:
        - ingredients: [tofu, dried wakame]
        - steps: [4]
      anchor_type: preparation_group
    occurrences:
      - OCC-EXEC-004
      - OCC-EXEC-005

  SEC-EXEC-003:
    title: Warm soup components without overcooking
    anchor:
      source: SRC-recipe-miso-soup-sketch-001
      source_fragments:
        - ingredients: [dashi, tofu, wakame]
        - steps: [5]
      anchor_type: assembly_step
    occurrences:
      - OCC-EXEC-006

  SEC-EXEC-004:
    title: Add miso off heat
    anchor:
      source: SRC-recipe-miso-soup-sketch-001
      source_fragments:
        - ingredients: [miso paste]
        - steps: [6]
      anchor_type: heat_control_step
    occurrences:
      - OCC-EXEC-007
      - OCC-EXEC-008

  SEC-EXEC-005:
    title: Finish and serve
    anchor:
      source: SRC-recipe-miso-soup-sketch-001
      source_fragments:
        - ingredients: [green onion]
        - steps: [7]
      anchor_type: serving_step
    occurrences:
      - OCC-EXEC-009

entities:
  IE-EXEC-001:
    kind: cooking_step
    content: |
      Soak kombu in water and heat gently to begin extracting the dashi base.
    source_role: dashi_start

  IE-EXEC-002:
    kind: timing_constraint
    content: |
      Remove kombu before boiling.
    source_role: avoid_overheating_kombu

  IE-EXEC-003:
    kind: cooking_step
    content: |
      Add bonito flakes, simmer briefly, then strain to complete dashi.
    source_role: dashi_completion

  IE-EXEC-004:
    kind: prep_task
    content: |
      Rehydrate dried wakame before adding it to the soup.
    source_role: ingredient_readiness

  IE-EXEC-005:
    kind: prep_task
    content: |
      Cut tofu before final assembly.
    source_role: ingredient_readiness

  IE-EXEC-006:
    kind: assembly_step
    content: |
      Warm the dashi and add tofu and wakame.
    source_role: combine_components

  IE-EXEC-007:
    kind: heat_control_rule
    content: |
      Turn off the heat before dissolving miso paste.
    source_role: miso_heat_control

  IE-EXEC-008:
    kind: cooking_step
    content: |
      Dissolve miso paste into the soup after heat is turned off.
    source_role: miso_addition

  IE-EXEC-009:
    kind: finishing_step
    content: |
      Serve with sliced green onion.
    source_role: finishing_garnish

occurrences:
  OCC-EXEC-001:
    entity: IE-EXEC-001
    role: begins_base_preparation
    rationale: |
      The execution Projection treats kombu soaking and gentle heating as the first procedural unit.

  OCC-EXEC-002:
    entity: IE-EXEC-002
    role: constrains_heat_timing
    rationale: |
      Removing kombu before boiling is represented as a timing and heat-control constraint.

  OCC-EXEC-003:
    entity: IE-EXEC-003
    role: completes_base_preparation
    rationale: |
      Bonito addition and straining complete the dashi stage before add-ins are handled.

  OCC-EXEC-004:
    entity: IE-EXEC-004
    role: prepares_ingredient_for_assembly
    rationale: |
      Wakame must be ready before the soup is assembled.

  OCC-EXEC-005:
    entity: IE-EXEC-005
    role: prepares_ingredient_for_assembly
    rationale: |
      Tofu cutting is treated as readiness work rather than flavor logic.

  OCC-EXEC-006:
    entity: IE-EXEC-006
    role: assembles_soup_components
    rationale: |
      The Projection organizes this as a procedural assembly step.

  OCC-EXEC-007:
    entity: IE-EXEC-007
    role: prevents_execution_error
    rationale: |
      Heat control is crucial to successful execution of the recipe as written.

  OCC-EXEC-008:
    entity: IE-EXEC-008
    role: finishes_seasoning_step
    rationale: |
      Miso addition is grouped with heat control because execution success depends on the order.

  OCC-EXEC-009:
    entity: IE-EXEC-009
    role: completes_serving_sequence
    rationale: |
      Garnish is treated as the final serving action.

structure:
  sections:
    - SEC-EXEC-001
    - SEC-EXEC-002
    - SEC-EXEC-003
    - SEC-EXEC-004
    - SEC-EXEC-005
```

### 2.2 Possible Activation Expression

> To cook the soup as written, first prepare the dashi in order: soak and gently heat kombu, remove it before boiling, then briefly simmer bonito flakes and strain. While the base is ready, rehydrate wakame and cut tofu. Warm the dashi with tofu and wakame, then turn off the heat before dissolving miso. Finish with sliced green onion.

## 3. Candidate B — Ingredient Function / Substitution Projection

```yaml
meta:
  experiment_id: recipe-ingredient-function-candidate-001
  status: exploratory
  projections:
    - role: generation
      id: recipe-ingredient-function-substitution-v0
      purpose: identify ingredient functions and support substitution decisions
      focus:
        - umami source
        - saltiness
        - aroma
        - texture
        - broth base
        - garnish
```

### 3.1 Candidate Structure

```yaml
sections:
  SEC-FUNC-001:
    title: Dashi ingredients as umami system
    anchor:
      source: SRC-recipe-miso-soup-sketch-001
      source_fragments:
        - ingredients: [water, kombu, bonito flakes]
        - steps: [1, 2, 3]
      anchor_type: ingredient_function_group
    occurrences:
      - OCC-FUNC-001
      - OCC-FUNC-002
      - OCC-FUNC-003

  SEC-FUNC-002:
    title: Miso as seasoning and body
    anchor:
      source: SRC-recipe-miso-soup-sketch-001
      source_fragments:
        - ingredients: [miso paste]
        - steps: [6]
      anchor_type: seasoning_function
    occurrences:
      - OCC-FUNC-004
      - OCC-FUNC-005

  SEC-FUNC-003:
    title: Tofu as soft protein texture
    anchor:
      source: SRC-recipe-miso-soup-sketch-001
      source_fragments:
        - ingredients: [tofu]
        - steps: [4, 5]
      anchor_type: texture_function
    occurrences:
      - OCC-FUNC-006

  SEC-FUNC-004:
    title: Wakame as marine texture and aroma
    anchor:
      source: SRC-recipe-miso-soup-sketch-001
      source_fragments:
        - ingredients: [dried wakame]
        - steps: [4, 5]
      anchor_type: texture_aroma_function
    occurrences:
      - OCC-FUNC-007

  SEC-FUNC-005:
    title: Green onion as fresh aromatic garnish
    anchor:
      source: SRC-recipe-miso-soup-sketch-001
      source_fragments:
        - ingredients: [green onion]
        - steps: [7]
      anchor_type: garnish_function
    occurrences:
      - OCC-FUNC-008

entities:
  IE-FUNC-001:
    kind: ingredient_function
    content: |
      Kombu contributes savory depth to the broth base.
    source_role: umami_base

  IE-FUNC-002:
    kind: ingredient_function
    content: |
      Bonito flakes contribute savory and aromatic character to the dashi.
    source_role: umami_aroma

  IE-FUNC-003:
    kind: substitution_target
    content: |
      Dashi can be approximated by another broth or ingredient combination that supplies savory depth.
    source_role: broth_substitution_target

  IE-FUNC-004:
    kind: ingredient_function
    content: |
      Miso paste provides saltiness, fermented aroma, and body to the soup.
    source_role: seasoning_body

  IE-FUNC-005:
    kind: substitution_constraint
    content: |
      Replacing miso requires preserving both saltiness and fermented savory character, not only salt level.
    source_role: miso_substitution_constraint

  IE-FUNC-006:
    kind: texture_function
    content: |
      Tofu provides soft protein texture and mild body.
    source_role: soft_protein_texture

  IE-FUNC-007:
    kind: texture_function
    content: |
      Wakame provides marine aroma and slippery-soft seaweed texture.
    source_role: marine_texture_aroma

  IE-FUNC-008:
    kind: garnish_function
    content: |
      Green onion adds fresh aroma and visual finish at serving.
    source_role: fresh_aromatic_finish

occurrences:
  OCC-FUNC-001:
    entity: IE-FUNC-001
    role: identifies_primary_umami_source
    rationale: |
      Under this Projection, kombu is not mainly a step item but a functional flavor contributor.

  OCC-FUNC-002:
    entity: IE-FUNC-002
    role: identifies_secondary_umami_source
    rationale: |
      Bonito flakes are modeled by contribution to broth function rather than by cooking order.

  OCC-FUNC-003:
    entity: IE-FUNC-003
    role: opens_substitution_space
    rationale: |
      The combined dashi function defines what a substitute must approximate.

  OCC-FUNC-004:
    entity: IE-FUNC-004
    role: identifies_seasoning_function
    rationale: |
      Miso is interpreted as a flavor and body component rather than only a late recipe step.

  OCC-FUNC-005:
    entity: IE-FUNC-005
    role: constrains_substitution_quality
    rationale: |
      The Projection requires replacement logic, so miso's functional profile becomes important.

  OCC-FUNC-006:
    entity: IE-FUNC-006
    role: identifies_texture_role
    rationale: |
      Tofu's practical role is texture and body, not timing.

  OCC-FUNC-007:
    entity: IE-FUNC-007
    role: identifies_texture_and_aroma_role
    rationale: |
      Wakame is interpreted as a functional ingredient with texture and aroma.

  OCC-FUNC-008:
    entity: IE-FUNC-008
    role: identifies_finish_role
    rationale: |
      Green onion is treated as a garnish function rather than merely the final step.

structure:
  sections:
    - SEC-FUNC-001
    - SEC-FUNC-002
    - SEC-FUNC-003
    - SEC-FUNC-004
    - SEC-FUNC-005
```

### 3.2 Possible Activation Expression

> If an ingredient is unavailable, do not replace it by name alone; replace its function. Kombu and bonito together form the savory dashi base, so a substitute should supply broth depth and aroma. Miso contributes saltiness, fermented aroma, and body, so replacing it requires more than adding salt. Tofu supplies soft protein texture, wakame adds marine texture and aroma, and green onion provides a fresh finish.

## 4. Comparison Between Candidate A and Candidate B

| Aspect | Cooking Execution Projection | Ingredient Function / Substitution Projection |
|---|---|---|
| Primary source organization | ordered procedural stages | ingredient function groups |
| Section shape | step windows | functional ingredient windows |
| Entity kinds | cooking_step, prep_task, heat_control_rule, finishing_step | ingredient_function, substitution_target, substitution_constraint, texture_function |
| Occurrence roles | begins, constrains timing, prepares, assembles, finishes | identifies function, opens substitution space, constrains substitution quality |
| Treatment of kombu | timed procedural ingredient to remove before boiling | umami contributor in broth system |
| Treatment of miso | late step added off heat | seasoning/body function with substitution constraint |
| Treatment of tofu | prep and assembly item | soft protein texture function |
| Future activity | cook the dish correctly | adapt the recipe while preserving function |

## 5. Part 3 Finding

The recipe test strongly supports the Projection-shaped interpretation of Section / Occurrence / Entity.

The Original Source is the same, but the generated IdeaMark-like structures are meaningfully different.

The difference is not a technical artifact of code or RFCs.

It appears in everyday procedural knowledge as well.

## 6. Important Observation

The same source fragment may appear in both candidates while playing a different role.

For example:

```text
Step 6: Turn off heat and dissolve miso paste into the soup.
```

Under Cooking Execution:

```text
role = prevents_execution_error / finishes seasoning step
```

Under Ingredient Function / Substitution:

```text
role = identifies seasoning function / constrains substitution quality
```

This supports the idea that Occurrence is not merely a source occurrence.

It is the placement of reusable material within a Projection-shaped Section.

## 7. Cross-Domain Comparison

Across technical and non-technical sources, the same pattern appears:

```text
Original Source + Projection
  -> Projection-shaped Sections
  -> role-bearing Occurrences
  -> Projection-shaped reusable Entities
```

The source domains tested so far are:

- algorithm implementation code (`heapq.py`);
- subsystem/invariant code (`sqlite pager.c`);
- formal design RFC (`Rust RFC 0001`);
- everyday recipe procedure (`miso soup sketch`).

This suggests that Section / Occurrence / Entity is not merely a code-documentation structure.

It may be a general enough Core structure for Projection-guided knowledge reuse.

## 8. Feedback for Part 3

The recipe test suggests the following refinements for Part 3:

1. Section should be defined as a Projection-shaped local source window, not a document heading.
2. Occurrence should be defined as a role-bearing placement of Entity material within a Section.
3. Entity should be defined as reusable material shaped by Projection, not as a universal concept or summary.
4. Source anchors may refer to ingredient lines, steps, or grouped recipe contexts, not only line ranges.
5. The same source fragment may participate in multiple generated IdeaMark Documents under different roles.

## 9. Remaining Question

The main remaining risk is that Entity content can become too explanatory.

For recipes, this risk is especially visible because ingredient functions are already interpretive.

Part 3 should clarify that Entity payload may contain projection-shaped reusable material, but it should not pretend to store final meaning independent of Original Source, Projection, Situation, and reconstruction activity.
