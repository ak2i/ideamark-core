---
ideamark_version: 1
doc_id: "imdoc.sample.policy_compare.fhi-5cases"
title: "富士箱根伊豆交流圏構想（神奈川含む）改善点抽出のための比較IdeaMarkサンプル（英国・神奈川・豪州・米国・欧州）"
lang: "ja-JP"
status: "draft-sample"
created_at: "2026-01-11"
source_policy_target: "神奈川県を含む富士箱根伊豆交流圏構想（kousou3.pdf）"
purpose: "神奈川の既存設計（広域連携構想）の改善点を見出すため、類似の課題（観光圧・文化/自然資源の保全・安全/防災・交通/サイン・ガバナンス/財源）に関する国外事例（英国・豪州・米国・欧州）と比較できる形で情報を整理する。"
assumptions:
  - "IdeaMarkの書式はサンプル。実装の最終スキーマではない。"
  - "外部事例は“管理メカニズム”の断片抽出であり、現地制度の完全な網羅ではない。"
sources:
  kanagawa_pdf: "/mnt/data/kousou3.pdf"
  australia_pdf: "/mnt/data/2015-8-1.9.pdf"
  europe_pdf_url: "https://www.env.go.jp/content/900492493.pdf"
  us_web_url: "https://natgeo.nikkeibp.co.jp/nng/feature/0610/index3.shtml"
  uk_web_examples:
    - "GOV.UK: The Countryside Code"
    - "Lake District National Park: Impacts of tourism"
    - "Regenerative Tourism in UK National Parks (nationalparks.uk)"
---

# 0. 文書の位置づけ
本ドキュメントは **神奈川（富士箱根伊豆交流圏構想）を改善する**ことを目的とした比較整理である。

- **主語（Target）**：神奈川の既存設計（現状の構想・施策群・運用設計）
- **参照（Benchmarks）**：英国・豪州・米国・欧州の「管理メカニズム（制度・運用・合意装置）」
- **成果物**：改善仮説（改善点のリスト）＋再利用可能なパターン束（pattern bundle）

> 記号論的には、SectionMeta が anchorage（読みの固定）、
> Occurrence/Relation が relay（意味の継起）を担う。

---

# 1. 共通語彙（このサンプルが使う最小セット）
- **IdeaEntity**：意味の最小単位の“候補”。atomic（原子的）かどうかは状態として扱う。
- **Section**：読む観点（anchorage）を宣言し、IdeaEntityを並べ、関係（relation）を張る容器。
- **Occurrence**：Section内でのIdeaEntityの“出現”に付与する属性（role/weight/note 等）。
- **Relation**：IdeaEntity同士の結合。意味を固定せず、比較のための接続点として使う。

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
  - is_example_of
  - derives_from
  - suggests
  - governance_of

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

# 2. ケースA：神奈川（富士箱根伊豆交流圏構想）— 現状設計（ベースライン）
## 2.1 Section: 目的・範囲・ガバナンス（anchorage: governance）
section_id: "SEC-KNG-01"
anchorage: ["governance", "scope", "timebox"]
detail_docs:
  - uri: "./detail/kng-governance-operating-model.ideamark.md"
    relation: "elaborates"
    covers: ["IE-KNG-GOV-01", "IE-KNG-MON-01"]
    summary: "推進体制と進行管理の運用モデル"
entities:
  - id: "IE-KNG-OBJ-01"
    kind: "policy_goal"
    atomic_state: true
    content: "三県（山梨・静岡・神奈川）が、市町村・関係団体等と協力しながら連携して取り組み、将来にわたり交流圏の活性化を図る。"
    source_hint: "kousou3.pdf p2（要旨）"
  - id: "IE-KNG-PERIOD-01"
    kind: "constraint"
    atomic_state: true
    content: "構想期間：平成21年度〜平成30年度"
    source_hint: "kousou3.pdf p2"
  - id: "IE-KNG-GOV-01"
    kind: "mechanism"
    atomic_state: true
    content: "推進体制：三県サミットを核に、市町村・関係団体と連携・協力し、役割分担のもと推進する。"
    source_hint: "kousou3.pdf p2"
    detail_doc:
      uri: "./detail/kng-summit-governance.ideamark.md"
      relation: "elaborates"
      summary: "三県サミットの意思決定フローと協議体設計"
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
    note: "レビュー設計が自己修正能力に直結"

## 2.2 Section: 背景（anchorage: problem-framing）
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
    content: "広域的行政課題（東海地震・富士山噴火・県境河川の防災、環境課題など）が存在する。"
    source_hint: "kousou3.pdf p1/p19/p20（要旨）"
  - id: "IE-KNG-BG-INFRA-01"
    kind: "context"
    atomic_state: true
    content: "空港・道路等の基盤整備が進み、広域交流のポテンシャルが増している。"
    source_hint: "kousou3.pdf p1/p13（要旨）"
occurrences:
  - entity: "IE-KNG-BG-RISK-01"
    role: "problem"

## 2.3 Section: 施策（観光）（anchorage: measures）
section_id: "SEC-KNG-03"
anchorage: ["tourism", "measures", "visitor-experience"]
entities:
  - id: "IE-KNG-TOUR-ROUTE-01"
    kind: "measure"
    atomic_state: true
    content: "周遊モデルコースの開発・商品化支援（テーマ型観光）"
    source_hint: "kousou3.pdf p17"
  - id: "IE-KNG-TOUR-PROMO-01"
    kind: "measure"
    atomic_state: true
    content: "三県共同観光プロモーション（ターゲット地域を絞り合同プロモーション）"
    source_hint: "kousou3.pdf p17"
  - id: "IE-KNG-TOUR-LONGSTAY-01"
    kind: "measure"
    atomic_state: true
    content: "長期滞在推進（2泊3日以上の滞在型プログラム開発）"
    source_hint: "kousou3.pdf p17"
  - id: "IE-KNG-TOUR-INBOUND-01"
    kind: "measure"
    atomic_state: true
    content: "外国人観光客誘致（ルート設定、海外観光展・商談会、受入体制整備）"
    source_hint: "kousou3.pdf p17"
  - id: "IE-KNG-TOUR-SIGN-01"
    kind: "mechanism"
    atomic_state: true
    content: "公共サイン整備（案内標識の連続性・統一性、多言語化、ピクト活用、広域観光地図作成等）"
    source_hint: "kousou3.pdf p18"
relations:
  - type: "enables"
    from: "IE-KNG-TOUR-SIGN-01"
    to: "IE-KNG-TOUR-LONGSTAY-01"
    note: "回遊/滞在UXの土台"

## 2.4 Section: 施策（防災）（anchorage: safety）
section_id: "SEC-KNG-04"
anchorage: ["safety", "disaster", "measures"]
entities:
  - id: "IE-KNG-DS-VOLC-01"
    kind: "measure"
    atomic_state: true
    content: "富士山火山防災：相互応援体制のマニュアル整備等"
    source_hint: "kousou3.pdf p19"
  - id: "IE-KNG-DS-DRILL-01"
    kind: "measure"
    atomic_state: true
    content: "合同防災訓練（噴火・地震想定で連携強化）"
    source_hint: "kousou3.pdf p19"
  - id: "IE-KNG-DS-RIVER-01"
    kind: "mechanism"
    atomic_state: true
    content: "県境河川の防災：水防情報共有、雨量・水位データ共有、注意喚起"
    source_hint: "kousou3.pdf p20"
relations:
  - type: "mitigates"
    from: "IE-KNG-DS-DRILL-01"
    to: "IE-KNG-BG-RISK-01"

---

# 3. ケースB：英国（行動規範＋受け皿整備）
## 3.1 Section: 行動規範（anchorage: visitor-behavior）
section_id: "SEC-UK-01"
anchorage: ["visitor-behavior", "norms"]
entities:
  - id: "IE-UK-CC-01"
    kind: "mechanism"
    atomic_state: true
    content: "The Countryside Code：訪問者向けに行動規範を提示し、自然・地域住民・他者への配慮を促す。"
  - id: "IE-UK-CC-02"
    kind: "lesson"
    atomic_state: true
    content: "権利（楽しむ）と責任（保護する）をセットで提示し、分散した管理主体でも共通ルールが成立しやすい。"

## 3.2 Section: 観光圧と受け皿（anchorage: capacity-management）
section_id: "SEC-UK-02"
anchorage: ["capacity-management", "transport", "erosion"]
entities:
  - id: "IE-UK-LD-OVR-01"
    kind: "problem"
    atomic_state: true
    content: "大量の訪問者が経済効果と同時に交通混雑・環境負荷などの課題を生む。"
  - id: "IE-UK-LD-TRANS-01"
    kind: "measure"
    atomic_state: true
    content: "シャトル運行・駐車運用など、局所ボトルネックを“交通×受け皿”で緩和する。"
  - id: "IE-UK-PATH-01"
    kind: "measure"
    atomic_state: true
    content: "歩道侵食への長期補修・資金調達（調査→修復→資金ループ）。"
  - id: "IE-UK-REG-TOUR-01"
    kind: "policy_goal"
    atomic_state: true
    content: "Regenerative tourism：負の影響最小化に留まらず“純増の好影響（ネットポジティブ）”を目指す。"
relations:
  - type: "refines"
    from: "IE-UK-REG-TOUR-01"
    to: "IE-KNG-OBJ-01"
    note: "“活性化”の定義をネットポジティブへ拡張可能"

---

# 4. ケースC：豪州（聖地ウルル：価値競合の統治）
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
    content: "聖地としての価値と観光資源としての価値が衝突し、正当性・体験・保全のジレンマが生じる。"
    source_hint: "2015-8-1.9.pdf（要旨）"
  - id: "IE-AUS-ULU-MECH-01"
    kind: "mechanism"
    atomic_state: true
    content: "登山（climb）の是非・制限をめぐる“場所のポリティクス”が、文化の真正性・政府努力・ツーリスト満足を担保する装置として機能しうる。"
    source_hint: "2015-8-1.9.pdf（要旨）"
relations:
  - type: "contrasts"
    from: "IE-AUS-ULU-MECH-01"
    to: "IE-KNG-TOUR-PROMO-01"
    note: "促進だけでなく“制限を含む管理装置”が正当性を支える場合"

---

# 5. ケースD：米国（国立公園：過密とTimed Entry）
section_id: "SEC-US-01"
anchorage: ["access-control", "capacity-management", "fairness"]
entities:
  - id: "IE-US-TE-01"
    kind: "mechanism"
    atomic_state: true
    content: "Timed entry / reservation：入園・入域を時間枠で配分し、混雑緩和・資源保護・待ち行列減少を狙う。"
  - id: "IE-US-TE-02"
    kind: "tradeoff"
    atomic_state: true
    content: "予約取得の難しさ・公平性（誰が枠を取れるか）など、新たな勝者/敗者を作りうる。"
  - id: "IE-US-TE-03"
    kind: "metric"
    atomic_state: true
    content: "効果指標：ゲート待ち、駐車場満車、ピーク集中、資源影響、満足度等。"
relations:
  - type: "suggests"
    from: "IE-US-TE-01"
    to: "IE-KNG-TOUR-LONGSTAY-01"
    note: "“量を増やす”より“時間に分散させる”軸の導入"

---

# 6. ケースE：欧州（イタリア・フランス：国立公園のガバナンス制度）
## 6.1 Section: イタリア（公園局：多層ガバナンス＋法定計画）
section_id: "SEC-EU-IT-01"
anchorage: ["institutional-governance", "legal-plans", "stakeholder-council"]
entities:
  - id: "IE-EU-IT-AUTH-01"
    kind: "mechanism"
    atomic_state: true
    content: "国立公園の管理は公的法人格を有する『公園局』が担い、国の監督下に置かれる。局長は環境大臣が任命。"
    source_hint: "env.go.jp 900492493.pdf L3-L4"
  - id: "IE-EU-IT-BOARD-01"
    kind: "mechanism"
    atomic_state: true
    content: "理事会：国の行政機関、地方自治体、学識者、環境NGOの指名者が参加（局長含め13名）。"
    source_hint: "env.go.jp 900492493.pdf L7-L12"
  - id: "IE-EU-IT-COMM-01"
    kind: "mechanism"
    atomic_state: true
    content: "公園共同体：地域の意見をきく諮問機関（公園区域内の州・県・市町村等の長が参加）。"
    source_hint: "env.go.jp 900492493.pdf L13-L16"
  - id: "IE-EU-IT-BUDG-01"
    kind: "mechanism"
    atomic_state: true
    content: "予算の大部分は国の拠出金。例：アブルッツォ国立公園（国72%、自己収入14%、その他14%）。"
    source_hint: "env.go.jp 900492493.pdf L4/L17-L18"
  - id: "IE-EU-IT-PLAN-01"
    kind: "mechanism"
    atomic_state: true
    content: "法定計画：公園計画（ゾーニング、利用目的、施設・サービス、自然環境介入基準等）と経済社会計画（エコツーリズム等）。"
    source_hint: "env.go.jp 900492493.pdf L32-L38"
relations:
  - type: "generalizes"
    from: "IE-EU-IT-PLAN-01"
    to: "IE-KNG-GOV-01"
    note: "広域連携を“法定計画＋協議体”として制度化する参照点"

## 6.2 Section: フランス（公施設法人：目標契約＋憲章＋公衆協議）
section_id: "SEC-EU-FR-01"
anchorage: ["institutional-governance", "contracting", "public-consultation"]
entities:
  - id: "IE-EU-FR-AUTH-01"
    kind: "mechanism"
    atomic_state: true
    content: "管理は公的法人格を有する『公施設法人』が担い、国と目標契約を締結して実施。予算の大部分は契約に基づく国の負担金。"
    source_hint: "env.go.jp 900492493.pdf L45-L46"
  - id: "IE-EU-FR-BOARD-01"
    kind: "mechanism"
    atomic_state: true
    content: "運営理事会：国の行政機関、地方自治体、学識者、職員代表等が参加（40〜80名程度）。"
    source_hint: "env.go.jp 900492493.pdf L49-L53"
  - id: "IE-EU-FR-SCI-01"
    kind: "mechanism"
    atomic_state: true
    content: "科学委員会：自然科学・人文・社会科学の専門家で構成される諮問機関。"
    source_hint: "env.go.jp 900492493.pdf L54-L56"
  - id: "IE-EU-FR-SSC-01"
    kind: "mechanism"
    atomic_state: true
    content: "経済社会文化委員会：農林水産・観光・自然エネルギー・文化・地域づくり等の地域専門家で構成。"
    source_hint: "env.go.jp 900492493.pdf L57-L59"
  - id: "IE-EU-FR-DECREE-01"
    kind: "mechanism"
    atomic_state: true
    content: "規制は政令で定め、制定に際して市町村・県・レジオンとの協議と公衆協議を行う。許認可はディレクターが実施。"
    source_hint: "env.go.jp 900492493.pdf L76-L78"
  - id: "IE-EU-FR-CHARTER-01"
    kind: "mechanism"
    atomic_state: true
    content: "国立公園憲章：将来ビジョン・目標・具体取組を策定し、地方自治体・公衆・審議会等と協議して形成。"
    source_hint: "env.go.jp 900492493.pdf L79-L81"
relations:
  - type: "contrasts"
    from: "IE-EU-FR-CHARTER-01"
    to: "IE-KNG-OBJ-01"
    note: "『憲章（ビジョン＋取組）』を制度・契約で束ねる強度が高い"

---

# 7. 横断比較：同じ課題を“どの機能”で処理しているか
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
  - id: "IE-FUNC-06"
    kind: "concept"
    atomic_state: true
    content: "多層ガバナンス（理事会/諮問/公衆協議/契約）"
  - id: "IE-FUNC-07"
    kind: "concept"
    atomic_state: true
    content: "財源の制度化（国負担金/自己収入/基金）"
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
  - type: "is_example_of"
    from: "IE-EU-IT-BOARD-01"
    to: "IE-FUNC-06"
  - type: "is_example_of"
    from: "IE-EU-IT-BUDG-01"
    to: "IE-FUNC-07"

---

# 8. 神奈川の改善仮説（国外事例→神奈川への転写）
section_id: "SEC-KNG-IMPROVE-01"
anchorage: ["improvement", "hypothesis", "actionable"]
entities:
  - id: "IE-IMP-01"
    kind: "improvement_hypothesis"
    atomic_state: true
    content: "（英国）行動規範の“共通テキスト”を交流圏のサイン/案内/サイトに統一実装し、権利と責任をセットで提示する。"
  - id: "IE-IMP-02"
    kind: "improvement_hypothesis"
    atomic_state: true
    content: "（米国）ピーク集中地点で timed-entry / shuttle-first を試行し、KPIで評価して段階導入する。"
  - id: "IE-IMP-03"
    kind: "improvement_hypothesis"
    atomic_state: true
    content: "（豪州）価値競合（聖性・景観・生活・満足）を明示し、“制限/禁忌/代替体験”を含む管理装置を導入する。"
  - id: "IE-IMP-04"
    kind: "improvement_hypothesis"
    atomic_state: true
    content: "（英国）損耗（侵食等）の長期補修＋資金ループを設計し、保全の運用能力を底上げする。"
  - id: "IE-IMP-05"
    kind: "improvement_hypothesis"
    atomic_state: true
    content: "（神奈川既存）年次進捗/5年見直しを共通KPIと結び、適応管理（adaptive management）化する。"
  - id: "IE-IMP-06"
    kind: "improvement_hypothesis"
    atomic_state: true
    content: "（欧州）重点地域で『憲章（ビジョン＋取組）』『法定計画（ゾーニング/基準）』『公衆協議』を束ねた規則体系を段階導入する。"
  - id: "IE-IMP-07"
    kind: "improvement_hypothesis"
    atomic_state: true
    content: "（欧州）『科学/安全委員会』『観光・地域産業委員会』等の専門諮問を明示し、意思決定根拠と責任分界を透明化する。"
  - id: "IE-IMP-08"
    kind: "improvement_hypothesis"
    atomic_state: true
    content: "（欧州）維持管理（歩道補修、サイン更新、防災訓練）に継続財源を割り当てる仕組み（基金/使用料/協賛）を検討する。"
relations:
  - type: "derives_from"
    from: "IE-IMP-06"
    to: "IE-EU-FR-CHARTER-01"
  - type: "derives_from"
    from: "IE-IMP-07"
    to: "IE-EU-FR-SCI-01"
  - type: "derives_from"
    from: "IE-IMP-08"
    to: "IE-EU-IT-BUDG-01"

---

# 9. Pattern Catalog（再利用ライブラリ）
section_id: "SEC-PATTERN-01"
anchorage: ["pattern", "reusable", "library"]
entities:
  - id: "IE-PAT-01"
    kind: "pattern"
    atomic_state: true
    content: "Normative Code + Signage"
  - id: "IE-PAT-02"
    kind: "pattern"
    atomic_state: true
    content: "Timed Entry Pilot"
  - id: "IE-PAT-03"
    kind: "pattern"
    atomic_state: true
    content: "Sacredness Governance"
  - id: "IE-PAT-04"
    kind: "pattern"
    atomic_state: true
    content: "Maintenance Funding Loop"
  - id: "IE-PAT-05"
    kind: "pattern"
    atomic_state: true
    content: "Charter + Legal Plans + Public Consultation"

---

# 10. 1ドキュメント構造（Index）
- SEC-KNG-01..04：神奈川（現状設計）
- SEC-UK-01..02 / SEC-AUS-01 / SEC-US-01 / SEC-EU-IT-01 / SEC-EU-FR-01：国外事例
- SEC-CMP-01：機能比較ハブ
- SEC-KNG-IMPROVE-01：改善仮説
- SEC-PATTERN-01：再利用パターン


# 11. 神奈川の“重点地域（地点）”での適用検討（Breakdown-ready）
> ここからは「比較→改善」のブリッジとして、**場所（place）** を単位に分解して評価できるようにする。  
> ＝後で機械的に `breakdown` しやすい（各地点＝小文書化しやすい）構造。

## 11.1 Section: 重点地域の定義（anchorage: scope.place）
section_id: "SEC-KNG-REGIONS-01"
anchorage: ["scope", "place", "targeting"]
entities:
  - id: "IE-KNG-REGION-DEF-01"
    kind: "mechanism"
    atomic_state: true
    content: "交流圏の改善は『全域一律』ではなく、負荷・価値・危険度が高い“重点地域（地点）”を定義し、介入設計（ルール・交通・資金・協議）を段階導入する。"
  - id: "IE-KNG-REGION-LIST-01"
    kind: "asset"
    atomic_state: true
    content: "重点地域（例）：富士山周辺（登山口/五合目等）、箱根（湖畔/温泉街/交通結節点）、伊豆（海岸部/自然公園）、主要幹線（渋滞ボトルネック）、防災上の重要区間（緊急輸送路/県境河川）。"
relations:
  - type: "operationalizes"
    from: "IE-KNG-REGION-DEF-01"
    to: "IE-KNG-OBJ-01"
    note: "目的を“場所単位の介入設計”に落とす"

## 11.2 Section: 地点評価の観点（anchorage: evaluation.frame）
section_id: "SEC-KNG-EVAL-FRAME-01"
anchorage: ["evaluation", "frame", "metrics"]
entities:
  - id: "IE-EVAL-AXIS-01"
    kind: "metric"
    atomic_state: true
    content: "混雑（ピーク集中/待ち時間/駐車満車頻度）"
  - id: "IE-EVAL-AXIS-02"
    kind: "metric"
    atomic_state: true
    content: "資源影響（侵食/ゴミ/騒音/生態系/景観）"
  - id: "IE-EVAL-AXIS-03"
    kind: "metric"
    atomic_state: true
    content: "安全（事故/災害時の脆弱性/避難輸送）"
  - id: "IE-EVAL-AXIS-04"
    kind: "metric"
    atomic_state: true
    content: "地域受容（住民苦情/生活圧/事業者影響）"
  - id: "IE-EVAL-AXIS-05"
    kind: "metric"
    atomic_state: true
    content: "体験価値（満足度/学習/文化理解/再訪）"
  - id: "IE-EVAL-AXIS-06"
    kind: "metric"
    atomic_state: true
    content: "公平性（予約/移動手段/情報格差/アクセシビリティ）"
  - id: "IE-EVAL-AXIS-07"
    kind: "metric"
    atomic_state: true
    content: "運用可能性（人員/権限/法的根拠/財源/データ）"
relations:
  - type: "generalizes"
    from: "IE-US-TE-03"
    to: "IE-EVAL-AXIS-01"

---

# 12. 地点別：富士山周辺（観光圧・安全・聖性/景観）
## 12.1 Section: 富士山の課題仮説（anchorage: place.fuji.problem）
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
section_id: "SEC-KNG-FUJI-02"
anchorage: ["place:fuji", "measures", "pattern-mapping"]
entities:
  - id: "IE-KNG-FUJI-MEAS-01"
    kind: "measure"
    atomic_state: true
    content: "（PAT-02）Timed Entry Pilot：特定期間・特定地点（登山口/駐車/バス結節）で時間枠予約を試行し、ピーク分散と安全確保を狙う。"
  - id: "IE-KNG-FUJI-MEAS-02"
    kind: "measure"
    atomic_state: true
    content: "（PAT-01）Normative Code + Signage：行動規範（自然/地域/安全）を短く提示し、現場の多言語サインと一体運用する。"
  - id: "IE-KNG-FUJI-MEAS-03"
    kind: "measure"
    atomic_state: true
    content: "（PAT-05）Charter + Legal Plans + Public Consultation：重点地域のビジョン/目標/取組（憲章相当）と、利用基準（ゾーン/禁止・許可）を協議プロセスつきで整備する。"
  - id: "IE-KNG-FUJI-MEAS-04"
    kind: "measure"
    atomic_state: true
    content: "（PAT-04）Maintenance Funding Loop：損耗指標→補修計画→財源→実装→再計測のループを明示し、保全の運用能力を作る。"
occurrences:
  - entity: "IE-KNG-FUJI-MEAS-01"
    role: "measure"
    note: "US事例の転写（予約枠・公平性が焦点）"
  - entity: "IE-KNG-FUJI-MEAS-03"
    role: "mechanism"
    note: "EU事例の転写（協議と規則体系）"
relations:
  - type: "derives_from"
    from: "IE-KNG-FUJI-MEAS-01"
    to: "IE-US-TE-01"
  - type: "derives_from"
    from: "IE-KNG-FUJI-MEAS-02"
    to: "IE-UK-CC-01"
  - type: "derives_from"
    from: "IE-KNG-FUJI-MEAS-03"
    to: "IE-EU-FR-CHARTER-01"
  - type: "derives_from"
    from: "IE-KNG-FUJI-MEAS-04"
    to: "IE-UK-PATH-01"

---

# 13. 地点別：箱根（交通・受け皿・住民受容）
## 13.1 Section: 箱根の課題仮説（anchorage: place.hakone.problem）
section_id: "SEC-KNG-HAKONE-01"
anchorage: ["place:hakone", "problem-framing"]
entities:
  - id: "IE-KNG-HAKONE-PROB-01"
    kind: "problem"
    atomic_state: true
    content: "交通混雑（道路・駐車・公共交通のピーク集中）が体験価値と生活圧を同時に悪化させる。"
  - id: "IE-KNG-HAKONE-PROB-02"
    kind: "problem"
    atomic_state: true
    content: "受け皿（シャトル/駐車/動線）の運用が“局所最適”になりやすく、全体の分散設計が必要。"
relations:
  - type: "generalizes"
    from: "IE-UK-LD-OVR-01"
    to: "IE-KNG-HAKONE-PROB-01"

## 13.2 Section: 箱根の介入候補（anchorage: place.hakone.measures）
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
section_id: "SEC-KNG-IZU-01"
anchorage: ["place:izu", "problem-framing", "measures"]
entities:
  - id: "IE-KNG-IZU-PROB-01"
    kind: "problem"
    atomic_state: true
    content: "自然資源が分散しており、回遊促進と保全（損耗管理）を同時に設計する必要がある。"
  - id: "IE-KNG-IZU-MEAS-01"
    kind: "measure"
    atomic_state: true
    content: "（PAT-04）保全の運用能力：資源インベントリ→影響指標→補修計画→財源のループを地域単位で設計する。"
  - id: "IE-KNG-IZU-MEAS-02"
    kind: "measure"
    atomic_state: true
    content: "（PAT-01）規範＋サインで『分散回遊』を促し、単一地点のピーク集中を避ける。"

---

# 15. Decision / View / Projection（Convergent-ready）
> ここは **convergent（収束）** の入口：地点別のbreakdown結果を、意思決定と運用に束ねる。

## 15.1 Section: Decision候補（anchorage: decision.set）
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
section_id: "SEC-KNG-PROJ-01"
anchorage: ["projection", "operational", "data"]
entities:
  - id: "IE-PROJ-01"
    kind: "projection"
    atomic_state: true
    content: "予約/配分の運用（枠定義、取得導線、現場確認、例外、返金/変更、当日枠、公平性ルール）"
  - id: "IE-PROJ-02"
    kind: "projection"
    atomic_state: true
    content: "行動規範の運用（短文規範、Do/Don't例、ローカル例外、なぜ重要か、多言語、掲示場所）"
  - id: "IE-PROJ-03"
    kind: "projection"
    atomic_state: true
    content: "KPIと観測（混雑、資源影響、安全、受容、満足、公平性、運用コスト）"
  - id: "IE-PROJ-04"
    kind: "projection"
    atomic_state: true
    content: "協議プロセス（参加者、議題、公開、フィードバック反映、改定周期）"

---

# 16. 機械的操作のための分割・収束ルール（案）
## 16.1 Breakdown（分割）ルール
section_id: "SEC-MECH-BREAKDOWN-01"
anchorage: ["mechanical", "breakdown"]
entities:
  - id: "IE-BR-01"
    kind: "mechanism"
    atomic_state: true
    content: "Sectionを最小分割単位とし、`doc_id + section_id` をキーに小文書化する。"
  - id: "IE-BR-02"
    kind: "mechanism"
    atomic_state: true
    content: "地点別Section（SEC-KNG-FUJI/HAKONE/IZU）を優先して分割し、各文書は『課題→介入候補→評価軸→Decision候補』を持つ。"
  - id: "IE-BR-03"
    kind: "mechanism"
    atomic_state: true
    content: "分割後も Relation は `doc_id#entity_id` 参照で保持し、convergent時に再結合できるようにする。"

## 16.2 Convergent（収束）ルール
section_id: "SEC-MECH-CONVERGE-01"
anchorage: ["mechanical", "convergent"]
entities:
  - id: "IE-CV-01"
    kind: "mechanism"
    atomic_state: true
    content: "Pattern Catalog（SEC-PATTERN-01）を“共通語彙”として、地点別の介入候補をパターンIDに正規化する。"
  - id: "IE-CV-02"
    kind: "mechanism"
    atomic_state: true
    content: "Decision候補（SEC-KNG-DECIDE-01）に向けて、地点別の評価（pros/cons/risks/metrics）を集約し、採否判断に必要な最小集合へ圧縮する。"
  - id: "IE-CV-03"
    kind: "mechanism"
    atomic_state: true
    content: "Projection（SEC-KNG-PROJ-01）をインタフェースとして、UI/運用/データ設計（WorkCell/Decision6等）へ接続する。"
