# Part 3 Theoretical Review and Part 5 Transition

**Part:** 3 — Core Model  
**Status:** Review Note  
**Type:** Theory Review / Drafting Transition  
**Version:** IdeaMark Core v1.2.0

## 1. Purpose

This note reviews whether Part 1, Part 2, and Part 3 form a coherent theoretical chain.

It also records the drafting decision that Part 5 should be developed before Part 4.

Part 4 is expected to define concrete YAML representation.

However, the correct YAML shape depends heavily on how Projection is defined as a reusable strategy object.

Therefore, Part 5 should be clarified before Part 4 becomes normative.

## 2. Reviewed Theoretical Chain

The current IdeaMark theory can be summarized as:

```text
Part 1
  Meaning cannot be fixed inside a document.

Part 2
  Human-AI Intellectual Activity requires source-mediated reconstruction under Projection.

Part 3
  Therefore, the Core Model should preserve Projection-shaped access structures, not final meaning.
```

This chain is coherent.

Part 3 now follows from Part 1 and Part 2 rather than competing with them.

## 3. Part 1 to Part 2

Part 1 establishes the philosophical stance that meaning is not simply stored inside source text or generated explanation.

Meaning becomes observable only when expression, interpretation, Situation, and activity produce some consequence.

This implies that a document format should not claim to preserve final meaning.

Part 2 answers this by introducing a reconstruction architecture.

Instead of treating stored knowledge as finished meaning, the architecture treats future use as a reconstruction process involving:

- Original Source material;
- Projection;
- Situation;
- human and AI participants;
- activation expressions;
- intellectual or practical activity.

The theoretical transition is sound:

```text
If meaning cannot be stored as final content,
then the system must preserve the conditions for later reconstruction.
```

## 4. Part 2 to Part 3

Part 2 requires a structure that can support reconstruction without becoming a final interpretation.

Part 3 provides this structure.

The key move is to define Section, Occurrence, and Entity functionally:

```text
Section
  = Projection-shaped local source window

Occurrence
  = role-bearing placement of reusable material within that window

Entity
  = reusable material shaped by Projection and available for later reconstruction
```

This solves an important modeling problem.

If Entity were defined as a fixed semantic object, Part 3 would contradict the Part 1 stance.

If Section were defined as a source heading, Part 3 would collapse back into source structure.

If Occurrence were defined as a textual occurrence only, it would fail to model Projection-shaped role placement.

The current definitions avoid these failures.

## 5. The Core Model No Longer Stores Meaning

The previous risk was that Part 3 might become a knowledge model.

The current draft avoids that by treating the IdeaMark document as an access structure.

The most important correction is:

```text
The question is not:
  Can the IdeaMark document reconstruct the activation expression by itself?

The question is:
  Does the IdeaMark document reduce the cost of returning to the right Original Source material under a Projection or compatible Projection?
```

This makes Part 3 consistent with Part 1 and Part 2.

## 6. Section / Occurrence / Entity Review

### 6.1 Section

Section is now correctly placed as the local source window object.

It is neither a source heading nor a chapter.

It is a bounded context for reopening or reasoning over Original Source material under a Projection.

This is theoretically important because it preserves source-mediated reconstruction.

### 6.2 Occurrence

Occurrence is now correctly placed as the role-bearing placement object.

It explains why Entity material matters in a local source window.

This prevents Entity from having to carry all contextual meaning by itself.

### 6.3 Entity

Entity is now correctly placed as reusable material.

It is not a universal meaning unit.

This prevents Core from becoming an ontology.

Entity becomes useful through Occurrence placement in Section context.

## 7. Relation / Perspective / Provenance Review

The decision to remove Relation, Perspective, and Provenance from required Core namespaces is theoretically consistent.

### 7.1 Relation

Relation would risk turning Core into a semantic graph or ontology.

The experiments showed that Section grouping, Occurrence roles, anchors, and optional structure are enough for the Core layer.

Relation can remain an extension or profile feature.

### 7.2 Perspective

Perspective overlaps heavily with Projection Context.

If Core required Perspective separately, it could create an unnecessary interpretive object between Projection and metadata.

The current design treats Perspective-like information as metadata or Projection context.

### 7.3 Provenance

Provenance overlaps with source references, anchors, generation metadata, local rationale, status, and versioning.

A richer provenance system may be useful later, but Core does not need it as a required namespace.

This keeps Part 3 minimal.

## 8. Traceability Review

Traceability is correctly treated as a Core responsibility.

Because IdeaMark does not replace Original Source material, it must preserve return paths.

The anchor model is also correctly generalized.

Anchors are not text spans.

They are media-independent traceability claims.

This keeps IdeaMark compatible with code, documents, recipes, datasets, images, media, generated artifacts, and future accessible sources.

## 9. Experimental Support Review

The experiments support the theoretical model across multiple domains:

- algorithm implementation code;
- system correctness and state-machine code;
- formal RFC design prose;
- everyday recipe procedure.

The same pattern appeared:

```text
Original Source + Projection
  -> Projection-shaped Sections
  -> role-bearing Occurrences
  -> Projection-shaped reusable Entities
  -> source-mediated reconstruction
```

This is strong enough for Part 3 initial specification draft.

Further domain experiments are not required before moving on.

## 10. Remaining Theoretical Risk

The main remaining theoretical risk is Entity payload inflation.

Entity content may become too explanatory and begin to act like a summary or stored meaning.

Part 3 already warns against this.

Part 5 should help by defining Projection as the object that determines acceptable Entity granularity, payload type, and role vocabulary.

Part 4 should not define Entity payload rules before Part 5 clarifies Projection responsibilities.

## 11. Why Part 5 Should Precede Part 4

The original plan to draft Part 5 before Part 4 is still correct.

Part 4 will define concrete YAML syntax.

But Part 4 cannot safely decide the YAML details until Part 5 clarifies what a Projection is and how it is represented or referenced.

Important unresolved Part 4 questions depend on Part 5:

- How should `meta.projections` be represented?
- What is the minimum Projection reference?
- Can a Projection be inline?
- Can multiple Projections shape one document?
- How are Projection roles recorded?
- How should Projection compatibility be hinted, if at all?
- Are role vocabularies Projection-defined?
- Are Entity kinds Projection-defined?
- How should Projection coverage or non-goals be recorded?
- How should generation Projection and reconstruction Projection differ?

These are not YAML questions first.

They are Projection model questions first.

Therefore, Part 5 should be drafted before Part 4.

## 12. Recommended Revised Drafting Order

The revised drafting order should be:

```text
Part 1 — Philosophy / Meaning stance
Part 2 — Human-AI Intellectual Activity architecture
Part 3 — Core Model
Part 5 — Projection Model and Projection Library Concept
Part 4 — YAML Representation and Validation
```

This order is not numerically sequential, but it is theoretically safer.

Part 5 defines what Part 4 must be able to represent.

Part 4 then serializes the Core Model and Projection references with fewer premature assumptions.

## 13. Part 5 Questions to Resolve Before Part 4

Part 5 should answer at least the following questions before Part 4 is made normative.

### 13.1 Projection Identity

- What is a Projection?
- Is it a document, strategy, profile, reusable context, or all of these depending on layer?
- What minimal identity does a Projection need?
- Are Projection IDs local, library-scoped, URI-like, or implementation-defined?

### 13.2 Projection Content

- What fields define a Projection?
- Does it include purpose, audience, focus, non-goals, assumptions, role vocabulary, Entity kind guidance, source-selection rules, and reconstruction goals?
- Which of these are required versus optional?

### 13.3 Projection Roles

- How does a generation Projection differ from a reconstruction Projection?
- How are compatibility hints represented?
- Can one document have multiple generation Projections?

### 13.4 Projection Compatibility

- Does Part 5 define compatibility conceptually only?
- Should compatibility be exact, partial, functional, or transformation-based?
- Should Part 5 avoid formal scoring and leave it to implementations?

### 13.5 Projection Libraries

- What is a Projection Library?
- Is it a governance system, catalog, pattern library, or reuse infrastructure?
- How are Projection versions handled?
- How are deprecated or superseded Projections handled?

### 13.6 Projection and Core Object Shaping

- How does a Projection shape Section granularity?
- How does a Projection define Occurrence role vocabulary?
- How does a Projection guide Entity kinds and payload boundaries?
- How does a Projection define coverage and non-goals?

## 14. Part 3 Adjustments Before Part 5

Part 3 is ready enough to support Part 5 drafting.

Before or during Part 5, only light Part 3 adjustments may be needed:

- reduce repeated warnings about final meaning;
- align use of `Projection Context` versus `Projection`;
- keep all YAML-like examples explicitly non-normative;
- ensure Part 3 does not accidentally define Projection internals that belong to Part 5.

These are editorial adjustments, not conceptual blockers.

## 15. Conclusion

Part 1, Part 2, and Part 3 now form a coherent theoretical chain.

Part 3 successfully avoids becoming a meaning store, ontology, or source replacement.

The next theoretical dependency is Projection.

Therefore, the project should proceed to Part 5 before Part 4.

Part 5 should define Projection well enough that Part 4 can later serialize IdeaMark documents and Projection references without prematurely freezing the wrong structure.
