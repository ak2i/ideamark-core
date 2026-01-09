---
ideamark_version: 1
template_id: "imtpl.detail.ui"
template_name: "Detail UI Template"
template_version: "1.0.0"
description: "WorkCell Integration Spec / Service Flow / Decision6 を入力として、UIの画面・操作・状態遷移・観測を定義するテンプレート。"
domain: ["software-design", "ui", "workcell"]
tags: ["detail", "ui", "spec", "traceability"]
lang: "ja-JP"
status: stable
created_at: "2026-01-09"
---

# Detail UI Template

本テンプレートは、WorkCellのUI仕様を **「フロー・統合仕様・意思決定」から導出**するためのもの。  
API/DB/Infra の前提にもなるが、特に **ユーザー操作と状態** をUIに埋め込むことを目的とする。

- **正（source of truth）**：Integration Spec / Service Flow / Decision6
- **本テンプレの役割**：上流で固定された語彙・状態遷移を、実装可能なUI仕様に落とす

---

## Slot: Provenance（参照元の明確化）【必須】

```yaml
provenance:
  ui_spec_id: "<stable id, e.g. ui.relatea.v1>"
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

## Slot: UI Context（前提）【必須】

```yaml
ui_context:
  target_platforms: ["web", "mobile"]
  audience:
    - "end-user"
    - "operator"
  navigation_model:
    - "single-page"
```

---

## Slot: Screens & States（画面・状態）【必須】

```yaml
screens:
  - id: "screen.sign_in"
    title: "サインイン"
    states: ["idle", "loading", "error", "success"]
  - id: "screen.dashboard"
    title: "ダッシュボード"
    states: ["loading", "ready"]
```

---

## Slot: User Actions（操作）【必須】

```yaml
actions:
  - id: "action.sign_in"
    screen: "screen.sign_in"
    trigger: "button.click"
    command: "cmd.auth.sign_in_password"
```

---

## Slot: State Transition Enforcement（状態遷移の強制）【必須】

```yaml
ui_state_rules:
  - screen: "screen.sign_in"
    allowed_transitions:
      - {from: "idle", to: "loading", by_action: "action.sign_in"}
      - {from: "loading", to: "success", by_event: "event.auth.session.established"}
```

---

## Slot: Observability & Audit（観測・監査）【必須】

```yaml
observability:
  ui_events:
    - "event.ui.sign_in.click"
  logging_rules:
    - "PII をイベントに入れない"
```

---

## Slot: Error & Recovery（エラーと回復）【推奨】

```yaml
errors:
  - code: "AUTH_INVALID_CREDENTIALS"
    display: "メールまたはパスワードが違います"
    recovery: "再入力"
```

---

## Slot: References（参照）【必須】

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
  - id: "render.ui.flow.v1"
    type: "mermaid.flowchart"
    generated_from: "<ui_spec_id>@<hash>"
```
