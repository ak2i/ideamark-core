# 14. Common Authoring Mistakes

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 14.1 Purpose

This chapter lists common mistakes that weaken IdeaMark authoring.

Some mistakes may still produce valid Core YAML.

The issue is that they reduce future reuse, reconstruction, reviewability, or traceability.

## 14.2 Starting with a Generic Summary

A common mistake is to summarize the Original Source first and then try to convert the summary into IdeaMark objects.

This often removes the local structure needed for reuse.

Better practice:

- start with the Projection;
- identify future activity;
- preserve return paths to source regions;
- design Sections, Occurrences, and Entities for reuse.

## 14.3 Ignoring the Projection

A document may mention a Projection but not actually use it to shape decomposition.

Symptoms:

- Sections follow source headings mechanically;
- Entities look like generic notes;
- Occurrence roles are vague;
- non-goals are ignored;
- different Projections produce nearly identical documents.

Better practice:

- check whether Section boundaries and Entity granularity would change under another Projection;
- remove material that belongs to non-goals;
- make roles reflect the intended future activity.

## 14.4 Source Flattening

Source flattening converts a rich source into a flat list before authoring.

Examples:

- converting code into a list of function names;
- converting a recipe into a list of ingredients;
- converting a report into a list of bullet points;
- converting an image into only a caption.

Flattening may lose local context, ordering, evidence, visual structure, or design rationale.

Better practice:

- preserve local activity units;
- retain anchors to meaningful source regions;
- use Sections to preserve source context relevant to reuse.

## 14.5 Summary-only Entities

A document may use Entities as miniature summaries.

Symptoms:

- each Entity contains several conclusions;
- Entities cannot be reused independently;
- future search retrieves broad paragraphs instead of reusable material;
- Occurrence roles add little information.

Better practice:

- split Entities when separate reusable materials need independent roles;
- keep summary Entities only when the Projection requires reusable summary payloads;
- evaluate Entity granularity by reuse.

## 14.6 Decorative Sections

Decorative Sections are Sections that do not support future activity.

Symptoms:

- Section titles are generic;
- Sections contain only one arbitrary item;
- boundaries follow formatting rather than Projection;
- a future user would not retrieve or review the Section as a unit.

Better practice:

- model Sections as local activity units;
- merge decorative Sections;
- split large Sections only when reuse improves.

## 14.7 Weak Occurrence Roles

Weak Occurrence roles fail to explain local function.

Examples:

- `related`;
- `item`;
- `mentioned`;
- `contains`;
- `part`.

These roles may be acceptable in early drafts, but they often do not support reconstruction.

Better practice:

- use Projection-shaped roles such as `evidence`, `constraint`, `rationale`, `ordered_step`, `warning`, `substitution_target`, or profile-defined terms;
- make the role local to the Section.

## 14.8 Overusing Relations Too Early

Authors may add Relations before Section and Occurrence structure is sufficient.

This can make the document complex without improving reuse.

Better practice:

- start with Section grouping, Occurrence roles, Entity kinds, and anchors;
- add Relations only when the relationship must be queried, validated, exchanged, or reused independently.

## 14.9 False Precision

False precision occurs when authors invent exact-looking anchors, roles, or source relationships without sufficient support.

Examples:

- exact line ranges after lossy conversion;
- confident source interpretation from uncertain OCR;
- precise binary region references without reliable region mapping;
- generated labels presented as source facts.

Better practice:

- mark approximate or inferred anchors;
- record uncertainty;
- distinguish source-derived material from generated authoring notes.

## 14.10 Hidden Incompleteness

Incomplete documents are allowed, but hidden incompleteness is harmful.

Symptoms:

- missing source references without status notes;
- placeholder material presented as final;
- unresolved references not marked;
- draft AI output treated as reviewed;
- profile-required fields omitted silently.

Better practice:

- use status, notes, warnings, placeholders, or review markers;
- make known limitations visible.

## 14.11 Treating AI Output as Final by Default

AI-generated drafts may be useful, but they should not be treated as final merely because they are fluent or syntactically valid.

Better practice:

- validate references;
- review Projection fit;
- check Entity granularity;
- inspect Section boundaries;
- evaluate retrieval scenarios;
- preserve reviewable changes.

## 14.12 Treating Core as a Domain Ontology

Core provides minimal reusable access-structure concepts.

It is not a domain ontology.

Mistakes include:

- forcing all Entities into universal categories;
- treating `kind` as closed in Core mode;
- adding domain constraints to Core rather than profiles;
- making authoring less reusable by over-normalizing meaning.

Better practice:

- keep Core open;
- move domain-specific strictness to profiles;
- let Projection shape reusable material.

## 14.13 Ignoring Working-artifact Status

IdeaMark Documents may evolve.

Treating every document as final can discourage useful authoring, review, validation, and regeneration.

Better practice:

- record status;
- allow warnings and placeholders when appropriate;
- preserve design history;
- regenerate when reuse evaluation fails;
- treat stability as use-specific rather than permanent.

## 14.14 Mistake Review Checklist

When reviewing a document, ask:

1. Did authoring start from a Projection or from a generic summary?
2. Do Sections represent local activity units?
3. Are Entities reusable under the Projection?
4. Do Occurrence roles explain local function?
5. Are anchors trustworthy enough?
6. Is uncertainty visible?
7. Are Relations justified?
8. Can future retrieval scenarios succeed?
9. Is the document treated as a working artifact when appropriate?
