# 1. Authoring Principles

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 1.1 Authoring Is the Ongoing Activity of Improving Reuse

Authoring is the ongoing activity of improving an IdeaMark Document so that knowledge becomes more reusable under one or more Projections.

Authoring is not a single mandatory workflow.

It may include design, drafting, editing, validation, review, regeneration, migration, and tool-assisted methods such as Progressive Occurrence Resolution.

An authoring process may use all of these activities or only the ones needed for the current situation.

The specification should not require every IdeaMark document to pass through the same human or AI workflow.

## 1.2 Do Not Start by Summarizing

IdeaMark authoring should not begin with a generic summary of the Original Source.

A summary compresses expression.

IdeaMark authoring creates reusable access structures.

The author should first ask:

- What future activity should this IdeaMark document support?
- Which Projection is shaping the decomposition?
- What source regions should future users return to?
- What reusable material should be preserved as Entities?
- How does that material participate in local activity units?

## 1.3 Projection Comes Before Decomposition

The same Original Source may produce different IdeaMark documents under different Projections.

For example, the same recipe may be authored as:

- a cooking execution guide;
- an ingredient substitution guide;
- a shopping and prep plan;
- a beginner teaching aid;
- a dietary constraint review.

The author should not try to create a Projection-neutral master decomposition.

Projection-neutral decomposition tends to become a catalog, index, or dictionary rather than an access structure for future reconstruction.

## 1.4 Section Represents a Local Activity Unit

A Section is a Projection-shaped local source window, but in authoring practice it can be understood as a local activity unit.

A local activity unit is a bounded part of the intended future intellectual activity that can be reopened, inspected, reconstructed, or reused.

A single IdeaMark Document normally contains multiple Sections because the intended activity may involve:

- multiple steps;
- conditional branches;
- alternative paths;
- supporting observations;
- review checkpoints;
- reusable substructures;
- different local contexts within the same Projection.

For example, a recipe source may produce different Sections depending on Projection:

- under a cooking execution Projection, a Section may be "prepare dashi";
- under an ingredient substitution Projection, a Section may be "dashi ingredients as umami system".

The source material may overlap, but the local activity unit differs.

## 1.5 Entity Quality Means Projection-shaped Reusability

Entity quality is not measured by whether an Entity is short, long, abstract, concrete, quoted, summarized, textual, or binary.

Entity quality depends on whether the Entity supports reuse under the Projection.

An Entity may be:

- a source excerpt;
- a summary;
- a phrase that names a useful cut;
- a URI;
- a JSON fragment;
- an image or reference to an image;
- binary material or a reference to binary material;
- a generated label;
- another reusable payload.

The author should ask:

- Can this material be reused later?
- Does it help reconstruct a useful activation expression?
- Is it shaped by the Projection rather than by a generic extraction habit?
- Is it too large to reuse, or too small to reconstruct?
- Is its source relationship traceable enough for the intended use?

## 1.6 Preserve Return Paths to the Source

An IdeaMark document should help future humans and AI systems return to the right source material.

Anchors do not need to be perfect.

Approximate and inferred anchors are acceptable when exact anchors are unavailable.

However, the document should preserve enough traceability to support review and reconstruction.

## 1.7 Keep Meaning Activatable, Not Stored

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

## 1.8 Treat IdeaMark Documents as Working Artifacts

An IdeaMark Document does not need to be treated only as a final completed artifact.

It may be a working artifact in an ongoing knowledge reuse design process.

It may be improved through human review, AI regeneration, validation warnings, Projection changes, sample comparison, migration, or later reuse experience.

This working-artifact stance explains why Core mode allows:

- placeholder objects;
- warning-level incompleteness;
- open vocabularies;
- optional `structure`;
- optional `relations`;
- status and versioning metadata.

A document can become stable enough for a given use without becoming closed to future refinement.

## 1.9 Prefer Functional Boundaries Over Semantic Labels

Section, Occurrence, and Entity are functional modeling objects.

They should not be treated as fixed semantic categories.

A Section is not necessarily a source heading.

An Occurrence is not necessarily a textual occurrence.

An Entity is not necessarily a real-world object or ontology node.

The author should choose boundaries that support future reconstruction under the Projection.

## 1.10 Make Incompleteness Visible

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

## 1.11 Keep Core Open and Profiles Specific

Core authoring should use open vocabularies when needed.

Domain-specific strictness should move to profiles.

For example:

- recipe-specific Entity kinds belong to a recipe profile;
- audit-grade anchor requirements belong to an audit profile;
- code-analysis role vocabularies belong to a code profile;
- CLI diagnostic codes belong to CLI tooling.

## 1.12 Author for Reuse, Not Exhaustiveness

An IdeaMark document does not need to extract everything.

It should extract what is useful for the intended future activity.

Useful omission is allowed.

Omission should become a problem only when it prevents the intended reconstruction or hides important traceability.

## 1.13 Authoring Methods Are Not Core Requirements

Manual authoring, AI-assisted drafting, batch conversion, collaborative review, and Progressive Occurrence Resolution are authoring methods.

They may produce, revise, or evaluate IdeaMark Documents.

They are not Core requirements by themselves.

Part 6 may describe these methods as practical options, but Part 4 remains the source of Core document conformance.

## 1.14 Separate Authoring Notes from Core Claims

Authors may record rationale, uncertainty, review notes, or generation notes.

Such notes are useful for collaboration and review.

They should not be confused with verified source content or final meaning.

When possible, make local rationale clearly distinct from source-derived material.

## 1.15 Treat Samples as Tests of Authoring Judgment

Part 4 samples are not just syntax examples.

They demonstrate authoring judgment:

- choosing Section boundaries;
- deciding Entity granularity;
- assigning Occurrence roles;
- selecting anchor precision;
- deciding whether optional `structure` helps.

Part 6 should use samples to explain those judgments.
