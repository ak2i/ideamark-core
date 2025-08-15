// Auto-generated from IdeaMark DesignDoc
// Source: StoryCraft AI Core

export type Id = string; // URN-like id e.g., 'user:123'

export interface InterestTemplate {
  /** example: template:interest:engagement_rate */
  id: Id;
  tag: string;
  label: string;
  description?: string;
  source?: string;
  category?: string;
  /** example: percentage|score|count */
  valueType?: string;
  /** example: %|件 */
  unit?: string;
  /** example: llm|function|human */
  generatedBy?: string;
  confidence?: number;
  validated?: boolean;
}

export interface StoryTemplate {
  /** example: template:story:quarterly_highlights */
  id: Id;
  title: string;
  applicableTags?: string[];
  requiredTags?: string[];
  sections: SectionSpec[];
  renderingInstructions?: string;
}

export interface Story {
  /** example: story:2025q2_highlights */
  id: Id;
  templateId: Id;
  tagsUsed?: string[];
  sections?: SectionOutput[];
  createdAt: string;
}

export interface OutputUnit {
  /** example: output:abc123 */
  outputId: Id;
  /** enum_ref: vocabulary.output_type_vocab */
  type: string;
  /** enum_ref: vocabulary.format_vocab */
  format: string;
  title?: string;
  generatedFromStoryId: Id;
  bundleId?: string;
  seriesId?: string;
  sections?: SectionOutput[];
  media?: MediaInfo;
  storage?: StorageTarget;
  notification?: NotificationConfig;
  jwtMetadata?: Record<string, unknown>;
  metadata?: Record<string, unknown>;
  createdAt: string;
}

export interface SectionSpec {
  id: string;
  /** example: text|chart|table|image */
  type: string;
  template?: string;
  requiredTags?: string[];
  /** example: interest.tag=='growth' && interest.value>0 */
  expression?: string;
  trueBranch?: SectionSpec[];
  falseBranch?: SectionSpec[];
  renderHints?: RenderHints;
}

export interface RenderHints {
  /** example: hero|grid|list */
  layout?: string;
  /** example: neutral|optimistic|critical */
  tone?: string;
  ui?: Record<string, unknown>;
}

export interface SectionOutput {
  id: string;
  type: string;
  content?: string;
  dataRef?: string;
}

export interface MediaInfo {
  url: string;
  mime: string;
  bytes?: number;
}

export interface StorageTarget {
  /** example: s3|gcs|local */
  provider: string;
  uri: string;
  /** example: ttl=30d */
  lifecycle?: string;
}

export interface NotificationConfig {
  /** example: email|webpush */
  channels?: string[];
  recipients?: string[];
  templateId?: string;
}
