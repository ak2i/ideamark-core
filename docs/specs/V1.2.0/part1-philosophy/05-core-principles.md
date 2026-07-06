# 5. Core Principles

**Part:** 1 — Philosophy  
**Status:** Draft Rev006  
**Type:** Informative / Guiding Principles

This section defines the core principles that guide the design of IdeaMark Core v1.2.0.

These principles are not YAML syntax rules. They are architectural and philosophical commitments that later parts of the specification should preserve.

Part 2 and later specifications should be able to refer back to these principles when explaining design decisions.

## 5.1 Reuse over Representation

### Principle

IdeaMark is designed to maximize reusability rather than representational completeness.

### Rationale

A complete representation of knowledge or meaning is not the primary objective.

The objective is to make intellectual activities reusable across different Situations, Projections, interpreters, and levels of expertise.

A representation may be incomplete and still useful if it helps future humans and AI reconstruct intellectual activity from Original Sources.

### Consequences

- IdeaMark should not attempt to become a universal knowledge representation language.
- Validation should focus on structural usefulness, traceability, and consistency rather than semantic completeness.
- Multiple valid IdeaMark documents may exist for the same Original Source.

## 5.2 Separate Structure from Meaning

### Principle

IdeaMark separates reusable structure from meaning.

### Rationale

Meaning depends on Original Sources, interpreters, Situations, purposes, Projections, and future contexts.

If meaning is fixed inside IdeaMark, future reuse becomes constrained by a prior interpretation.

Separating structure from meaning allows reusable structures to remain available while interpretation evolves.

### Consequences

- IdeaMark preserves reusable structures rather than final meanings.
- Meaning is reconstructed from Original Sources under future Projections and Situations.
- Different Projections may legitimately produce different entities, occurrences, and sections from the same source.

## 5.3 Original Source as Authority for Projection-guided Reconstruction

### Principle

Original Sources are treated as the authority for Projection-guided generation and reconstruction activities.

### Rationale

IdeaMark does not replace Original Sources.

A summary, interpretation, or generated explanation may be useful, but it is not the final authority for future reuse.

Calling an Original Source authority in this context does not mean the source is universally true, complete, unbiased, lawful, ethical, or final.

It means the source is the material basis to which an IdeaMark document and later reconstruction should remain traceable under a Projection.

Original Sources preserve future potential because they allow new Projections and interpreters to reconstruct meaning under new conditions.

### Consequences

- IdeaMark should guide interpreters back to Original Sources whenever possible.
- Generated interpretations should not be treated as substitutes for Original Sources.
- Source traceability is a core design requirement.
- The Core should not define a universal theory of source authority.

## 5.4 Projection Defines Reuse Strategy

### Principle

Projection defines reuse strategy rather than truth.

### Rationale

The same Original Source can support many intellectual activities.

A field operator, policy designer, researcher, educator, investor, engineer, or citizen may require different entry points, different entity boundaries, and different retrieval priorities.

Projection specifies how an Original Source is made reusable for a future class of intellectual activities.

Projection may reduce interpretation cost by providing a reusable direction, emphasis, and structure for reconstruction.

### Consequences

- Multiple Projections over the same Original Source are expected, not exceptional.
- Projection may change entity boundaries, occurrence structures, and section organization.
- Projection should be treated as a reusable intellectual asset, not merely a prompt parameter.
- The Core should not prescribe how Projections must be created, selected, governed, shared, or evaluated.

## 5.5 Preserve Reusable Intellectual Structures Instead of Fixed Interpretations

### Principle

IdeaMark preserves reusable intellectual structures rather than fixed interpretations.

### Rationale

Experts often understand complex material by recognizing reusable structures, patterns, names, roles, and relationships.

These structures allow detailed understanding to be compressed, transferred, expanded, and adapted.

IdeaMark should preserve these reusable structures without claiming that any one expansion is final.

### Consequences

- Entities should not be treated as fixed meanings.
- Occurrences should represent reusable intellectual episodes or activations, not merely textual appearances.
- Sections should organize intellectual activity rather than merely reproduce document headings.

## 5.6 Engineer Through Separation

### Principle

IdeaMark uses separation as an engineering strategy.

### Rationale

Engineering often becomes possible when tightly coupled phenomena are decomposed into independently manageable representations.

Shannon's information theory is an important analogy: communication could be engineered by separating signal transmission from semantic meaning.

IdeaMark adopts a related strategy for intellectual activity by separating reusable structure from meaning.

### Consequences

- Meaning remains outside the Core as something reconstructed from Original Sources.
- The Core can specify structural requirements without defining universal meanings.
- Projection can vary without invalidating the source or the Core model.

## 5.7 Engineer Through Reconstruction

### Principle

IdeaMark supports reconstruction rather than prescribing final answers.

### Rationale

Reuse is not simple copying.

Future humans and AI must reconstruct relevance, meaning, judgment, explanation, and action under new Situations.

IdeaMark should provide structures that support this reconstruction cycle.

### Consequences

- Retrieval should help users find where thinking can begin, not merely retrieve answers.
- AI-generated outputs should remain connected to Original Sources and reusable structures.
- Part 2 should describe the reconstruction flow among Original Source, Projection, IdeaMark, retrieval, Human-AI Intellectual Activity, action, traces, and new Original Sources.

## 5.8 Future Interpretability over Present Interpretation

### Principle

IdeaMark should maximize future interpretability rather than preserve only present interpretations.

### Rationale

Present interpretations are valuable, but they are situated.

Future users, organizations, AI systems, and societies may have different goals, constraints, literacy levels, and technologies.

A useful IdeaMark document should increase the ability of future interpreters to return to Original Sources and reconstruct meaning.

### Consequences

- IdeaMark should avoid overfitting to one current audience or use case.
- Authoring should preserve enough traceability and structure to support future reinterpretation.
- Documents may be regenerated or versioned when Projections, contexts, or sources evolve.

## 5.9 Interpretation Cost Reduction

### Principle

IdeaMark should reduce the interpretation cost of intellectual work across its lifecycle.

### Rationale

A method may be correct, powerful, or sophisticated, but if it is too costly to understand, maintain, teach, review, or reuse, it may fail to become widely useful.

IdeaMark therefore values reusable access structures, Projections, traceability, and reconstruction paths that make intellectual work easier to create, understand, review, maintain, teach, and reuse.

### Consequences

- Projection should be evaluated partly by whether it reduces reconstruction and review cost for intended use.
- IdeaMark documents should be understandable as access structures, not opaque generated artifacts.
- Repository and generation choices may trade off cost across background generation, on-demand generation, review, persistence, and reuse.

## 5.10 Capability Expansion over Automation

### Principle

IdeaMark prioritizes capability expansion over automation.

### Rationale

Automation can improve efficiency, but it may also reduce human participation if treated as the primary goal.

IdeaMark is motivated by capability-oriented Human-AI collaboration: expanding what individuals, groups, organizations, AI systems, and societies can meaningfully participate in and accomplish.

Capability expansion is a long-horizon orientation, not a required metric for every use.

### Consequences

- AI-enabled systems should keep humans engaged as interpreters and contributors.
- Productivity should be treated as a result, not the sole objective.
- IdeaMark should support social and intellectual inclusion by reducing the cost of participation.
- The Core should not require a universal capability score.

## 5.11 Humans and AI are Interpreters and Participants

### Principle

Meaning may be reconstructed by humans, AI systems, or both together.

### Rationale

IdeaMark is designed for Human-AI co-evolution.

It should not assume that only humans interpret, nor should it reduce humans to passive consumers of AI-generated answers.

AI systems and humans should be treated as participants in a shared intellectual ecosystem, while avoiding premature claims about AI personhood or legal status.

### Consequences

- Retrieval and authoring systems should support both human-readable and AI-usable structures.
- AI should be able to use IdeaMark to guide interpretation, not merely consume documents.
- Human participation remains essential to sustainable intellectual ecosystems.

## 5.12 IdeaMark Documents are Operational Snapshots

### Principle

IdeaMark documents are operational snapshots.

### Rationale

Original Sources, Projections, organizations, AI systems, and retrieval needs evolve.

A single IdeaMark document should not be treated as an immutable final representation of a source.

### Consequences

- IdeaMark documents may be regenerated, replaced, versioned, or allowed to coexist.
- Regeneration may be preferable to manual synchronization when sources or Projections change significantly.
- Implementations should preserve traceability across versions where possible.

## 5.13 Do Not Define the Limits of Intellectual Activity

### Principle

IdeaMark intentionally avoids defining the limits of intellectual activity.

### Rationale

Future intellectual activities may be performed by humans, AI systems, organizations, instruments, or combinations not yet anticipated.

Defining the boundary too narrowly would constrain future reuse.

### Consequences

- The Core should define reusable structural mechanisms rather than a closed taxonomy of intellectual activities.
- Domain vocabularies and coordinate systems should evolve outside the Core when appropriate.
- Future Projections and authoring practices may expand the range of supported intellectual activities.

## Design Rationale

These principles keep IdeaMark open to future Projections, AI systems, domains, media, and intellectual activities.

They also define the continuity between Part 1 and the later specifications:

- Part 2 should explain reconstruction, Human-AI Intellectual Activity, Situation evolution, interpretation cost, and capability-oriented co-evolution.
- Part 3 should define the conceptual model without collapsing structure into meaning.
- Part 4 should specify YAML and validation rules that preserve traceability and reusability.
- Part 5 should define Projection as reuse strategy.
- Part 6 should guide practical authoring and evaluation.
