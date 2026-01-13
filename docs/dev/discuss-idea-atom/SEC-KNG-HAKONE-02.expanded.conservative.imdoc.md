---
ideamark_version: 1
doc_id: "imdoc.breakdown.sec-kng-hakone-02"
parent_doc: "imdoc.sample.policy_compare.fhi-5cases"
section_id: "SEC-KNG-HAKONE-02"
generated_by: "breakdown-sim"
created_at: "2026-01-11"
---

# Breakdown: SEC-KNG-HAKONE-02

section_id: "SEC-KNG-HAKONE-02"
anchorage: ["place:hakone", "measures", "pattern-mapping"]
entities:
  - id: "IE-KNG-HAKONE-MEAS-01"
    kind: "measure"
    atomic_state: true
    content: "（PAT-03）受け皿整備：シャトル運行・駐車運用・交通案内を統合し、ボトルネックを“交通×受け皿”で緩和する。"
  - id: "IE-KNG-HAKONE-MEAS-02"
    kind: "measure"
    atomic_state: true
    content: "（PAT-01）行動規範＋サイン：混雑期の推奨行動（分散ルート/公共交通優先）を短い規範とサインで実装する。"
  - id: "IE-KNG-HAKONE-MEAS-03"
    kind: "measure"
    atomic_state: true
    content: "（PAT-02）Timed Entry（限定）：施設や駐車場など“単一ゲート”に近い地点で予約配分を試行し、公平性ルールとセットで設計する。"
relations:
  - type: "derives_from"
    from: "IE-KNG-HAKONE-MEAS-01"
    to: "IE-UK-LD-TRANS-01"
  - type: "derives_from"
    from: "IE-KNG-HAKONE-MEAS-03"
    to: "IE-US-TE-01"

---

# 14. 地点別：伊豆（自然資源・分散回遊・保全財源）



---
# Expansion (conservative): SEC-KNG-HAKONE-02
mode: "conservative"

## Section: 箱根の介入候補（拡張：slot-based）
section_id: "SEC-KNG-HAKONE-02"
anchorage: ["place:hakone", "measures", "conservative-expansion", "slots"]

entities:
  - id: "IE-KNG-HAKONE-SHUT-SLOT-01"
    kind: "projection"
    atomic_state: true
    content: "Shuttle: 路線・頻度スロット"
  - id: "IE-KNG-HAKONE-SHUT-SLOT-02"
    kind: "projection"
    atomic_state: true
    content: "Parking: 立地・容量・価格スロット"
  - id: "IE-KNG-HAKONE-TE-SLOT-01"
    kind: "projection"
    atomic_state: true
    content: "Timed Entry: 対象施設・公平性スロット"
