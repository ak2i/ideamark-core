---
ideamark_version: 1
template_id: "imtpl.detail.db"
template_name: "Detail DB Template"
template_version: "1.0.0"
description: "WorkCell Integration Spec / Service Flow / Decision6 を入力として、DBの論理構造・制約・権限・監査/観測を定義するテンプレート。正は上流（Integration/Flow/Decision6）であり、本テンプレは実装可能なDB仕様へ落とす。"
domain: ["software-design", "database", "workcell"]
tags: ["detail", "db", "spec", "schema", "rls", "traceability"]
lang: "ja-JP"
status: stable
created_at: "2026-01-09"
---

# Detail DB Template

本テンプレートは、WorkCellのDB仕様を **「フロー・統合仕様・意思決定」から導出**するためのもの。  
API/Infra の前提にもなるが、特に **状態整合・権限・監査性** をDBに埋め込むことを目的とする。

- **正（source of truth）**：Integration Spec / Service Flow / Decision6
- **本テンプレの役割**：上流で固定された語彙・状態遷移を、実装可能なDB仕様に落とす

---

## 0. Provenance（参照元の明確化）【必須】

このDB仕様が **どの版・どのファイル**に基づくかを機械可読で記録する。

```yaml
provenance:
  db_spec_id: "<stable id, e.g. db.relatea.v1>"
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

## 1. DB Context（前提）【必須】

```yaml
db_context:
  purpose:
    - "state と event を永続化する"
    - "API と UI の整合性を担保する"
  storage_model:
    - "relational"
  security_baseline:
    - "RLS を基本とする"
    - "PII は分離する"
```

---

## 2. Canonical Entities（共通語彙）【必須】

Integration Spec の `canonical_entities` をDB資源として確定する。

```yaml
entities:
  - name: "booking"
    id_field: "booking_id"
    description: "予約"
```

---

## 3. Logical Schema（論理スキーマ）【必須】

```yaml
schema:
  tables:
    - name: "booking"
      pk: "booking_id"
      columns: ["client_id", "status", "created_at"]
      indexes: ["client_id", "status"]
```

---

## 4. Constraints & Policies（制約・権限）【必須】

```yaml
constraints:
  - "status は state_model の状態のみを許可"
policies:
  - entity: "booking"
    rule: "owner-only"
    description: "本人のみ閲覧・更新可能"
```

---

## 5. State Alignment（状態整合）【必須】

```yaml
state_alignment:
  - entity: "booking"
    allowed_states: ["draft", "pending", "confirmed", "done", "canceled"]
    transition_guard:
      - "confirmed -> done は event.session.done でのみ許可"
```

---

## 6. Observability & Audit（観測・監査）【必須】

```yaml
observability:
  audit_tables:
    - "event_log"
  logging_rules:
    - "state 変更は必ず event_log に記録"
    - "PII を event_log に入れない"
```

---

## 7. Migration & Change Policy（変更規約）【推奨】

```yaml
migration_policy:
  - "breaking change は version を上げる"
  - "既存データの移行手順を明記する"
```

---

## 8. References（参照）【必須】

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

任意で ER 図 / DDL / Mermaid 等を置けるが、正は上の意味構造。

```yaml
renderings:
  - id: "render.db.erd.v1"
    type: "mermaid.er"
    generated_from: "<db_spec_id>@<hash>"
```
