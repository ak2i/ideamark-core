---
ideamark_version: 1
doc_id: "imdoc.breakdown.sec-kng-fuji-01"
parent_doc: "imdoc.sample.policy_compare.fhi-5cases"
section_id: "SEC-KNG-FUJI-01"
generated_by: "breakdown-sim"
created_at: "2026-01-11"
---

# Breakdown: SEC-KNG-FUJI-01

section_id: "SEC-KNG-FUJI-01"
anchorage: ["place:fuji", "problem-framing"]
entities:
  - id: "IE-KNG-FUJI-PROB-01"
    kind: "problem"
    atomic_state: true
    content: "ピーク時に人流が集中し、交通・駐車・歩行動線・安全（救護/避難）がボトルネック化しやすい。"
  - id: "IE-KNG-FUJI-PROB-02"
    kind: "problem"
    atomic_state: true
    content: "景観・自然資源の損耗（侵食/ゴミ等）が発生しうる。"
  - id: "IE-KNG-FUJI-PROB-03"
    kind: "problem"
    atomic_state: true
    content: "文化・信仰・聖性の扱いが“体験価値”と“規範/制限”の設計に影響する可能性がある。"
relations:
  - type: "supports"
    from: "IE-KNG-BG-RISK-01"
    to: "IE-KNG-FUJI-PROB-01"
  - type: "generalizes"
    from: "IE-AUS-ULU-CONF-01"
    to: "IE-KNG-FUJI-PROB-03"

## 12.2 Section: 富士山の介入候補（anchorage: place.fuji.measures）



---
# Expansion (conservative): SEC-KNG-FUJI-01
mode: "conservative"

## Section: 富士山の課題仮説（拡張：slot-based）
section_id: "SEC-KNG-FUJI-01"
anchorage: ["place:fuji", "problem-framing", "conservative-expansion", "slots"]

entities:
  - id: "IE-KNG-FUJI-PROB-SLOT-01"
    kind: "projection"
    atomic_state: true
    content: "混雑発生源スロット（地点/時間帯/要因）"
  - id: "IE-KNG-FUJI-PROB-SLOT-02"
    kind: "projection"
    atomic_state: true
    content: "資源影響スロット（侵食/ゴミ/景観/生態）"
  - id: "IE-KNG-FUJI-PROB-SLOT-03"
    kind: "projection"
    atomic_state: true
    content: "安全リスクスロット（事故/救護/避難）"
  - id: "IE-KNG-FUJI-PROB-SLOT-04"
    kind: "projection"
    atomic_state: true
    content: "価値競合スロット（文化/信仰/観光/経済）"
  - id: "IE-KNG-FUJI-PROB-SLOT-05"
    kind: "projection"
    atomic_state: true
    content: "ステークホルダースロット（誰が影響を受けるか）"
  - id: "IE-KNG-FUJI-PROB-SLOT-06"
    kind: "projection"
    atomic_state: true
    content: "制度制約スロット（権限/法/財源/境界）"
