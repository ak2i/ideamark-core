---
ideamark_version: 1
template_id: "imtpl.detail.infra"
template_name: "Detail Infra Template"
template_version: "1.0.0"
description: "WorkCell Integration Spec / Service Flow / Decision6 を入力として、Infraの構成・運用・観測・セキュリティを定義するテンプレート。正は上流（Integration/Flow/Decision6）であり、本テンプレは実装可能なInfra仕様へ落とす。"
domain: ["software-design", "infrastructure", "workcell"]
tags: ["detail", "infra", "spec", "runtime", "observability", "security"]
lang: "ja-JP"
status: stable
created_at: "2026-01-09"
---

# Detail Infra Template

本テンプレートは、WorkCellのInfra仕様を **「フロー・統合仕様・意思決定」から導出**するためのもの。  
UI/API/DB の前提にもなるが、特に **実行環境・運用・監査性** をInfraに埋め込むことを目的とする。

- **正（source of truth）**：Integration Spec / Service Flow / Decision6
- **本テンプレの役割**：上流で固定されたイベント・状態を、実装可能なInfra仕様に落とす

---

## 0. Provenance（参照元の明確化）【必須】

このInfra仕様が **どの版・どのファイル**に基づくかを機械可読で記録する。

```yaml
provenance:
  infra_spec_id: "<stable id, e.g. infra.relatea.v1>"
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

## 1. Infra Context（前提）【必須】

```yaml
infra_context:
  runtime:
    - "browser"
    - "node"
    - "deno"
  network:
    - "HTTPS"
    - "WebSocket (if required)"
  constraints:
    - "secret はクライアントに置かない"
```

---

## 2. Components（構成要素）【必須】

```yaml
components:
  - id: "comp.client_app"
    type: "runtime"
    description: "SDK を実行するクライアント"
  - id: "comp.api_gateway"
    type: "edge"
    description: "API エンドポイント"
```

---

## 3. Integration Points（接続点）【必須】

```yaml
integration_points:
  - name: "auth"
    protocol: "HTTPS"
  - name: "realtime"
    protocol: "WebSocket"
```

---

## 4. Event & Job Wiring（イベント/ジョブ連携）【推奨】

```yaml
event_wiring:
  - event: "event.booking.confirmed"
    consumer: "job.reminder"
    delivery: "queue"
```

---

## 5. Secrets & Security（秘密情報・セキュリティ）【必須】

```yaml
security:
  secrets:
    - "anon key"
  forbidden:
    - "service_role key"
  token_handling:
    - "access_token をログに残さない"
```

---

## 6. Observability & Audit（観測・監査）【必須】

```yaml
observability:
  logs:
    - "event logs"
  metrics:
    - "latency"
    - "error rate"
  tracing:
    - "trace_id"
```

---

## 7. Operations & SLO（運用・SLO）【推奨】

```yaml
operations:
  slo:
    - "p95 latency < 500ms"
  alerts:
    - "error rate > 1%"
```

---

## 8. Deployment & Release（デプロイ・リリース）【推奨】

```yaml
deployment:
  release_strategy:
    - "minor release for runtime support changes"
  compatibility:
    - "LTS runtime only"
```

---

## 9. References（参照）【必須】

```yaml
refs:
  - id: "ref.integration"
    kind: "ideamark_doc"
    title: "WorkCell Integration Spec"
    locator: "<integ-doc-uri>"
  - id: "ref.flow.*"
    kind: "ideamark_doc"
    title: "Service Flows"
    locator: "<flow-doc-uri>"
```

---

# Renderings (Optional)

任意で構成図 / Mermaid 等を置けるが、正は上の意味構造。

```yaml
renderings:
  - id: "render.infra.diagram.v1"
    type: "mermaid.flowchart"
    generated_from: "<infra_spec_id>@<hash>"
```
