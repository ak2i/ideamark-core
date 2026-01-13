
---
ideamark_version: 1
doc_id: "imdoc.viewpoint.kanagawa_officer.fuji"
created_at: "2026-01-11"
---

# Viewpoint Experiment: 神奈川県担当者（富士山）

## A. 主体的視野で見えている「事実」
section_id: "SEC-VP-KNG-SUBJ"
anchorage: ["viewpoint:kanagawa", "subjective"]

entities:
  - id: IE-KNG-SUBJ-01
    kind: fact_subjective
    atomic_state: true
    content: "複数県・市町村・関係省庁の調整が最大のボトルネックである。"
  - id: IE-KNG-SUBJ-02
    kind: fact_subjective
    atomic_state: true
    content: "県民・観光事業者への説明責任を果たせるかが制度導入の可否を左右する。"
  - id: IE-KNG-SUBJ-03
    kind: fact_subjective
    atomic_state: true
    content: "強い規制は反発を招き、政治的に実行困難になりやすい。"

## B. 客観的視野から見た「事実」
section_id: "SEC-VP-KNG-OBJ"
anchorage: ["viewpoint:kanagawa", "objective"]

entities:
  - id: IE-KNG-OBJ-01
    kind: fact_objective
    atomic_state: true
    content: "調整コストは初期に集中するが、制度化後は運用コストが低減する傾向がある。"
  - id: IE-KNG-OBJ-02
    kind: fact_objective
    atomic_state: true
    content: "明確なKPIとレビュー設計があれば、説明責任は制度的に補強できる。"

## C. ズレ
section_id: "SEC-VP-KNG-GAP"
anchorage: ["gap"]

entities:
  - id: IE-KNG-GAP-01
    kind: gap
    atomic_state: true
    content: "『調整が大変＝実行不可能』と『制度化すれば持続可能』のズレ。"
