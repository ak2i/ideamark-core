---
ideamark_version: 1
template_id: "imtpl.detail.api"
template_name: "Detail API Template"
template_version: "1.0.0"
description: "WorkCell Integration Spec / Service Flow / Decision6 を入力として、APIの資源・操作・イベント・状態遷移・監査/観測を定義するテンプレート。正は上流（Integration/Flow/Decision6）であり、本テンプレは実装可能なAPI仕様へ落とす。"
domain: ["software-design", "api", "workcell"]
tags: ["detail", "api", "spec", "event-driven", "traceability"]
lang: "ja-JP"
status: stable
created_at: "2026-01-07"
---

# Detail API Template

本テンプレートは、WorkCellのAPI仕様を **「フロー・統合仕様・意思決定」から導出**するためのもの。  
UI/DB/Infra の前提にもなるが、特に **イベント・状態・監査性** をAPIに埋め込むことを目的とする。

- **正（source of truth）**：Integration Spec / Service Flow / Decision6
- **本テンプレの役割**：上流で固定された語彙・イベント・状態遷移を、実装可能なAPI仕様に落とす

---

## Slot: Provenance（参照元の明確化）【必須】

このAPI仕様が **どの版・どのファイル**に基づくかを機械可読で記録する。

```yaml
provenance:
  api_spec_id: "<stable id, e.g. api.relatea.v1>"
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

## Slot: API Context（前提）【必須】

```yaml
api_context:
  audience:
    - "WorkCell UI（管理画面/LINE導線）"
    - "外部チャネル（例: LINE Webhook）"
  interaction_style:
    - "sync: request/response"
    - "async: event + job"
  security_baseline:
    authn:
      - "channel signature verification (e.g. LINE)"
      - "trainer console auth (if any)"
    authz:
      - "actor-based (client vs trainer)"
  pii_policy:
    - "event/logにはPIIを入れない（hashを基本）"
    - "PIIは別ストア/別テーブルに分離"
```

---

## Slot: Canonical Resources（資源）【必須】

Integration Spec の `canonical_entities` をAPI資源として確定する。

```yaml
resources:
  - name: "booking"
    id_field: "booking_id"
    description: "予約"
  - name: "slot"
    id_field: "slot_id"
    description: "予約枠"
  - name: "session"
    id_field: "session_id"
    description: "実施単位"
  - name: "chart"
    id_field: "chart_id"
    description: "記録"
```

---

## Slot: Commands（操作）【必須】

フローの step と状態遷移に対応する「操作（command）」を定義する。  
UIはこの操作を呼び出し、Infraはこの操作が発火するイベントを運ぶ。

```yaml
commands:
  - id: "cmd.booking.start"
    purpose: "予約開始（flow step S1）"
    actor: "client"
    request:
      fields: ["client_id_hash", "channel", "flow_id"]
    response:
      fields: ["booking_id", "next_actions"]
    emits: ["event.booking.started"]
    state_effect: {entity: "booking", to: "draft"}

  - id: "cmd.booking.confirm"
    purpose: "予約確定（flow step S4）"
    actor: "trainer|system"
    request:
      fields: ["booking_id", "slot_id"]
    response:
      fields: ["booking_id", "session_id"]
    emits: ["event.booking.confirmed"]
    state_effect: {entity: "booking", to: "confirmed"}
```

---

## Slot: Read Models（参照系）【推奨】

```yaml
read_models:
  - id: "rm.booking.summary"
    purpose: "LINE導線で表示する最小情報"
    fields: ["booking_id", "status", "slot_time", "location", "client_display_name?"]
    notes:
      - "display_name はPII扱いなので取り扱いを明記"
```

---

## Slot: State Transition Enforcement（状態遷移の強制）【必須】

Integration Spec の `canonical_transitions` をAPIレベルで守る。

```yaml
state_enforcement:
  - entity: "booking"
    allowed_transitions:
      - {from: "pending", to: "confirmed", by_command: "cmd.booking.confirm"}
      - {from: "confirmed", to: "done", by_event: "event.session.done"}
  - entity: "session"
    allowed_transitions:
      - {from: "scheduled", to: "in_progress", by_command: "cmd.session.checkin"}
      - {from: "in_progress", to: "done", by_command: "cmd.session.done"}
```

---

## Slot: Event Emission Contract（イベント契約）【必須】

Integration Spec の `event_catalog.required_fields` を満たすこと。

```yaml
event_contract:
  - event: "event.booking.confirmed"
    required_fields: ["timestamp", "booking_id", "slot_id"]
    produced_by_commands: ["cmd.booking.confirm"]
  - event: "event.session.done"
    required_fields: ["timestamp", "session_id", "trainer_id"]
    produced_by_commands: ["cmd.session.done"]
```

---

## Slot: Observability & Audit（観測・監査）【必須】

Decision6 の Metric を “計測可能” にするログ/イベントを保証する。

```yaml
observability:
  correlation:
    - "trace_id"
    - "flow_id"
    - "booking_id"
    - "session_id"
  logging_rules:
    - "eventを必ず永続化（append-only推奨）"
    - "PIIをログに入れない"
  metric_support:
    - metric: "<M-xxx>"
      depends_on_events: ["<event.aaa>", "<event.bbb>"]
```

---

## Slot: Error Model（エラー規約）【推奨】

```yaml
errors:
  - code: "CONFLICT_SLOT_UNAVAILABLE"
    when: "slot競合"
    maps_to_event: "event.booking.conflict"
  - code: "TIMEOUT_PENDING"
    when: "確定前タイムアウト"
    maps_to_event: "event.booking.timeout"
```

---

## Slot: References（参照）【必須】

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
  - id: "ref.db"
    kind: "ideamark_doc"
    title: "Detail DB Spec"
    locator: "<db-doc-uri>"
  - id: "ref.infra"
    kind: "ideamark_doc"
    title: "Detail Infra Spec"
    locator: "<infra-doc-uri>"
```

---

# Renderings (Optional)

任意で OpenAPI / Mermaid / シーケンス図等を置けるが、正は上の意味構造。

```yaml
renderings:
  - id: "render.openapi.v1"
    type: "openapi"
    generated_from: "<api_spec_id>@<hash>"
```
