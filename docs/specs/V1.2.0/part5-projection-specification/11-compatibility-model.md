# 11. Projection Compatibility Model

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## Purpose

This chapter defines a conceptual compatibility model for Projection-based reuse.

Compatibility is the judgment that a Projection, IdeaMark document, Original Source, or generated structure is suitable enough for a use-side Projection.

Compatibility is not equality.

IdeaMark reuse becomes powerful when different Projections can still cooperate through partial overlap, transformation, specialization, generalization, or analogy.

## Compatibility Subject

A compatibility judgment may apply to:

- Projection to Projection;
- Projection to IdeaMark document;
- Projection to Original Source;
- Projection to Section;
- Projection to Occurrence;
- Projection to Entity;
- Projection to reconstruction target;
- generated document to use-side Situation;
- one Projection version to another Projection version.

A Profile or implementation SHOULD state what kind of compatibility is being judged.

## Compatibility Classes

A Projection Profile MAY define compatibility classes.

Recommended conceptual classes are:

### Exact

The candidate was generated or designed under the same Projection, or under a version explicitly declared compatible.

Exact compatibility is useful, but it should not be the only reuse path.

### Compatible

The candidate satisfies the hard requirements of the use-side Projection and can be used without major transformation.

Some assumptions may differ, but they do not block the intended reconstruction.

### Partial

The candidate contains useful reusable material but does not fully satisfy the use-side Projection.

Partial compatibility may require:

- source review;
- additional Decomposition;
- warning;
- adaptation;
- human approval;
- combination with other candidates.

### Analogical

The candidate comes from another domain or Situation class but preserves a functional structure useful for the current Projection.

Analogical compatibility is important for cross-domain reuse.

It usually requires explicit transformation and stronger review.

### Transformable

The candidate is not directly compatible, but a known transformation may make it usable.

Transformations may include specialization, generalization, terminology mapping, capability adjustment, medium conversion, or risk-level adjustment.

### Incompatible

The candidate fails a blocking requirement or would likely mislead reconstruction.

Incompatible candidates should be excluded or clearly marked.

### Unknown

The available metadata or source access is insufficient to decide.

Unknown should not be silently treated as compatible.

## Hard Requirements and Soft Preferences

Compatibility SHOULD distinguish hard requirements from soft preferences.

A hard requirement blocks reuse when violated.

A soft preference affects ranking, quality, or review priority but does not necessarily block reuse.

Examples of hard requirements may include:

- required source authority;
- required privacy level;
- required traceability;
- prohibited audience;
- prohibited domain transfer;
- required review status;
- incompatible legal or organizational constraint.

Examples of soft preferences may include:

- preferred granularity;
- preferred output style;
- preferred Section strategy;
- preferred vocabulary;
- preferred examples;
- preferred language.

## Compatibility Explanation

Compatibility judgments SHOULD be explainable when they affect reconstruction.

An explanation may include:

- class assigned;
- matched requirements;
- failed requirements;
- unknown requirements;
- needed transformation;
- remaining risk;
- recommended review action;
- source anchors to inspect.

Explanation is important because compatibility is often a Projection-side judgment, not a simple schema validation result.

## Compatibility and Source Traceability

Traceability is a major compatibility condition.

A document may appear relevant but be unsuitable if it cannot return to the needed Original Source material.

A use-side Projection SHOULD be able to require stronger traceability for high-risk reconstruction.

Conversely, exploratory or low-risk reconstruction may tolerate approximate anchors or weaker source return.

## Compatibility and Capability

A Projection may encode assumptions about the interpreter's capability.

A candidate generated for experts may be partially compatible with a novice-facing Projection if reconstruction can add prerequisites, warnings, or simplified explanations.

A novice-facing candidate may be incompatible with an expert-facing Projection when it omits technical constraints needed for expert action.

Capability mismatch should be treated as a compatibility issue, not merely a tone issue.

## Compatibility and Versioning

Projection versions SHOULD declare compatibility expectations when practical.

Possible version relationships include:

- backward compatible;
- forward compatible;
- compatible with migration;
- compatible only for retrieval;
- compatible only for reconstruction after review;
- incompatible;
- unknown.

A Projection Library MAY maintain compatibility tables or transformation notes.

## Compatibility Non-goal

Part 5 does not define a universal scoring algorithm.

An implementation may use rules, metadata, indexes, human review, embeddings, graphs, or hybrid methods.

Part 5 defines the conceptual responsibility: compatibility should be judged, represented, and explained sufficiently for safe and useful reuse.
