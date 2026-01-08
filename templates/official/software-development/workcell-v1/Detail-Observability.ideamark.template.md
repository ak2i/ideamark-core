---
ideamark_version: 1
template_id: "imtpl.detail.observability"
template_name: "Detail Observability Template"
template_version: "1.0.0"
description: "WorkCell Integration Spec / Service Flow / Decision6 を入力として、ログ/メトリクス/トレースの設計を定義するテンプレート。"
domain: ["software-design", "observability", "workcell"]
tags: ["detail", "observability", "metrics", "logging", "tracing"]
lang: "ja-JP"
status: stable
created_at: "2026-01-09"
---

# Detail Observability Template

本テンプレートは、WorkCellの観測仕様を **「フロー・統合仕様・意思決定」から導出**するためのもの。  
特に **イベント契約・相関ID・メトリクス定義** を固定する。

---

## 0. Provenance（参照元の明確化）【必須】

```yaml
provenance:
  obs_spec_id: "<stable id, e.g. obs.relatea.v1>"
  created_by: "<human or tool>"
  created_at: "<ISO-8601 datetime>"
  method: "manual|engine|hybrid"
  based_on:
    integration_spec:
      - doc_id: "<integ doc_id>"
        template_ref: "<template ref>"
        locator: "<path/uri>"
        content_hash: "<optional sha256>"
    decision6:
      - doc_id: "<decision6 doc_id>"
        template_ref: "<template ref>"
        locator: "<path/uri>"
        content_hash: "<optional sha256>"
    flows:
      - doc_id: "<flow doc_id>"
        flow_id: "<flow_id>"
        locator: "<path/uri>"
        content_hash: "<optional sha256>"
  notes: []
```

---

## 1. Observability Context（前提）【必須】

```yaml
observability_context:
  goals:
    - "意思決定の評価可能性"
    - "障害の検知と原因追跡"
  retention:
    logs: "P30D"
    metrics: "P90D"
```

---

## 2. Event Contract（イベント契約）【必須】

```yaml
event_contract:
  - event: "event.auth.session.established"
    required_fields: ["timestamp", "user_id", "session_id"]
```

---

## 3. Metrics（メトリクス）【必須】

```yaml
metrics:
  - id: "metric.auth.session_success_rate"
    definition: "event.auth.session.established / event.auth.signin.requested"
    unit: "ratio"
```

---

## 4. Logs（ログ）【必須】

```yaml
logs:
  - stream: "event_log"
    fields: ["timestamp", "event", "trace_id", "project_ref"]
```

---

## 5. Tracing（トレース）【推奨】

```yaml
tracing:
  correlation_keys:
    - "trace_id"
    - "request_id"
```

---

## 6. Alerting（アラート）【推奨】

```yaml
alerts:
  - name: "auth_session_success_low"
    condition: "metric.auth.session_success_rate < 0.99"
```

---

## 7. References（参照）【必須】

```yaml
refs:
  - id: "ref.integration"
    kind: "ideamark_doc"
    title: "WorkCell Integration Spec"
    locator: "<integ-doc-uri>"
```

---

# Renderings (Optional)

```yaml
renderings:
  - id: "render.obs.metrics.v1"
    type: "table"
    generated_from: "<obs_spec_id>@<hash>"
```
