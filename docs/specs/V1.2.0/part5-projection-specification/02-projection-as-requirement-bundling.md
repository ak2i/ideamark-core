# 2. Projection as Requirement Bundling

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## Purpose

This chapter defines Projection as a finite bundle of requirements.

Human-AI Intellectual Activity often depends on many layers of context: law, domain practice, organizational routines, role expectations, user capability, risk, urgency, available media, and future use.

The whole Situation cannot be copied into every IdeaMark document or every authoring prompt.

Projection bundles the relevant requirements into a reusable strategy that can guide finite operations.

## Requirement Layers

A Projection MAY contain requirements from many layers, including:

- legal or regulatory requirements;
- social customs and ethical expectations;
- domain standards;
- organizational policies;
- project goals;
- task constraints;
- role responsibilities;
- user capability and literacy assumptions;
- medium and format constraints;
- time, cost, and risk constraints;
- source reliability assumptions;
- expected reconstruction tasks.

These layers do not have to be represented with a universal taxonomy.

A Projection Library or domain profile MAY define its own requirement categories.

## Requirement Selection

A Projection MUST be selective.

It should not attempt to include every observable fact about the Situation.

The purpose of requirement bundling is to identify which constraints and assumptions are necessary for useful Decomposition, retrieval, matching, filtering, and reconstruction.

A requirement should be included when omitting it would likely cause one of the following failures:

- wrong source material is selected;
- useful source material is ignored;
- material is split at the wrong boundary;
- future retrieval cannot find the document;
- incompatible documents are treated as compatible;
- reconstruction produces an unsuitable expression;
- a human or AI system misunderstands the intended reuse context;
- a safety, governance, or responsibility constraint is lost.

## Requirement Kinds

A Projection MAY distinguish requirement kinds such as:

- **hard requirement** — violation makes the output unsuitable;
- **soft preference** — guides quality but may be traded off;
- **negative requirement** — identifies what must be excluded;
- **coverage requirement** — identifies what must be represented;
- **traceability requirement** — identifies how return to source should be supported;
- **capability requirement** — identifies interpreter or tool assumptions;
- **evaluation requirement** — identifies how the resulting structures should be judged.

This distinction helps matching and reconstruction.

A candidate may partially match soft preferences while failing a hard requirement.

## Requirement Conflicts

Requirement bundles MAY contain internal tension.

For example, a Projection may need both concise reconstruction and strong traceability.

It may need to simplify professional knowledge for a novice while avoiding misleading oversimplification.

A Projection SHOULD make important tensions visible when they materially affect Decomposition or reconstruction.

Conflict resolution may be handled by authoring workflow, human review, library policy, or implementation-specific ranking.

Part 5 does not prescribe a universal conflict-resolution algorithm.

## Requirement Provenance

A Projection SHOULD preserve enough provenance to understand where important requirements came from.

Provenance may identify:

- a law, rule, or policy;
- a domain practice;
- an organizational template;
- a user preference;
- an expert decision;
- an AI-generated draft;
- an experimental result;
- a previous Projection version.

Projection provenance is not the same as Original Source provenance.

Original Source provenance helps return to the material being decomposed.

Projection provenance helps explain why the decomposition and reconstruction strategy was shaped in a particular way.

## Requirement Privacy

Some requirements may be private or sensitive.

A Projection MAY be referenced without fully disclosing all requirement details.

For example, an organization may publish a stable Projection identifier while keeping internal risk scoring, legal interpretation, or user capability assumptions private.

Part 5 allows private, shared, and public Projections because reuse should not require universal disclosure.
