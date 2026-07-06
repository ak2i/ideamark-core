# Non-normative YAML Note

**Part:** 3 — Core Model  
**Status:** Design History Note

## Purpose

YAML fragments in this directory are exploratory design artifacts.

They were created to test the Part 3 Core Model before the Part 4 Core Specification adopted the normative array-based object representation.

Therefore, YAML-like fragments in Part 3 experiments may use provisional shapes such as:

- keyed maps for `sections`, `occurrences`, or `entities`;
- `original_sources` inside `meta`;
- singular `anchor` fields;
- `line_ranges` instead of `ranges`;
- `anchor_type` instead of anchor `role` or `purpose`;
- experimental names such as `activity_frames`;
- superseded or exploratory terminology.

These fragments are intentionally preserved as design history.

They should not be treated as normative IdeaMark Core v1.2.0 examples.

## Where to Find Normative-style Samples

Implementation-oriented YAML samples are maintained under:

```text
docs/specs/V1.2.0/part4-core-specification/samples/
```

Those samples use the Part 4 array-based object representation and are intended to support parsers, validators, formatters, migration tests, and conformance-suite development.

## Migration Interpretation

When comparing Part 3 experiments to Part 4 samples, the intended migration direction is generally:

```yaml
sections:
  SEC-001:
    title: Example
```

becomes:

```yaml
sections:
  - id: SEC-001
    title: Example
```

and:

```yaml
anchor:
  source: SRC-001
  line_ranges:
    - start: 1
      end: 10
  anchor_type: source_context
```

becomes:

```yaml
anchors:
  - source: SRC-001
    type: line_range
    ranges:
      - start: 1
        end: 10
    role: source_context
```

The exact migration behavior belongs to migration tools or implementation test suites, not to Part 3 experiments.
