# Heapq JSON and MongoDB Search Simulation

**Part:** 3 — Core Model  
**Status:** Design Experiment  
**Type:** JSON Conversion / Search Simulation

This document simulates how a candidate IdeaMark Document generated from CPython `Lib/heapq.py` could be converted to JSON and searched if stored in MongoDB.

No MongoDB execution is required at this stage.

The purpose is to evaluate whether the document structure supports useful retrieval, matching, filtering, and reconstruction.

## 1. Simulation Goals

This simulation asks:

1. What JSON shape would be natural for a generated IdeaMark Document?
2. Which fields would be useful for retrieval?
3. Which searches become simple with the current Section / Occurrence / Entity structure?
4. Which searches become easier with a flatter activity-frame structure?
5. What does this imply for Part 3 Core Model design?

## 2. JSON Shape A — Section / Occurrence / Entity

The current candidate can be represented as a document-level JSON object.

```json
{
  "doc_id": "part3-heapq-performance-001",
  "doc_type": "design_experiment",
  "status": "exploratory",
  "meta": {
    "original_sources": [
      {
        "id": "SRC-heapq-py",
        "repository": "python/cpython",
        "path": "Lib/heapq.py",
        "ref": "main",
        "source_type": "public_source_code"
      }
    ],
    "projections": [
      {
        "role": "generation",
        "id": "code-design-performance-heapq-v0",
        "purpose": "extract implementation and performance reasoning from source code",
        "focus": [
          "heap invariant",
          "comparison cost",
          "implementation rationale",
          "empirical comparison counts"
        ]
      }
    ]
  },
  "sections": [
    {
      "id": "SEC-002",
      "title": "Comparison-cost-aware sift strategy",
      "anchor": {
        "source": "SRC-heapq-py",
        "line_ranges": [
          { "start": 58, "end": 95 }
        ],
        "anchor_type": "implementation_rationale"
      },
      "occurrences": ["OCC-004", "OCC-005", "OCC-006"]
    }
  ],
  "occurrences": [
    {
      "id": "OCC-004",
      "entity": "IE-004",
      "role": "explains_non_textbook_choice",
      "rationale": "This is a reusable performance-engineering lesson: do not assume a local early-exit optimization improves the real workload."
    }
  ],
  "entities": [
    {
      "id": "IE-004",
      "kind": "implementation_rationale",
      "content": "The implementation deliberately avoids an early break in _siftup because the moved item after a heap pop tends to be large, and early comparisons often do not pay off.",
      "source_role": "optimization_rationale"
    }
  ],
  "structure": {
    "sections": ["SEC-001", "SEC-002", "SEC-003", "SEC-004"]
  }
}
```

### 2.1 Strengths

This shape preserves separation of:

- source-anchored local frames;
- reusable payloads;
- role placements;
- document-level metadata.

It supports reuse of the same Entity across multiple Occurrences if needed.

### 2.2 Weaknesses

MongoDB-style querying becomes more complex because important reconstruction material is split across arrays.

For example, answering:

> Find source regions where comparison cost supports an implementation choice.

requires matching across:

- `sections.anchor`
- `sections.occurrences`
- `occurrences.role`
- `occurrences.entity`
- `entities.kind`
- `entities.source_role`

This is possible, but less direct.

## 3. JSON Shape B — Flattened Activity Frames

A flatter representation can embed role-bearing items inside source-anchored local frames.

```json
{
  "doc_id": "part3-heapq-performance-001",
  "doc_type": "design_experiment",
  "status": "exploratory",
  "meta": {
    "original_sources": [
      {
        "id": "SRC-heapq-py",
        "repository": "python/cpython",
        "path": "Lib/heapq.py",
        "ref": "main",
        "source_type": "public_source_code"
      }
    ],
    "projections": [
      {
        "role": "generation",
        "id": "code-design-performance-heapq-v0",
        "focus": [
          "heap invariant",
          "comparison cost",
          "implementation rationale",
          "empirical comparison counts"
        ]
      }
    ]
  },
  "activity_frames": [
    {
      "id": "AF-002",
      "title": "Comparison-cost-aware sift strategy",
      "source_anchor": {
        "source": "SRC-heapq-py",
        "line_ranges": [
          { "start": 58, "end": 95 }
        ],
        "anchor_type": "implementation_rationale"
      },
      "projection_fit": {
        "generated_for": [
          "comparison_cost",
          "implementation_rationale"
        ],
        "compatible_with": [
          "performance_engineering",
          "api_design"
        ],
        "weak_for": [
          "stream_merge",
          "scheduler_domain_adaptation"
        ]
      },
      "items": [
        {
          "id": "AI-004",
          "role": "optimization_rationale",
          "kind": "implementation_rationale",
          "material": "avoid early break in _siftup",
          "rationale": "local early-exit optimization may not reduce total comparison cost under repeated pop workloads"
        },
        {
          "id": "AI-005",
          "role": "cost_driver",
          "kind": "performance_factor",
          "material": "comparisons may be expensive",
          "rationale": "priority may be hidden in custom comparison methods or tuple comparison"
        },
        {
          "id": "AI-006",
          "role": "empirical_support",
          "kind": "empirical_evidence",
          "material": "comparison-count examples support the selected strategy"
        }
      ]
    }
  ]
}
```

### 3.1 Strengths

This shape makes reconstruction-oriented retrieval simpler.

The local frame contains:

- source anchor;
- projection fit metadata;
- ordered items;
- item roles;
- rationale.

This matches how the candidate was actually used during cross-Projection reconstruction.

### 3.2 Weaknesses

This shape reduces global Entity reuse.

If the same material needs to appear in multiple frames, it may be duplicated or require item references.

However, duplication may be acceptable if the Core Model prioritizes reconstruction cost reduction over global semantic identity.

## 4. Simulated MongoDB Collections

Two storage approaches are possible.

### 4.1 Single Document Collection

```text
ideamark_documents
```

Each IdeaMark Document is stored as one MongoDB document.

Good for:

- document retrieval;
- projection-level filtering;
- source-level filtering;
- whole-document reconstruction.

Less good for:

- item-level search across many documents;
- high-volume retrieval of individual frames;
- aggregation by role or anchor.

### 4.2 Split Frame Collection

```text
ideamark_documents
ideamark_activity_frames
```

Each local activity frame is stored as a separate document with duplicated document metadata.

Example frame document:

```json
{
  "doc_id": "part3-heapq-performance-001",
  "frame_id": "AF-002",
  "source": {
    "repository": "python/cpython",
    "path": "Lib/heapq.py",
    "ref": "main",
    "line_ranges": [
      { "start": 58, "end": 95 }
    ]
  },
  "generation_projection": "code-design-performance-heapq-v0",
  "projection_focus": [
    "comparison_cost",
    "implementation_rationale",
    "empirical_comparison_counts"
  ],
  "projection_fit": {
    "compatible_with": ["performance_engineering", "api_design"],
    "weak_for": ["stream_merge", "scheduler_domain_adaptation"]
  },
  "title": "Comparison-cost-aware sift strategy",
  "items": [
    {
      "role": "optimization_rationale",
      "kind": "implementation_rationale",
      "material": "avoid early break in _siftup"
    },
    {
      "role": "cost_driver",
      "kind": "performance_factor",
      "material": "comparisons may be expensive"
    },
    {
      "role": "empirical_support",
      "kind": "empirical_evidence",
      "material": "comparison-count examples support the selected strategy"
    }
  ]
}
```

This shape is likely more useful for retrieval.

## 5. Simulated Searches

### 5.1 Find frames about comparison cost

Intent:

> Retrieve reusable implementation reasoning related to comparison cost.

Possible MongoDB-style query:

```javascript
db.ideamark_activity_frames.find({
  $or: [
    { "projection_focus": "comparison_cost" },
    { "items.role": "cost_driver" },
    { "items.material": /comparison/i }
  ]
})
```

Expected result:

```text
AF-002: Comparison-cost-aware sift strategy
```

### 5.2 Find frames compatible with API Design Projection

Intent:

> A reconstruction Projection about API design searches for previously generated material that may be useful.

Possible query:

```javascript
db.ideamark_activity_frames.find({
  "projection_fit.compatible_with": "api_design"
})
```

Expected result:

```text
AF-002: Comparison-cost-aware sift strategy
AF-003: Choosing heap operations for fixed-size workflows
```

### 5.3 Find source anchors for a code review assistant

Intent:

> Return original source locations that support an implementation rationale.

Possible query:

```javascript
db.ideamark_activity_frames.find(
  {
    "source.repository": "python/cpython",
    "source.path": "Lib/heapq.py",
    "items.kind": "implementation_rationale"
  },
  {
    frame_id: 1,
    title: 1,
    "source.line_ranges": 1,
    items: 1
  }
)
```

Expected result:

```text
AF-002 with line range 58-95.
```

### 5.4 Find candidate material for stream merge reconstruction

Intent:

> A data-pipeline Projection searches for stream merge material.

Possible query:

```javascript
db.ideamark_activity_frames.find({
  $or: [
    { "projection_fit.compatible_with": "stream_merge" },
    { "projection_focus": "stream_merge" },
    { "items.material": /merge|stream|sorted/i }
  ]
})
```

Expected result:

```text
No direct frame from the current candidate.
```

Interpretation:

The stored IdeaMark Document is not sufficient for this reconstruction.

The system should either:

- return low confidence;
- reopen the Original Source;
- trigger a new Decomposition under a stream-merge Projection.

### 5.5 Find reusable top-k or fixed-size heap guidance

Intent:

> Retrieve implementation guidance for maintaining a fixed-size heap.

Possible query:

```javascript
db.ideamark_activity_frames.find({
  $or: [
    { "title": /fixed-size/i },
    { "items.role": "fixed_size_heap_choice" },
    { "items.material": /heapreplace|heappushpop|fixed-size/i }
  ]
})
```

Expected result:

```text
AF-003: Choosing heap operations for fixed-size workflows.
```

## 6. Search Types Enabled

The flattened frame shape enables several useful search modes.

### 6.1 Projection-fit search

Search by compatibility between generation Projection and reconstruction Projection.

Example:

```text
Find frames generated for performance engineering but compatible with API design.
```

### 6.2 Source-anchor search

Search by repository, path, line range, source type, or source role.

Example:

```text
Find all IdeaMark frames anchored to CPython heapq.py implementation rationale comments.
```

### 6.3 Role search

Search by item role.

Example:

```text
Find all items that act as empirical support for an implementation choice.
```

### 6.4 Material keyword search

Search by text fields such as title, material, rationale, and projection focus.

Example:

```text
Find frames mentioning comparison count, custom comparison methods, or heapify.
```

### 6.5 Reconstruction gap search

Search for absence or weakness.

Example:

```text
Find whether this document contains material compatible with stream-merge reconstruction.
```

If no direct match exists, the document may still be useful as a source pointer but not as a ready reconstruction structure.

## 7. Index Candidates

If stored in MongoDB, useful indexes may include:

```javascript
db.ideamark_activity_frames.createIndex({ "source.repository": 1, "source.path": 1 })
db.ideamark_activity_frames.createIndex({ "generation_projection": 1 })
db.ideamark_activity_frames.createIndex({ "projection_focus": 1 })
db.ideamark_activity_frames.createIndex({ "projection_fit.compatible_with": 1 })
db.ideamark_activity_frames.createIndex({ "items.role": 1 })
db.ideamark_activity_frames.createIndex({ "items.kind": 1 })
db.ideamark_activity_frames.createIndex({ "source.line_ranges.start": 1, "source.line_ranges.end": 1 })
```

A text index may also be useful:

```javascript
db.ideamark_activity_frames.createIndex({
  "title": "text",
  "items.material": "text",
  "items.rationale": "text",
  "projection_focus": "text"
})
```

Vector search could later be added for approximate Projection compatibility or conceptual similarity, but it is not required for the basic structural simulation.

## 8. Design Findings

### 8.1 Activity-frame storage matches retrieval better than separate registries

For MongoDB-style retrieval, the flattened activity-frame structure appears more practical than separate Section / Occurrence / Entity registries.

It allows one query result to contain enough material for reconstruction without requiring multiple joins or post-processing steps.

### 8.2 Global Entity identity is less important than local reconstruction utility

The simulation suggests that global reusable Entity identity may not be necessary for the Core.

For this use case, it is more important that a source-anchored frame contains the role-bearing materials needed for reconstruction.

### 8.3 Projection-fit metadata is useful but must stay lightweight

Fields such as `generated_for`, `compatible_with`, and `weak_for` are useful for search simulation.

However, they should not become a universal ontology.

They should be treated as Projection- or implementation-defined metadata.

### 8.4 Source-mediated reuse should be explicit

A search may find:

1. a direct reconstruction frame; or
2. a source pointer that may require new Decomposition.

The system should distinguish these outcomes.

This suggests a useful retrieval classification:

```yaml
retrieval_match_type:
  - direct_frame_match
  - partial_frame_match
  - source_pointer_only
  - no_match
```

### 8.5 Relation remains unnecessary for search

The simulated searches did not require a Relation namespace.

Searches worked through frame grouping, item roles, source anchors, projection metadata, and text search.

## 9. Implication for Part 3

The experiment suggests that the final Part 3 Core Model may be better framed around:

```text
IdeaMark Document
  -> metadata
  -> source-anchored activity frames
  -> ordered role-bearing materials
```

rather than:

```text
IdeaMark Document
  -> sections
  -> occurrences
  -> entities
  -> relations
```

This does not necessarily mean the old names must be discarded immediately.

But it suggests that the essential structure is:

1. **Document metadata** — sources, projections, status, generation context.
2. **Local activity frame** — a Projection-shaped, source-anchored reconstruction unit.
3. **Frame item** — a role-bearing material used to generate activation expressions.
4. **Source anchor** — a traceability claim connecting the frame to Original Source material.

## 10. Next Step

Create a candidate Part 3 replacement model based on:

```yaml
meta:
activity_frames:
  - source_anchor:
    projection_fit:
    items:
structure:
```

Then compare it against the Section / Occurrence / Entity model using the existing constraint set.
