# 7. Situation-driven Reconstruction Layer

**Part:** 2 — Architecture of Human-AI Co-evolution  
**Status:** Draft Rev003  
**Type:** Informative / Reference Architecture

The Situation-driven Reconstruction Layer uses Situation Vectors, Projections, IdeaMark documents, and Original Sources to support current intellectual activity.

Reconstruction is not merely answering a question.

It is the process of making prior intellectual activity usable under a current Situation.

## 7.1 Purpose

The purpose of the Situation-driven Reconstruction Layer is to help humans and AI systems return to relevant Original Sources and reconstruct meaning, judgment, explanation, or action under a current Situation and Projection.

```text
Situation Vector
        ↓
Projection Selection or Generation
        ↓
IdeaMark Retrieval or Generation
        ↓
Original Source Access
        ↓
Human-AI Intellectual Activity
        ↓
Judgment / Decision / Action / Explanation / Trace
        ↓
Situation(t + 1)
```

The output of reconstruction may be a recommendation, explanation, warning, plan, question, comparison, learning material, operational guidance, or another form of intellectual support.

Part 2 does not prescribe the output form.

## 7.2 Reconstruction Is Situation-Dependent

The same Original Source may support different reconstructions under different Situation Vectors.

A technical report may be reconstructed as beginner education in a calm situation, emergency guidance in a hazardous situation, policy evidence in an administrative situation, or design precedent in an engineering situation.

The Original Source is treated as the material basis for the selected Projection-guided reconstruction.

The reconstruction changes because the Situation and Projection change.

## 7.3 Reconstruction Is Projection-Dependent

Projection determines how the system approaches the Original Source and IdeaMark document.

It may influence:

- which Original Source sections are relevant;
- which IdeaMark structures should be prioritized;
- what level of detail is appropriate;
- what form of explanation is useful;
- what risks or constraints should dominate;
- what prior knowledge can be assumed;
- what action horizon matters;
- whether education, decision, operation, safety, exploration, or review is the primary activity.

Projection therefore shapes reconstruction without becoming a universal truth model.

## 7.4 IdeaMark Retrieval or Generation

The Reconstruction Layer may use an existing IdeaMark document, generate a new one, regenerate an insufficient one, or combine several documents.

```text
Situation Vector + Projection
        ↓
Find existing IdeaMark document
        or
Generate / Regenerate IdeaMark document
        ↓
Access Original Source
```

This step should be understood architecturally.

Part 2 does not define a required retrieval interface, ranking algorithm, database query, vector search method, or generation pipeline.

## 7.5 Return to Original Sources

Reconstruction should return to Original Sources whenever possible.

An IdeaMark document guides reconstruction but does not replace the source.

The Original Source provides the material basis from which meaning may be reconstructed under a current Situation and Projection.

In some situations, the system may present a compressed or transformed expression to the user.

Even then, source traceability remains important because the user, reviewer, AI system, or later process may need to inspect the original basis.

## 7.6 Human-AI Intellectual Activity

Reconstruction leads into Human-AI Intellectual Activity.

Human and AI participation may be interleaved.

For example:

- AI may interpret a Situation Vector and propose a Projection;
- a human may select, reject, question, or modify the Projection;
- AI may retrieve IdeaMark documents;
- AI may read or summarize relevant Original Sources;
- a human may provide judgment, preference, domain knowledge, or lived context;
- AI may generate action-oriented guidance;
- a human, AI system, organization, or workflow may perform further intellectual activity;
- a human or organization may make decisions where decision authority is assigned to them;
- the result may become a new source or new observation.

Part 2 does not assume that either humans or AI are infallible.

Both may participate as interpreters and contributors within the reconstruction process.

AI participation in this context is architectural participation in intellectual activity.

It does not imply legal personhood, moral status, or human-equivalent rights.

## 7.7 Judgment and Action

Reconstruction may support judgment and action, but IdeaMark Core does not decide the final normative outcome.

A Projection may prioritize safety, legality, learning, operational continuity, economic value, scientific rigor, individual preference, public responsibility, or another domain-specific priority.

Core does not define which priority must dominate in all situations.

It defines how such priorities can be made explicit through Projection and connected to Original Sources through IdeaMark.

## 7.8 Reconstruction Changes Situation

Reconstruction changes future Situation.

A warning may cause evacuation.

An explanation may improve understanding.

A design review may change a specification.

A business analysis may change investment priorities.

A system incident reconstruction may change operational procedures.

These changes create new observations and new source material.

Thus reconstruction participates in the Situation trajectory rather than terminating as a one-time answer.

## 7.9 Examples

### 7.9.1 Volcanic Tourism

A tourist under normal conditions may receive educational reconstruction that helps them enjoy the mountain while understanding risk.

The same tourist during visible eruption or strong shaking may receive safety-oriented reconstruction that compresses relevant knowledge into immediate action guidance.

The difference is not the Original Source alone.

It is the Situation Vector and Projection.

### 7.9.2 Business Strategy and Field Operations

A strategy document may be reconstructed differently for executives, managers, and field staff.

Executives may need strategic implications.

Managers may need coordination priorities.

Field staff may need operational actions and constraints.

The same source can support multiple legitimate reconstructions.

### 7.9.3 System Design and Incident Response

A design pattern or architecture decision record may be reconstructed differently in early design, implementation review, compliance review, and active production incident response.

During an incident, the Projection may prioritize risk containment and reliability over conceptual exploration.

## 7.10 Non-goals

The Situation-driven Reconstruction Layer does not define:

- a chat interface;
- a retrieval algorithm;
- a ranking system;
- a prompt template;
- a decision authority model;
- a universal ethical rule;
- a required output format;
- a required level of automation;
- a required AI model.

These belong to implementations, Projections, domain practices, organizations, or future specifications.

## 7.11 Design Rationale

Reconstruction is the reason IdeaMark documents exist.

If IdeaMark documents were only stored and never used to return to Original Sources under new Situations, they would become static documentation.

If reconstruction ignored Original Sources, IdeaMark would become an unsupported summary system.

If reconstruction ignored Projection, it would fail to adapt to different intellectual activities.

If reconstruction ignored Situation, it would become generic explanation rather than useful support.

If reconstruction excluded AI from intellectual activity, it would fail to describe the collaborative architecture that makes IdeaMark practical in AI-enabled environments.

The Situation-driven Reconstruction Layer binds these elements together.

It reduces interpretation cost by helping participants avoid starting from zero while still returning to source material and Projection context.

## 7.12 Summary

The Situation-driven Reconstruction Layer transforms Situation-specific need into traceable intellectual activity.

It uses Projection to guide access through IdeaMark documents back to Original Sources treated as the material basis for reconstruction.

It supports Human-AI Intellectual Activity, judgment, explanation, and action.

It also changes the next Situation, making reconstruction part of a continuing intellectual activity cycle.
