# About the IdeaMark Schema (Revised)

_Generated from `/mnt/data/ideamark.schema.yaml` on 2025-08-15 21:56 UTC._

This document is an AI-facing guide to the **IdeaMark** JSON Schema. It reflects the corrected, stricter version intended for TypeScript code generation, runtime validation, and LLM interpretation.

## Root
- **Type**: `object`
- **Title**: IdeaMark Template Schema
- **Description**: Schema for documenting structured, reusable patterns for social, industrial, or business challenges and solutions. It also supports an optional system-design extension (`design`, DesignDoc v0.1) to maximize searchability, reuse, and LLM-friendly comparison/composition. This schema is suitable for TypeScript type generation, runtime validation, and AI interpretation.
- **Required root fields**: id, title, type, problem, solution
- **Additional properties**: not allowed at the root

### Top-level Fields
- `id` — **Type**: string; **Purpose**: Globally unique ID (UUID format prefixed with 'IdeaMark-'); **Pattern**: `^IdeaMark-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
- `title` — **Type**: string; **Purpose**: Human-readable title of the IdeaMark pattern
- `type` — **Type**: string; **Purpose**: Domain or category tag (e.g., 'system_design', 'urban_design', 'platform_pivot')
- `author` — **Type**: string; **Purpose**: Optional contact; GitHub ID, email, or SNS handle
- `provenance` — **Type**: object; **Purpose**: Optional provenance for search/reuse; **Additional properties**: not allowed; **Fields**:
  - `owner` — **Type**: string
  - `authors` — **Type**: array; **Items**: string
  - `last_updated` — **Type**: string (format: date-time)
  - `license` — **Type**: string
- `context` — **Type**: array; **Purpose**: Background contexts where this pattern applies; **Items**: string
- `problem` — **Type**: object; **Required fields**: summary; **Additional properties**: not allowed; **Fields**:
  - `summary` — **Type**: string
  - `factors` — **Type**: array; **Items**: string
- `solution` — **Type**: object; **Required fields**: approach; **Additional properties**: not allowed; **Fields**:
  - `approach` — **Type**: string
  - `components` — **Type**: array; **Items**: string
  - `examples` — **Type**: array; **Items**: string
- `children` — **Type**: array; **Purpose**: List of child IdeaMark IDs; **Items**: string
- `relations` — **Type**: object; **Additional properties**: not allowed; **Fields**:
  - `siblings` — **Type**: array; **Items**: string
  - `derived_from` — **Type**: array; **Items**: string
- `metadata` — **Type**: object; **Additional properties**: not allowed; **Fields**:
  - `tags` — **Type**: array; **Items**: string
  - `scalefactor` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `timewindow` — **Type**: string
    - `spacemetrics` — **Type**: string
    - `regions` — **Type**: array; **Items**: string
    - `organizations` — **Type**: array; **Items**: string
- `range` — **Type**: object; **Additional properties**: not allowed; **Fields**:
  - `spatial` — **Type**: string (enum: global, national, regional, local, site-specific); **Allowed**: `global, national, regional, local, site-specific`
  - `temporal` — **Type**: string (enum: long-term, mid-term, short-term); **Allowed**: `long-term, mid-term, short-term`
  - `social_scope` — **Type**: string (enum: individual, group, organization, community, society, civilization); **Allowed**: `individual, group, organization, community, society, civilization`
- `granularity` — **Type**: object; **Additional properties**: not allowed; **Fields**:
  - `level` — **Type**: string (enum: conceptual, strategic, tactical, operational, implementation); **Allowed**: `conceptual, strategic, tactical, operational, implementation`
  - `description` — **Type**: string
- `reference` — **Type**: array; **Items**: object
- `evidence` — **Type**: array; **Items**: object
- `usage_scenarios` — **Type**: array; **Items**: string
- `access` — **Type**: object; **Required fields**: uri, visibility; **Additional properties**: not allowed; **Fields**:
  - `uri` — **Type**: string (format: uri)
  - `visibility` — **Type**: string (enum: public, private, restricted); **Allowed**: `public, private, restricted`
  - `credentials` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `type` — **Type**: string (enum: basic_auth, oauth, token, session); **Allowed**: `basic_auth, oauth, token, session`
    - `contact` — **Type**: string
- `timeline` — **Type**: array; **Items**: object
- `dependencies` — **Type**: array; **Items**: object
- `observed_metrics` — **Type**: array; **Items**: object
- `patterns` — **Type**: array; **Items**: object
- `hypotheses` — **Type**: array; **Items**: object
- `design` — **Type**: object; **Purpose**: Optional DesignDoc v0.1 for system design patterns and specs.; **Required fields**: version; **Additional properties**: not allowed; **Fields**:
  - `version` — **Type**: string; **Pattern**: `^ideamark-design/0\.1$`
  - `taxonomy` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `domain` — **Type**: string
    - `subdomain` — **Type**: string
    - `patterns` — **Type**: array; **Items**: string
    - `maturity` — **Type**: string (enum: draft, beta, prod); **Allowed**: `draft, beta, prod`
    - `compat` — **Type**: array; **Items**: string
  - `vocabulary` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `reserved_prefixes` — **Type**: array; **Items**: string
    - `relation_vocab` — **Type**: array; **Items**: string
    - `action_vocab` — **Type**: array; **Items**: string
    - `resource_kinds` — **Type**: array; **Items**: string
    - `tag_vocab` — **Type**: array; **Items**: string
    - `format_vocab` — **Type**: array; **Items**: string
    - `output_type_vocab` — **Type**: array; **Items**: string
  - `applicability` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `applies_when` — **Type**: array; **Items**: string
    - `not_applies_when` — **Type**: array; **Items**: string
    - `scale_consistency` — **Type**: object; **Additional properties**: not allowed; **Fields**:
      - `consistency` — **Type**: string
      - `expected_qps` — **Type**: object; **Additional properties**: string
    - `tradeoffs` — **Type**: array; **Items**: string
    - `regulatory_notes` — **Type**: array; **Items**: string
  - `comparability` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `shape_signature` — **Type**: object; **Additional properties**: not allowed; **Fields**:
      - `id_scheme` — **Type**: string
      - `uniqueness` — **Type**: array; **Items**: string
      - `time_semantics` — **Type**: string
    - `capability_vector` — **Type**: object; **Additional properties**: not allowed; **Fields**:
      - `commands` — **Type**: array; **Items**: string
      - `queries` — **Type**: array; **Items**: string
      - `policies` — **Type**: array; **Items**: string
    - `constraint_set` — **Type**: array; **Items**: string
    - `observability_pack` — **Type**: object; **Additional properties**: not allowed; **Fields**:
      - `events` — **Type**: array; **Items**: string
      - `metrics` — **Type**: array; **Items**: string
      - `logs` — **Type**: array; **Items**: string
    - `evolvability_hooks` — **Type**: object; **Additional properties**: not allowed; **Fields**:
      - `versioning` — **Type**: string
      - `delegation` — **Type**: string
      - `ttl_policy` — **Type**: string
      - `adapters` — **Type**: array; **Items**: string
  - `naming` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `style` — **Type**: string
    - `urn` — **Type**: object; **Additional properties**: not allowed; **Fields**:
      - `format` — **Type**: string
      - `reserved_prefixes` — **Type**: array; **Items**: string
      - `collision_policy` — **Type**: string
  - `domain` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `entities` — **Type**: array; **Items**: ref: `#/$defs/EntityDef`
    - `valueObjects` — **Type**: array; **Items**: ref: `#/$defs/ValueObjectDef`
    - `enums` — **Type**: array; **Items**: ref: `#/$defs/EnumDef`
    - `relations` — **Type**: array; **Items**: ref: `#/$defs/RelationDef`
  - `capabilities` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `commands` — **Type**: array; **Items**: ref: `#/$defs/CommandDef`
    - `queries` — **Type**: array; **Items**: ref: `#/$defs/QueryDef`
  - `policies` — **Type**: array; **Items**: ref: `#/$defs/PolicyDef`
  - `constraints` — **Type**: array; **Items**: string
  - `scenarios` — **Type**: array; **Items**: ref: `#/$defs/ScenarioDef`
  - `artifacts` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `typescript` — **Type**: string (format: uri)
    - `json_schema` — **Type**: string (format: uri)
    - `adr` — **Type**: string (format: uri)

## Optional `design` Block (DesignDoc v0.1)
- **Additional properties**: not allowed within `design`.

### `design` Fields
- `version` — **Type**: string; **Pattern**: `^ideamark-design/0\.1$`
- `taxonomy` — **Type**: object; **Additional properties**: not allowed; **Fields**:
  - `domain` — **Type**: string
  - `subdomain` — **Type**: string
  - `patterns` — **Type**: array; **Items**: string
  - `maturity` — **Type**: string (enum: draft, beta, prod); **Allowed**: `draft, beta, prod`
  - `compat` — **Type**: array; **Items**: string
- `vocabulary` — **Type**: object; **Additional properties**: not allowed; **Fields**:
  - `reserved_prefixes` — **Type**: array; **Items**: string
  - `relation_vocab` — **Type**: array; **Items**: string
  - `action_vocab` — **Type**: array; **Items**: string
  - `resource_kinds` — **Type**: array; **Items**: string
  - `tag_vocab` — **Type**: array; **Items**: string
  - `format_vocab` — **Type**: array; **Items**: string
  - `output_type_vocab` — **Type**: array; **Items**: string
- `applicability` — **Type**: object; **Additional properties**: not allowed; **Fields**:
  - `applies_when` — **Type**: array; **Items**: string
  - `not_applies_when` — **Type**: array; **Items**: string
  - `scale_consistency` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `consistency` — **Type**: string
    - `expected_qps` — **Type**: object; **Additional properties**: string
  - `tradeoffs` — **Type**: array; **Items**: string
  - `regulatory_notes` — **Type**: array; **Items**: string
- `comparability` — **Type**: object; **Additional properties**: not allowed; **Fields**:
  - `shape_signature` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `id_scheme` — **Type**: string
    - `uniqueness` — **Type**: array; **Items**: string
    - `time_semantics` — **Type**: string
  - `capability_vector` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `commands` — **Type**: array; **Items**: string
    - `queries` — **Type**: array; **Items**: string
    - `policies` — **Type**: array; **Items**: string
  - `constraint_set` — **Type**: array; **Items**: string
  - `observability_pack` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `events` — **Type**: array; **Items**: string
    - `metrics` — **Type**: array; **Items**: string
    - `logs` — **Type**: array; **Items**: string
  - `evolvability_hooks` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `versioning` — **Type**: string
    - `delegation` — **Type**: string
    - `ttl_policy` — **Type**: string
    - `adapters` — **Type**: array; **Items**: string
- `naming` — **Type**: object; **Additional properties**: not allowed; **Fields**:
  - `style` — **Type**: string
  - `urn` — **Type**: object; **Additional properties**: not allowed; **Fields**:
    - `format` — **Type**: string
    - `reserved_prefixes` — **Type**: array; **Items**: string
    - `collision_policy` — **Type**: string
- `domain` — **Type**: object; **Additional properties**: not allowed; **Fields**:
  - `entities` — **Type**: array; **Items**: ref: `#/$defs/EntityDef`
  - `valueObjects` — **Type**: array; **Items**: ref: `#/$defs/ValueObjectDef`
  - `enums` — **Type**: array; **Items**: ref: `#/$defs/EnumDef`
  - `relations` — **Type**: array; **Items**: ref: `#/$defs/RelationDef`
- `capabilities` — **Type**: object; **Additional properties**: not allowed; **Fields**:
  - `commands` — **Type**: array; **Items**: ref: `#/$defs/CommandDef`
  - `queries` — **Type**: array; **Items**: ref: `#/$defs/QueryDef`
- `policies` — **Type**: array; **Items**: ref: `#/$defs/PolicyDef`
- `constraints` — **Type**: array; **Items**: string
- `scenarios` — **Type**: array; **Items**: ref: `#/$defs/ScenarioDef`
- `artifacts` — **Type**: object; **Additional properties**: not allowed; **Fields**:
  - `typescript` — **Type**: string (format: uri)
  - `json_schema` — **Type**: string (format: uri)
  - `adr` — **Type**: string (format: uri)

## `$defs` (Reusable Shapes for `design`)
### `AttrDef`
- **Required**: name, type
- **Additional properties**: not allowed
#### Fields
  - `name` — **Type**: string
  - `type` — **Type**: string
  - `required` — **Type**: boolean
  - `enum` — **Type**: array; **Items**: string
  - `enum_ref` — **Type**: string; **Purpose**: Path-like pointer to a vocabulary list (e.g., 'vocabulary.relation_vocab')
  - `example` — **Type**: any

### `EntityDef`
- **Required**: name
- **Additional properties**: not allowed
#### Fields
  - `name` — **Type**: string
  - `ns` — **Type**: string
  - `attrs` — **Type**: array; **Items**: ref: `#/$defs/AttrDef`

### `ValueObjectDef`
- **Required**: name
- **Additional properties**: not allowed
#### Fields
  - `name` — **Type**: string
  - `attrs` — **Type**: array; **Items**: ref: `#/$defs/AttrDef`

### `EnumDef`
- **Required**: name, values
- **Additional properties**: not allowed
#### Fields
  - `name` — **Type**: string
  - `values` — **Type**: array; **Items**: string

### `RelationDef`
- **Required**: name, kind, True
- **Additional properties**: not allowed
#### Fields
  - `name` — **Type**: string
  - `kind` — **Type**: string (enum: UNIQUE); **Allowed**: `UNIQUE`
  - `True` — **Type**: array; **Items**: string

### `CommandDef`
- **Required**: name
- **Additional properties**: not allowed
#### Fields
  - `name` — **Type**: string
  - `input` — **Type**: array; **Items**: ref: `#/$defs/AttrDef`
  - `output` — **Type**: array; **Items**: string
  - `invariants` — **Type**: array; **Items**: string

### `QueryDef`
- **Required**: name
- **Additional properties**: not allowed
#### Fields
  - `name` — **Type**: string
  - `input` — **Type**: array; **Items**: ref: `#/$defs/AttrDef`
  - `output` — **Type**: array; **Items**: string

### `PolicyDef`
- **Required**: name
- **Additional properties**: not allowed
#### Fields
  - `name` — **Type**: string
  - `dsl` — **Type**: string

### `ScenarioDef`
- **Required**: id
- **Additional properties**: not allowed
#### Fields
  - `id` — **Type**: string
  - `given` — **Type**: object
  - `precondition` — **Type**: array; **Items**: any
  - `when` — **Type**: object
  - `then` — **Type**: object
  - `expect` — **Type**: object
