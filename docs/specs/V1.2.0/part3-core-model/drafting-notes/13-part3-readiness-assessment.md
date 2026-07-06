# Part 3 Readiness Assessment

**Part:** 3 — Core Model  
**Status:** Design Assessment  
**Type:** Readiness / Remaining Questions

This document assesses whether Part 3 is ready to move from exploratory design experiments into specification drafting.

## 1. Summary

Part 3 is now ready to proceed.

The design experiments across multiple Original Source types support the conclusion that the Section / Occurrence / Entity structure is a viable Core Model candidate when defined functionally rather than semantically.

The key interpretation is:

```text
Section
  = Projection-shaped local source window

Occurrence
  = role-bearing placement of reusable material within that window

Entity
  = reusable material shaped by Projection and available for later reconstruction
```

This interpretation is consistent with the Part 1 and Part 2 stance that IdeaMark is not a meaning store and does not replace Original Source material.

## 2. Evidence from Experiments

The following design experiments were created:

- `01-ideamark-document-constraints.md`
- `02-code-original-source-experiment.md`
- `03-heapq-performance-candidate.md`
- `04-heapq-cross-projection-reconstruction.md`
- `05-heapq-json-mongodb-search-simulation.md`
- `06-heapq-multi-projection-generation.md`
- `07-sqlite-pager-original-source-test.md`
- `08-rust-rfc-original-source-test.md`
- `09-sqlite-pager-multi-projection-candidates.md`
- `10-rust-rfc-multi-projection-candidates.md`
- `11-recipe-original-source-test.md`
- `12-recipe-multi-projection-candidates.md`

These experiments covered:

1. algorithm implementation code;
2. subsystem and correctness-invariant code;
3. formal design RFC prose;
4. everyday recipe procedure.

Across these sources, the same pattern appeared:

```text
Original Source + Projection
  -> Projection-shaped Sections
  -> role-bearing Occurrences
  -> Projection-shaped reusable Entities
  -> lower-cost return to Original Source
  -> future activation expression
```

## 3. Main Findings

### 3.1 Projection changes generation

The same Original Source produced different IdeaMark-like structures when the generation Projection changed.

The difference was visible in:

- source regions selected;
- Section boundaries;
- Occurrence roles;
- Entity kinds;
- source anchors;
- likely future activation expressions.

This supports the claim that IdeaMark generation is Projection-guided Decomposition rather than general extraction.

### 3.2 Reconstruction does not require self-contained IdeaMark

The experiments clarified that the important question is not whether an IdeaMark Document alone can reconstruct an activation expression.

The better question is:

> Does the IdeaMark Document reduce the cost of returning to the right Original Source material under a Projection or compatible Projection?

In most non-trivial cases, reconstruction should involve Original Source material again.

### 3.3 Section remains useful

Section is useful when redefined as a Projection-shaped local source window.

It is not:

- a document chapter;
- a topic heading;
- a stored meaning unit;
- an intellectual activity itself.

It is the local source context made useful by a Projection.

### 3.4 Occurrence remains useful

Occurrence is useful when redefined as a role-bearing placement of Entity material within a Section.

It is not merely a textual occurrence or event.

The same Entity-like material may occur under different roles depending on Projection and Section context.

### 3.5 Entity remains useful but needs discipline

Entity is useful as reusable material shaped by Projection.

However, Entity content can easily become a compact summary or mini-meaning store.

Part 3 should clarify that Entity payload preserves reconstruction material, not final meaning independent of Original Source, Projection, Situation, and later activity.

### 3.6 Relation remains unnecessary for Core

The experiments did not require a separate Relation namespace.

Ordering, Section grouping, Occurrence roles, source anchors, and metadata were sufficient.

Relation-like structures may remain a future extension, but they do not appear necessary for the Core Model.

### 3.7 Perspective and Provenance can remain metadata

The experiments did not require Perspective or Provenance as separate Core objects.

Projection references, source references, generation context, source anchors, and local rationale were sufficient.

This supports keeping Perspective and Provenance out of the required Core namespace.

## 4. Recommended Part 3 Direction

Part 3 should now be drafted around the following core objects:

```text
IdeaMark Document
  -> meta
  -> sections
  -> occurrences
  -> entities
  -> structure
```

Where:

```text
meta
  = document-level source, projection, generation, status, and compatibility metadata

sections
  = Projection-shaped local source windows

occurrences
  = role-bearing placements of Entity material within Sections

entities
  = reusable materials shaped by Projection

structure
  = ordering, grouping, or navigation information needed for document-level reconstruction
```

## 5. Remaining Questions Before Final Spec Text

Part 3 can proceed without additional domain experiments, but several specification-level questions remain.

### 5.1 Required versus optional fields

Need to decide the minimal required fields for:

- `meta`;
- `sections`;
- `occurrences`;
- `entities`;
- `structure`.

Likely required fields may include:

```yaml
meta:
  spec_version:
  sources:
  projections:

sections:
  <id>:
    title:
    occurrences:

occurrences:
  <id>:
    entity:
    role:

entities:
  <id>:
    kind:
    content:
```

Source anchors may be required in practical profiles but may remain optional at the abstract Core level if some source types cannot support exact anchors.

### 5.2 Source anchor model

Need to define source anchors flexibly enough to support:

- line ranges;
- paragraphs;
- code spans;
- ingredient lines;
- recipe steps;
- media time ranges;
- image regions;
- dataset rows or columns;
- composite source fragments.

The concept should probably be:

```text
source anchor = traceability claim back to Original Source material
```

not:

```text
source anchor = line range
```

### 5.3 Entity payload boundary

Need to decide how strongly Part 3 warns against summary-like Entities.

A workable stance:

> Entity content may be projection-shaped and explanatory enough to support reconstruction, but it must not be treated as final meaning or as a substitute for Original Source.

### 5.4 Occurrence role vocabulary

Need to decide whether Core defines a controlled vocabulary for Occurrence roles.

Recommendation:

- Core should not define a universal role ontology.
- It may define role as a required or recommended string field.
- Profiles or Projection libraries may define role vocabularies.

### 5.5 Structure namespace

Need to decide whether `structure` is required.

Recommendation:

- Keep `structure` optional in Core.
- Use it for document-level ordering, grouping, navigation, or reconstruction paths.
- Do not use it to reintroduce Relation as mandatory Core.

### 5.6 Status and versioning

Need to define document status and versioning minimally.

Possible fields:

```yaml
meta:
  spec_version:
  document_id:
  status:
  generated_at:
  generator:
  source_revision:
  projection_revision:
```

This is likely enough for Part 3 Core.

### 5.7 Multi-Projection and multi-source handling

Need to clarify that:

- one IdeaMark Document may reference multiple Original Sources;
- one IdeaMark Document may reference multiple Projections;
- multiple IdeaMark Documents may be generated from the same Original Source under different Projections;
- different generated documents may later be searched, compared, or reconstructed together.

## 6. No Additional Domain Experiments Required

Additional experiments could be useful later, but they are no longer required to proceed with Part 3.

The current evidence already covers enough diversity:

- technical algorithm code;
- system correctness code;
- formal proposal prose;
- everyday procedural knowledge.

Further experiments should be deferred unless they answer a specific unresolved specification question.

## 7. Recommended Next Step

Begin rewriting the Part 3 README and section drafts around the refined definitions:

```text
Section = Projection-shaped local source window
Occurrence = role-bearing placement within that window
Entity = Projection-shaped reusable material
```

The next drafting task should be:

1. update Part 3 overview;
2. update model boundary and non-goals;
3. define `meta`;
4. define `sections`;
5. define `occurrences`;
6. define `entities`;
7. define anchoring and traceability;
8. define invariants;
9. define minimal JSON/YAML shape.

This is sufficient to move Part 3 from exploration to specification drafting.
