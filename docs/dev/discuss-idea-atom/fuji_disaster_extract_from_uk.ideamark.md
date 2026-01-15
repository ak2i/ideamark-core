---
ideamark_version: 1
doc_id: "imdoc.extract.fuji_disaster_from_uk_access"
title: "富士山防災政策への示唆 —イギリス田園アクセス権制度からの部分抽出"
lang: "ja-JP"
status: "draft"
created_at: "2026-01-15"
created_by: "hybrid"
extraction_context:
  purpose: |
    富士山における登山者の安全確保・防災政策を検討するにあたり、
    イギリスの田園アクセス権制度から転用可能な設計パターンを抽出する。
  source_document: "imdoc.case.uk_countryside_access.iwamoto1997"
  target_problem:
    source: "吉本ほか(2019) 富士山チャレンジ"
    summary: |
      御嶽山噴火（2014年）では入山者数が不明で救助活動が困難を極めた。
      富士山では登山者動態把握の実証実験を実施し、
      ビーコンによる位置追跡システムを構築している。
      噴火時の登山者把握に有効であることが確認された。
  extraction_criteria:
    - 登山者の把握・管理に関する制度設計
    - 権利と義務の明確化
    - 情報の可視化・法定化
    - ステークホルダー間の責任分担
refs:
  - uri: "imdoc.case.uk_countryside_access.iwamoto1997"
    role: "extracted_from"
  - uri: "ideamark://cases/SEC-KNG-FUJI-01"
    role: "informs"
    note: "富士山の課題仮説への示唆"
  - uri: "ideamark://cases/SEC-KNG-FUJI-02"
    role: "informs"
    note: "富士山の介入候補への示唆"
---

# 0. 抽出の観点（Extraction View）

```yaml
extraction_view:
  source_anchorage:
    - view: "institutional_analysis"
    - domain: "legal_framework"
  target_anchorage:
    - view: "policy_transfer"
    - phase: "hypothesis"
    - domain: "disaster_prevention"
    - place: "fuji"
  mapping_logic: |
    イギリスの「通行権管理」を
    富士山の「登山者安全管理」に読み替える。
    
    - public right of way → 登山ルート
    - definitive map → 登山者動態把握システム
    - landowner's duty → 山小屋・自治体の責任
    - rambler's right → 登山者の権利と義務
```

**ドメイン間マッピング**：

| イギリス（アクセス権） | 富士山（防災） |
|------------------------|----------------|
| 通行権の確立 | 登山ルートの指定・管理 |
| 確定地図（definitive map） | 登山者位置把握システム |
| 土地所有者の維持義務 | 山小屋・管理者の情報提供義務 |
| 市民の通行権 | 登山者の安全を守られる権利 |
| trespass（不法侵入） | 立入禁止区域への侵入 |

---

# 1. 抽出：確定地図パターン → 登山者動態把握

```yaml
section_id: "SEC-EXTRACT-01"
anchorage:
  - view: "pattern_transfer"
  - phase: "hypothesis"
  - focus: "solution"
  - domain: "disaster_prevention"
  - place: "fuji"
intent: |
  イギリスの definitive map（確定地図）制度を、
  富士山における登山者動態把握システムの制度設計に転用する。
refs:
  - uri: "imdoc.case.uk_countryside_access.iwamoto1997#IE-PAT-UK-DEFINITIVE-MAP"
    role: "extracted_from"
  - uri: "imdoc.case.uk_countryside_access.iwamoto1997#SEC-IWAMOTO-02"
    role: "source_section"
```

## 抽出元 IdeaEntity

```yaml
extracted_entity:
  id: "IE-PAT-UK-DEFINITIVE-MAP"
  original_payload: |
    パターン：Definitive Map（確定地図）
    
    問題：アクセス可能なルートが不明確で紛争が生じる
    解決：すべての公共通行権を地図上に記録し法的証拠とする
    
    構成要素：
    - 地図の作成・更新手続き
    - 異議申立・確定手続き
    - 法的効力の付与
    - 維持管理責任の明確化
```

## 転用仮説

```yaml
occurrences:
  - id: "occ-extract-01-001"
    role: "transfer_hypothesis"
    entity: "IE-FUJI-HIKER-REGISTRY"
    note: "確定地図 → 登山者登録・追跡システム"

  - id: "occ-extract-01-002"
    role: "mechanism"
    entity: "IE-FUJI-BEACON-AS-REGISTRY"
    note: "ビーコン配布を確定地図的制度として設計"

  - id: "occ-extract-01-003"
    role: "gap"
    entity: "IE-FUJI-VOLUNTARY-VS-MANDATORY"
    note: "任意参加 vs 義務化の設計判断"
```

## 転用 IdeaEntities

```yaml
idea_entities:
  - id: "IE-FUJI-HIKER-REGISTRY"
    atomic_state: true
    payload: |
      転用仮説：登山者登録・追跡システムの制度化
      
      イギリスの確定地図が「ルートの法的確定」であるのに対し、
      富士山では「登山者の位置の確定」が課題となる。
      
      転用の構造：
      - 確定地図 → 登山者動態データベース
      - 地図の法的効力 → 登録データの法的・運用的効力
      - 異議申立手続き → 登録情報の訂正・更新手続き
      
      御嶽山の教訓：入山者数が不明で救助活動が困難
      → 「誰がどこにいるか」の可視化・確定が本質的課題
    refs:
      - uri: "IE-PAT-UK-DEFINITIVE-MAP"
        role: "derived_from"

  - id: "IE-FUJI-BEACON-AS-REGISTRY"
    atomic_state: true
    payload: |
      富士山チャレンジのビーコンシステムを「確定地図」的に設計する仮説：
      
      現状（実証実験）：
      - ビーコン配布は任意参加
      - 2018年で14,672名がモニター協力
      - 3時間で97%の位置把握が可能
      
      制度化への示唆（イギリスからの転用）：
      1. 法的根拠：登山届と連動した位置把握の法的位置づけ
      2. 網羅性：全登山者を対象とする仕組み（任意→義務化の段階設計）
      3. 確定性：位置情報の法的証拠としての扱い（救助責任の判断基準）
      4. 更新手続き：リアルタイム更新と事後確定の使い分け
    refs:
      - uri: "biblio:YOSHIMOTO2019"
        role: "source"

  - id: "IE-FUJI-VOLUNTARY-VS-MANDATORY"
    atomic_state: true
    payload: |
      任意参加 vs 義務化の設計判断：
      
      イギリスの通行権は「権利」として確立 → 法的強制力あり
      富士山のビーコンは「実証実験」→ 任意参加
      
      段階的移行の仮説：
      1. 任意参加（現状）：モニター協力、データ蓄積
      2. 推奨（次段階）：登山届と連動、非携帯者への情報提供制限
      3. 条件付き義務（将来）：特定期間・特定ルートでの携帯義務化
      4. 全面義務（最終）：入山条件としての登録義務
      
      イギリスの「推定的供用」（20年の利用で権利成立）に倣えば、
      長期間の任意運用を経て社会的合意を形成する道筋もありうる。
    refs:
      - uri: "IE-UK-ROW-PRESUMED"
        role: "analogous_pattern"
```

---

# 2. 抽出：維持管理責任 → 山小屋・管理者の義務

```yaml
section_id: "SEC-EXTRACT-02"
anchorage:
  - view: "pattern_transfer"
  - phase: "hypothesis"
  - focus: "solution"
  - domain: "responsibility_allocation"
  - place: "fuji"
intent: |
  イギリスにおける土地所有者の維持管理義務を、
  富士山における山小屋・自治体・登山者間の責任分担に転用する。
refs:
  - uri: "imdoc.case.uk_countryside_access.iwamoto1997#IE-UK-ROW-TYPES"
    role: "extracted_from"
  - uri: "imdoc.case.uk_countryside_access.iwamoto1997#SEC-IWAMOTO-04"
    role: "source_section"
```

## 抽出元 IdeaEntity

```yaml
extracted_entity:
  id: "IE-UK-SH-LANDOWNERS"
  original_payload: |
    土地所有者（地主・自作農）：
    所有権に基づく排他的利用権を主張。
    trespass（不法侵入）に対する法的保護を重視。
    一部は保全や景観管理の担い手として自己認識。
    
    （補足）維持管理責任：
    stiles（踏み越し段）、gates の管理義務が土地所有者に課される。
```

## 転用仮説

```yaml
occurrences:
  - id: "occ-extract-02-001"
    role: "transfer_hypothesis"
    entity: "IE-FUJI-HUT-RESPONSIBILITY"
    note: "土地所有者の義務 → 山小屋の義務"

  - id: "occ-extract-02-002"
    role: "mechanism"
    entity: "IE-FUJI-RECEIVER-NETWORK"
    note: "受信機設置を維持管理義務として設計"

  - id: "occ-extract-02-003"
    role: "tradeoff"
    entity: "IE-FUJI-COST-SHARING"
    note: "義務の代償としての支援・補償"
```

## 転用 IdeaEntities

```yaml
idea_entities:
  - id: "IE-FUJI-HUT-RESPONSIBILITY"
    atomic_state: true
    payload: |
      転用仮説：山小屋の情報インフラ維持義務
      
      イギリスでは土地所有者に stiles（踏み越し段）等の維持義務がある。
      富士山では山小屋が登山道沿いの主要施設として分布。
      
      転用の構造：
      - 土地所有者 → 山小屋経営者
      - stiles の維持 → 受信機の設置・維持
      - 通行権の保障 → 登山者位置情報の収集・提供
      
      2018年実験では山小屋を中心に50カ所に受信機を設置。
      これを制度化し、山小屋の「防災インフラ維持義務」として位置づける仮説。
    refs:
      - uri: "IE-UK-SH-LANDOWNERS"
        role: "derived_from"

  - id: "IE-FUJI-RECEIVER-NETWORK"
    atomic_state: true
    payload: |
      受信機ネットワークの制度的位置づけ：
      
      現状：実証実験として山小屋の協力を得て設置
      
      制度化の仮説：
      1. 設置義務：山小屋営業許可の条件として受信機設置を義務化
      2. 維持義務：稼働状況の報告、故障時の修理義務
      3. データ提供義務：収集データの防災機関への提供義務
      4. 情報発信義務：噴火警報等の登山者への伝達義務
      
      イギリスの definitive map が自治体の作成義務であるように、
      受信機ネットワークも公的義務として位置づけることで
      網羅性と継続性を担保する。

  - id: "IE-FUJI-COST-SHARING"
    atomic_state: true
    payload: |
      義務化に伴うコスト負担の設計：
      
      イギリスでは：
      - 土地所有者の維持義務 ↔ 通行権による土地利用制限への補償は限定的
      - access agreement では補償あり、access order では強制的補償
      
      富士山への転用：
      - 山小屋の義務 ↔ 設備費・運用費の公的補助
      - 登山者の義務 ↔ 安全情報・救助サービスの提供
      
      財源候補：
      - 入山料（富士山保全協力金）の一部
      - 防災関連予算
      - 保険制度との連動（位置情報提供で保険料割引等）
    refs:
      - uri: "IE-UK-ACCESS-AGREEMENT"
        role: "analogous_pattern"
```

---

# 3. 抽出：市民運動による制度形成 → 登山文化と安全意識

```yaml
section_id: "SEC-EXTRACT-03"
anchorage:
  - view: "pattern_transfer"
  - phase: "hypothesis"
  - focus: "both"
  - domain: "social_consensus"
  - place: "fuji"
intent: |
  イギリスにおける150年にわたる市民運動による制度形成を参照し、
  富士山における登山者安全管理の社会的合意形成を検討する。
refs:
  - uri: "imdoc.case.uk_countryside_access.iwamoto1997#IE-UK-RAMBLING-MOVEMENT"
    role: "extracted_from"
  - uri: "imdoc.case.uk_countryside_access.iwamoto1997#IE-PAT-UK-CITIZEN-MOVEMENT"
    role: "extracted_from"
```

## 抽出元 IdeaEntity

```yaml
extracted_entity:
  id: "IE-UK-LESSON-INCREMENTAL"
  original_payload: |
    漸進的制度形成の教訓：
    
    イギリスのアクセス権は一挙に確立したのではなく、
    150年以上にわたる市民運動・立法・判例の積み重ねで形成された。
    
    - 1865年 Open Spaces Society 設立
    - 1932年 Rights of Way Act（推定的供用の法定化）
    - 1949年 National Parks Act（国立公園・通行権保護）
    - 2000年 CROW Act（面的アクセス権の法制化）
    
    制度は社会的合意の漸進的形成を反映する。
```

## 転用仮説

```yaml
occurrences:
  - id: "occ-extract-03-001"
    role: "transfer_hypothesis"
    entity: "IE-FUJI-SAFETY-CONSENSUS"
    note: "市民運動 → 登山安全文化の形成"

  - id: "occ-extract-03-002"
    role: "contrast"
    entity: "IE-FUJI-TOP-DOWN-VS-BOTTOM-UP"
    note: "上からの制度化 vs 下からの合意形成"

  - id: "occ-extract-03-003"
    role: "lesson"
    entity: "IE-FUJI-DISASTER-AS-TRIGGER"
    note: "災害を契機とした制度形成の加速"
```

## 転用 IdeaEntities

```yaml
idea_entities:
  - id: "IE-FUJI-SAFETY-CONSENSUS"
    atomic_state: true
    payload: |
      転用仮説：登山安全文化の漸進的形成
      
      イギリスでは Ramblers' Association 等の市民団体が
      「歩く権利」を主張し、150年かけて制度化した。
      
      富士山における類似構造：
      - 山岳会・登山団体：登山文化の担い手
      - 地元住民・山小屋：現場の安全管理者
      - 自治体・防災機関：制度の設計者
      
      「位置情報を提供することが登山者の責務である」
      という社会的合意を形成する道筋の検討。
      
      イギリスの「権利と責任のセット」に倣えば：
      - 登山者の権利：安全情報を受け取る、救助を受ける
      - 登山者の責任：位置情報を提供する、規範を遵守する

  - id: "IE-FUJI-TOP-DOWN-VS-BOTTOM-UP"
    atomic_state: true
    payload: |
      上からの制度化 vs 下からの合意形成：
      
      イギリス：下からの運動（市民団体）→ 上への立法化
      日本：上からの制度設計（行政）→ 下への浸透
      
      御嶽山・草津白根山の災害は、
      下からの合意形成を待たずに上からの制度化を加速させうる。
      
      ただしイギリスの教訓：
      - 社会的合意なき制度化は実効性が低い
      - 長期的な運用には当事者の参加が不可欠
      
      富士山チャレンジの「実証実験」フェーズは、
      この合意形成プロセスの一部として位置づけられる。
    refs:
      - uri: "IE-UK-LESSON-INCREMENTAL"
        role: "derived_from"

  - id: "IE-FUJI-DISASTER-AS-TRIGGER"
    atomic_state: true
    payload: |
      災害を契機とした制度形成の加速：
      
      御嶽山噴火（2014年）→ 富士山チャレンジ開始（2015年）
      草津白根山噴火（2018年）→ 登山者把握の課題が再認識
      
      イギリスでも象徴的事件が制度化を加速した：
      - 1932年 Kinder Scout mass trespass → アクセス権運動の象徴
      - 第二次大戦後の「平和の配当」→ 1949年国立公園法
      
      災害は「窓」（policy window）を開く。
      この機会に制度の骨格を確立することで、
      長期的な社会的合意形成の基盤となりうる。
```

---

# 4. 抽出：権利と許可の区別 → 登山規制の法的性格

```yaml
section_id: "SEC-EXTRACT-04"
anchorage:
  - view: "pattern_transfer"
  - phase: "hypothesis"
  - focus: "problem"
  - domain: "legal_design"
  - place: "fuji"
intent: |
  イギリスにおける「権利」と「許可」の法的区別を参照し、
  富士山における登山規制の法的性格を検討する。
refs:
  - uri: "imdoc.case.uk_countryside_access.iwamoto1997#IE-UK-ROW-VS-ACCESS"
    role: "extracted_from"
  - uri: "imdoc.case.uk_countryside_access.iwamoto1997#IE-UK-LESSON-TRADEOFF"
    role: "extracted_from"
```

## 抽出元 IdeaEntity

```yaml
extracted_entity:
  id: "IE-UK-ROW-VS-ACCESS"
  original_payload: |
    通行権（right of way）とアクセス権（right of access）の本質的差異：
    
    - 通行権：線的（passage to and fro）、逸脱は trespass
    - アクセス権：面的（right to roam）、区域内を自由に移動
    
    イギリスでは通行権は確立しているが、
    面的アクセス権は依然として限定的・例外的である。
```

## 転用仮説

```yaml
occurrences:
  - id: "occ-extract-04-001"
    role: "transfer_hypothesis"
    entity: "IE-FUJI-ROUTE-VS-AREA"
    note: "線的管理 vs 面的管理"

  - id: "occ-extract-04-002"
    role: "mechanism"
    entity: "IE-FUJI-TRESPASS-EQUIVALENT"
    note: "逸脱行為の法的扱い"

  - id: "occ-extract-04-003"
    role: "tradeoff"
    entity: "IE-FUJI-FREEDOM-VS-SAFETY"
    note: "登山の自由 vs 安全管理"
```

## 転用 IdeaEntities

```yaml
idea_entities:
  - id: "IE-FUJI-ROUTE-VS-AREA"
    atomic_state: true
    payload: |
      転用仮説：線的管理と面的管理の区別
      
      イギリスの right of way は「線」（ルート）に対する権利。
      逸脱は trespass（不法侵入）となる。
      
      富士山への転用：
      - 登山道（線）：指定ルートに沿った移動
      - 山域（面）：火口周辺等の危険区域
      
      噴火時の避難を考えると：
      - 通常時：線的管理（ルートに沿った追跡）
      - 緊急時：面的把握（山域全体での位置確認）
      
      富士山チャレンジの受信機は「線」上に配置（山小屋＝登山道沿い）。
      面的把握には GPS 等の追加技術が必要となる可能性。

  - id: "IE-FUJI-TRESPASS-EQUIVALENT"
    atomic_state: true
    payload: |
      逸脱行為の法的扱い：
      
      イギリス：trespass は民事上の不法行為、刑事罰は限定的
      
      富士山で考えられる「逸脱」：
      - 立入禁止区域への侵入（火口周辺、噴火警戒区域）
      - 指定ルート外への逸脱（バリエーションルート）
      - ビーコン不携帯・登山届未提出
      
      法的性格の選択肢：
      1. 行政指導（現状）：強制力なし
      2. 条例による規制：罰則付きの義務化
      3. 民事責任：救助費用の自己負担等
      4. 刑事罰：悪質な違反への適用
      
      イギリスの教訓：法的強制力よりも社会的規範の形成が重要
    refs:
      - uri: "IE-UK-PRIVATE-PUBLIC-TENSION"
        role: "analogous_pattern"

  - id: "IE-FUJI-FREEDOM-VS-SAFETY"
    atomic_state: true
    payload: |
      登山の自由 vs 安全管理のトレードオフ：
      
      イギリスの価値競合：
      - 私的所有権 vs 公共的利用権
      
      富士山の価値競合：
      - 登山の自由 vs 安全管理の必要性
      - プライバシー vs 位置情報把握
      - 個人の自己責任 vs 公的救助の義務
      
      イギリスの「権利と責任のセット」という発想は、
      このトレードオフの調整原理として参照可能：
      
      「登山する権利」には「位置情報を提供する責任」が伴う
      「救助を受ける権利」には「登山届を提出する責任」が伴う
```

---

# 5. 統合：富士山防災への示唆パッケージ

```yaml
section_id: "SEC-EXTRACT-05"
anchorage:
  - view: "synthesis"
  - phase: "hypothesis"
  - focus: "solution"
  - domain: "policy_recommendation"
  - place: "fuji"
intent: |
  抽出した各要素を統合し、
  富士山防災政策への具体的示唆としてパッケージ化する。
refs:
  - uri: "ideamark://cases/SEC-KNG-DECIDE-01"
    role: "feeds_into"
    note: "神奈川の意思決定候補への入力"
```

## Occurrences

```yaml
occurrences:
  - id: "occ-extract-05-001"
    role: "improvement_hypothesis"
    entity: "IE-FUJI-PACKAGE-FROM-UK"
    note: "イギリスからの転用パッケージ"

  - id: "occ-extract-05-002"
    role: "metric"
    entity: "IE-FUJI-EVALUATION-CRITERIA"
    note: "評価基準"

  - id: "occ-extract-05-003"
    role: "risk"
    entity: "IE-FUJI-TRANSFER-RISKS"
    note: "転用に伴うリスク"
```

## 統合 IdeaEntities

```yaml
idea_entities:
  - id: "IE-FUJI-PACKAGE-FROM-UK"
    atomic_state: false
    payload: |
      イギリス田園アクセス権制度から富士山防災への転用パッケージ
    children:
      - id: "IE-FUJI-PKG-01"
        atomic_state: true
        payload: |
          1. 登山者登録・追跡システムの制度化
          - 富士山チャレンジを制度化の基盤とする
          - 段階的に任意→推奨→義務化を検討
          - 確定地図に倣い、登録データの法的位置づけを明確化

      - id: "IE-FUJI-PKG-02"
        atomic_state: true
        payload: |
          2. 山小屋の防災インフラ維持義務
          - 受信機設置・維持を営業条件に組み込む
          - 費用は公的補助と入山料で分担
          - データ提供・情報伝達義務を明文化

      - id: "IE-FUJI-PKG-03"
        atomic_state: true
        payload: |
          3. 権利と責任のセット化
          - 「登山する権利」と「位置情報提供の責任」
          - 「救助を受ける権利」と「登山届提出の責任」
          - 行動規範として提示し、社会的合意を形成

      - id: "IE-FUJI-PKG-04"
        atomic_state: true
        payload: |
          4. 漸進的制度形成
          - 実証実験（現状）→ 推奨運用 → 条例化 → 法制化
          - 災害を契機とした「窓」を活用
          - 長期的な社会的合意形成を並行して進める

  - id: "IE-FUJI-EVALUATION-CRITERIA"
    atomic_state: true
    payload: |
      転用の評価基準（富士山チャレンジの指標を拡張）：
      
      1. 網羅性：登山者の何%を把握できるか
         - 2018年実験：14,672名（登山者全体の一部）
         - 目標：主要ルートで90%以上
      
      2. 即時性：噴火時に何分で位置把握できるか
         - 2018年実験：3時間で97%
         - 目標：30分で80%以上（避難開始の判断に間に合う）
      
      3. 持続性：システムが何年継続運用できるか
         - 現状：年次の実証実験
         - 目標：通年・継続的運用
      
      4. 受容性：登山者・山小屋の参加率
         - 現状：任意協力ベース
         - 目標：社会的規範として定着

  - id: "IE-FUJI-TRANSFER-RISKS"
    atomic_state: true
    payload: |
      転用に伴うリスク：
      
      1. 文脈の相違
         - イギリス：土地所有権 vs 公共的利用権（水平的対立）
         - 富士山：登山者の自由 vs 公的安全管理（垂直的対立）
         - 制度設計の正当化根拠が異なる
      
      2. 時間スケールの相違
         - イギリス：150年の漸進的形成
         - 富士山：噴火リスクは待ってくれない
         - 災害を契機に短期間での制度化が求められる可能性
      
      3. 技術的前提の相違
         - イギリス：紙の地図、物理的標識
         - 富士山：デジタル追跡、リアルタイム通信
         - 技術の信頼性・持続性への依存
      
      4. プライバシー問題
         - イギリスの通行権は位置追跡を含まない
         - 富士山のビーコンは個人の移動を追跡
         - 目的外利用の防止、データ管理の厳格化が必要
```

---

# Appendix A. 抽出メタデータ

```yaml
extraction_metadata:
  source_document: "imdoc.case.uk_countryside_access.iwamoto1997"
  source_sections:
    - "SEC-IWAMOTO-02"  # 通行権の法的構造
    - "SEC-IWAMOTO-04"  # 土地所有とアクセスの緊張
    - "SEC-IWAMOTO-06"  # 政策的含意
    - "SEC-IWAMOTO-07"  # Pattern Catalog
  
  extracted_entities:
    - "IE-PAT-UK-DEFINITIVE-MAP"
    - "IE-UK-ROW-VS-ACCESS"
    - "IE-UK-SH-LANDOWNERS"
    - "IE-UK-LESSON-INCREMENTAL"
    - "IE-UK-LESSON-TRADEOFF"
    - "IE-PAT-UK-CITIZEN-MOVEMENT"
  
  generated_entities:
    - "IE-FUJI-HIKER-REGISTRY"
    - "IE-FUJI-BEACON-AS-REGISTRY"
    - "IE-FUJI-VOLUNTARY-VS-MANDATORY"
    - "IE-FUJI-HUT-RESPONSIBILITY"
    - "IE-FUJI-RECEIVER-NETWORK"
    - "IE-FUJI-COST-SHARING"
    - "IE-FUJI-SAFETY-CONSENSUS"
    - "IE-FUJI-TOP-DOWN-VS-BOTTOM-UP"
    - "IE-FUJI-DISASTER-AS-TRIGGER"
    - "IE-FUJI-ROUTE-VS-AREA"
    - "IE-FUJI-TRESPASS-EQUIVALENT"
    - "IE-FUJI-FREEDOM-VS-SAFETY"
    - "IE-FUJI-PACKAGE-FROM-UK"
    - "IE-FUJI-EVALUATION-CRITERIA"
    - "IE-FUJI-TRANSFER-RISKS"
  
  transfer_type: "analogical"
  confidence: "hypothesis"
  requires_validation:
    - "法的実現可能性の検証"
    - "山小屋・登山者へのヒアリング"
    - "技術的実現可能性の確認"
    - "コスト試算"
```

---

# Appendix B. Convergent 候補

```yaml
convergent_candidates:
  - target: "ideamark://cases/SEC-KNG-FUJI-02"
    merge_entities:
      - "IE-FUJI-PACKAGE-FROM-UK" → "IE-KNG-FUJI-MEAS-01"（Timed Entry との統合）
    rationale: |
      富士山チャレンジのビーコンシステムは、
      Timed Entry（時間枠予約）と組み合わせることで、
      「予約時に登録 → 入山時にビーコン受取 → 追跡 → 下山時に返却」
      という一貫したフローを構築できる。
  
  - target: "ideamark://patterns/PAT-04"
    merge_entities:
      - "IE-FUJI-COST-SHARING" → Maintenance Funding Loop
    rationale: |
      受信機ネットワークの維持費用は、
      保全財源ループの一部として設計可能。
      入山料 → 設備維持 → 安全情報提供 → 登山者満足 → 入山料
```
