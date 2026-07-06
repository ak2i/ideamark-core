# 1. Authoring Principles

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 1.1 Do Not Start by Summarizing

IdeaMark authoring should not begin with a generic summary of the Original Source.

A summary compresses expression.

IdeaMark authoring creates reusable access structures.

The author should first ask:

- What future activity should this IdeaMark document support?
- Which Projection is shaping the decomposition?
- What source regions should future users return to?
- What reusable material should be preserved as Entities?
- How does that material participate in local source windows?

## 1.2 Projection Comes Before Decomposition

The same Original Source may produce different IdeaMark documents under different Projections.

For example, the same recipe may be authored as:

- a cooking execution guide;
- an ingredient substitution guide;
- a shopping and prep plan;
- a beginner teaching aid;
- a dietary constraint review.

The author should not try to create a Projection-neutral master decomposition.

Projection-neutral decomposition tends to become a catalog, index, or dictionary rather than an access structure for future reconstruction.

## 1.3 Preserve Return Paths to the Source

An IdeaMark document should help future humans and AI systems return to the right source material.

Anchors do not need to be perfect.

Approximate and inferred anchors are acceptable when exact anchors are unavailable.

However, the document should preserve enough traceability to support review and reconstruction.

## 1.4 Keep Meaning Activatable, Not Stored

IdeaMark does not need to store final meaning.

It should preserve enough structure to help future activity generate an activation expression.

An activation expression may be:

- an explanation;
- a diagram;
- a plan;
- a warning;
- a question;
- a checklist;
- a code review note;
- a teaching prompt;
- a decision memo.

The authored document should make such activation easier without claiming to contain the final meaning itself.

## 1.5 Prefer Functional Boundaries Over Semantic Labels

Section, Occurrence, and Entity are functional modeling objects.

They should not be treated as fixed semantic categories.

A Section is not necessarily a source heading.

An Occurrence is not necessarily a textual occurrence.

An Entity is not necessarily a real-world object or ontology node.

The author should choose boundaries that support future reconstruction under the Projection.

## 1.6 Make Incompleteness Visible

Incomplete documents are allowed in Core mode.

Drafts, templates, staged authoring outputs, and partial AI generations may intentionally contain placeholders.

However, incompleteness should be visible through:

- `status` fields;
- notes;
- empty arrays;
- review markers;
- validator warnings;
- profile-specific review queues.

Do not hide uncertainty by inventing precise-looking structure.

## 1.7 Keep Core Open and Profiles Specific

Core authoring should use open vocabularies when needed.

Domain-specific strictness should move to profiles.

For example:

- recipe-specific Entity kinds belong to a recipe profile;
- audit-grade anchor requirements belong to an audit profile;
- code-analysis role vocabularies belong to a code profile;
- CLI diagnostic codes belong to CLI tooling.

## 1.8 Author for Reuse, Not Exhaustiveness

An IdeaMark document does not need to extract everything.

It should extract what is useful for the intended future activity.

Useful omission is allowed.

Omission should become a problem only when it prevents the intended reconstruction or hides important traceability.

## 1.9 Separate Authoring Notes from Core Claims

Authors may record rationale, uncertainty, review notes, or generation notes.

Such notes are useful for collaboration and review.

They should not be confused with verified source content or final meaning.

When possible, make local rationale clearly distinct from source-derived material.

## 1.10 Treat Samples as Tests of Authoring Judgment

Part 4 samples are not just syntax examples.

They demonstrate authoring judgment:

- choosing Section boundaries;
- deciding Entity granularity;
- assigning Occurrence roles;
- selecting anchor precision;
- deciding whether optional `structure` helps.

Part 6 should use samples to explain those judgments.
