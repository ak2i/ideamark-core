---
ideamark_version: 1
doc_id: "imdoc.sample.policy_compare.fhi-4cases"
title: "富士箱根伊豆交流圏構想（神奈川含む）改善点抽出のための比較IdeaMarkサンプル（英国・神奈川・豪州・米国）"
lang: "ja-JP"
status: "draft-sample"
created_at: "2026-01-11"
source_policy_target: "神奈川県を含む富士箱根伊豆交流圏構想（kousou3.pdf）"
purpose: "神奈川の既存設計（広域連携構想）の改善点を見出すため、類似の課題（観光圧・聖地/自然資源の保全・安全/防災・交通/サイン）に関する国外事例（英国・豪州・米国）と比較できる形で情報を整理する。"
assumptions:
  - "IdeaMarkの書式はサンプル。実装の最終スキーマではない。"
  - "外部事例は“制度の断片”を抽出した比較サンプルであり、網羅的な現地調査ではない。"
sources:
  kanagawa_pdf: "/mnt/data/kousou3.pdf"
  australia_pdf: "/mnt/data/2015-8-1.9.pdf"
  us_web_examples:
    - "DOI: Overcrowding in Parks"
    - "NPS: Timed Entry Tickets (例：Arches)"
    - "National Geographic: National park reservations overview"
  uk_web_examples:
    - "GOV.UK: The Countryside Code"
    - "Lake District National Park: Impacts of tourism"
    - "Regenerative Tourism in UK National Parks (nationalparks.uk)"
---

# 0. 読み方（このサンプルの狙い）
この文書は **「神奈川（富士箱根伊豆交流圏構想）」を主語**にして、海外事例を *参照（reference）* として比較します。

- **Anchorage（固定）**：各Sectionは「どの観点で読むか」を *Sectionの属性* として明示し、読者（人間/AI）の解釈の自由度を制御します。
- **Relay（継起）**：Section間のつながりは、**関係（relation）** と **Occurrence（出現）** で作ります（例：同じ課題が別制度でどう処理されるか、など）。

---

# 1. ドキュメント・スコープ（Meta / View）
## 1.1 View（この文書が提供する“見え”）
view:
  focus: "policy-design.compare"
  phase: ["problem-framing", "solution-benchmarking", "improvement-hypothesis"]
  audience: ["policy-planner", "analyst", "researcher", "ai-assistant"]
  output_intent:
    - "神奈川の既存設計を、国外の“管理メカニズム”と突き合わせて改善仮説を列挙する"
    - "IdeaEntity（＝意味の最小単位の“候補”）を再利用しやすい粒度で刻む"

## 1.2 結論の前提（比較のバイアス）
- 本文書は「神奈川を改善する」ための比較なので、国外事例は **良い/悪い** でなく **機能（function）** と **トレードオフ** を抽出する。
- 観光・保全・安全・交通の“正解”は一つではない（価値の競合がある）。

---

# 2. 共通語彙（このサンプルで使う最小セット）
> ※ここでは “用語の実装” ではなく “比較に使う語彙” を列挙します。  
> ※IdeaAtomという呼称は避け、**atomic（原子的）なIdeaEntity** として扱います。

- **IdeaEntity**: 人間/AIが文脈を当てることで意味を取り出せる最小単位（atomicとして扱うかは状態）
- **Section**: “読む観点（anchorage）” を宣言し、IdeaEntityを並べ、関係（relay）を張る容器
- **Occurrence**: Section内でのIdeaEntityの“出現”に対する補助属性（role/weight/noteなど）
- **Relation**: IdeaEntity同士、Section同士の意味的結合（supports/contrasts/derives_fromなど）

relation_vocab (sample):
  - supports
  - contrasts
  - refines
  - generalizes
  - operationalizes
  - risks
  - mitigates
  - requires
  - enables
  - measures
  - governance_of
  - is_example_of
  - derives_from
  - suggests

role_vocab (sample):
  - problem
  - context
  - constraint
  - stakeholder
  - asset
  - policy_goal
  - measure
  - mechanism
  - metric
  - risk
  - tradeoff
  - lesson
  - improvement_hypothesis

---

# 3. ケースA：神奈川（富士箱根伊豆交流圏構想）— “現状設計（ベースライン）”
## 3.1 Section: 構想の目的・範囲・ガバナンス（anchorage: governance）
section_id: "SEC-KNG-01"
anchorage: ["governance", "scope", "timebox"]
entities:
  - id: "IE-KNG-OBJ-01"
    kind: "statement"
    atomic_state: true
    content: "富士箱根伊豆交流圏の広域的行政課題に対し、山梨・静岡・神奈川の三県が、市町村・関係団体と連携し、役割分担のもと活性化を図る。"
    source_hint: "kousou3.pdf p2（要旨）"
  - id: "IE-KNG-PERIOD-01"
    kind: "constraint"
    atomic_state: true
    content: "構想期間：平成21年度〜平成30年度"
    source_hint: "kousou3.pdf p2"
  - id: "IE-KNG-GOV-01"
    kind: "mechanism"
    atomic_state: true
    content: "推進体制：三県サミットを核に、市町村・関係団体と連携・協力し、役割分担して推進する。"
    source_hint: "kousou3.pdf p2"
  - id: "IE-KNG-MON-01"
    kind: "mechanism"
    atomic_state: true
    content: "進行管理：毎年進捗把握、策定後5年で見直し検討。"
    source_hint: "kousou3.pdf p2"
occurrences:
  - entity: "IE-KNG-OBJ-01"
    role: "policy_goal"
  - entity: "IE-KNG-GOV-01"
    role: "mechanism"
  - entity: "IE-KNG-MON-01"
    role: "mechanism"
relations:
  - type: "requires"
    from: "IE-KNG-OBJ-01"
    to: "IE-KNG-GOV-01"
    note: "広域連携＝多主体調整が必須"
  - type: "measures"
    from: "IE-KNG-MON-01"
    to: "IE-KNG-OBJ-01"
    note: "レビュー周期が目的実現の自己修正能力に直結"

## 3.2 Section: 課題の背景（anchorage: problem-framing）
section_id: "SEC-KNG-02"
anchorage: ["problem-framing", "macro-trend"]
entities:
  - id: "IE-KNG-BG-POP-01"
    kind: "context"
    atomic_state: true
    content: "交流圏では人口減少・少子高齢化が進み、地域活力低下が懸念される。"
    source_hint: "kousou3.pdf p1（要旨）"
  - id: "IE-KNG-BG-RISK-01"
    kind: "problem"
    atomic_state: true
    content: "東海地震・火山・県境河川など、防災上の広域課題がある（不法投棄など環境課題も含む）。"
    source_hint: "kousou3.pdf p1"
  - id: "IE-KNG-BG-INFRA-01"
    kind: "context"
    atomic_state: true
    content: "空港・道路など基盤整備が進展し、広域交流のポテンシャルが増している。"
    source_hint: "kousou3.pdf p1/p13（要旨）"
occurrences:
  - entity: "IE-KNG-BG-RISK-01"
    role: "problem"
  - entity: "IE-KNG-BG-POP-01"
    role: "context"
  - entity: "IE-KNG-BG-INFRA-01"
    role: "context"

## 3.3 Section: 施策パッケージ（観光振興）（anchorage: measures）
section_id: "SEC-KNG-03"
anchorage: ["tourism", "measures", "visitor-experience"]
detail_docs:
  - uri: "./detail/kng-tourism-packages.ideamark.md"
    relation: "elaborates"
    covers: ["IE-KNG-TOUR-ROUTE-01", "IE-KNG-TOUR-SIGN-01"]
    summary: "周遊モデルコースとサイン整備の詳細設計"
entities:
  - id: "IE-KNG-TOUR-ROUTE-01"
    kind: "measure"
    atomic_state: true
    content: "新たな周遊モデルコースの開発・商品化支援（テーマ型観光：温泉・食・癒し・産業観光等）"
    source_hint: "kousou3.pdf p17"
  - id: "IE-KNG-TOUR-PROMO-01"
    kind: "measure"
    atomic_state: true
    content: "三県共同観光プロモーション（ターゲット地域を絞り合同プロモーション）"
    source_hint: "kousou3.pdf p17"
  - id: "IE-KNG-TOUR-LONGSTAY-01"
    kind: "measure"
    atomic_state: true
    content: "長期滞在推進（2泊3日以上の滞在型プログラム開発：体験・交流・学習・食等）"
    source_hint: "kousou3.pdf p17"
  - id: "IE-KNG-TOUR-INBOUND-01"
    kind: "measure"
    atomic_state: true
    content: "外国人観光客誘致：観光ルート設定、海外観光展・商談会、案内施設の受入体制整備"
    source_hint: "kousou3.pdf p17"
  - id: "IE-KNG-TOUR-SIGN-01"
    kind: "measure"
    atomic_state: true
    content: "公共サイン整備（案内標識の連続性・統一性、多言語化、ピクト活用、広域観光地図作成等）"
    source_hint: "kousou3.pdf p18"
    detail_doc:
      uri: "./detail/kng-signage-guide.ideamark.md"
      relation: "elaborates"
      summary: "サイン統一ルールと多言語化のガイド"
occurrences:
  - entity: "IE-KNG-TOUR-ROUTE-01"
    role: "measure"
  - entity: "IE-KNG-TOUR-SIGN-01"
    role: "mechanism"
relations:
  - type: "operationalizes"
    from: "IE-KNG-TOUR-PROMO-01"
    to: "IE-KNG-OBJ-01"
  - type: "enables"
    from: "IE-KNG-TOUR-SIGN-01"
    to: "IE-KNG-TOUR-LONGSTAY-01"
    note: "回遊/滞在UXの土台"

## 3.4 Section: 施策パッケージ（防災）（anchorage: safety）
section_id: "SEC-KNG-04"
anchorage: ["safety", "disaster", "measures"]
entities:
  - id: "IE-KNG-DS-VOLC-01"
    kind: "measure"
    atomic_state: true
    content: "富士山火山防災：相互応援体制を円滑に運用するためのマニュアル整備等"
    source_hint: "kousou3.pdf p19"
  - id: "IE-KNG-DS-DRILL-01"
    kind: "measure"
    atomic_state: true
    content: "合同防災訓練（富士山噴火・地震等を想定し、関係機関との連携強化）"
    source_hint: "kousou3.pdf p19"
  - id: "IE-KNG-DS-EVAC-01"
    kind: "measure"
    atomic_state: true
    content: "緊急輸送道路ネットワーク整備（代替性確保）"
    source_hint: "kousou3.pdf p19"
  - id: "IE-KNG-DS-RIVER-01"
    kind: "mechanism"
    atomic_state: true
    content: "県境河川の防災：水防情報共有、雨量・水位データ共有、増水注意喚起"
    source_hint: "kousou3.pdf p20"
relations:
  - type: "mitigates"
    from: "IE-KNG-DS-DRILL-01"
    to: "IE-KNG-BG-RISK-01"

---

# 4. ケースB：英国（自然地域の利用圧と“行動規範＋受け皿整備”）
## 4.1 Section: 行動規範（Countryside Code）（anchorage: visitor-behavior）
section_id: "SEC-UK-01"
anchorage: ["visitor-behavior", "norms", "anchorage"]
entities:
  - id: "IE-UK-CC-01"
    kind: "mechanism"
    atomic_state: true
    content: "The Countryside Code：訪問者向けに行動規範を提示し、自然・地域住民・他者への配慮を促す。"
    source_hint: "GOV.UK"
  - id: "IE-UK-CC-02"
    kind: "lesson"
    atomic_state: true
    content: "権利（楽しむ）と責任（保護する）をセットで提示することで、分散した管理主体でも“最低限の共通ルール”が成立しやすい。"
    source_hint: "GOV.UK / Lake District NP"
occurrences:
  - entity: "IE-UK-CC-01"
    role: "mechanism"
  - entity: "IE-UK-CC-02"
    role: "lesson"

## 4.2 Section: 観光圧（Lake District等）と受け皿（anchorage: capacity-management）
section_id: "SEC-UK-02"
anchorage: ["capacity-management", "transport", "erosion"]
entities:
  - id: "IE-UK-LD-OVR-01"
    kind: "problem"
    atomic_state: true
    content: "大量の訪問者が経済効果と同時に交通混雑・環境負荷などの課題を生む。"
    source_hint: "Lake District NP"
  - id: "IE-UK-LD-TRANS-01"
    kind: "measure"
    atomic_state: true
    content: "局所ボトルネックに対してシャトル運行・駐車運用など“交通×受け皿”で緩和する。"
    source_hint: "Lake District visitor management measures"
  - id: "IE-UK-PATH-01"
    kind: "measure"
    atomic_state: true
    content: "歩道侵食への長期補修・資金調達（調査→修復→資金ループ）。"
    source_hint: "National Trust / Fix the Fells 等"
  - id: "IE-UK-REG-TOUR-01"
    kind: "policy_goal"
    atomic_state: true
    content: "Regenerative tourism：負の影響最小化に留まらず“純増の好影響（ネットポジティブ）”を目指す。"
    source_hint: "nationalparks.uk"
relations:
  - type: "refines"
    from: "IE-UK-REG-TOUR-01"
    to: "IE-KNG-OBJ-01"
    note: "“活性化”の定義をネットポジティブへ拡張可能"

---

# 5. ケースC：豪州（聖地ウルル：文化・観光・統治の三角形）
## 5.1 Section: 聖地管理とツーリズムのジレンマ（anchorage: sacredness）
section_id: "SEC-AUS-01"
anchorage: ["sacredness", "stakeholder-conflict", "governance"]
entities:
  - id: "IE-AUS-ULU-STAKE-01"
    kind: "stakeholder"
    atomic_state: true
    content: "ステークホルダー：先住民（アナング）／政府／ツーリスト"
    source_hint: "2015-8-1.9.pdf（要旨）"
  - id: "IE-AUS-ULU-CONF-01"
    kind: "problem"
    atomic_state: true
    content: "ウルルは先住民にとって神話的意味世界の中心である一方、観光資源として高い価値を持つため相剋が生じる。"
    source_hint: "2015-8-1.9.pdf（要旨）"
  - id: "IE-AUS-ULU-MECH-01"
    kind: "mechanism"
    atomic_state: true
    content: "登山（climb）の是非・制限をめぐる“場所のポリティクス”は、文化の真正性・政府努力・ツーリスト満足を担保する装置として機能しうる。"
    source_hint: "2015-8-1.9.pdf（要旨）"
relations:
  - type: "contrasts"
    from: "IE-AUS-ULU-MECH-01"
    to: "IE-KNG-TOUR-PROMO-01"
    note: "誘致・促進だけでなく“制限を含む管理装置”が正当性を支える場合がある"

---

# 6. ケースD：米国（国立公園：過密と“Timed Entry / Permit”）
## 6.1 Section: 過密への制度対応（anchorage: access-control）
section_id: "SEC-US-01"
anchorage: ["access-control", "capacity-management", "fairness"]
entities:
  - id: "IE-US-TE-01"
    kind: "mechanism"
    atomic_state: true
    content: "Timed entry / reservation：入園・入域を時間枠で配分し、混雑緩和・資源保護・待ち行列減少を狙う。"
    source_hint: "DOI / NPS"
  - id: "IE-US-TE-02"
    kind: "tradeoff"
    atomic_state: true
    content: "予約取得の難しさ・公平性（誰が枠を取れるか）など、新たな勝者/敗者を作りうる。"
    source_hint: "National Geographic"
  - id: "IE-US-TE-03"
    kind: "metric"
    atomic_state: true
    content: "効果指標：ゲート待ち、駐車場満車、ピーク集中、資源影響、満足度等。"
    source_hint: "DOI / NPS（一般化）"
relations:
  - type: "suggests"
    from: "IE-US-TE-01"
    to: "IE-KNG-TOUR-LONGSTAY-01"
    note: "“量を増やす”より“時間に分散させる”軸の導入"

---

# 7. 横断比較（Comparison Matrix）
## 7.1 Section: 同じ課題を“どの機能”で処理しているか（anchorage: functional-compare）
section_id: "SEC-CMP-01"
anchorage: ["compare", "functions", "relay"]
entities:
  - id: "IE-FUNC-01"
    kind: "concept"
    atomic_state: true
    content: "訪問者行動の制御（norm / code / signage）"
  - id: "IE-FUNC-02"
    kind: "concept"
    atomic_state: true
    content: "アクセス量の制御（予約・許可・枠配分）"
  - id: "IE-FUNC-03"
    kind: "concept"
    atomic_state: true
    content: "受け皿整備（交通・駐車・歩道・案内所）"
  - id: "IE-FUNC-04"
    kind: "concept"
    atomic_state: true
    content: "価値の競合解消（聖性・自然保護・経済・満足）"
  - id: "IE-FUNC-05"
    kind: "concept"
    atomic_state: true
    content: "モニタリングと適応（metrics → review）"
relations:
  - type: "is_example_of"
    from: "IE-UK-CC-01"
    to: "IE-FUNC-01"
  - type: "is_example_of"
    from: "IE-US-TE-01"
    to: "IE-FUNC-02"
  - type: "is_example_of"
    from: "IE-KNG-TOUR-SIGN-01"
    to: "IE-FUNC-03"
  - type: "is_example_of"
    from: "IE-AUS-ULU-MECH-01"
    to: "IE-FUNC-04"
  - type: "is_example_of"
    from: "IE-KNG-MON-01"
    to: "IE-FUNC-05"

---

# 8. 神奈川の改善仮説（国外事例→神奈川への“転写”）
## 8.1 Section: 改善点の抽出（anchorage: improvement）
section_id: "SEC-KNG-IMPROVE-01"
anchorage: ["improvement", "hypothesis", "actionable"]
entities:
  - id: "IE-IMP-01"
    kind: "improvement_hypothesis"
    atomic_state: true
    content: "（英国）行動規範の“共通テキスト”を交流圏のサイン/案内/サイトに統一実装し、権利と責任をセットで提示する（多主体でも最低限の共通運用が成立）。"
  - id: "IE-IMP-02"
    kind: "improvement_hypothesis"
    atomic_state: true
    content: "（米国）ピーク集中が顕著な地点について、期間限定・地点限定で timed-entry / shuttle-first 等“アクセス配分”を試行し、指標で効果検証する。"
  - id: "IE-IMP-03"
    kind: "improvement_hypothesis"
    atomic_state: true
    content: "（豪州）“価値の競合”を明示し、観光促進だけでなく“制限/禁忌/儀礼”を含む管理装置を議論できる枠組みを導入する（文化・景観・宗教性を保全対象として扱う）。"
  - id: "IE-IMP-04"
    kind: "improvement_hypothesis"
    atomic_state: true
    content: "（英国）歩道・景観・自然資源の損耗（侵食等）を“長期補修プログラム＋資金調達”として設計し、観光と保全の財源ループを作る。"
  - id: "IE-IMP-05"
    kind: "improvement_hypothesis"
    atomic_state: true
    content: "（神奈川既存）年次進捗把握/5年見直しを、観光・交通・安全・環境の共通KPI（混雑・満足・資源影響・事故/災害対応）と結びつけ、適応管理（adaptive management）化する。"
relations:
  - type: "derives_from"
    from: "IE-IMP-01"
    to: "IE-UK-CC-01"
  - type: "derives_from"
    from: "IE-IMP-02"
    to: "IE-US-TE-01"
  - type: "derives_from"
    from: "IE-IMP-03"
    to: "IE-AUS-ULU-MECH-01"
  - type: "derives_from"
    from: "IE-IMP-04"
    to: "IE-UK-PATH-01"
  - type: "operationalizes"
    from: "IE-IMP-05"
    to: "IE-KNG-MON-01"

---

# 9. 参考：再利用しやすい“パターン”としてのIdeaEntity束（Bundle）
## 9.1 Section: Pattern Catalog（anchorage: reusable-pattern）
section_id: "SEC-PATTERN-01"
anchorage: ["pattern", "reusable", "library"]
entities:
  - id: "IE-PAT-01"
    kind: "pattern"
    atomic_state: true
    content: "Normative Code + Signage：行動規範（短い原則）＋現場サイン（具体）＋違反時の影響説明"
    slots:
      must:
        - "principles (short)"
        - "do/don't examples"
        - "local exceptions"
        - "why it matters (resource/people)"
  - id: "IE-PAT-02"
    kind: "pattern"
    atomic_state: true
    content: "Timed Entry Pilot：地点限定の予約/枠配分→KPI評価→拡大/撤退"
    slots:
      must:
        - "scope (where/when)"
        - "capacity model"
        - "equity policy"
        - "metrics + review cadence"
  - id: "IE-PAT-03"
    kind: "pattern"
    atomic_state: true
    content: "Sacredness Governance：価値競合の明示→ステークホルダー合意→禁止/制限/代替体験の設計"
    slots:
      must:
        - "stakeholder map"
        - "protected values"
        - "restricted actions"
        - "alternative experiences"
  - id: "IE-PAT-04"
    kind: "pattern"
    atomic_state: true
    content: "Maintenance Funding Loop：損耗計測→補修計画→資金→実装→再計測"
    slots:
      must:
        - "asset inventory"
        - "damage/erosion indicators"
        - "funding mechanism"
        - "public reporting"

---

# 10. “1ドキュメント化”したときの全体構造（Index）
- **SEC-KNG-01..04**：神奈川（現状設計の核）
- **SEC-UK-01..02 / SEC-AUS-01 / SEC-US-01**：国外事例（比較用の参照レイヤ）
- **SEC-CMP-01**：機能比較のハブ（relay）
- **SEC-KNG-IMPROVE-01**：改善仮説（神奈川への転写）
- **SEC-PATTERN-01**：再利用ライブラリ（IdeaMark DB蓄積の単位候補）

---

# Appendix A. 外部参照（最小セット）
- UK:
  - GOV.UK: The Countryside Code
  - Lake District National Park: Impacts of tourism
  - Regenerative Tourism in UK National Parks (nationalparks.uk)
- US:
  - U.S. Department of the Interior: Overcrowding in Parks
  - U.S. National Park Service: Timed Entry Tickets（例：Arches）
  - National Geographic: national park reservations overview
