# 6. Projection Retrieval, Matching, and Compatibility

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## Purpose

This chapter defines Projection responsibilities for retrieval, matching, filtering, and compatibility judgment.

IdeaMark reuse depends not only on generating documents, but also on finding and adapting them later.

Projection makes this use-side activity explicit.

## Retrieval Intent

A Projection SHOULD describe what future retrieval should be able to find.

Retrieval intent may include:

- relevant Original Sources;
- relevant IdeaMark documents;
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

Projection-guided retrieval may depend on structure, role, source coverage, intended use, compatibility, or reconstruction need.

## Candidate Matching

A Projection MAY define matching criteria for candidate documents, sources, or Projections.

Matching criteria may consider:

- shared activity purpose;
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

## Compatibility Classes

A Projection Library MAY define compatibility classes.

Common classes include:

- **exact match** — the candidate was generated under the same Projection or a version-compatible Projection;
- **compatible match** — the candidate satisfies the hard requirements of the use-side Projection;
- **partial match** — the candidate contains useful structures but needs adaptation or review;
- **analogical match** — the candidate comes from another domain but has reusable functional structure;
- **unsafe match** — the candidate may look relevant but violates a blocking requirement;
- **unknown match** — available metadata is insufficient to judge compatibility.

These classes are Projection-side concepts.

Part 5 does not require a universal ranking algorithm.

## Filtering

A Projection SHOULD define important filters when misuse would be costly.

Filters may exclude candidates because:

- the source is outside the allowed authority range;
- the document was generated under an incompatible Projection;
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

- which requirements matched;
- which requirements failed;
- which assumptions differ;
- which transformation is needed;
- which risks remain;
- which source anchors should be reviewed;
- whether human review is recommended.

Explanations reduce interpretation cost and help Projection Libraries improve over time.

## Compatibility and Versioning

Projection version changes may affect compatibility.

A later Projection version may be compatible with earlier documents, incompatible with them, or compatible only through migration rules.

A Projection SHOULD record versioning expectations when documents generated under old versions are expected to remain reusable.

## Compatibility as a Quality Signal

Repeated compatibility success is evidence that a Projection is useful.

Repeated mismatch, unsafe retrieval, excessive filtering, or reconstruction failure may indicate that the Projection boundary, requirement bundle, or metadata strategy should be revised.

Projection Libraries SHOULD treat retrieval and matching feedback as an important input to lifecycle improvement.
