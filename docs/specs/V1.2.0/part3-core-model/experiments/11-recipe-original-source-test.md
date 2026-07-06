# Recipe Original Source Test

**Part:** 3 — Core Model  
**Status:** Design Experiment  
**Type:** Non-technical Domain / Multi-Projection Generation Test

This document proposes a non-technical Original Source test for Part 3 using a cooking recipe.

The purpose is to check whether the Section / Occurrence / Entity interpretation still works outside code, RFCs, and engineering documents.

Cooking recipes are useful because the same recipe can support many different Human-AI Intellectual Activities:

- cooking the dish as written;
- substituting unavailable ingredients;
- planning shopping and prep work;
- adapting for dietary constraints;
- teaching a beginner;
- optimizing timing and kitchen workflow;
- understanding the functional role of ingredients;
- scaling portions;
- converting the recipe into a meal plan.

## 1. Candidate Original Source

For this design experiment, the source may be any sufficiently explicit recipe with ingredients and steps.

To avoid dependence on a particular external recipe at this planning stage, this note uses a generic recipe source pattern.

```yaml
original_source:
  id: SRC-recipe-sample-001
  source_type: cooking_recipe
  media_type: text
  expected_parts:
    - title
    - ingredients
    - quantities
    - preparation steps
    - cooking steps
    - timing information
    - serving notes
```

A later experiment may replace this with a public-domain or permissively licensed recipe.

## 2. Why Recipes Are Useful for Part 3

A recipe looks simple, but it contains multiple kinds of reusable intellectual material.

For example, a single instruction such as:

```text
Simmer kombu and bonito flakes to make dashi, then use it as the base of the soup.
```

may be decomposed differently depending on Projection:

- as a step in a procedure;
- as an ingredient transformation;
- as a source of umami;
- as a timing dependency;
- as an allergen or dietary issue;
- as a substitution target;
- as a beginner explanation target;
- as a shopping item.

This makes recipes a useful test for whether Section / Occurrence / Entity are truly Projection-shaped rather than domain-specific engineering artifacts.

## 3. Candidate Recipe Sketch

The following sketch is only a test fixture, not a normative recipe.

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

This sketch is intentionally ordinary.

The test is not whether the recipe is special, but whether Projections generate different useful structures from the same source.

## 4. Candidate Generation Projections

### 4.1 Cooking Execution Projection

```yaml
projection:
  id: recipe-cooking-execution-v0
  purpose: help a cook execute the recipe successfully as written
  intended_activity:
    - cook the dish
    - follow timing and order
    - avoid common execution mistakes
  focus:
    - ordered steps
    - timing dependencies
    - heat control
    - ingredient readiness
    - serving sequence
  non_goals:
    - nutritional analysis
    - ingredient substitution
    - cultural explanation
```

Expected Sections:

```yaml
sections:
  - title: Prepare dashi base
  - title: Prepare tofu and wakame
  - title: Combine soup components
  - title: Add miso without boiling
  - title: Finish and serve
```

Expected Entities:

```yaml
entities:
  - kind: cooking_step
    material: soak kombu and heat gently
  - kind: timing_constraint
    material: remove kombu before boiling
  - kind: cooking_step
    material: add bonito flakes and strain dashi
  - kind: heat_control_rule
    material: turn off heat before dissolving miso
```

### 4.2 Ingredient Function / Substitution Projection

```yaml
projection:
  id: recipe-ingredient-function-substitution-v0
  purpose: identify ingredient functions and support substitution decisions
  intended_activity:
    - understand what each ingredient contributes
    - replace unavailable ingredients
    - preserve functional outcome where possible
  focus:
    - umami source
    - saltiness
    - aroma
    - texture
    - broth base
    - garnish
  non_goals:
    - strict authenticity
    - exact recipe execution
```

Expected Sections:

```yaml
sections:
  - title: Dashi ingredients as umami system
  - title: Miso as seasoning and body
  - title: Tofu as soft protein texture
  - title: Wakame as marine texture and aroma
  - title: Green onion as fresh aromatic garnish
```

Expected Entities:

```yaml
entities:
  - kind: ingredient_function
    material: kombu contributes glutamate-rich umami
  - kind: ingredient_function
    material: bonito flakes contribute smoky and savory flavor
  - kind: substitution_target
    material: dashi can be approximated by another broth that supplies savory depth
  - kind: texture_function
    material: tofu provides soft protein body
```

### 4.3 Shopping and Prep Planning Projection

```yaml
projection:
  id: recipe-shopping-prep-v0
  purpose: turn the recipe into shopping and preparation tasks
  intended_activity:
    - make a shopping list
    - group pantry and fresh items
    - plan prep before cooking
  focus:
    - ingredient list
    - quantities if available
    - pantry vs fresh items
    - pre-soak and rehydration tasks
    - cutting tasks
  non_goals:
    - cooking theory
    - substitution reasoning
```

Expected Sections:

```yaml
sections:
  - title: Pantry and shelf-stable items
  - title: Fresh refrigerated items
  - title: Pre-cooking hydration tasks
  - title: Knife prep tasks
  - title: Ready-to-cook checklist
```

Expected Entities:

```yaml
entities:
  - kind: shopping_item
    material: kombu
  - kind: shopping_item
    material: miso paste
  - kind: prep_task
    material: rehydrate wakame
  - kind: prep_task
    material: cut tofu and slice green onion
```

### 4.4 Beginner Teaching Projection

```yaml
projection:
  id: recipe-beginner-teaching-v0
  purpose: teach a beginner why the recipe steps matter
  intended_activity:
    - explain unfamiliar cooking terms
    - prevent common mistakes
    - generate coaching guidance
  focus:
    - why kombu is removed before boiling
    - why miso is dissolved off heat
    - how dashi works
    - what to prepare before heating
  non_goals:
    - advanced flavor theory
    - exact cultural history
```

Expected Sections:

```yaml
sections:
  - title: What dashi is doing in the soup
  - title: Why kombu should not be boiled hard
  - title: Why miso should not be boiled
  - title: How to prepare add-ins before combining
  - title: Beginner-friendly execution flow
```

Expected Entities:

```yaml
entities:
  - kind: beginner_explanation
    material: dashi is the soup's savory base
  - kind: mistake_prevention
    material: remove kombu before boiling to avoid unwanted flavor or texture
  - kind: mistake_prevention
    material: dissolve miso off heat to preserve flavor and avoid harsh boiling
  - kind: coaching_prompt
    material: prepare wakame and tofu before final assembly
```

### 4.5 Dietary Constraint Projection

```yaml
projection:
  id: recipe-dietary-constraint-v0
  purpose: adapt the recipe for dietary requirements
  intended_activity:
    - identify animal-derived ingredients
    - identify soy-based ingredients
    - propose constraint-aware substitutions
  focus:
    - bonito flakes as fish product
    - miso and tofu as soy products
    - sodium from miso
    - vegetarian or vegan adaptation
    - allergy concerns
  non_goals:
    - exact nutritional calculation
    - full medical advice
```

Expected Sections:

```yaml
sections:
  - title: Animal-derived ingredients
  - title: Soy-based ingredients
  - title: Sodium-heavy components
  - title: Vegan or vegetarian adaptation points
  - title: Allergy review checklist
```

Expected Entities:

```yaml
entities:
  - kind: dietary_constraint_flag
    material: bonito flakes are fish-derived
  - kind: dietary_constraint_flag
    material: miso and tofu are soy-based
  - kind: adaptation_target
    material: replace bonito-based dashi for vegan adaptation
  - kind: caution
    material: miso may contribute substantial sodium
```

## 5. Expected Multi-Projection Differences

| Projection | Likely Section Shape | Entity Shape | Future Activity |
|---|---|---|---|
| Cooking Execution | ordered procedural windows | step, timing constraint, heat rule | cook the dish |
| Ingredient Function / Substitution | functional ingredient windows | ingredient function, substitution target | replace ingredients |
| Shopping and Prep | procurement and task windows | shopping item, prep task, checklist item | shop and prepare |
| Beginner Teaching | explanation and mistake-prevention windows | explanation, mistake prevention, coaching prompt | teach or coach |
| Dietary Constraint | risk and adaptation windows | constraint flag, adaptation target, caution | dietary adaptation |

## 6. Why This Test Matters

The recipe domain forces IdeaMark to separate source text from intended activity.

A recipe source may appear to be a procedure, but it can also support substitution reasoning, education, shopping, dietary adaptation, or workflow planning.

If Section / Occurrence / Entity works here, the model is less likely to be limited to technical documentation.

## 7. Part 3 Hypothesis

The same recipe should produce different IdeaMark-like Documents under different Projections.

This should reinforce the interpretation:

```text
Section
  = Projection-shaped local source window

Occurrence
  = role-bearing placement of reusable material within that window

Entity
  = reusable material shaped by Projection and available for later reconstruction
```

For recipes, Section may be especially important because different Projections reorganize the same source across different practical concerns.

For example, the same ingredient line may appear in:

- an execution Section;
- a substitution Section;
- a shopping Section;
- a dietary constraint Section.

The Entity may remain similar, but the Occurrence role and Section context change.

## 8. Expected Feedback for Core Model

This test should help answer:

1. Whether Section is still useful outside technical domains.
2. Whether Occurrence role can express practical use without a Relation object.
3. Whether Entity should represent ingredients, functions, tasks, cautions, or all of these depending on Projection.
4. Whether the same source fragment can appear in multiple Sections under different Projections.
5. Whether source anchors should refer to ingredient lines, steps, groups, or inferred recipe contexts.

## 9. Next Step

Generate two candidate IdeaMark-like structures from the same recipe sketch:

1. Cooking Execution Projection.
2. Ingredient Function / Substitution Projection.

Then compare how Section, Occurrence, and Entity differ.

A later test may replace the sketch with a public-domain recipe or a recipe explicitly authored for the IdeaMark sample library.
