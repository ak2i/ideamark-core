# 0. Projection Overview

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## Purpose

This chapter defines Projection at the Part 5 level.

Projection is a reusable specification of how Original Source material, existing IdeaMark documents, and future Situations should be approached for Decomposition, retrieval, matching, filtering, and reconstruction.

Projection is not the same as a prompt, user request, search query, template, schema, or workflow.

Those artifacts may express or carry parts of a Projection, but Projection is the reusable intellectual strategy that makes those artifacts coherent.

## Definition

A Projection is a finite, reusable transformation strategy that selects, constrains, and evaluates how material may become useful for a future Human-AI Intellectual Activity.

A Projection may guide at least five activities:

1. **Decomposition** — deciding which structures should be produced from Original Source material.
2. **Retrieval** — deciding what kinds of IdeaMark documents or Original Sources should be found.
3. **Matching** — deciding whether a candidate document, source, or Projection is compatible enough to use.
4. **Filtering** — excluding candidates that would create unsuitable, unsafe, misleading, or wasteful reconstruction.
5. **Reconstruction** — deciding how retrieved structures and Original Source material should be transformed into an activation expression.

## Projection and Core

Projection is external to the Core Model.

The Core Model defines reusable access structures such as Section, Occurrence, Entity, source references, anchors, status, and metadata.

Projection defines why those structures are worth producing, which boundaries matter, what future reuse is expected, and how compatibility should be judged.

This separation is intentional.

Core structures should remain small enough to preserve traceable access without becoming a domain ontology or workflow engine.

Projection may carry domain-specific, organizational, role-specific, legal, practical, or experimental assumptions that should not be forced into the Core.

## Projection and Meaning

Projection does not store final meaning.

It provides an approach for selecting, decomposing, retrieving, and reconstructing material so that meaning may later become activated in a Situation.

A Projection can strongly shape what becomes visible, relevant, reusable, or ignorable.

However, the final meaning of a reconstructed expression still depends on the interpreter, Situation, activity, medium, and consequences of use.

## Projection and Original Source

Projection must preserve the priority of Original Source material.

A Projection may guide how a source is decomposed or reconstructed, but it should not replace the source with an untraceable interpretation.

When a Projection causes a source fragment to be selected, summarized, grouped, ignored, or transformed, the resulting access structure should still make it possible to return to the Original Source when practical.

## Projection and Reuse

A Projection is reusable when it can be applied, adapted, compared, or referenced across more than one authoring or reconstruction event.

Reuse may be exact, partial, approximate, or analogical.

A cooking Projection designed for professional kitchens may not match a household cooking Situation exactly.

Even so, it may still be useful if it exposes functional structures such as heat control, umami generation, substitution constraints, or texture management.

Part 5 therefore treats Projection compatibility as more important than Projection identity.

## Normative Intent

Part 5 uses the following terminology levels:

- **MUST** indicates a requirement for a conforming Projection specification or Projection-capable profile.
- **SHOULD** indicates a strong recommendation that may be relaxed when the reason is explicit.
- **MAY** indicates an allowed option.

Part 5 is not yet a concrete serialization schema.

Concrete YAML fields, JSON schemas, CLI validation behavior, and document-profile rules belong to Part 4, Doc CLI profiles, or companion specifications.
