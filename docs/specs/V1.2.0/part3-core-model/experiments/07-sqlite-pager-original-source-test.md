# SQLite Pager Original Source Test

**Part:** 3 — Core Model  
**Status:** Design Experiment  
**Type:** Second Original Source / Multi-Projection Generation Test

This document proposes the second Original Source test for Part 3: SQLite `src/pager.c`.

The purpose is to check whether the Section / Occurrence / Entity interpretation developed through the CPython `heapq.py` experiment generalizes to a different kind of source code.

Unlike `heapq.py`, this source is not primarily a compact algorithm teaching module.

It describes a subsystem with correctness invariants, rollback-journal assumptions, file locking, transaction state transitions, and failure behavior.

## 1. Candidate Original Source

```yaml
original_source:
  id: SRC-sqlite-pager-c
  repository: sqlite/sqlite
  path: src/pager.c
  ref: master
  source_type: public_source_code
```

## 2. Initial Source Observations

The file identifies the pager as the subsystem used to access a database disk file.

It implements atomic commit and rollback using a separate journal file, and it implements file locking to prevent simultaneous unsafe access.

The design comment block explicitly lists rollback-journal invariants.

It defines when a page is overwriteable, when writes are allowed, when sync must occur, what logical equivalence means, and what locking guarantees must hold.

The file also documents a pager state machine with states such as `OPEN`, `READER`, `WRITER_LOCKED`, `WRITER_CACHEMOD`, `WRITER_DBMOD`, `WRITER_FINISHED`, and `ERROR`, along with the functions responsible for state transitions.

## 3. Why This Source Is Useful

This source tests a different kind of Intellectual Activity from `heapq.py`.

It can support:

- correctness reasoning;
- transactional durability reasoning;
- state-machine design;
- concurrency and locking design;
- failure recovery analysis;
- subsystem architecture documentation;
- implementation review.

If Section / Occurrence / Entity works here, it is less likely to be an artifact of algorithm-tutorial code.

## 4. Candidate Generation Projections

### 4.1 Correctness Invariant Projection

```yaml
projection:
  id: sqlite-pager-correctness-invariants-v0
  purpose: extract correctness invariants that constrain pager behavior
  intended_activity:
    - explain why rollback journaling preserves database consistency
    - help reviewers identify invariant-preserving implementation paths
  focus:
    - overwriteable page definition
    - rollback journal guarantees
    - sync-before-delete constraints
    - logical equivalence
    - well-formed transaction boundaries
  non_goals:
    - complete pager API documentation
    - full state-machine walkthrough
    - WAL-mode behavior
```

Expected Sections:

```yaml
sections:
  - title: Overwriteable pages as safety boundary
  - title: Journal content as rollback evidence
  - title: Sync ordering before journal removal
  - title: Logical equivalence after rollback
  - title: Well-formed transaction boundaries
```

Expected Entities:

```yaml
entities:
  - kind: correctness_invariant
    material: database pages are overwritten only when rollback safety conditions hold
  - kind: durability_constraint
    material: database writes are synced before journal deletion or truncation
  - kind: equivalence_condition
    material: rollback produces a database logically equivalent to transaction start
```

### 4.2 State Machine Projection

```yaml
projection:
  id: sqlite-pager-state-machine-v0
  purpose: reconstruct pager behavior as a state machine
  intended_activity:
    - generate state diagrams
    - explain legal transitions
    - support implementation review around state changes
  focus:
    - pager states
    - transition functions
    - lock requirements per state
    - trusted and untrusted variables per state
  non_goals:
    - journal invariant proof
    - SQL-level transaction explanation
```

Expected Sections:

```yaml
sections:
  - title: Pager state diagram
  - title: OPEN and READER baseline states
  - title: Writer state progression
  - title: ERROR recovery path
  - title: Transition functions as implementation hooks
```

Expected Entities:

```yaml
entities:
  - kind: state
    material: OPEN state has no guaranteed lock or database size knowledge
  - kind: state
    material: READER state permits reading and has known database size
  - kind: transition
    material: sqlite3PagerBegin moves READER to WRITER_LOCKED
  - kind: transition
    material: pager_error moves writer states to ERROR
```

### 4.3 Concurrency / Locking Projection

```yaml
projection:
  id: sqlite-pager-locking-v0
  purpose: extract concurrency and locking rules from pager implementation
  intended_activity:
    - explain how pager prevents unsafe simultaneous access
    - help engineers reason about lock acquisition and release
  focus:
    - shared lock while reading
    - exclusive lock while writing
    - write transaction lock progression
    - cache invalidation signaling
  non_goals:
    - full VFS implementation
    - SQL transaction semantics
```

Expected Sections:

```yaml
sections:
  - title: Locking as access safety boundary
  - title: Shared lock during reads
  - title: Exclusive lock during writes
  - title: Writer lock acquisition before modification
  - title: Cache flush signaling before releasing exclusive lock
```

Expected Entities:

```yaml
entities:
  - kind: locking_rule
    material: a SHARED lock is held while reading database content
  - kind: locking_rule
    material: an EXCLUSIVE lock is held when writing the database file
  - kind: cache_consistency_rule
    material: bytes 24 through 39 change before releasing exclusive lock after modification
```

### 4.4 Failure Recovery Projection

```yaml
projection:
  id: sqlite-pager-failure-recovery-v0
  purpose: reconstruct how pager design supports rollback and recovery after partial failure
  intended_activity:
    - explain crash recovery assumptions
    - identify recovery-critical ordering constraints
    - generate failure scenario reviews
  focus:
    - rollback journal
    - unsynced changes
    - journal removal
    - truncate behavior
    - ERROR state
  non_goals:
    - normal read path explanation
    - high-level database user API
```

Expected Sections:

```yaml
sections:
  - title: Rollback journal as recovery basis
  - title: Removing unsynced changes and rolling back
  - title: Truncation after rollback
  - title: ERROR state as recovery path
  - title: Sync ordering and failure windows
```

Expected Entities:

```yaml
entities:
  - kind: recovery_invariant
    material: rollback after removing unsynced journal changes yields logical equivalence
  - kind: recovery_action
    material: xTruncate restores database size at transaction start
  - kind: error_state_behavior
    material: ERROR returns to OPEN through pager_unlock
```

### 4.5 Architecture Documentation Projection

```yaml
projection:
  id: sqlite-pager-architecture-doc-v0
  purpose: explain the pager subsystem for engineers entering the codebase
  intended_activity:
    - produce subsystem overview
    - identify responsibilities and boundaries
    - guide further source reading
  focus:
    - pager responsibility
    - disk file access
    - journal file role
    - locking role
    - state machine overview
  non_goals:
    - formal invariant proof
    - complete line-by-line implementation guide
```

Expected Sections:

```yaml
sections:
  - title: Pager subsystem responsibility
  - title: Journal file as transaction safety mechanism
  - title: Locking as multi-process safety mechanism
  - title: State machine as operational map
  - title: Where to continue reading implementation
```

Expected Entities:

```yaml
entities:
  - kind: subsystem_responsibility
    material: pager accesses database disk files
  - kind: architectural_mechanism
    material: separate journal file supports atomic commit and rollback
  - kind: architectural_mechanism
    material: file locking prevents unsafe simultaneous writing or reading during writing
```

## 5. Expected Multi-Projection Differences

| Projection | Likely Section Shape | Entity Shape | Future Activity |
|---|---|---|---|
| Correctness Invariant | invariant windows | invariant, constraint, equivalence condition | proof sketch, review checklist |
| State Machine | state and transition windows | state, transition, state guarantee | diagram, state transition explanation |
| Concurrency / Locking | access-control windows | locking rule, cache rule | concurrency review, race analysis |
| Failure Recovery | failure-window windows | recovery invariant, recovery action | crash scenario review |
| Architecture Documentation | subsystem overview windows | responsibility, mechanism, reading guide | onboarding explanation |

## 6. Initial Design Hypothesis

SQLite `pager.c` should produce clearer differences between generation Projections than `heapq.py` because different Projections focus on substantially different conceptual layers:

```text
correctness invariant
state machine
locking protocol
failure recovery
architecture overview
```

This should be a strong test of whether Section can function as a Projection-shaped local source window.

## 7. Expected Feedback for Part 3

This test should help answer:

1. Whether Section-level anchors remain sufficient for subsystem code.
2. Whether Occurrence roles need to support state, transition, invariant, and failure-window placements.
3. Whether Entity payload can remain compact without becoming full documentation.
4. Whether source code comments can serve as Original Source anchors alongside executable implementation.
5. Whether multiple generated IdeaMark Documents from the same Original Source should be stored separately or as variants under shared source metadata.

## 8. Next Step

Generate one small candidate IdeaMark-like structure under the Correctness Invariant Projection.

Then perform cross-Projection reconstruction under the other four Projections.

If the structure fails to support State Machine or Locking reconstruction, generate additional candidate structures under those Projections and compare how the IdeaMark Documents differ.
