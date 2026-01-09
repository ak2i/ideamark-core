---
ideamark_version: 1
template_id: "imtpl.decision6.workcell"
template_name: "Decision6 WorkCell Template"
template_version: "1.0.0"
description: "意思決定の質にコミットするWorkCell向け、6要素ノードによる要件・設計・開発ループ定義テンプレート"
domain: ["software-development", "workcell", "decision-support"]
tags: ["decision6", "workcell", "requirements", "development-loop"]
lang: "ja-JP"
status: stable
created_at: "2026-01-06"
---

# Decision6 WorkCell Template

本テンプレートは、**システム開発・AI開発・業務改善**において、  
「何を作るか」ではなく **「どの判断を、どの根拠で行うか」** を中心に据えた  
**Decision-centric な WorkCell 定義**のためのテンプレートである。

---

## Template Scope

### This template is suitable for
- 小〜中規模のWorkCell設計
- MVP / PoC / 初期本番を跨ぐ開発
- AIを含む探索的・反復的な開発
- 意思決定の根拠と履歴を残したいケース
 - 問題整理〜解決整理〜再利用までの文脈を持つケース

### This template is NOT responsible for
- 詳細UI設計
- 物理DB設計
- API詳細仕様
- インフラ構成詳細

これらは **別テンプレートで定義し、本テンプレートから `ref` で参照する**。

---

## Node Types (Required)

本テンプレートでは、以下の **6要素ノード**を必須とする。

---

## Problem/Solution Context (Recommended)

IdeaMarkは **Problem と Solution の記録を再利用可能にする**ことが主目的である。  
そのため、各スロットが **Problem / Solution / 両方**のどれに属するか、  
そして **仮説 / 計画 / 実績**のどれに当たるかを明示することを推奨する。

### Context Tags
各スロットに以下の補助タグを追加できる（任意）。
```yaml
context:
  focus: "problem | solution | both"
  phase: "hypothesis | plan | outcome | other"
  origin: "new | observed | reused | retroactive"
```
- focus: 問題と解決のどちらに重心があるか
- phase: 記述の性質（仮説 / 計画 / 実績 / その他）
- origin: どういう文脈で作成されたか（新規 / 観測 / 再利用 / 事後整理）

---

## Slot: Intent
```yaml
type: intent
summary: "<このWorkCellで達成したい状態>"
stakeholders: []
constraints: []
non_goals: []
success_definition_ref: []
links: []
context:
  focus: "problem | solution | both"
  phase: "hypothesis | plan | outcome | other"
  origin: "new | observed | reused | retroactive"
```
**目的・意図・スコープ境界**を定義する。  
要件定義の代替であり、最上流の判断固定点。

---

## Slot: Hypothesis
```yaml
type: hypothesis
claim: "<この設計・構成がうまくいくという仮説>"
tags: []
falsifiable_by: []
links: []
context:
  focus: "problem | solution | both"
  phase: "hypothesis | plan | outcome | other"
  origin: "new | observed | reused | retroactive"
```
Intentを実現するための **成立仮説**。  
必ず **反証可能** な形で書く。

---

## Slot: DecisionOption
```yaml
type: decision_option
option: "<今回採用する設計・方針>"
pros: []
cons: []
prerequisites: []
links: []
context:
  focus: "problem | solution | both"
  phase: "hypothesis | plan | outcome | other"
  origin: "new | observed | reused | retroactive"
```
今回の開発・設計で **採用する選択肢** を明示する。  
「作らないこと」を含めるのが重要。

---

## Slot: Experiment
```yaml
type: experiment
purpose: "<このProductionで何を確かめるか>"
scope: []
out_of_scope: []
artifact: []
links: []
refs: []
context:
  focus: "problem | solution | both"
  phase: "hypothesis | plan | outcome | other"
  origin: "new | observed | reused | retroactive"
```
Experiment = Production。  
作ること自体ではなく、**判断材料を得るための生産**を定義する。

---

## Slot: Metric
```yaml
type: metric
name: "<計測指標名>"
definition: "<何を測るか>"
unit: "<単位>"
time_window: "<ISO 8601 duration or semantic window>"
collection:
  method: "<計測方法>"
refs: []
context:
  focus: "problem | solution | both"
  phase: "hypothesis | plan | outcome | other"
  origin: "new | observed | reused | retroactive"
```
意思決定の質を担保する **観測点**。  
結果指標よりも **近接指標** を優先する。

---

## Slot: DecisionLog
```yaml
type: decision_log
decision: "<今回の判断内容>"
why_now: "<なぜ今判断するのか>"
stop_rule_ref: []
evidence_refs: []
next_candidates: []
context:
  focus: "problem | solution | both"
  phase: "hypothesis | plan | outcome | other"
  origin: "new | observed | reused | retroactive"
```
進む／止める／変える、を正式な成果物として残す。  
失敗ではなく **学習の記録**。

---

## Linking Rules

- links は `{to, rel}` を基本構造とする
- 推奨 rel:
  - drives
  - has_option
  - implemented_as
  - tested_by
  - measured_by
  - leads_to
  - refines

---

## Reference Usage

- 詳細設計（UI / DB / API / Infra）は **別Ideamarkドキュメント** として作成
- 本テンプレートからは `refs` により参照のみ行う
- 判断の根拠となるデータは `refs` / `evidence_refs` に必ず紐づける

---

## Design Principle

- 正解を出さない
- 判断を代行しない
- しかし、判断から逃げない

Decision6 WorkCell Template は、  
**意思決定の質を高めるための最小構造**である。
