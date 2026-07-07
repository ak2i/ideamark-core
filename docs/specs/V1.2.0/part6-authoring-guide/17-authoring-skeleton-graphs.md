# 17. Authoring Skeleton Graphs

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 17.1 Purpose

This chapter provides practical guidance for authoring **Intellectual Activity Skeleton Graphs**.

Skeleton Graph authoring is retrieval-oriented. It helps future systems find candidate IdeaMark documents, Sections, Occurrences, Entities, and source anchors before full reconstruction.

Skeleton Graphs are optional. They should be added when future retrieval would otherwise require expensive full-document inspection, fragile keyword search, or overly broad domain filtering.

## 17.2 Do Not Start with Keywords

Do not begin Skeleton Graph authoring by listing words that appear in the Original Source.

Instead, ask:

- What future activity should this material help start?
- What activity slots does the Projection require?
- Which Sections, Occurrences, or Entities fill those slots?
- Which compositional links make the candidate reusable?
- Which slots are missing and should become warnings or review points?

## 17.3 Remove Domain Surface Before Naming Slots

Skeleton slots should avoid unnecessary domain vocabulary when the purpose is cross-domain retrieval.

For example, prefer:

```text
unavailable_or_blocked_element
preserved_effect_or_function
alternative_space
compatibility_boundary
confirmation_signal
```

rather than:

```text
missing_ingredient
umami_substitute
recipe_adjustment
```

Domain-specific words may still appear in:

- Entity content;
- Section title;
- Original Source description;
- source anchors;
- Projection notes;
- reconstruction guidance.

The Skeleton Graph should preserve activity composition, not domain-specific surface terms.

## 17.4 Authoring Procedure

A practical authoring procedure is:

1. Read the Projection first.
2. Identify the future retrieval or reconstruction scenario.
3. Identify the activity slots required by the Projection.
4. Create or review Sections, Occurrences, and Entities.
5. Add Skeleton Nodes that reference the relevant structures.
6. Add Skeleton Links that express the activity composition.
7. Mark missing slots as underspecified instead of hiding incompleteness.
8. Test retrieval by asking whether a use-side Projection could match the graph without knowing source-specific keywords.

## 17.5 Node Selection Guidance

Use Section references when a whole local source window participates in the activity structure.

Use Occurrence references when the role-bearing placement matters.

Use Entity references when the reusable material itself is the best retrieval handle.

Use placeholder nodes when the Projection expects a slot but the current document does not provide it.

Example:

```yaml
nodes:
  - id: skn-confirmation
    slot: confirmation_signal
    status: underspecified
```

This is preferable to inventing a source-backed confirmation that does not exist.

## 17.6 Link Selection Guidance

Use Skeleton Links as structural operators, not semantic claims.

Examples:

- use `constraint` when one node bounds another's usability;
- use `dependency` when one node is needed to use or evaluate another;
- use `alternative` when nodes represent selectable options;
- use `confirmation` when one node supplies a check or review point;
- use `aggregation` when multiple nodes form a larger activity unit.

Avoid using Skeleton Links to encode detailed domain claims that should remain in Entity content, Occurrence rationale, or Original Source anchors.

## 17.7 Example: Recipe Substitution

A recipe substitution Projection may need to retrieve material useful for replacing an unavailable component while preserving an effect or function.

A Skeleton Graph can represent that without requiring the user to know the source term.

```yaml
skeletons:
  - id: skel-recipe-substitution-001
    role: retrieval
    projection: projection://recipe-ingredient-function-substitution-v0
    nodes:
      - id: skn-blocked-element
        ref:
          kind: occurrence
          id: OCC-bonito-function
        slot: unavailable_or_blocked_element
      - id: skn-preserved-function
        ref:
          kind: occurrence
          id: OCC-dashi-substitution-target
        slot: preserved_effect_or_function
      - id: skn-alternative-space
        ref:
          kind: section
          id: SEC-dashi-function
        slot: alternative_space
      - id: skn-confirmation
        slot: confirmation_signal
        status: underspecified
    links:
      - id: skl-001
        from: skn-blocked-element
        to: skn-preserved-function
        type: constraint
      - id: skl-002
        from: skn-preserved-function
        to: skn-alternative-space
        type: dependency
      - id: skl-003
        from: skn-alternative-space
        to: skn-confirmation
        type: confirmation
```

A retrieval system can then match a use-side Projection that asks for function-preserving alternatives even if the future query never mentions bonito flakes.

## 17.8 Example: Heapq Performance

A code performance Projection may need to retrieve material useful for explaining how an implementation preserves an invariant while making a design choice.

```yaml
skeletons:
  - id: skel-heapq-performance-001
    role: retrieval
    projection: projection://code-design-performance-heapq-v0
    nodes:
      - id: skn-boundary
        ref:
          kind: occurrence
          id: OCC-001
        slot: preserved_invariant_or_boundary
      - id: skn-design-choice
        ref:
          kind: occurrence
          id: OCC-002
        slot: chosen_operational_form
      - id: skn-restoration
        ref:
          kind: occurrence
          id: OCC-003
        slot: restoration_or_recovery_strategy
    links:
      - id: skl-001
        from: skn-boundary
        to: skn-design-choice
        type: constraint
      - id: skl-002
        from: skn-design-choice
        to: skn-restoration
        type: dependency
```

This graph can support retrieval for questions such as "find implementation material where a design choice is constrained by an invariant and requires a restoration strategy" without depending on exact heap-specific vocabulary.

## 17.9 Retrieval-oriented Review Questions

Review a Skeleton Graph with questions such as:

1. Could a use-side Projection match this graph without knowing the source keywords?
2. Are the slot names domain-reduced enough for the intended reuse scope?
3. Are the Skeleton Links structural rather than semantic claims?
4. Does the graph point back to Sections, Occurrences, Entities, or anchors that support reconstruction?
5. Are missing slots visible?
6. Would a false positive be filtered or marked for review?
7. Does the graph help explain why a candidate was retrieved?

## 17.10 Common Mistakes

Common mistakes include:

- using Skeleton Graphs as keyword lists;
- using domain-specific verbs where domain-reduced slots would work;
- duplicating all semantic relations as Skeleton Links;
- connecting Entities directly without explaining their activity-composition role;
- hiding missing confirmation or review slots;
- treating Skeleton Graphs as a replacement for source anchors;
- treating Skeleton Graph match as proof that reconstruction is safe.

## 17.11 Good Skeleton Graphs Fail Gracefully

A good Skeleton Graph can expose partial matches.

If a candidate contains a blocked element, a preserved function, and an alternative space but lacks a confirmation signal, the retrieval result should not silently fail or silently succeed.

It should produce a partial match with a visible missing slot.

This makes Skeleton Graphs useful not only for retrieval success, but also for responsible reconstruction failure, review routing, and Projection improvement.
