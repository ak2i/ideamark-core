---
ideamark_version: 1
doc_id: "imdoc.breakdown.sec-kng-decide-01"
parent_doc: "imdoc.sample.policy_compare.fhi-5cases"
section_id: "SEC-KNG-DECIDE-01"
generated_by: "breakdown-sim"
created_at: "2026-01-11"
---

# Breakdown: SEC-KNG-DECIDE-01

section_id: "SEC-KNG-DECIDE-01"
anchorage: ["decision", "governance", "pilot"]
entities:
  - id: "IE-DEC-01"
    kind: "decision_candidate"
    atomic_state: true
    content: "重点地域制度：交流圏を“重点地域（地点）”に分割し、介入（ルール/交通/財源/協議）を段階導入する。"
  - id: "IE-DEC-02"
    kind: "decision_candidate"
    atomic_state: true
    content: "富士山Timed Entry Pilot：期間・地点限定で予約配分を試行し、KPI（混雑・安全・資源影響・公平性）で評価する。"
  - id: "IE-DEC-03"
    kind: "decision_candidate"
    atomic_state: true
    content: "共通行動規範の制定：交流圏共通の短い行動規範を策定し、サイン・Web・案内所で統一実装する。"
  - id: "IE-DEC-04"
    kind: "decision_candidate"
    atomic_state: true
    content: "憲章＋協議プロセス：重点地域ごとにビジョン/目標/取組（憲章相当）と利用基準を策定し、公衆協議を制度化する。"
  - id: "IE-DEC-05"
    kind: "decision_candidate"
    atomic_state: true
    content: "維持管理財源ループ：保全・サイン更新・防災訓練等の継続財源を基金等で確保し、損耗指標と公開報告で運用する。"
relations:
  - type: "derives_from"
    from: "IE-DEC-02"
    to: "IE-KNG-FUJI-MEAS-01"
  - type: "derives_from"
    from: "IE-DEC-03"
    to: "IE-UK-CC-01"
  - type: "derives_from"
    from: "IE-DEC-04"
    to: "IE-EU-FR-CHARTER-01"
  - type: "derives_from"
    from: "IE-DEC-05"
    to: "IE-PAT-04"

## 15.2 Section: Projection（UI/運用へ投影する項目）（anchorage: projection）



---
# Convergent Expansion: SEC-KNG-DECIDE-01
mode: "convergent"

## Section: 意思決定パッケージ（富士山）
section_id: "SEC-KNG-DECIDE-01"
anchorage: ["decision", "convergent", "fuji"]

entities:
  - id: "IE-DEC-FUJI-01"
    kind: "decision_package"
    atomic_state: true
    content: "富士山重点地域パッケージ：Timed Entry Pilot + 行動規範 + 受け皿交通 + KPIレビュー"

  - id: "IE-DEC-FUJI-CRIT-01"
    kind: "metric"
    atomic_state: true
    content: "採否基準：ピーク混雑30%低減、安全事故減少、資源影響の悪化停止、著しい不公平の不発生"

  - id: "IE-DEC-FUJI-ROAD-01"
    kind: "mechanism"
    atomic_state: true
    content: "ロードマップ：①設計（1年）→②Pilot（1-2年）→③評価→④拡張/修正"

  - id: "IE-DEC-FUJI-RISK-01"
    kind: "risk"
    atomic_state: true
    content: "主リスク：公平性批判・現場運用負荷・関係自治体間調整"

relations:
  - type: "derives_from"
    from: "IE-DEC-FUJI-01"
    to: "IE-KNG-FUJI-MEAS-01"
  - type: "informed_by"
    from: "IE-DEC-FUJI-01"
    to: "IE-KNG-FUJI-PROB-01"
