# Extended Analysis Fields

IdeaMark allows optional structures to capture progress and operational metrics for tasks or projects.
These fields are especially useful for `project-analysis` or `work-review` documents.

## timeline / statusHistory

```yaml
timeline:
  - entity: task:product-release
    year: 2023
    milestone: "\u4ed5\u69d8\u78ba\u5b9a"
    status: delayed
```

Record annual events or status changes for any task or organizational unit.

## dependencies / blockers

```yaml
dependencies:
  - from: task:design
    to: task:implementation
    type: sequential
    risk: medium
```

Declare relationships or blockers between tasks to clarify scheduling risk.

## observed_metrics

```yaml
observed_metrics:
  - entity: task:delivery
    metric: response_time
    average: "5d"
    stdev: "2d"
```

Store measured KPIs or process metrics as part of the pattern record.

## patterns / anti-patterns

```yaml
patterns:
  - type: delayed-decision
    occurred_in: ["task:x", "task:y"]
    severity: high
```

Capture recurring patterns or anti-patterns observed during execution.

## hypotheses / questions

```yaml
hypotheses:
  - text: "\u3053\u306e\u9045\u5ef6\u306f\u8a2d\u8a08\u5de5\u7a0b\u306e\u5c5e\u4eba\u6027\u304c\u539f\u56e0\u3067\u3042\u308b\u53ef\u80fd\u6027\u304c\u9ad8\u3044"
    confidence: 0.7
```

Use hypotheses to state possible causes or open questions along with a confidence score.

These fields complement existing metadata and can be mixed and matched as needed.
