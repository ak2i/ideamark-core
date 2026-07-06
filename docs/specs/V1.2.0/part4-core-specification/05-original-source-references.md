# 5. Original Source References

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 5.1 Purpose

`sources` records Original Source references.

Original Sources are materials that a document uses, observes, transforms, extracts from, compares against, or reconstructs access to.

A Source reference identifies material; it does not by itself define the meaning extracted from that material.

Sections, Occurrences, Entities, and anchors provide the access structure that relates reusable material to sources.

## 5.2 Required Shape

`sources` MUST be an array.

Each item in `sources` MUST be a mapping object.

Each Source object MUST contain:

```yaml
sources:
  - id: src-001
```

A Source object SHOULD contain:

```yaml
sources:
  - id: src-001
    type: document
    title: Example Source
    uri: ./example-source.md
```

## 5.3 Required Fields

| Field | Type | Requirement |
| --- | --- | --- |
| `id` | string | MUST |

The `id` field identifies the source within this document.

A validator MUST reject missing, null, empty, or non-string source IDs.

A validator MUST reject duplicate source IDs within `sources`.

## 5.4 Recommended Fields

| Field | Type | Meaning |
| --- | --- | --- |
| `type` | string | Source type |
| `title` | string | Human-readable title |
| `uri` | string | Source URI or path |
| `description` | string | Human-readable description |
| `revision` | string | Version, commit, edition, or revision |
| `accessed_at` | string | Timestamp when source was accessed |
| `media_type` | string | Media type or MIME-like type |
| `lang` | string | Source language |
| `license` | string or mapping | Source license information |
| `authors` | array | Source author or contributor names |

Core mode does not require all recommended fields because some Original Sources may be private, generated, temporary, composite, or not addressable by stable URI.

Profiles MAY require stronger source metadata.

## 5.5 Source Type

`type` SHOULD identify the general kind of source.

Recommended source type values are:

- `document`
- `web_page`
- `code_file`
- `repository`
- `dataset`
- `image`
- `audio`
- `video`
- `stream`
- `generated_artifact`
- `composite`
- `other`

Core mode validators SHOULD warn on unknown source type values unless declared by a profile.

Strict mode MAY reject unknown source type values.

The source type vocabulary is intentionally open to support future media types and domain-specific profiles.

## 5.6 URI and Addressability

`uri` SHOULD identify where the source can be found or how it was referenced at authoring time.

A URI MAY be:

- a relative path;
- an absolute URL;
- an IdeaMark URI;
- a repository path;
- a content-addressed URI;
- a local system URI;
- a profile-defined identifier.

A missing `uri` does not make a Source invalid in Core mode if the source is still identified by `id` and enough metadata exists for the use case.

Profiles or exchange formats MAY require `uri`.

## 5.7 Revision and Stability

`revision` SHOULD be used when source identity depends on a specific version.

Examples:

```yaml
sources:
  - id: src-001
    type: repository
    uri: https://github.com/example/project
    revision: 9fceb02
```

```yaml
sources:
  - id: src-002
    type: document
    title: Example Report
    revision: 2026-07-07-edition
```

A Source reference SHOULD be stable enough for later reconstruction when the document claims traceability.

Core does not require content-addressed references, but profiles MAY require them.

## 5.8 Composite Sources

A composite source represents a source assembled from multiple materials.

Example:

```yaml
sources:
  - id: src-composite-001
    type: composite
    title: Interview packet
    components:
      - source: src-001
      - source: src-002
```

Composite source component structure is profile-defined unless a later Core chapter or companion specification defines it.

Core validators SHOULD preserve composite metadata.

Core validators SHOULD NOT require tools to dereference composite sources.

## 5.9 Generated Sources

Generated artifacts MAY be recorded as sources when later document structure depends on them.

Example:

```yaml
sources:
  - id: src-generated-summary
    type: generated_artifact
    title: Generated preprocessing summary
    generated_by: preprocessing-tool
    generated_at: 2026-07-07T00:00:00Z
```

A generated source is still an Original Source relative to the current IdeaMark document if the current document uses it as input material.

Generation metadata MAY also be recorded in `meta.generation` when it describes the current document rather than an input source.

## 5.10 Source Access

A Source MAY include an `access` field.

Example:

```yaml
sources:
  - id: src-001
    type: document
    uri: ./private-report.md
    access:
      visibility: private
      note: Internal document; do not publish source text.
```

`access` is informational in Core mode.

Core does not define authorization or security enforcement.

Profiles MAY define access metadata and enforcement behavior.

## 5.11 Source Language

A Source MAY declare `lang`.

Example:

```yaml
sources:
  - id: src-001
    type: document
    lang: ja-JP
```

`lang` SHOULD use a BCP 47 language tag.

Source language may differ from `meta.lang` and from Entity content language.

## 5.12 Relationship to Anchors

Source objects identify source materials.

Anchors identify locations or regions within those source materials.

A Source object SHOULD NOT be overloaded with all extraction details.

Instead, use `anchors` on Sections, Occurrences, or Entities when traceability requires location-level reference.

## 5.13 Source Completeness

`sources` MAY be empty in Core mode.

An empty `sources` array is valid for:

- template documents;
- authored documents that do not claim external source traceability;
- documents in early draft state;
- documents whose sources are intentionally omitted by profile policy.

If a document claims source traceability, a profile SHOULD require at least one Source.

## 5.14 Validation Requirements

A Core validator MUST check:

- `sources` exists;
- `sources` is an array;
- every item in `sources` is a mapping;
- every Source has a valid `id`;
- Source IDs are unique within `sources`.

A Core validator SHOULD warn when:

- a Source has no `type`;
- a Source has no `title`, `uri`, or other human-identifying metadata;
- source type is unknown;
- source URI appears malformed;
- a Source is never referenced by any anchor and the document appears to claim source traceability.

Strict mode MAY promote warnings to errors.
