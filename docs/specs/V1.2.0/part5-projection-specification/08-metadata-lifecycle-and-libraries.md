# 8. Projection Metadata, Lifecycle, and Libraries

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## Purpose

This chapter defines Projection metadata, lifecycle responsibilities, and Projection Library responsibilities.

Projection is a reusable intellectual asset.

Therefore, a Projection should be identifiable, comparable, versionable, reviewable, and reusable when practical.

## Projection Metadata

A Projection SHOULD have metadata sufficient for reuse and review.

Metadata may include:

- identifier;
- name;
- version;
- status;
- description;
- intended reuse activity;
- intended audience;
- source domain;
- target domain;
- author or maintainer;
- creation date;
- update date;
- provenance;
- license or sharing policy;
- privacy level;
- compatibility notes;
- deprecation notes;
- related Projections.

Not every Projection requires all fields.

Exploratory or private Projections may begin with light metadata.

Shared, institutional, or public Projections SHOULD provide stronger metadata because other users and tools cannot rely on unstated local context.

## Projection Status

A Projection MAY define lifecycle status values.

Common statuses include:

- **experimental** — being explored or tested;
- **draft** — intentionally authored but not yet stable;
- **active** — recommended for use;
- **restricted** — usable only under defined conditions;
- **deprecated** — retained for compatibility but no longer recommended;
- **retired** — no longer intended for use;
- **superseded** — replaced by a newer Projection.

Status should help users and tools decide whether a Projection is suitable for generation, retrieval, matching, filtering, or reconstruction.

## Versioning

A Projection SHOULD be versioned when it is reused beyond a single local session.

Versioning is important because Projection changes may alter:

- source coverage;
- reusable unit boundaries;
- Section strategy;
- role strategy;
- traceability requirements;
- matching behavior;
- reconstruction behavior;
- risk and exclusion rules;
- compatibility with documents generated under older versions.

A Projection version change SHOULD indicate whether previous outputs remain compatible.

A Projection Library MAY define migration notes or compatibility ranges.

## Lifecycle Feedback

Projection lifecycle should be informed by use.

Feedback may come from:

- authoring review;
- validation or lint diagnostics;
- retrieval success or failure;
- matching explanations;
- reconstruction failures;
- human review;
- user outcomes;
- organizational policy changes;
- domain changes;
- legal or regulatory changes;
- repeated mismatch patterns.

A mature Projection should improve as repeated intellectual activity reveals which strategies reduce interpretation cost.

## Projection Library

A Projection Library is a collection of reusable Projections.

It is not merely a template catalog.

A Projection Library preserves reusable strategies for Decomposition, retrieval, matching, filtering, reconstruction, and evaluation.

A Library may support:

- discovery;
- selection;
- versioning;
- compatibility checking;
- governance;
- reuse examples;
- authoring guidance;
- deprecation management;
- feedback capture;
- private and shared distribution.

## Library Discovery

A Projection Library SHOULD help users or tools discover appropriate Projections.

Discovery may use:

- intended activity;
- domain;
- audience;
- source type;
- target output;
- capability level;
- risk level;
- organizational context;
- known compatible Projections;
- examples of successful use.

Discovery should not be reduced to keyword search when structural or functional compatibility matters.

## Private, Shared, and Public Libraries

Projection Libraries MAY be private, organizational, domain-specific, public, experimental, or standardized.

A private Library may capture personal workflows, sensitive organizational routines, or strategic reasoning.

An organizational Library may help many participants reduce interpretation cost without exposing all internal requirements publicly.

A public Library may support social reuse, interoperability, education, or open tooling.

Part 5 does not require that all Projections be public.

## Projection Templates

A Projection Template is a reusable pattern for creating Projections.

A template may provide:

- required metadata fields;
- common requirement categories;
- suggested decomposition strategies;
- matching criteria;
- reconstruction target patterns;
- evaluation checklist;
- examples.

A template is not itself always a Projection.

It becomes a Projection when enough concrete intent, boundary, requirements, and reuse strategy are supplied for a specific class of use.

## Governance Boundary

Part 5 defines why lifecycle and library responsibilities matter.

It does not prescribe a universal governance process.

Governance may be handled by individuals, organizations, open communities, regulated bodies, or tool vendors.

Different governance styles may be appropriate for experimental personal use, organizational operations, domain standards, and public infrastructure.
