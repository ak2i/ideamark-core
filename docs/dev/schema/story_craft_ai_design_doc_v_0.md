# StoryCraft AI DesignDoc v0.1（IdeaMark Template に準拠した拡張サンプル）

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
id: IdeaMark-3d2a9c88-3b1f-4c07-9b2e-5c6f9a4d1e77
title: StoryCraft AI Core
type: system_design
author: you@example.com
provenance:
  owner: storycraft-core-team
  authors: [you@example.com]
  last_updated: '2025-08-09T00:00:00Z'
  license: CC0-1.0
context:
  - Interest → Story → Output のAI協調型生成ワークフローを標準化したい
  - LLM/関数/外部APIを混在させるテンプレ駆動の生成を再利用可能にしたい
problem:
  summary: interest_template / story_template / output_unit の3スキーマを中立表現で定義し、検索・比較・合成・自動生成をしやすくする。
  factors:
    - 同一タグ語彙に基づくテンプレ合成が要件
    - GUI/ノード構成や継承による再利用も視野
solution:
  approach: テンプレ(Interest/Story)と成果物(OutputUnit)をシステム設計メタモデルに落とし込み、比較ファセットを明示化する。
  components:
    - InterestTemplate / StoryTemplate / OutputUnit の定義
    - SectionSpec / RenderHints / MediaInfo 等のVO群
    - Render・Publish・Notify のコマンド群
  examples:
    - SECデータから抽出した複数Interestで「四半期ハイライト」ストーリーを生成しPDF配布
metadata:
  tags: [storycraft, template, content-generation, publishing]
range:
  spatial: global
  temporal: mid-term
  social_scope: organization
granularity:
  level: strategic
  description: 実装非依存のテンプレ/出力構造の合意
usage_scenarios:
  - 投資家向けレポート（Qvest）
  - 広告ストーリー（Questory）
  - 一般的な自動レポーティング

# -------------------------------
# System Design extension (DesignDoc v0.1)
# -------------------------------
design:
  version: ideamark-design/0.1

  taxonomy:
    domain: content
    subdomain: storycraft
    patterns: [InterestTemplate, StoryTemplate, OutputUnit, RenderingPipeline]
    maturity: draft
    compat: [LLM, FunctionCall, Webhook]

  vocabulary:
    reserved_prefixes: [interest, story, output, bundle, series, media, template]
    tag_vocab: []            # 任意: ドメイン共通タグを列挙
    format_vocab: [text, image, video, audio, pdf]
    output_type_vocab: [narrative, media]
    action_vocab: [analyze, validate, select, render, bundle, publish, notify]
    resource_kinds: [interest_template, story_template, output_unit, story, media]

  applicability:
    applies_when:
      - テンプレ駆動でNarrative/Mediaを生成・配布する
      - タグや式に基づく分岐/再利用を行う
    not_applies_when:
      - 厳密なリアルタイム合成(ミリ秒単位)で複雑な動画編集が必須
    scale_consistency:
      consistency: Strong for template registry; eventual for read-heavy rendering
      expected_qps:
        render: "<= thousands/min"
        publish: "<= hundreds/min"
    tradeoffs:
      - 高度な分岐や継承はテンプレの可読性を下げる
    regulatory_notes:
      - 生成物にPIIを含む場合は出力時にマスキング/同意管理

  comparability:
    shape_signature:
      id_scheme: "URN (prefix:slug) e.g., story:2025q2_highlights"
      uniqueness:
        - SectionSpec.id は story_template 内で一意
        - OutputUnit.outputId はグローバル一意
      time_semantics: "createdAt は ISO8601/UTC; ttl は 'timestamp|null'"
    capability_vector:
      commands:
        - "GenerateInterest(inputRef, adapter?) -> 'Interest[]'"
        - "ValidateInterest(interest) -> 'ValidationResult'"
        - "SelectStoryTemplate(requiredTags, optionalTags?) -> 'StoryTemplate'"
        - "RenderStory(storyTemplateId, interests, options?) -> 'Story'"
        - "GenerateOutputUnit(storyId, format, storage?) -> 'OutputUnit'"
        - "PublishOutputUnit(outputId, channels, jwtConfig?) -> 'Success'"
        - "Notify(outputId, channels) -> 'Success'"
      queries:
        - "ListStoryTemplatesByTags(tags) -> 'StoryTemplate[]'"
        - "ListInterestsByTag(tag) -> 'Interest[]'"
        - "GetOutput(outputId) -> 'OutputUnit'"
        - "ListOutputsByBundle(bundleId) -> 'OutputUnit[]'"
      policies:
        - "CanPublish(principal, output)"
        - "CanReadMedia(principal, media)"
    constraint_set:
      - "story_template.required_tags は interests.tags の部分集合である"
      - "SectionSpec.id はテンプレ内で一意"
      - "OutputUnit は sections(narrative) または media のどちらかを必須"
      - "URI/URL/時間はISO8601/UTC, format は vocabulary.format_vocab に従う"
    observability_pack:
      events: [StoryRendered, OutputGenerated, OutputPublished, NotificationSent]
      metrics: [render.latency_ms{p50,p95}, output.count{by_type}, publish.success_rate]
      logs: [audit(render/publish/notify)]
    evolvability_hooks:
      versioning: story_template の継承(base_template_id)と非破壊追加
      composition: SectionSpec の再利用コンポーネント化
      adapters: [Webhook, Storage(S3/GCS), Notifier(Email/WebPush)]

  naming:
    style: camelCase
    urn:
      format: "<prefix>:<slug>"
      reserved_prefixes: [interest, story, output, bundle, series, media, template]
      collision_policy: reject on registry; suggest slug mutation

  domain:
    entities:
      - name: InterestTemplate
        ns: storycraft
        attrs:
          - { name: id, type: Id, required: true, example: "template:interest:engagement_rate" }
          - { name: tag, type: string, required: true }
          - { name: label, type: string, required: true }
          - { name: description, type: string, required: false }
          - { name: source, type: string, required: false }
          - { name: category, type: string, required: false }
          - { name: valueType, type: string, required: false, example: "percentage|score|count" }
          - { name: unit, type: string, required: false, example: "%|件" }
          - { name: generatedBy, type: string, required: false, example: "llm|function|human" }
          - { name: confidence, type: number, required: false }
          - { name: validated, type: boolean, required: false }
      - name: StoryTemplate
        ns: storycraft
        attrs:
          - { name: id, type: Id, required: true, example: "template:story:quarterly_highlights" }
          - { name: title, type: string, required: true }
          - { name: applicableTags, type: 'string[]', required: false }
          - { name: requiredTags, type: 'string[]', required: false }
          - { name: sections, type: 'SectionSpec[]', required: true }
          - { name: renderingInstructions, type: string, required: false }
      - name: Story
        ns: storycraft
        attrs:
          - { name: id, type: Id, required: true, example: "story:2025q2_highlights" }
          - { name: templateId, type: Id, required: true }
          - { name: tagsUsed, type: 'string[]', required: false }
          - { name: sections, type: 'SectionOutput[]', required: false }
          - { name: createdAt, type: timestamp, required: true }
      - name: OutputUnit
        ns: storycraft
        attrs:
          - { name: outputId, type: Id, required: true, example: "output:abc123" }
          - { name: type, type: string, required: true, enum_ref: vocabulary.output_type_vocab }
          - { name: format, type: string, required: true, enum_ref: vocabulary.format_vocab }
          - { name: title, type: string, required: false }
          - { name: generatedFromStoryId, type: Id, required: true }
          - { name: bundleId, type: string, required: false }
          - { name: seriesId, type: string, required: false }
          - { name: sections, type: 'SectionOutput[]', required: false }
          - { name: media, type: MediaInfo, required: false }
          - { name: storage, type: StorageTarget, required: false }
          - { name: notification, type: NotificationConfig, required: false }
          - { name: jwtMetadata, type: 'map<string, any>', required: false }
          - { name: metadata, type: 'map<string, any>', required: false }
          - { name: createdAt, type: timestamp, required: true }
    valueObjects:
      - name: SectionSpec
        attrs:
          - { name: id, type: string, required: true }
          - { name: type, type: string, required: true, example: "text|chart|table|image" }
          - { name: template, type: string, required: false }
          - { name: requiredTags, type: 'string[]', required: false }
          - { name: expression, type: string, required: false, example: "interest.tag=='growth' && interest.value>0" }
          - { name: trueBranch, type: 'SectionSpec[]', required: false }
          - { name: falseBranch, type: 'SectionSpec[]', required: false }
          - { name: renderHints, type: RenderHints, required: false }
      - name: RenderHints
        attrs:
          - { name: layout, type: string, required: false, example: "hero|grid|list" }
          - { name: tone, type: string, required: false, example: "neutral|optimistic|critical" }
          - { name: ui, type: 'map<string, any>', required: false }
      - name: SectionOutput
        attrs:
          - { name: id, type: string, required: true }
          - { name: type, type: string, required: true }
          - { name: content, type: string, required: false }
          - { name: dataRef, type: string, required: false }
      - name: MediaInfo
        attrs:
          - { name: url, type: string, required: true }
          - { name: mime, type: string, required: true }
          - { name: bytes, type: number, required: false }
      - name: StorageTarget
        attrs:
          - { name: provider, type: string, required: true, example: "s3|gcs|local" }
          - { name: uri, type: string, required: true }
          - { name: lifecycle, type: string, required: false, example: "ttl=30d" }
      - name: NotificationConfig
        attrs:
          - { name: channels, type: 'string[]', required: false, example: "email|webpush" }
          - { name: recipients, type: 'string[]', required: false }
          - { name: templateId, type: string, required: false }

    enums: []
    relations:
      - name: SectionIdUniqWithinTemplate
        kind: UNIQUE
        on: [id]

  capabilities:
    commands:
      - name: GenerateInterest
        input:
          - { name: inputRef, type: string, required: true }
          - { name: adapter, type: string, required: false }
        output: ['Interest[]']
      - name: ValidateInterest
        input:
          - { name: interest, type: 'map<string, any>', required: true }
        output: ['ValidationResult']
      - name: SelectStoryTemplate
        input:
          - { name: requiredTags, type: 'string[]', required: true }
          - { name: optionalTags, type: 'string[]', required: false }
        output: ['StoryTemplate']
      - name: RenderStory
        input:
          - { name: storyTemplateId, type: Id, required: true }
          - { name: interests, type: 'Interest[]', required: true }
          - { name: options, type: 'map<string, any>', required: false }
        output: ['Story']
      - name: GenerateOutputUnit
        input:
          - { name: storyId, type: Id, required: true }
          - { name: format, type: string, required: true, enum_ref: vocabulary.format_vocab }
          - { name: storage, type: StorageTarget, required: false }
        output: ['OutputUnit']
      - name: PublishOutputUnit
        input:
          - { name: outputId, type: Id, required: true }
          - { name: channels, type: 'string[]', required: true }
          - { name: jwtConfig, type: 'map<string, any>', required: false }
        output: ['Success']
      - name: Notify
        input:
          - { name: outputId, type: Id, required: true }
          - { name: channels, type: 'string[]', required: true }
        output: ['Success']
    queries:
      - name: ListStoryTemplatesByTags
        input:
          - { name: tags, type: 'string[]', required: true }
        output: ['StoryTemplate[]']
      - name: ListInterestsByTag
        input:
          - { name: tag, type: string, required: true }
        output: ['Interest[]']
      - name: GetOutput
        input:
          - { name: outputId, type: Id, required: true }
        output: ['OutputUnit']
      - name: ListOutputsByBundle
        input:
          - { name: bundleId, type: string, required: true }
        output: ['OutputUnit[]']

  policies:
    - name: CanPublish
      dsl: |
        allow(principal, output, action) if
          action == "publish" &&
          'admin' in principal.roles;
    - name: CanReadMedia
      dsl: |
        allow(principal, media, action) if
          action == "read" &&
          (media.public == true or 'member' in principal.roles);

  constraints:
    - story_template.requiredTags ⊆ interests.tags
    - SectionSpec.id は story_template 内で一意
    - OutputUnit は sections(narrative) または media のどちらかを必須
    - すべての時間は ISO8601/UTC

  scenarios:
    - id: select-and-render-story
      given:
        interests:
          - { tag: growth, value: 0.12 }
          - { tag: churn, value: 0.03 }
      when:
        command: SelectStoryTemplate
        args: { requiredTags: [growth], optionalTags: [churn] }
      then:
        command: RenderStory
        args: { storyTemplateId: template:story:quarterly_highlights, interests: [{ tag: growth, value: 0.12 }, { tag: churn, value: 0.03 }] }
      expect:
        events: [StoryRendered]

    - id: generate-output-and-publish
      given:
        storyId: story:2025q2_highlights
      when:
        command: GenerateOutputUnit
        args: { storyId: story:2025q2_highlights, format: pdf, storage: { provider: s3, uri: s3://bucket/report.pdf } }
      then:
        command: PublishOutputUnit
        args: { outputId: output:abc123, channels: [email] }
      expect:
        events: [OutputGenerated, OutputPublished]

  artifacts:
    typescript: https://example.com/artifacts/storycraft-core/types.ts
    json_schema: https://example.com/artifacts/storycraft-core/schema.json
    adr: https://example.com/artifacts/storycraft-core/adr-0001.md
```

