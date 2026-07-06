# SQLite Pager Multi-Projection Candidate Test

**Part:** 3 — Core Model  
**Status:** Design Experiment  
**Type:** Multi-Projection Candidate IdeaMark-like Documents

This document generates two small candidate IdeaMark-like structures from SQLite `src/pager.c` under different generation Projections.

The purpose is to test whether the same Original Source produces different Section / Occurrence / Entity structures depending on the Projection.

## 1. Original Source

```yaml
original_sources:
  - id: SRC-sqlite-pager-c
    repository: sqlite/sqlite
    path: src/pager.c
    ref: master
    source_type: public_source_code
```

The source describes the SQLite pager as the subsystem that accesses the database disk file, implements atomic commit and rollback through a separate journal file, and uses file locking to prevent unsafe simultaneous access.

The source also contains a large design comment describing rollback-journal invariants and a pager state diagram.

## 2. Candidate A — Correctness Invariant Projection

```yaml
meta:
  experiment_id: sqlite-pager-correctness-candidate-001
  status: exploratory
  projections:
    - role: generation
      id: sqlite-pager-correctness-invariants-v0
      purpose: extract correctness invariants that constrain pager behavior
      focus:
        - overwriteable page definition
        - rollback journal guarantees
        - sync-before-delete constraints
        - logical equivalence
        - well-formed transaction boundaries
```

### 2.1 Candidate Structure

```yaml
sections:
  SEC-CORR-001:
    title: Overwriteable pages as safety boundary
    anchor:
      source: SRC-sqlite-pager-c
      line_ranges:
        - start: 39
          end: 59
      anchor_type: correctness_condition
    occurrences:
      - OCC-CORR-001
      - OCC-CORR-002

  SEC-CORR-002:
    title: Journal content as rollback evidence
    anchor:
      source: SRC-sqlite-pager-c
      line_ranges:
        - start: 60
          end: 64
      anchor_type: rollback_evidence
    occurrences:
      - OCC-CORR-003

  SEC-CORR-003:
    title: Sync ordering before journal removal
    anchor:
      source: SRC-sqlite-pager-c
      line_ranges:
        - start: 72
          end: 77
      anchor_type: durability_ordering
    occurrences:
      - OCC-CORR-004

  SEC-CORR-004:
    title: Logical equivalence after rollback
    anchor:
      source: SRC-sqlite-pager-c
      line_ranges:
        - start: 78
          end: 88
      anchor_type: recovery_correctness
    occurrences:
      - OCC-CORR-005

  SEC-CORR-005:
    title: Transaction boundary well-formedness
    anchor:
      source: SRC-sqlite-pager-c
      line_ranges:
        - start: 103
          end: 110
      anchor_type: transaction_boundary
    occurrences:
      - OCC-CORR-006
      - OCC-CORR-007

entities:
  IE-CORR-001:
    kind: correctness_definition
    content: |
      A database page is overwriteable only when rollback safety conditions make later recovery possible.
    source_role: overwriteable_boundary

  IE-CORR-002:
    kind: safety_rule
    content: |
      A page is never overwritten unless the page and all pages on the same sector are overwriteable, or atomic page write optimization applies.
    source_role: write_permission_rule

  IE-CORR-003:
    kind: rollback_evidence
    content: |
      Journaled page content must match both the database content when the journal was written and the content at transaction start.
    source_role: journal_identity_rule

  IE-CORR-004:
    kind: durability_constraint
    content: |
      Database file writes are synced before the rollback journal or super-journal is deleted, truncated, or zeroed.
    source_role: sync_before_journal_removal

  IE-CORR-005:
    kind: recovery_invariant
    content: |
      If unsynced rollback-journal changes are removed and the journal is rolled back, the resulting database is logically equivalent to the transaction start.
    source_role: logical_equivalence_after_rollback

  IE-CORR-006:
    kind: transaction_invariant
    content: |
      The database file is well-formed at the beginning and conclusion of every transaction.
    source_role: boundary_well_formedness

  IE-CORR-007:
    kind: locking_precondition
    content: |
      An EXCLUSIVE lock is held when writing and a SHARED lock is held while reading database content.
    source_role: lock_as_correctness_boundary

occurrences:
  OCC-CORR-001:
    entity: IE-CORR-001
    role: defines_safety_boundary
    rationale: |
      The overwriteable definition determines when data can be modified without losing rollback safety.

  OCC-CORR-002:
    entity: IE-CORR-002
    role: constrains_write_operation
    rationale: |
      The write rule converts the definition of overwriteability into an operational constraint.

  OCC-CORR-003:
    entity: IE-CORR-003
    role: preserves_recovery_basis
    rationale: |
      Rollback requires journal content that can restore the transaction-start database state.

  OCC-CORR-004:
    entity: IE-CORR-004
    role: orders_durable_commit_steps
    rationale: |
      The sync-before-removal rule prevents journal disappearance before database writes become durable.

  OCC-CORR-005:
    entity: IE-CORR-005
    role: states_recovery_guarantee
    rationale: |
      Logical equivalence is the correctness target after rollback under partial journal loss.

  OCC-CORR-006:
    entity: IE-CORR-006
    role: constrains_transaction_boundary
    rationale: |
      Well-formedness at transaction boundaries gives a stable target for commit and rollback.

  OCC-CORR-007:
    entity: IE-CORR-007
    role: connects_locking_to_correctness
    rationale: |
      Locking rules are included only insofar as they protect correctness conditions.

structure:
  sections:
    - SEC-CORR-001
    - SEC-CORR-002
    - SEC-CORR-003
    - SEC-CORR-004
    - SEC-CORR-005
```

### 2.2 Possible Activation Expression

> SQLite's rollback-journal pager design can be read as a set of correctness constraints. The system first defines when a page is safe to overwrite, then restricts writes to those conditions. It records original page content in the journal, orders sync operations before journal removal, and defines rollback success as logical equivalence to the transaction start. Under this Projection, locking matters mainly because it protects the correctness boundary around reads and writes.

## 3. Candidate B — State Machine Projection

```yaml
meta:
  experiment_id: sqlite-pager-state-machine-candidate-001
  status: exploratory
  projections:
    - role: generation
      id: sqlite-pager-state-machine-v0
      purpose: reconstruct pager behavior as a state machine
      focus:
        - pager states
        - transition functions
        - lock requirements per state
        - trusted and untrusted variables per state
```

### 3.1 Candidate Structure

```yaml
sections:
  SEC-STATE-001:
    title: Pager state diagram as operational map
    anchor:
      source: SRC-sqlite-pager-c
      line_ranges:
        - start: 136
          end: 172
      anchor_type: state_machine_overview
    occurrences:
      - OCC-STATE-001
      - OCC-STATE-002

  SEC-STATE-002:
    title: OPEN as untrusted baseline state
    anchor:
      source: SRC-sqlite-pager-c
      line_ranges:
        - start: 174
          end: 183
      anchor_type: state_definition
    occurrences:
      - OCC-STATE-003

  SEC-STATE-003:
    title: READER as stable read state
    anchor:
      source: SRC-sqlite-pager-c
      line_ranges:
        - start: 184
          end: 207
      anchor_type: state_definition
    occurrences:
      - OCC-STATE-004
      - OCC-STATE-005

  SEC-STATE-004:
    title: WRITER_LOCKED as write transaction entry
    anchor:
      source: SRC-sqlite-pager-c
      line_ranges:
        - start: 208
          end: 222
      anchor_type: state_definition
    occurrences:
      - OCC-STATE-006

  SEC-STATE-005:
    title: Transition functions as implementation hooks
    anchor:
      source: SRC-sqlite-pager-c
      line_ranges:
        - start: 159
          end: 172
      anchor_type: transition_list
    occurrences:
      - OCC-STATE-007
      - OCC-STATE-008
      - OCC-STATE-009

entities:
  IE-STATE-001:
    kind: state_machine
    content: |
      The pager behavior is organized into seven named states connected by documented transitions.
    source_role: operational_map

  IE-STATE-002:
    kind: transition_map
    content: |
      The source associates state transitions with concrete C functions.
    source_role: transition_implementation_link

  IE-STATE-003:
    kind: state_definition
    content: |
      OPEN is a baseline state where no read or write transaction is active and database size variables may not be trusted.
    source_role: baseline_state

  IE-STATE-004:
    kind: state_definition
    content: |
      READER is a state where read requirements are met, database size is known, and a SHARED or greater lock is held.
    source_role: read_state

  IE-STATE-005:
    kind: state_guarantee
    content: |
      In READER state, there is no hot journal in the file-system even if a read transaction is not open.
    source_role: read_safety_condition

  IE-STATE-006:
    kind: state_definition
    content: |
      WRITER_LOCKED is entered when a write transaction is opened and required locks are held before cache or database modification.
    source_role: writer_entry_state

  IE-STATE-007:
    kind: transition
    content: |
      sqlite3PagerSharedLock transitions OPEN to READER.
    source_role: read_transition

  IE-STATE-008:
    kind: transition
    content: |
      sqlite3PagerBegin transitions READER to WRITER_LOCKED.
    source_role: write_begin_transition

  IE-STATE-009:
    kind: error_transition
    content: |
      pager_error moves writer states to ERROR, and pager_unlock moves ERROR to OPEN.
    source_role: recovery_transition

occurrences:
  OCC-STATE-001:
    entity: IE-STATE-001
    role: introduces_operational_coordinate_system
    rationale: |
      The state diagram is the local coordinate system for explaining pager operation.

  OCC-STATE-002:
    entity: IE-STATE-002
    role: binds_model_to_implementation
    rationale: |
      The transition list connects conceptual states to implementation functions.

  OCC-STATE-003:
    entity: IE-STATE-003
    role: defines_initial_state
    rationale: |
      OPEN is important because it identifies what is not guaranteed before a read or write transaction begins.

  OCC-STATE-004:
    entity: IE-STATE-004
    role: defines_read_state
    rationale: |
      READER marks the point where read safety requirements are satisfied.

  OCC-STATE-005:
    entity: IE-STATE-005
    role: records_state_guarantee
    rationale: |
      The no-hot-journal guarantee is useful for recovery and correctness reasoning but is placed here as a state guarantee.

  OCC-STATE-006:
    entity: IE-STATE-006
    role: defines_write_entry_state
    rationale: |
      WRITER_LOCKED separates acquiring write permission from actually modifying cache or database state.

  OCC-STATE-007:
    entity: IE-STATE-007
    role: identifies_read_entry_function
    rationale: |
      Transition functions serve as anchors for source navigation during implementation review.

  OCC-STATE-008:
    entity: IE-STATE-008
    role: identifies_write_begin_function
    rationale: |
      The write-begin function is a key navigation point for deeper source reading.

  OCC-STATE-009:
    entity: IE-STATE-009
    role: identifies_error_recovery_path
    rationale: |
      The ERROR path is modeled as part of the state machine rather than as a rollback invariant.

structure:
  sections:
    - SEC-STATE-001
    - SEC-STATE-002
    - SEC-STATE-003
    - SEC-STATE-004
    - SEC-STATE-005
```

### 3.2 Possible Activation Expression

> SQLite's pager can also be reconstructed as a state machine. In this reading, the important material is not the rollback invariant list but the operational map: OPEN has few guarantees, READER establishes read conditions and database size knowledge, WRITER_LOCKED marks the entry into write transaction state before modification, and named functions perform transitions. The same source therefore supports a different intellectual activity: state diagram explanation and implementation navigation.

## 4. Comparison Between Candidate A and Candidate B

| Aspect | Correctness Invariant Projection | State Machine Projection |
|---|---|---|
| Primary source region | rollback-journal invariants | pager state diagram and state descriptions |
| Section shape | safety and durability windows | state and transition windows |
| Entity kinds | correctness definition, durability constraint, recovery invariant | state, transition, state guarantee |
| Occurrence roles | constrains, preserves, orders, states guarantee | defines state, binds transition, identifies function |
| Activation expression | correctness review / rollback explanation | state diagram / implementation navigation |
| Treatment of locking | correctness boundary | state guarantee / transition condition |
| Treatment of ERROR | mostly omitted | explicit recovery path |

## 5. Part 3 Finding

The same Original Source produces substantially different IdeaMark-like Documents under different generation Projections.

The difference is not only in selected text spans.

It changes:

- what a Section is;
- what an Entity contains;
- what an Occurrence role means;
- what source anchors are worth preserving;
- what future Intellectual Activity becomes cheap to activate.

This strongly supports the Part 3 interpretation:

```text
Section = Projection-shaped local source window
Occurrence = role-bearing placement within that window
Entity = reusable material shaped by Projection
```

## 6. Next Test

Apply the same two-candidate generation test to Rust RFC 0001.

The RFC test should show whether Projection-shaped Sections emerge even when the Original Source already has explicit prose headings.
