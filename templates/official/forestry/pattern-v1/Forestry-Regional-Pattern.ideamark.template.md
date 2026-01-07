---
ideamark_version: 1
template_id: "imtpl.pattern.forestry"
template_name: "Forestry Regional Pattern Template"
template_version: "1.0.0"
description: "森林資源・カーボン・保全の価値連鎖を整理し、事業化や合意形成へ接続するテンプレート。"
domain: ["forestry", "regional-innovation"]
tags: ["pattern", "forestry", "carbon", "problem-solution"]
lang: "ja-JP"
status: draft
created_at: "2026-01-08"
---

# Forestry Regional Pattern Template

本テンプレートは、林業・森林資源の地域課題を「文脈・課題・解決・スケール条件」で整理し、
保全/活用の設計へつなげるための最小構造を提供する。

---

## Template Scope

### Suitable for
- 森林資源の活用と保全の両立に関する課題整理
- カーボン市場や環境価値の事業化整理
- 長期運用や合意形成の前段整理

### Not responsible for
- 施業計画や測量の詳細設計
- 精緻な経済シミュレーション
- 認証/法令の詳細解釈

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

## Forest Assets & Ecology
```yaml
forest_assets:
  forest_type: "<人工林/天然林など>"
  age_structure: "<樹齢/更新状況>"
  biodiversity_risks: ["<生態系リスク>"]
```
- 資源の状態を明示する

---

## Carbon & Monitoring
```yaml
carbon_plan:
  measurement_method: "<測定/推計方法>"
  data_sources: ["<衛星/現地調査/台帳>"]
  certification_needs: ["<認証/基準>"]
```
- カーボン価値化の前提を整理する

---

## Governance & Revenue
```yaml
governance:
  owners: ["<所有者/権利者>"]
  operators: ["<施業主体>"]
  revenue_model: "<収益モデル>"
```
- 合意形成と収益分配の構造を置く

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
- CO2削減や保全効果の評価に使う
