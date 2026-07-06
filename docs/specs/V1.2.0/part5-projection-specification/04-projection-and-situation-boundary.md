# 4. Projection and Situation Boundary

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## Purpose

This chapter defines the boundary between Situation and Projection.

A Situation may include unbounded context: people, goals, histories, institutions, tools, media, constraints, moods, risks, permissions, costs, and future consequences.

Projection is a finite strategy derived from or selected for a Situation.

Projection exists because finite Decomposition, retrieval, matching, filtering, and reconstruction cannot operate over the whole Situation space directly.

## Situation Is Not Projection

A Projection MUST NOT be treated as the complete Situation.

A Situation may contain many facts that are irrelevant to the current reuse strategy.

A Projection selects and organizes only those assumptions and requirements that are expected to matter for the intended operations.

The same Situation may support multiple Projections.

The same Projection may be reused across multiple Situations.

## Situation Vector

Part 2 uses the term Situation Vector to describe a structured observation or interpretation of the current Situation.

A Situation Vector may help select, generate, or adapt a Projection.

However, a Projection should remain separable from the Situation Vector when practical.

This separation allows a Projection to be:

- reused;
- compared;
- versioned;
- tested;
- governed;
- shared;
- kept private;
- improved through feedback.

## Boundary Selection

A Projection SHOULD define its Situation boundary.

The boundary may state:

- what contextual assumptions are included;
- what contextual assumptions are intentionally excluded;
- what external information must be supplied at use time;
- what assumptions are defaults rather than facts;
- what information is private or unavailable;
- what uncertainty remains unresolved.

Boundary definition is especially important when a Projection moves across users, organizations, domains, or capability levels.

## Runtime Context

Some information should not be frozen into a Projection.

Examples include:

- current date or deadline;
- current user identity;
- current permissions;
- live inventory;
- active legal status;
- current organizational assignment;
- real-time risk level;
- current device or medium constraints.

A Projection MAY specify that such values must be supplied at runtime.

This allows the Projection to remain reusable while still supporting Situation-sensitive reconstruction.

## Privacy Boundary

Projection boundaries may also be privacy boundaries.

A public Projection may expose a general reuse strategy while hiding sensitive organizational rules or personal capability assumptions.

A private Projection may be used locally without being published.

A Projection reference MAY identify a private Projection without making its full contents available to all consumers.

In that case, compatibility and reconstruction may depend on trusted tools, authorized users, or local governance.

## Boundary Drift

A Projection may become unreliable when the Situation class it assumes changes.

This is boundary drift.

Examples include:

- a legal rule changes;
- an organizational procedure changes;
- a user capability assumption becomes false;
- a domain practice becomes obsolete;
- a reconstruction medium changes;
- risk tolerance changes;
- the expected audience changes.

A Projection SHOULD support lifecycle metadata or review practices that help detect boundary drift.

## Boundary and Interpretation Cost

A good boundary reduces interpretation cost.

An overly broad Projection burdens users and tools with irrelevant requirements.

An overly narrow Projection fails when reused outside its local context.

Part 5 therefore treats boundary design as one of the central quality dimensions of Projection authoring.
