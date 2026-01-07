---
ideamark_version: 1
template_id: "imtpl.pattern.agriculture"
template_name: "Agriculture Regional Pattern Template"
template_version: "1.0.0"
description: "農業・農村の地域課題を、課題→解決の構造で整理し、実装へ接続するためのテンプレート。"
domain: ["agriculture", "regional-innovation"]
tags: ["pattern", "agri", "rural", "problem-solution"]
lang: "ja-JP"
status: draft
created_at: "2026-01-08"
---

# Agriculture Regional Pattern Template

本テンプレートは、農業分野の地域課題を「文脈・課題・解決・スケール条件」で整理し、
後続の要件設計や実装検討へ接続するための最小構造を提供する。

---

## Template Scope

### Suitable for
- 農業機械/労働力/物流などの地域課題整理
- 作物/季節性/地理条件が強く効く課題の整理
- 事業化や運用設計の前段整理

### Not responsible for
- UI/UXやAPIの詳細設計
- 物理設備設計や調達計画の詳細
- 精緻な経済シミュレーション

---

## Pattern Core (Required)
```yaml
id: "<IdeaMark-...>"
title: "<pattern title>"
type: "<pattern type>"
context:
  - "<背景/環境>"
problem:
  summary: "<解決したい課題>"
solution:
  approach: "<解決アプローチ>"
metadata:
  tags: []
  scalefactor:
    timewindow: "<導入/効果の時間軸>"
    spacemetrics: "<空間スケール>"
    regions: []
    organizations: []
access:
  uri: "<source or reference>"
  visibility: "public"
```

---

## Agricultural Context
```yaml
agri_context:
  crops_or_livestock: ["<主要作物/畜産>"]
  seasonality: "<季節性/収穫期>"
  terrain: "<地形/圃場条件>"
  climate_risks: ["<気象リスク>"]
```
- 作物/畜産、季節性、地形条件を明示する

---

## Operations & Resources
```yaml
operations:
  labor_structure: "<担い手/労働構成>"
  machinery: ["<主要機械/設備>"]
  logistics: "<出荷/集荷/輸送>"
  constraints: ["<燃料/人材/コスト制約>"]
```
- 現場運用でボトルネックになりやすい項目を置く

---

## Stakeholders & Value Chain
```yaml
stakeholders:
  - name: "<主体>"
    role: "<役割>"
value_chain:
  upstream: ["<資材/種苗/供給>"]
  downstream: ["<販売/加工/消費>"]
```
- 関係者の利害を明確にするための最小構造

---

## Impact & Metrics (Optional)
```yaml
impact:
  outcomes: ["<目標成果>"]
  metrics:
    - name: "<指標名>"
      definition: "<定義>"
      unit: "<単位>"
```
- 効果検証やPoC評価に使う
