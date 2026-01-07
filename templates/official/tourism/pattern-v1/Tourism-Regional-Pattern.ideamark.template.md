---
ideamark_version: 1
template_id: "imtpl.pattern.tourism"
template_name: "Tourism Regional Pattern Template"
template_version: "1.0.0"
description: "観光地の需要変動・保全制約・運営体制を整理し、施策やサービスの設計に接続するテンプレート。"
domain: ["tourism", "regional-innovation"]
tags: ["pattern", "tourism", "visitor-flow", "problem-solution"]
lang: "ja-JP"
status: draft
created_at: "2026-01-08"
---

# Tourism Regional Pattern Template

本テンプレートは、観光領域の地域課題を「文脈・課題・解決・スケール条件」で整理し、
運営・政策・サービス設計へつなげるための最小構造を提供する。

---

## Template Scope

### Suitable for
- 観光需要の季節変動や混雑の課題整理
- 観光資源の保全と利用のバランス設計
- 事業化や運営改善の前段整理

### Not responsible for
- UI/UXやAPIの詳細設計
- 施設詳細設計や施工計画
- 精緻な収支計画

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

## Visitor & Demand Profile
```yaml
visitor_profile:
  primary_segments: ["<主要な来訪者層>"]
  seasonality: "<季節/イベント/ピーク>"
  arrival_modes: ["<交通手段>"]
```
- 需要の偏りや到達性を把握する

---

## Assets & Capacity
```yaml
assets_capacity:
  attractions: ["<主要観光資源>"]
  capacity_constraints: ["<収容/輸送/環境上の制約>"]
  conservation_constraints: ["<保全/規制>"]
```
- 受け入れ可能量と保全制約を明示する

---

## Operations & Governance
```yaml
operations:
  operators: ["<運営主体>"]
  coordination_gaps: ["<連携の課題>"]
  data_sources: ["<来訪/交通/環境データ>"]
```
- 運営主体とデータ基盤の有無を整理する

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
- 混雑緩和/満足度/保全への効果測定に利用
