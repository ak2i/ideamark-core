// Auto-generated from IdeaMark DesignDoc
// Source: Entitlement-core

export type Id = string; // URN-like id e.g., 'user:123'

export interface Principal {
  /** example: user:123 */
  id: Id;
  roles?: string[];
  attrs?: Record<string, unknown>;
  claims?: Record<string, unknown>;
}

export interface Resource {
  /** example: feature:pro_reports */
  id: Id;
  kind: "feature" | "document" | "project";
  attrs?: Record<string, unknown>;
}

export interface Entitlement {
  subjectId: Id;
  resourceId: Id;
  /** enum_ref: vocabulary.relation_vocab */
  relation: string;
  issuedAt?: string;
  expiresAt?: string | null;
  meta?: Record<string, unknown>;
}

export interface DecisionContext {
  time?: string;
  ip?: string;
  userAgent?: string;
  sessionId?: string;
  extra?: Record<string, unknown>;
}

export interface DecisionRequest {
  principal: Principal;
  resource: Resource;
  /** enum_ref: vocabulary.action_vocab */
  action: string;
  context?: DecisionContext;
}

export interface DecisionResponse {
  allow: boolean;
  reason?: string;
  debug?: Record<string, unknown>;
}
