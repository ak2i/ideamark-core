---
ideamark_version: 1
template_id: "imtpl.pattern.fisheries"
template_name: "Fisheries Regional Pattern Template"
template_version: "1.0.0"
description: "水産業の供給・流通・収益構造を整理し、事業化やDX設計へ接続するテンプレート。"
domain: ["fisheries", "regional-innovation"]
tags: ["pattern", "fisheries", "value-chain", "problem-solution"]
lang: "ja-JP"
status: draft
created_at: "2026-01-08"
---

# Fisheries Regional Pattern Template

本テンプレートは、水産業の地域課題を「文脈・課題・解決・スケール条件」で整理し、
流通・販売・運用設計へつなげるための最小構造を提供する。

---

## Template Scope

### Suitable for
- 漁業収益の改善や販路転換の課題整理
- 漁協/自治体/流通事業者の連携整理
- 事業化や運用改善の前段整理

### Not responsible for
- UI/UXやAPIの詳細設計
- 冷凍/輸送設備の詳細設計
- 精緻な価格・収益シミュレーション

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

## Catch & Supply Profile
```yaml
catch_profile:
  target_species: ["<対象魚種>"]
  seasonality: "<漁期/旬>"
  landing_sites: ["<主要漁港>"]
```
- 魚種/漁期/拠点を明示する

---

## Cold Chain & Distribution
```yaml
distribution:
  storage_requirements: "<鮮度/温度条件>"
  channels: ["<卸/直販/EC>"]
  bottlenecks: ["<物流/在庫/品質課題>"]
```
- 供給・流通の制約を可視化する

---

## Stakeholders & Governance
```yaml
stakeholders:
  - name: "<主体>"
    role: "<役割>"
coop_structure: "<漁協/自治体/民間連携>"
```
- 合意形成の構造を明示する

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
- 収益/稼働率/廃棄率などを評価軸に置く
