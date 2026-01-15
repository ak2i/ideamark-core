---
ideamark_version: 1
doc_id: "imdoc.case.uk_countryside_access.iwamoto1997"
title: "田園レクリエーションとアクセス権 —イギリスの経験"
lang: "ja-JP"
status: "draft"
created_at: "2026-01-15"
created_by: "hybrid"
source:
  type: "academic_paper"
  author: "岩本純明"
  publication: "農耕の技術と文化"
  year: 1997
  volume: 20
  pages: "38-63"
  uri: "http://hdl.handle.net/2433/278615"
refs:
  - uri: "ideamark://patterns/PAT-01"
    role: "related_pattern"
    note: "Normative Code + Signage パターンとの関連"
  - uri: "ideamark://cases/SEC-UK-01"
    role: "complements"
    note: "既存のUK事例セクションを補完"
purpose: |
  イギリスにおける田園アクセス権の歴史的形成過程を記録し、
  観光・レクリエーション政策における「権利」と「許可」の設計パターンを抽出する。
  日本の富士箱根伊豆交流圏等への政策転写の参照点として機能させる。
---

# 0. 文書の読み方（Meta）

この文書は学術論文を IdeaMark 形式で構造化したものである。

**breakdown 可能な軸**：
- 時代区分（19世紀 / 戦間期 / 戦後 / 現代）
- 制度類型（通行権 / アクセス権 / 許可制）
- アクター（土地所有者 / 自治体 / 市民団体 / 国家）
- 価値競合（私的所有権 vs 公共的利用権）

**convergent 可能な対象**：
- 他国の類似制度（日本の入会権、ドイツの自然享受権等）
- IdeaMark パターンライブラリ（PAT-01〜05）

---

# 1. イギリス田園景観の特質（背景）

```yaml
section_id: "SEC-IWAMOTO-01"
anchorage:
  - view: "background"
  - phase: "context"
  - domain: "uk_countryside"
  - mode: "description"
intent: |
  イギリス田園景観が「人工的に作られた自然」であることを確認し、
  アクセス権の議論がこの景観認識を前提としていることを示す。
refs:
  - uri: "ideamark://concepts/idea.living_landscape"
    role: "instantiates"
```

## Occurrences

```yaml
occurrences:
  - id: "occ-01-001"
    role: "context"
    entity: "IE-UK-LANDSCAPE-01"
    note: "論文冒頭の景観認識"

  - id: "occ-01-002"
    role: "historical_pattern"
    entity: "IE-UK-FOOTPATH-ORIGIN"
    note: "フットパスの歴史的起源"
```

## IdeaEntities

```yaml
idea_entities:
  - id: "IE-UK-LANDSCAPE-01"
    atomic_state: true
    payload: |
      イギリスの田園景観は「ありのままの自然」ではなく、
      生け垣（hedge）や牧草地など、何世紀にもわたる人間の営為によって
      作り上げられた「人工的自然」である。
      この認識が、土地への公衆アクセスの正当化根拠となる。
    refs:
      - uri: "biblio:HOSKINS1955"
        role: "source"

  - id: "IE-UK-FOOTPATH-ORIGIN"
    atomic_state: true
    payload: |
      public footpath（公共歩道）と bridleway（乗馬道）は、
      かつての農村共同体における生活道路・作業道として発生し、
      囲い込み後も権利として維持された歴史を持つ。
    refs:
      - uri: "biblio:HOSKINS1955"
        role: "source"
```

---

# 2. 通行権の法的構造（制度分析）

```yaml
section_id: "SEC-IWAMOTO-02"
anchorage:
  - view: "institutional_analysis"
  - phase: "description"
  - domain: "legal_framework"
  - focus: "problem"
  - mode: "enumeration"
intent: |
  イギリスにおける田園アクセスの法的類型を整理し、
  「通行権」と「アクセス権」の区別を明確化する。
  これは政策設計における選択肢の構造を示す。
refs:
  - uri: "ideamark://patterns/IE-FUNC-02"
    role: "addresses"
    note: "アクセス量の制御という機能への解"
```

## Occurrences

```yaml
occurrences:
  - id: "occ-02-001"
    role: "mechanism"
    entity: "IE-UK-ROW-TYPES"
    note: "通行権の3類型"

  - id: "occ-02-002"
    role: "mechanism"
    entity: "IE-UK-ROW-ESTABLISHMENT"
    note: "通行権の成立方法"

  - id: "occ-02-003"
    role: "mechanism"
    entity: "IE-UK-ACCESS-TYPES"
    note: "アクセス権の類型"

  - id: "occ-02-004"
    role: "contrast"
    entity: "IE-UK-ROW-VS-ACCESS"
    note: "通行権とアクセス権の本質的差異"
```

## IdeaEntities

```yaml
idea_entities:
  - id: "IE-UK-ROW-TYPES"
    atomic_state: true
    payload: |
      public rights of way（公共通行権）は3種類：
      1. footpath：徒歩のみ
      2. bridleway：徒歩＋乗馬＋自転車
      3. byway open to all traffic：すべての交通手段
      
      総延長約169,000km（1994年時点）。
      footpath が78%、bridleway が17%、byway が5%。
    refs:
      - uri: "biblio:COUNTRYSIDE_COMMISSION1996"
        role: "source"

  - id: "IE-UK-ROW-ESTABLISHMENT"
    atomic_state: false
    payload: |
      通行権の成立方法は複数存在する。
    children:
      - id: "IE-UK-ROW-EXPRESS"
        atomic_state: true
        payload: |
          express dedication（明示的供用）：
          土地所有者が明瞭な意志表示により通行権を設定。
          freehold（自由土地保有権）を持つ者のみ可能。

      - id: "IE-UK-ROW-PRESUMED"
        atomic_state: true
        payload: |
          presumed dedication（推定的供用）：
          長期間（20年以上）の公衆利用により通行権が推定成立。
          1932年 Rights of Way Act、1980年 Highways Act で法定化。
          「一度 highway となれば、永遠に highway」の原則。

      - id: "IE-UK-ROW-ORDER"
        atomic_state: true
        payload: |
          public path creation orders：
          地方自治体が公益のため通行権を創設できる（1980年 Highways Act 26条）。
          definitive map（確定地図）への登載により法的効力。

  - id: "IE-UK-ACCESS-TYPES"
    atomic_state: false
    payload: |
      right of access to areas of land（土地区域へのアクセス権）は
      通行権とは異なり、特定区域内を自由に歩き回る権利。
    children:
      - id: "IE-UK-ACCESS-PERMISSION"
        atomic_state: true
        payload: |
          permission（許可）：
          土地所有者の明示的許可による。
          National Trust、Forestry Commission 等が多くの土地を開放。
          ただし法的権利ではなく、いつでも撤回可能。

      - id: "IE-UK-ACCESS-AGREEMENT"
        atomic_state: true
        payload: |
          access agreements（アクセス協定）：
          地方自治体がオープン・カントリーへのアクセスのため
          土地所有者と協定を締結（1949年 National Parks Act）。
          協定期間中は公衆のアクセス権が保障される。

      - id: "IE-UK-ACCESS-ORDER"
        atomic_state: true
        payload: |
          access orders（アクセス命令）：
          協定が成立しない場合、地方自治体が強制的にアクセス権を設定。
          ただし補償が必要であり、実際の適用例は極めて少ない。

      - id: "IE-UK-ACCESS-COMMON"
        atomic_state: true
        payload: |
          common land（共有地）へのアクセス：
          1925年 Law of Property Act により、都市近郊の共有地は
          運動・レクリエーション目的で公衆に開放。
          ただし農村部の共有地は対象外という制限あり。

  - id: "IE-UK-ROW-VS-ACCESS"
    atomic_state: true
    payload: |
      通行権（right of way）とアクセス権（right of access）の本質的差異：
      
      - 通行権：線的（passage to and fro）、逸脱は trespass
      - アクセス権：面的（right to roam）、区域内を自由に移動
      
      イギリスでは通行権は確立しているが、
      面的アクセス権は依然として限定的・例外的である。
```

---

# 3. 1949年国立公園法の構造（制度史）

```yaml
section_id: "SEC-IWAMOTO-03"
anchorage:
  - view: "institutional_history"
  - phase: "description"
  - domain: "national_parks"
  - focus: "solution"
  - mode: "structural_analysis"
intent: |
  1949年国立公園法の制度設計を分析し、
  「保全」と「レクリエーション」の両立という政策目標が
  どのような制度構造で実現されようとしたかを示す。
refs:
  - uri: "ideamark://patterns/PAT-05"
    role: "derives_from"
    note: "Charter + Legal Plans + Public Consultation パターンの源流"
```

## Occurrences

```yaml
occurrences:
  - id: "occ-03-001"
    role: "policy_goal"
    entity: "IE-UK-NP-PURPOSE"
    note: "国立公園法の目的規定"

  - id: "occ-03-002"
    role: "mechanism"
    entity: "IE-UK-NP-STRUCTURE"
    note: "制度構造（5つの柱）"

  - id: "occ-03-003"
    role: "constraint"
    entity: "IE-UK-NP-OWNERSHIP"
    note: "土地所有構造という制約"
```

## IdeaEntities

```yaml
idea_entities:
  - id: "IE-UK-NP-PURPOSE"
    atomic_state: true
    payload: |
      1949年 National Parks and Access to the Countryside Act の目的：
      (a) 自然美の保存・増進
      (b) 公衆のオープンエア・レクリエーション機会の提供
      (c) 上記目的のため自然保護区を設置
      (d) 公共通行権の記録と保護
      
      「保全」と「利用」の両立が法律上の目的として明記された。
    refs:
      - uri: "biblio:BLUNDEN_CURRY1990"
        role: "source"

  - id: "IE-UK-NP-STRUCTURE"
    atomic_state: false
    payload: |
      1949年法の制度構造は5つの柱から成る。
    children:
      - id: "IE-UK-NP-COMMISSION"
        atomic_state: true
        payload: |
          National Parks Commission（国立公園委員会）の設置：
          国立公園の指定、AONB（特別自然美観地域）の指定を担当。
          後に Countryside Commission へ改組。

      - id: "IE-UK-NP-AUTHORITY"
        atomic_state: true
        payload: |
          国立公園管理体制：
          Joint Planning Board（合同計画委員会）または
          地方計画当局（local planning authority）が管理。
          独立した管理主体ではなく、既存自治体の枠組みを活用。

      - id: "IE-UK-NP-RESERVE"
        atomic_state: true
        payload: |
          nature reserve（自然保護区）制度：
          (a) 国家的自然保護区 - Nature Conservancy が管理
          (b) 地方自然保護区 - 地方自治体が設定
          厳格な保全を目的とする区域。

      - id: "IE-UK-NP-MAP"
        atomic_state: true
        payload: |
          definitive map（確定地図）制度：
          すべての公共通行権を地図上に記録し、法的証拠とする。
          draft map → 異議申立 → 確定 の手続き。

      - id: "IE-UK-NP-LDR"
        atomic_state: true
        payload: |
          Long-Distance Routes（長距離ルート）制度：
          複数の通行権を接続し、連続した長距離歩道を整備。
          Pennine Way（約400km）等が代表例。

  - id: "IE-UK-NP-OWNERSHIP"
    atomic_state: true
    payload: |
      イギリス国立公園の特徴的制約：土地の大部分が私有地である。
      
      例：Lake District - 農用地57%、私有地率90%以上
      例：Peak District - 農用地80%
      
      したがって国立公園指定は土地所有権に影響せず、
      アクセス権は別途、協定や通行権で確保する必要がある。
    refs:
      - uri: "biblio:MACEWEN1982"
        role: "source"
```

---

# 4. 土地所有とアクセスの緊張（価値競合）

```yaml
section_id: "SEC-IWAMOTO-04"
anchorage:
  - view: "conflict_analysis"
  - phase: "problem-framing"
  - domain: "property_rights"
  - focus: "problem"
  - mode: "structural_comparison"
intent: |
  土地所有権と公衆アクセス権の間の構造的緊張を分析する。
  これは「価値競合の統治」パターン（PAT-03相当）の具体事例である。
refs:
  - uri: "ideamark://patterns/PAT-03"
    role: "instantiates"
    note: "Sacredness Governance パターンの世俗版"
  - uri: "ideamark://cases/IE-AUS-ULU-CONF-01"
    role: "parallels"
    note: "ウルルの価値競合との構造的類似"
```

## Occurrences

```yaml
occurrences:
  - id: "occ-04-001"
    role: "problem_core"
    entity: "IE-UK-OWNERSHIP-CONCENTRATION"
    note: "土地所有の集中構造"

  - id: "occ-04-002"
    role: "stakeholder"
    entity: "IE-UK-STAKEHOLDERS"
    note: "対立するステークホルダー群"

  - id: "occ-04-003"
    role: "tension"
    entity: "IE-UK-PRIVATE-PUBLIC-TENSION"
    note: "私的所有権vs公共的利用権"

  - id: "occ-04-004"
    role: "historical_pattern"
    entity: "IE-UK-RAMBLING-MOVEMENT"
    note: "徒歩旅行運動の歴史"
```

## IdeaEntities

```yaml
idea_entities:
  - id: "IE-UK-OWNERSHIP-CONCENTRATION"
    atomic_state: true
    payload: |
      イギリスの土地所有構造は極めて集中的である：
      
      - 農用地の80%以上が私有地
      - 1919年以降、自作農化が進展（1930年37%→1978年64%）
      - しかし大土地所有は依然存続
      - 5000エーカー（2000ha）以上の大地主が全農地の約20%を所有
      
      この所有構造が、アクセス権拡大の構造的障壁となっている。
    refs:
      - uri: "biblio:NORTON-TAYLOR1982"
        role: "source"

  - id: "IE-UK-STAKEHOLDERS"
    atomic_state: false
    payload: |
      田園アクセスをめぐるステークホルダー群。
    children:
      - id: "IE-UK-SH-LANDOWNERS"
        atomic_state: true
        payload: |
          土地所有者（地主・自作農）：
          所有権に基づく排他的利用権を主張。
          trespass（不法侵入）に対する法的保護を重視。
          一部は保全や景観管理の担い手として自己認識。

      - id: "IE-UK-SH-RAMBLERS"
        atomic_state: true
        payload: |
          Ramblers' Association（徒歩旅行者協会、1935年設立）：
          アクセス権の拡大を求める市民運動の中核。
          通行権の保護・創設、right to roam の法制化を主張。
          会員数は1990年代に約10万人。
        refs:
          - uri: "biblio:HOLT1995"
            role: "source"

      - id: "IE-UK-SH-OPEN-SPACES"
        atomic_state: true
        payload: |
          Open Spaces Society（オープンスペース協会、1865年設立）：
          共有地・オープンスペースの保全を目的とする最古の市民団体。
          共有地登録運動、フットパス保護運動の先駆。
        refs:
          - uri: "biblio:WILLIAMS1965"
            role: "source"

      - id: "IE-UK-SH-NATIONAL-TRUST"
        atomic_state: true
        payload: |
          National Trust（ナショナル・トラスト、1895年設立）：
          歴史的建造物・自然景観の保全と公開を目的。
          1995年時点で273,000haの土地を所有・管理。
          会員数約300万人（1997年時点）。
        refs:
          - uri: "biblio:WATERSON1994"
            role: "source"

  - id: "IE-UK-PRIVATE-PUBLIC-TENSION"
    atomic_state: true
    payload: |
      私的所有権と公共的利用権の間の構造的緊張：
      
      土地所有者側の論理：
      - 所有権は絶対的権利であり、アクセス許可は恩恵
      - 無秩序なアクセスは農業・狩猟・環境に悪影響
      - stewardship（管理責任）として景観を維持している
      
      アクセス推進側の論理：
      - 田園景観は国民共通の遺産（national heritage）
      - 歴史的に存在した慣行的アクセスを回復すべき
      - レクリエーションは citizen right（市民権）の一部
      
      この緊張は制度設計上、未解決のまま継続している。

  - id: "IE-UK-RAMBLING-MOVEMENT"
    atomic_state: false
    payload: |
      徒歩旅行運動（rambling movement）の歴史的展開。
    children:
      - id: "IE-UK-RAMBLING-ORIGIN"
        atomic_state: true
        payload: |
          19世紀後半〜20世紀初頭：
          都市労働者のレクリエーションとして徒歩旅行が普及。
          「イギリス人は歩く民族である」（Lowenthal and Prince）。
          
          1870年代以降、フットパス保護運動が組織化。
          Peak District Federation（1894年）等の団体結成。
        refs:
          - uri: "biblio:LOWENTHAL_PRINCE1964"
            role: "source"

      - id: "IE-UK-RAMBLING-INTERWAR"
        atomic_state: true
        payload: |
          戦間期（1920-30年代）：
          徒歩旅行が大衆的レジャーとして定着。
          週末には数万人がピーク地方等に押し寄せる。
          
          1932年 Kinder Scout mass trespass：
          約500人がピーク地方の私有地に集団侵入。
          アクセス権運動の象徴的事件となる。
        refs:
          - uri: "biblio:HILL1980"
            role: "source"

      - id: "IE-UK-RAMBLING-POSTWAR"
        atomic_state: true
        payload: |
          戦後〜現代：
          1949年法による部分的成果（国立公園・通行権保護）。
          しかし right to roam は実現せず。
          
          運動は継続し、2000年 Countryside and Rights of Way Act で
          ようやくオープンカントリーへの面的アクセス権が法制化。
          （本論文執筆時点では未実現）
```

---

# 5. イギリス的景観認識と保全思想（文化分析）

```yaml
section_id: "SEC-IWAMOTO-05"
anchorage:
  - view: "cultural_analysis"
  - phase: "context"
  - domain: "landscape_perception"
  - focus: "both"
  - mode: "interpretation"
intent: |
  アクセス権の議論を支える文化的・思想的基盤を分析する。
  「景観をどう認識するか」が「誰がアクセスできるか」を規定する構造。
refs:
  - uri: "ideamark://concepts/idea.living_landscape"
    role: "elaborates"
```

## Occurrences

```yaml
occurrences:
  - id: "occ-05-001"
    role: "context"
    entity: "IE-UK-LANDSCAPE-PERCEPTION"
    note: "イギリス的景観認識"

  - id: "occ-05-002"
    role: "mechanism"
    entity: "IE-UK-STEWARDSHIP"
    note: "stewardship（管理責任）概念"

  - id: "occ-05-003"
    role: "lesson"
    entity: "IE-UK-HERITAGE-ARGUMENT"
    note: "国民的遺産としての景観"
```

## IdeaEntities

```yaml
idea_entities:
  - id: "IE-UK-LANDSCAPE-PERCEPTION"
    atomic_state: true
    payload: |
      イギリスにおける景観認識の特質：
      
      - wilderness（原生自然）ではなく picturesque（絵画的美）を重視
      - 人間の手が入った「生きた景観」（living landscape）への愛着
      - 農村を「産業社会の対極」「本来のイギリス」として理想化
      
      この認識は、工業化・都市化への反発として19世紀に形成された。
      景観保全運動とアクセス権運動は同根の文化的基盤を持つ。
    refs:
      - uri: "biblio:LOWENTHAL_PRINCE1965"
        role: "source"
      - uri: "biblio:WIENER1981"
        role: "source"

  - id: "IE-UK-STEWARDSHIP"
    atomic_state: true
    payload: |
      stewardship（管理責任）概念：
      
      土地所有者は単なる所有者ではなく、
      景観の「管理人」（steward）・「保護者」（custodian）である
      という自己認識。
      
      この概念は：
      - 所有権の正当化根拠として機能
      - 同時に保全義務の根拠としても機能
      - アクセス許可の「恩恵」的性格を正当化
      
      しかし批判者（Shoard等）は、
      実際には景観破壊を行いながら stewardship を主張する矛盾を指摘。
    refs:
      - uri: "biblio:SHOARD1980"
        role: "source"

  - id: "IE-UK-HERITAGE-ARGUMENT"
    atomic_state: true
    payload: |
      「国民的遺産」（national heritage）としての景観という主張：
      
      アクセス権推進派の論理：
      - 田園景観は特定の所有者のものではなく国民共通の遺産
      - 歴史的に形成された景観は公共財的性格を持つ
      - したがって公衆アクセスは「権利」であり「恩恵」ではない
      
      この主張は、所有権の絶対性を相対化する論拠となるが、
      法的には依然として所有権が優位である。
```

---

# 6. 政策的含意の抽出（改善仮説）

```yaml
section_id: "SEC-IWAMOTO-06"
anchorage:
  - view: "policy_implications"
  - phase: "hypothesis"
  - domain: "policy_design"
  - focus: "solution"
  - mode: "synthesis"
intent: |
  本論文から抽出される政策設計上の教訓を整理し、
  他地域（日本等）への転写可能なパターンを特定する。
refs:
  - uri: "ideamark://cases/SEC-KNG-IMPROVE-01"
    role: "informs"
    note: "神奈川改善仮説への示唆"
```

## Occurrences

```yaml
occurrences:
  - id: "occ-06-001"
    role: "lesson"
    entity: "IE-UK-LESSON-ROW-SYSTEM"
    note: "通行権システムの教訓"

  - id: "occ-06-002"
    role: "lesson"
    entity: "IE-UK-LESSON-INCREMENTAL"
    note: "漸進的制度形成の教訓"

  - id: "occ-06-003"
    role: "improvement_hypothesis"
    entity: "IE-UK-LESSON-FOR-JAPAN"
    note: "日本への転写仮説"

  - id: "occ-06-004"
    role: "tradeoff"
    entity: "IE-UK-LESSON-TRADEOFF"
    note: "制度設計上のトレードオフ"
```

## IdeaEntities

```yaml
idea_entities:
  - id: "IE-UK-LESSON-ROW-SYSTEM"
    atomic_state: true
    payload: |
      通行権（rights of way）システムからの教訓：
      
      1. 法的確定性：definitive map による権利の可視化・法定化
      2. 歴史的連続性：「一度 highway となれば永遠に highway」
      3. 維持管理責任：土地所有者の維持義務（stiles, gates の管理等）
      4. 市民参加：draft map への異議申立手続き
      
      これらは「権利」として確立したアクセスの制度設計パターン。

  - id: "IE-UK-LESSON-INCREMENTAL"
    atomic_state: true
    payload: |
      漸進的制度形成の教訓：
      
      イギリスのアクセス権は一挙に確立したのではなく、
      150年以上にわたる市民運動・立法・判例の積み重ねで形成された。
      
      - 1865年 Open Spaces Society 設立
      - 1932年 Rights of Way Act（推定的供用の法定化）
      - 1949年 National Parks Act（国立公園・通行権保護）
      - 2000年 CROW Act（面的アクセス権の法制化）
      
      制度は社会的合意の漸進的形成を反映する。

  - id: "IE-UK-LESSON-FOR-JAPAN"
    atomic_state: true
    payload: |
      日本（富士箱根伊豆交流圏等）への転写仮説：
      
      1. 権利と許可の区別：
         - 現状は「許可」ベースのアクセス管理が多い
         - 「権利」として確立する場合の制度設計が参照点
      
      2. 確定地図の整備：
         - 利用可能ルートの法的確定と可視化
         - デジタル時代には GIS との統合が可能
      
      3. 市民参加の制度化：
         - ルート設定・変更への異議申立手続き
         - 長期的なステークホルダー合意形成
      
      4. 維持管理責任の明確化：
         - 誰が何を維持するかの明文化
         - 財源ループ（PAT-04）との接続

  - id: "IE-UK-LESSON-TRADEOFF"
    atomic_state: true
    payload: |
      制度設計上のトレードオフ：
      
      権利 vs 許可：
      - 権利として確立 → 安定性・予測可能性が高いが柔軟性が低い
      - 許可として運用 → 柔軟性が高いが不安定・恣意的になりうる
      
      線的 vs 面的：
      - 通行権（線的）→ 管理容易、資源影響限定的
      - アクセス権（面的）→ 自由度高いが管理困難、資源影響大
      
      法定化 vs 協定化：
      - 法定化 → 強制力あるが社会的合意が前提
      - 協定化 → 合意ベースだが実効性に限界
      
      これらのトレードオフは、対象地域の特性に応じて選択される。
```

---

# 7. Pattern Catalog への接続

```yaml
section_id: "SEC-IWAMOTO-07"
anchorage:
  - view: "pattern_mapping"
  - phase: "synthesis"
  - domain: "ideamark_patterns"
  - focus: "solution"
  - mode: "mapping"
intent: |
  本論文から抽出された知見を IdeaMark パターンライブラリに接続し、
  再利用可能な形式で整理する。
```

## Occurrences

```yaml
occurrences:
  - id: "occ-07-001"
    role: "pattern"
    entity: "IE-PAT-UK-DEFINITIVE-MAP"
    note: "確定地図パターン"

  - id: "occ-07-002"
    role: "pattern"
    entity: "IE-PAT-UK-ROW-PRESUMPTION"
    note: "推定的供用パターン"

  - id: "occ-07-003"
    role: "pattern"
    entity: "IE-PAT-UK-CITIZEN-MOVEMENT"
    note: "市民運動による制度形成パターン"
```

## IdeaEntities

```yaml
idea_entities:
  - id: "IE-PAT-UK-DEFINITIVE-MAP"
    atomic_state: true
    payload: |
      パターン：Definitive Map（確定地図）
      
      問題：アクセス可能なルートが不明確で紛争が生じる
      解決：すべての公共通行権を地図上に記録し法的証拠とする
      
      構成要素：
      - 地図の作成・更新手続き
      - 異議申立・確定手続き
      - 法的効力の付与
      - 維持管理責任の明確化
      
      トレードオフ：
      - 作成コスト vs 紛争解決コスト
      - 硬直性 vs 法的安定性
    refs:
      - uri: "ideamark://patterns/PAT-01"
        role: "variant_of"
        note: "Normative Code + Signage の法的強化版"

  - id: "IE-PAT-UK-ROW-PRESUMPTION"
    atomic_state: true
    payload: |
      パターン：Presumed Dedication（推定的供用）
      
      問題：歴史的に利用されてきたルートの法的地位が不明確
      解決：長期間（20年）の公衆利用により通行権の成立を推定
      
      構成要素：
      - 利用期間の要件（20年）
      - 所有者の異議がないことの要件
      - 推定を覆す証拠の扱い
      
      トレードオフ：
      - 慣行の尊重 vs 所有権の保護
      - 証拠収集の困難さ

  - id: "IE-PAT-UK-CITIZEN-MOVEMENT"
    atomic_state: true
    payload: |
      パターン：Citizen Movement for Access（市民運動による制度形成）
      
      問題：既存の所有権体制がアクセス拡大を阻む
      解決：市民運動による長期的な社会的合意形成と立法化
      
      構成要素：
      - 市民団体の組織化（Open Spaces Society, Ramblers' Association等）
      - 象徴的行動（mass trespass等）
      - 立法への働きかけ
      - 長期的な運動継続（150年以上）
      
      トレードオフ：
      - 時間コスト vs 合意の持続性
      - 対立的手法 vs 協調的手法
```

---

# Appendix A. 書誌情報

```yaml
bibliography:
  - id: "HOSKINS1955"
    citation: "Hoskins, W.G. 1955. The Making of the English Landscape. Hodder & Stoughton."
  
  - id: "COUNTRYSIDE_COMMISSION1996"
    citation: "Countryside Commission. 1996. Second National Rights of Way Condition Survey."
  
  - id: "BLUNDEN_CURRY1990"
    citation: "Blunden, J. and Curry, N. 1990. A People's Charter? Forty Years of the National Parks and Access to the Countryside Act 1949. HMSO."
  
  - id: "MACEWEN1982"
    citation: "Macewen, A. and Macewen, M. 1982. National Parks: Conservation or Cosmetics? George Allen and Unwin."
  
  - id: "NORTON-TAYLOR1982"
    citation: "Norton-Taylor, R. 1982. Whose Land Is It Anyway? Turnstone Press."
  
  - id: "HILL1980"
    citation: "Hill, H. 1980. Freedom to Roam: the Struggle for Access to Britain's Moors and Mountains. Moorland Publishing."
  
  - id: "HOLT1995"
    citation: "Holt, A. 1995. The Origins and Early Days of The Ramblers' Association. Ramblers' Association."
  
  - id: "WILLIAMS1965"
    citation: "Williams, W.H. 1965. The Commons, Open Spaces and Footpaths Preservation Society 1865-1965. The Open Spaces Society."
  
  - id: "WATERSON1994"
    citation: "Waterson, M. 1994. The National Trust, The First Hundred Years. BBC Enterprises Limited."
  
  - id: "SHOARD1980"
    citation: "Shoard, M. 1980. The Theft of the Countryside. Maurice Temple Smith."
  
  - id: "LOWENTHAL_PRINCE1964"
    citation: "Lowenthal, D. and Prince, H.C. 1964. The English landscape. The Geographical Review Vol.54(July): 309-346."
  
  - id: "LOWENTHAL_PRINCE1965"
    citation: "Lowenthal, D. and Prince, H.C. 1965. English landscape Tastes. The Geographical Review Vol.55(April): 186-222."
  
  - id: "WIENER1981"
    citation: "Wiener, M. 1981. English Culture and the Decline of the Industrial Spirit. Cambridge University Press."
```

---

# Appendix B. Breakdown / Convergent メモ

```yaml
breakdown_axes:
  - axis: "time_period"
    values: ["pre_1900", "interwar", "postwar_1949", "contemporary"]
    target_sections: ["SEC-IWAMOTO-03", "SEC-IWAMOTO-04"]
  
  - axis: "legal_type"
    values: ["right_of_way", "access_right", "permission"]
    target_sections: ["SEC-IWAMOTO-02"]
  
  - axis: "stakeholder"
    values: ["landowners", "ramblers", "government", "ngo"]
    target_sections: ["SEC-IWAMOTO-04"]

convergent_targets:
  - pattern: "ideamark://patterns/PAT-01"
    relevant_entities: ["IE-UK-CC-01", "IE-PAT-UK-DEFINITIVE-MAP"]
  
  - pattern: "ideamark://patterns/PAT-05"
    relevant_entities: ["IE-UK-NP-STRUCTURE", "IE-EU-FR-CHARTER-01"]
  
  - case: "ideamark://cases/SEC-KNG-IMPROVE-01"
    relevant_entities: ["IE-UK-LESSON-FOR-JAPAN"]
```
