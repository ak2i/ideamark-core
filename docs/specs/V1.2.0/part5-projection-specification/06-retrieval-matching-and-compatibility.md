# 6. Projection Retrieval, Matching, and Compatibility

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## Purpose

This chapter defines Projection responsibilities for retrieval, matching, filtering, and compatibility judgment.

IdeaMark reuse depends not only on generating documents, but also on finding and adapting them later.

Projection makes this use-side activity explicit.

The primary retrieval problem is not only finding semantically similar text. It is finding candidate structures that can help compose a future Human-AI Intellectual Activity.

Skeleton Graphs provide an optional structural interface for that problem.

## Retrieval Intent

A Projection SHOULD describe what future retrieval should be able to find.

Retrieval intent may include:

- relevant Original Sources;
- relevant IdeaMark documents;
- relevant Skeleton Graphs;
- relevant Sections;
- reusable Entities;
- role-bearing Occurrences;
- source anchors;
- previous Projections;
- examples or counterexamples;
- warnings or constraints;
- reconstruction-ready source windows.

Retrieval intent may be human-facing, AI-facing, or tool-facing.

A Projection should avoid pretending that keyword search is the only retrieval path.

Projection-guided retrieval may depend on structure, Skeleton Graph match, role, source coverage, intended use, compatibility, or reconstruction need.

## Skeleton-oriented Retrieval

A Projection MAY define one or more Skeleton Graph expectations for retrieval.

These expectations may be expressed as:

- required activity slots;
- preferred activity slots;
- excluded or unsafe slots;
- required Skeleton Links;
- optional Skeleton Links;
- partial-match tolerance;
- review requirements for missing slots;
- analogical transfer expectations.

The retrieval path may therefore be:

```text
Use-side Projection
  -> required_skeleton / preferred_skeletons / excluded_skeletons
  -> candidate IdeaMark document skeletons
  -> graph pattern match or partial match
  -> candidate Sections / Occurrences / Entities / anchors
  -> reconstruction or review
```

Part 5 does not require a particular graph matching algorithm.

A system may implement exact graph pattern matching, partial matching, heuristic matching, vector-assisted matching, database indexes, or human review workflows.

## Candidate Matching

A Projection MAY define matching criteria for candidate documents, sources, Projections, or Skeleton Graphs.

Matching criteria may consider:

- shared activity purpose;
- Skeleton Graph slots and links;
- required and missing activity slots;
- source domain;
- target domain;
- intended audience;
- user capability assumptions;
- reusable unit boundaries;
- Section strategy;
- source coverage policy;
- traceability sufficiency;
- risk constraints;
- required exclusions;
- reconstruction format.

Matching may be exact, partial, approximate, analogical, or incompatible.

A Projection SHOULD NOT require exact identity when partial compatibility would support useful reconstruction.

A Projection SHOULD also avoid treating a Skeleton Graph match as proof that reconstruction is safe. Skeleton match is a candidate-selection signal, not a final authority signal.

## Compatibility Classes

A Projection Library MAY define compatibility classes.

Common classes include:

- **exact match** — the candidate was generated under the same Projection, a version-compatible Projection, or an equivalent Skeleton Graph profile;
- **compatible match** — the candidate satisfies the hard requirements of the use-side Projection;
- **skeleton match** — the candidate contains a compatible Skeleton Graph even if its domain, source vocabulary, or generation Projection differs;
- **partial match** — the candidate contains useful structures but needs adaptation or review;
- **analogical match** — the candidate comes from another domain but has reusable activity composition structure;
- **unsafe match** — the candidate may look relevant but violates a blocking requirement;
- **unknown match** — available metadata or Skeleton Graph coverage is insufficient to judge compatibility.

These classes are Projection-side concepts.

Part 5 does not require a universal ranking algorithm.

## Filtering

A Projection SHOULD define important filters when misuse would be costly.

Filters may exclude candidates because:

- the source is outside the allowed authority range;
- the document was generated under an incompatible Projection;
- the candidate lacks required Skeleton Graph slots;
- the candidate has an unsafe Skeleton Link pattern;
- traceability is insufficient;
- the audience assumptions are unsafe;
- the domain transfer would be misleading;
- the material is outdated;
- required privacy or permission conditions are not met;
- the reconstruction task requires stronger evidence.

Filtering is not merely search narrowing.

It is part of responsibility control for reconstruction.

## Matching Explanation

A Projection-capable system SHOULD be able to explain important compatibility judgments when practical.

An explanation may state:

- which Projection requirements matched;
- which Skeleton Graph slots matched;
- which Skeleton Links matched;
- which required slots or links are missing;
- which assumptions differ;
- which transformation is needed;
- which risks remain;
- which source anchors should be reviewed;
- whether human review is recommended.

Explanations reduce interpretation cost and help Projection Libraries improve over time.

A Skeleton-oriented explanation should be framed around activity composition rather than opaque keyword scores.

## Compatibility and Versioning

Projection version changes may affect compatibility.

A later Projection version may be compatible with earlier documents, incompatible with them, or compatible only through migration rules.

A Projection SHOULD record versioning expectations when documents generated under old versions are expected to remain reusable.

If a Projection defines Skeleton Graph expectations, versioning should describe whether earlier Skeleton slot names, link types, or graph patterns remain compatible.

## Compatibility as a Quality Signal

Repeated compatibility success is evidence that a Projection is useful.

Repeated mismatch, unsafe retrieval, excessive filtering, missing Skeleton slots, noisy Skeleton matches, or reconstruction failure may indicate that the Projection boundary, requirement bundle, Skeleton Graph, or metadata strategy should be revised.

Projection Libraries SHOULD treat retrieval and matching feedback as an important input to lifecycle improvement.
