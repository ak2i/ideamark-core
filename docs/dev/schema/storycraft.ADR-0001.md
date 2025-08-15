# ADR-0001: StoryCraft AI Core Architectural Decision

- **Status**: Proposed
- **Date**: 2025-08-08
- **Domain/Subdomain**: content / storycraft
- **Maturity**: draft
- **Compat**: LLM, FunctionCall, Webhook

## Context
interest_template / story_template / output_unit の3スキーマを中立表現で定義し、検索・比較・合成・自動生成をしやすくする。

**Context notes:**
- Interest → Story → Output のAI協調型生成ワークフローを標準化したい
- LLM/関数/外部APIを混在させるテンプレ駆動の生成を再利用可能にしたい

## Decision
テンプレ(Interest/Story)と成果物(OutputUnit)をシステム設計メタモデルに落とし込み、比較ファセットを明示化する。

**Key components:**
- InterestTemplate / StoryTemplate / OutputUnit の定義
- SectionSpec / RenderHints / MediaInfo 等のVO群
- Render・Publish・Notify のコマンド群

## Consequences
**Trade-offs:**
- 高度な分岐や継承はテンプレの可読性を下げる
**Constraints:**
- story_template.requiredTags は interests.tags の部分集合である
- SectionSpec.id はテンプレ内で一意
- OutputUnit は sections(narrative) または media のどちらかを必須
- URI/URL/時間はISO8601/UTC, format は vocabulary.format_vocab に従う
**Observability:**
  - Events: StoryRendered, OutputGenerated, OutputPublished, NotificationSent
  - Metrics: render.latency_ms{p50,p95}, output.count{by_type}, publish.success_rate
  - Logs: audit(render/publish/notify)

## Alternatives (Considered)
- Keep ad-hoc, unstructured templates → poor search/reuse and fragile LLM prompting.
- Hard-code logic in a single framework → low portability across stacks.

## Security & Compliance Notes
- 生成物にPIIを含む場合は出力時にマスキング/同意管理

## Rollout / Evolution
- versioning: story_template の継承(base_template_id)と非破壊追加
- composition: SectionSpec の再利用コンポーネント化
- adapters: Webhook, Storage(S3/GCS), Notifier(Email/WebPush)