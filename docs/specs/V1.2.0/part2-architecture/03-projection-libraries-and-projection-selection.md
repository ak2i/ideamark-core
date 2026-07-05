# 3. Projection Libraries and Projection Selection

**Part:** 2 — Architecture of Human-AI Co-evolution  
**Status:** Draft Rev003  
**Type:** Informative / Reference Architecture

Projection defines a reuse strategy.

It specifies how an original source should be made accessible for a future class of intellectual activities.

Part 2 treats Projection as a reusable intellectual asset that may participate in both IdeaMark generation and later reconstruction.

## 3.1 Purpose

Projection selection determines how a current situation, task, or future reuse objective should approach original sources through IdeaMark.

A Projection may guide:

- what should become reusable structure;
- which source materials matter;
- how entity boundaries should be chosen;
- how occurrences should be recognized;
- how sections should organize intellectual activity;
- what retrieval should support;
- what can be ignored;
- what kind of future interpreter is expected;
- what urgency, risk, capability, or responsibility should shape reconstruction.

Projection therefore shapes both construction and reconstruction.

## 3.2 Projection as Reuse Strategy

Projection is not a truth model.

It does not declare the final meaning of an original source.

It defines a strategy for making an original source reusable under a particular class of future situations.

For example, the same technical report may be projected as:

- a field operation guide;
- a policy design source;
- a safety review source;
- a research synthesis source;
- an engineering design source;
- an educational source;
- a risk communication source.

Each Projection may produce different IdeaMark structures from the same original source.

This is expected.

The difference reflects distinct reuse strategies, not necessarily disagreement about the source.

## 3.3 Projection as Catalytic Interpretation Vector

Projection may be understood as a catalytic interpretation vector.

It does not contain meaning by itself.

It does not force a single interpretation.

It lowers the cost of reaching useful interpretations by providing a reusable direction, emphasis, and structure for reconstruction.

```text
Original Source
        x
Situation Vector
        x
Projection
        ↓
Lower-cost reconstruction of useful interpretation
```

In this role, Projection is similar to a design pattern, professional guideline, educational frame, operational checklist, research protocol, or organizational standard.

Such patterns are valuable not only because they help create something, but also because they help later participants understand, analyze, maintain, review, and improve what was created.

IdeaMark Core does not rename Projection as interpretation cost engineering.

However, interpretation cost reduction is an important design rationale for why Projection exists.

## 3.4 Projection Libraries

A Projection library is a collection of reusable Projections.

It may be maintained by an individual, team, organization, research community, standards body, consultant, open-source project, or AI-assisted authoring workflow.

A Projection library may contain:

- general-purpose Projections;
- domain-specific Projections;
- role-specific Projections;
- organization-specific Projections;
- task-specific Projections;
- experimental Projections;
- private Projections;
- shared Projections;
- deprecated Projections preserved for compatibility;
- derived or specialized Projections.

IdeaMark Core does not prescribe how Projection libraries are stored, versioned, approved, searched, or governed.

The architectural requirement is that Projections can be reused and applied in a way that supports interoperable IdeaMark generation and reconstruction.

## 3.5 Projection Libraries as Cognitive Scaffolding

A Projection library is not only a technical reuse mechanism.

It is also cognitive scaffolding for humans and organizations.

A sufficiently capable AI system may generate a Situation-specific Projection without relying on a pre-existing library.

However, humans and organizations often need shared patterns before they can understand, trust, evaluate, adopt, and govern a new intellectual activity.

Projection libraries provide such patterns.

They may offer:

- familiar starting points;
- examples of useful reuse strategies;
- shared language for discussing reconstruction;
- organizational defaults;
- domain-specific expectations;
- professional norms;
- educational scaffolding;
- reviewable precedents;
- a basis for trust and accountability.

A Projection library therefore helps humans begin acting rationally within a complex possibility space.

It reduces cognitive load without eliminating adaptation.

## 3.6 Projection Libraries as Authority and Assurance

Projection libraries may also function as sources of assurance.

A Projection may be trusted because it is maintained by a professional community, standards body, regulator, organization, expert group, open-source community, or long-running practice.

This does not make the Projection universally correct.

It means the Projection carries recognizable authority, provenance, and expectations that humans can use when deciding whether and how to rely on it.

For example, a disaster response Projection maintained by domain experts may help users accept urgent safety-oriented reconstruction.

An organizational design-review Projection may help engineers understand what kind of issues the organization considers important.

A novice-friendly educational Projection may help new users understand how IdeaMark works before they attempt custom Projection generation.

In this sense, Projection libraries support adoption as well as computation.

They make IdeaMark understandable before it becomes fully customizable.

## 3.7 Projection Origins

A Projection may originate from many sources.

For example, a Projection may be:

- authored through careful academic or professional design;
- developed by a project team;
- maintained as an organizational standard;
- published as part of an open-source library;
- provided by consultants or domain experts;
- standardized by an industry group;
- generated by an AI system;
- refined through human-AI collaboration;
- gradually cultivated through repeated use cases;
- discovered through experimentation;
- created accidentally and retained because it works.

IdeaMark Core should not privilege one origin over another.

A carefully designed Projection, a gradually cultivated Projection, and an experimental Projection may all function if they satisfy the expressive and functional requirements needed for IdeaMark generation and reconstruction.

What matters architecturally is whether the Projection can guide useful access to original sources and support future reconstruction.

## 3.8 Private and Shared Projections

Projection may be private, shared, organizational, domain-specific, public, or standardized.

A Projection specialized for one individual's private situation may not be suitable for broad sharing.

A Projection that repeatedly reduces interpretation cost for many participants may become valuable as a shared organizational or social asset.

Sharing is useful when it helps a community coordinate interpretation, reduce reconstruction cost, improve reviewability, or increase long-term capability.

Core does not require that all Projections be shared.

Privacy, domain sensitivity, personal context, law, competitive value, and social risk may justify keeping some Projections private.

## 3.9 Projection Selection

Projection selection is the process of choosing one or more Projections for construction or reconstruction.

Selection may occur before IdeaMark generation, during retrieval, during interpretation, or after an initial reconstruction attempt.

A system may select Projection based on:

- Situation Vector;
- user role;
- task type;
- domain;
- source type;
- organizational policy;
- language;
- literacy level;
- risk level;
- urgency;
- desired output form;
- previous successful use;
- AI recommendation;
- explicit human choice;
- library authority or organizational default.

Part 2 does not define a required selection algorithm.

Projection selection may be manual, automatic, interactive, policy-driven, AI-assisted, library-based, or experimental.

## 3.10 Projection Generation

In some situations, a suitable Projection may not exist in a library.

A human or AI system may generate a new Projection for the current situation.

This may occur when:

- the Situation Vector is novel;
- urgency or risk requires a more specific Projection;
- the source domain is unfamiliar;
- the user role is unusual;
- existing Projections are too broad;
- existing Projections are too narrow;
- retrieval results reveal a mismatch;
- a temporary exploratory Projection is sufficient.

Generated Projections may remain temporary, be refined into reusable assets, or be discarded after use.

Part 2 does not require generated Projections to be stored permanently.

## 3.11 Library-Guided Projection Generation

Projection generation and Projection libraries are complementary.

An AI system may generate a Situation-specific Projection by adapting, composing, constraining, or specializing library Projections.

```text
Projection Library
        x
Situation Vector
        ↓
Situation-specific Projection
```

This pattern allows the generated Projection to remain responsive to the current situation while preserving continuity with trusted or familiar reuse strategies.

For example:

- a safety Projection may be specialized for foreign tourists;
- a design-review Projection may be adapted for an early-stage startup;
- a compliance Projection may be combined with an incident-response Projection;
- an educational Projection may be compressed into emergency guidance.

Library-guided generation helps avoid the extremes of unrestricted improvisation and rigid template use.

## 3.12 Multiple Projections

A reconstruction activity may use multiple Projections.

Multiple Projections may be useful when:

- several user roles must collaborate;
- a source must be compared across domains;
- risk and opportunity must both be evaluated;
- a policy, engineering, and operational view are all needed;
- an AI system needs alternative access paths;
- uncertainty about the best reuse strategy remains high;
- normative priorities remain contested or domain-dependent.

Multiple Projections may produce complementary IdeaMark documents or alternative interpretations from the same original source.

The architecture should allow such coexistence.

It should not force premature convergence into a single Projection.

## 3.13 Projection and Human-AI Co-evolution

Projection libraries may improve through use.

Humans and AI systems may discover that a Projection is useful, misleading, incomplete, too abstract, too narrow, difficult to apply, insufficiently trusted, or inappropriate for a Situation Vector.

Feedback from reconstruction may therefore lead to:

- Projection refinement;
- Projection specialization;
- Projection generalization;
- Projection retirement;
- Projection combination;
- creation of new Projection families;
- better authoring guidance;
- improved examples and evaluation methods;
- clearer authority and provenance;
- better human understanding of available intellectual activity patterns.

This feedback loop is part of human-AI co-evolution.

The Projection library becomes a shared intellectual asset that records how a community has learned to reuse original sources.

## 3.14 Relationship to IdeaMark Documents

Projection influences the IdeaMark document generated from an original source.

A change in Projection may justify regeneration of the IdeaMark document.

However, the previous IdeaMark document may still remain useful for another reconstruction purpose.

Therefore, implementations may preserve multiple IdeaMark documents for the same original source under different Projections.

This is not duplication in the ordinary sense.

It is the preservation of multiple access strategies.

## 3.15 Non-goals

Part 2 does not define:

- a Projection file format;
- a Projection governance process;
- a Projection approval workflow;
- a Projection creation method;
- a Projection selection algorithm;
- a Projection marketplace;
- a Projection registry protocol;
- a universal Projection taxonomy;
- a required Projection library storage mechanism;
- a universal normative priority among individual preference, expert judgment, organizational policy, public safety, law, or social value.

These may be specified in later parts, companion specifications, implementations, domain practices, institutions, or future societies.

## 3.16 Design Rationale

Projection is central because reuse is situated.

The same original source may support many legitimate future intellectual activities.

If IdeaMark Core defined only one way to extract reusable structure, it would collapse reuse into a single interpretation.

If IdeaMark Core assumed that all Projections should be generated freely from each Situation Vector, it would ignore the human need for shared patterns, trust, authority, and cognitive scaffolding.

Projection is introduced not because there exists a single correct interpretation, but because reusable interpretation strategies can substantially reduce the cost of creating, understanding, maintaining, reviewing, and reusing intellectual work.

This is similar to why design patterns, guidelines, protocols, and other shared forms remain useful even when powerful AI systems can generate working outputs.

A working artifact that cannot be interpreted, maintained, reviewed, or trusted may have lower long-term value than an artifact whose structure and reconstruction path are understandable.

By treating Projection as a reusable intellectual asset, IdeaMark allows different access structures to coexist while keeping original sources authoritative for their Projection-guided construction.

By treating Projection libraries as scaffolding and assurance, IdeaMark also supports human adoption, organizational learning, accountable human-AI collaboration, and lower interpretation cost over time.

## 3.17 Summary

Projection defines how original sources become reusable for future intellectual activities.

Projection libraries preserve reusable access strategies and provide cognitive scaffolding, shared language, assurance, and authority.

Projection selection connects current situations to appropriate reconstruction paths.

Projection generation allows new situations to be handled when existing strategies are insufficient.

Library-guided Projection generation allows AI systems to adapt trusted patterns to current Situation Vectors.

Projection may be carefully designed, gradually cultivated, experimentally discovered, accidentally successful, private, shared, or standardized.

Together, Projection libraries and Projection selection make IdeaMark adaptable without turning IdeaMark documents into final meanings or making Projection generation an unrestricted black box.
