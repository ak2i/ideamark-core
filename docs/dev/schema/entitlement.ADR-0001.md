# ADR-0001: Entitlement-core Architectural Decision

- **Status**: Proposed
- **Date**: 2025-08-08
- **Domain/Subdomain**: access / entitlement
- **Maturity**: draft
- **Compat**: Cerbos-attrs, Oso

## Context
主体(ユーザー/グループ)に機能やプロジェクト等のリソースへの権利を発行/失効し、属性ベースで利用可否を判定したい。

**Context notes:**
- SaaSの機能開放/プラン差分を権利として扱いたい
- グループ委譲・有効期限付きの付与/剥奪を安全に運用したい

## Decision
エンタイトルメント台帳(EntitlementLedger) + ABAC判定I/O + URN命名ガバナンスをコアに据える。

**Key components:**
- Entitlement entity と Grant/Revoke コマンド
- DecisionRequest/Response によるABAC I/O
- URN命名ルールと予約prefix

## Consequences
**Trade-offs:**
- 発行台帳を強整合にするとスループットは低下
- 監査イベントを厚くすると書き込みコスト上昇
**Constraints:**
- (subjectId, resourceId, relation) は一意
- expiresAt は null または issuedAt より後
- time は ISO8601 / UTC 固定
- Id は reserved_prefixes 準拠の URN
**Observability:**
  - Events: EntitlementGranted, IdempotencyReused, EntitlementRevoked, EntitlementExpired, DecisionDenied
  - Metrics: grant.qps, revoke.qps, decision.allow_rate, decision.latency_ms{p50,p95}, entitlement.count{active,expired}
  - Logs: security_audit(grant/revoke/deny)

## Alternatives (Considered)
- Keep ad-hoc, unstructured templates → poor search/reuse and fragile LLM prompting.
- Hard-code logic in a single framework → low portability across stacks.

## Security & Compliance Notes
- PIIはattrs/claimsに格納しないかマスキング

## Rollout / Evolution
- versioning: relation語彙の非破壊追加、resource.kindの追加
- delegation: group:* を subject として許容
- ttl_policy: プランごとのデフォルト期限設定
- adapters: Cerbos, Oso