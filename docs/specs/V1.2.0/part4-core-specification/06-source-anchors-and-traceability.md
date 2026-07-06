# 6. Source Anchors and Traceability

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 6.1 Purpose

Source anchors record traceability from Core objects to locations, regions, fragments, or approximate positions within Original Sources.

Anchors support reconstruction and review.

Anchors do not define final meaning.

Anchors do not replace Sources, Sections, Occurrences, or Entities.

## 6.2 Anchor Placement

The `anchors` field MAY appear on:

- Section objects;
- Occurrence objects;
- Entity objects.

Section anchors SHOULD be supported.

Occurrence anchors MAY be supported.

Entity anchors MAY be supported.

Document-level source identity MUST be recorded through `sources` rather than a document-level anchor alone.

## 6.3 Anchor Field Shape

When present, `anchors` SHOULD be an array of anchor objects.

Example:

```yaml
sections:
  - id: sec-001
    anchors:
      - source: src-001
        type: line_range
        ranges:
          - start: 10
            end: 25
        precision: exact
```

Each anchor object MUST be a mapping.

Each anchor object MUST include:

| Field | Type | Requirement |
| --- | --- | --- |
| `source` | string | MUST |
| `type` | string | MUST |

`source` MUST reference an existing `sources[].id`.

`type` identifies the anchor mechanism or location kind, such as `line_range`, `page_range`, `heading_path`, or `media_time_range`.

## 6.3.1 Anchor Role and Purpose

An anchor MAY include `role` or `purpose` to describe why the source region is used.

This is distinct from `type`.

`type` identifies how the source location is addressed.

`role` or `purpose` identifies why the source location matters in the current document.

Example:

```yaml
anchors:
  - source: src-001
    type: line_range
    ranges:
      - start: 58
        end: 95
    precision: exact
    role: implementation_rationale
    purpose: identify source lines that explain a performance-oriented implementation choice
```

`role` and `purpose` are OPTIONAL.

Core does not define a closed vocabulary for anchor roles or purposes.

Profiles MAY define role or purpose vocabularies for source-specific, domain-specific, or audit-oriented documents.

## 6.4 Precision

An anchor MAY include `precision`.

Recommended precision values are:

- `exact`
- `approximate`
- `inferred`
- `unknown`

Example:

```yaml
anchors:
  - source: src-001
    type: paragraph
    paragraph: 4
    precision: approximate
```

Core mode validators SHOULD warn on unknown precision values unless declared by a profile.

Strict mode MAY reject unknown precision values.

## 6.5 Text Anchors

Text sources MAY use line, character, paragraph, or heading anchors.

### Line range

```yaml
anchors:
  - source: src-001
    type: line_range
    ranges:
      - start: 10
        end: 25
    precision: exact
```

For `line_range` anchors:

- `ranges` SHOULD be an array;
- each range SHOULD contain integer `start` and `end` fields;
- line numbers SHOULD be 1-based;
- `end` SHOULD be inclusive.

### Character range

```yaml
anchors:
  - source: src-001
    type: character_range
    ranges:
      - start: 120
        end: 340
    precision: exact
```

For `character_range` anchors:

- character offsets SHOULD be 0-based unless a profile declares otherwise;
- tools SHOULD document how offsets are calculated if Unicode normalization matters.

### Paragraph reference

```yaml
anchors:
  - source: src-001
    type: paragraph
    paragraph: 3
    precision: approximate
```

### Heading path

```yaml
anchors:
  - source: src-001
    type: heading_path
    path:
      - Chapter 2
      - Regional Monitoring
```

## 6.6 Page Anchors

Paginated sources MAY use page ranges.

```yaml
anchors:
  - source: src-001
    type: page_range
    ranges:
      - start: 12
        end: 15
    precision: exact
```

Page anchors MAY be used for PDFs, scans, books, reports, slide decks, or other paginated artifacts.

Page numbering SHOULD follow the source artifact's visible or declared page numbering when available.

Profiles MAY require physical page index, logical page label, or both.

## 6.7 Media Time Anchors

Audio and video sources MAY use media time ranges.

```yaml
anchors:
  - source: src-audio-001
    type: media_time_range
    start: 00:01:20
    end: 00:02:05
    precision: approximate
```

For `media_time_range` anchors:

- `start` SHOULD identify the beginning time;
- `end` SHOULD identify the ending time;
- time values SHOULD use a consistent profile-declared format when machine validation is required.

Core mode validators MAY treat time values as strings.

## 6.8 Image Region Anchors

Image sources MAY use region anchors.

```yaml
anchors:
  - source: src-image-001
    type: image_region
    region:
      unit: normalized
      x: 0.10
      y: 0.20
      width: 0.50
      height: 0.30
    precision: approximate
```

Image region coordinates MAY be normalized, pixel-based, or profile-defined.

The `region.unit` field SHOULD declare the coordinate system.

Core does not define image coordinate semantics beyond preserving the anchor object.

## 6.9 Dataset Anchors

Dataset sources MAY use row, column, cell, or query anchors.

```yaml
anchors:
  - source: src-dataset-001
    type: dataset_rows
    rows:
      - 10
      - 11
      - 12
```

```yaml
anchors:
  - source: src-dataset-001
    type: dataset_query
    query: "country = 'JP' AND year >= 2020"
    precision: inferred
```

Core does not define dataset query language semantics.

Profiles MAY define query syntax and validation.

## 6.10 Code and Repository Anchors

Code or repository sources MAY use repository paths, symbols, line ranges, commits, or file anchors.

```yaml
anchors:
  - source: src-repo-001
    type: repository_path
    path: src/parser/mod.ts
    revision: 9fceb02
```

```yaml
anchors:
  - source: src-code-001
    type: code_symbol
    symbol: parseIdeaMarkDocument
    path: src/parser/mod.ts
```

Repository anchor fields are intentionally open because repositories vary widely.

Profiles MAY define stricter code anchor behavior.

## 6.11 Composite Anchors

Composite sources or multi-source extraction may require multiple anchors.

An object MAY contain multiple anchors.

Example:

```yaml
sections:
  - id: sec-001
    anchors:
      - source: src-001
        type: line_range
        ranges:
          - start: 10
            end: 20
      - source: src-002
        type: page_range
        ranges:
          - start: 3
            end: 4
```

Multiple anchors on one object indicate that the object is traceable to multiple source regions.

They do not by themselves define whether the object synthesizes, compares, quotes, or transforms those sources.

That role may be expressed through Occurrences, Entities, anchor `role` or `purpose`, profiles, or extensions.

## 6.12 Approximate and Inferred Anchors

Core allows approximate anchors because many useful IdeaMark documents are produced from conversations, media, scans, generated artifacts, or partial source access.

Approximate anchors SHOULD be explicitly marked:

```yaml
anchors:
  - source: src-001
    type: heading_path
    path:
      - Background
    precision: approximate
```

Inferred anchors SHOULD be used when a tool or author estimates source location indirectly.

Core validators MUST NOT reject approximate or inferred anchors solely because they are not exact.

Profiles MAY require exact anchors for audit-grade documents.

## 6.13 Anchor Type Vocabulary

Recommended anchor type values include:

- `line_range`
- `character_range`
- `paragraph`
- `heading_path`
- `page_range`
- `media_time_range`
- `image_region`
- `dataset_rows`
- `dataset_columns`
- `dataset_cells`
- `dataset_query`
- `repository_path`
- `code_symbol`
- `composite_fragment`
- `other`

Core mode validators SHOULD warn on unknown anchor type values unless declared by a profile.

Strict mode MAY reject unknown anchor type values.

## 6.14 Traceability Boundary

Anchors provide traceability claims.

They do not require tools to:

- dereference source URIs;
- verify that source content still exists;
- perform OCR;
- calculate embeddings;
- compare extracted text;
- prove intellectual correctness;
- validate Projection quality.

Profiles or companion tools MAY perform stronger source verification.

## 6.15 Validation Requirements

A Core validator MUST check:

- when `anchors` appears, it is an array;
- every anchor item is a mapping;
- every anchor has a non-empty string `source` field;
- every anchor has a non-empty string `type` field;
- `anchors[].source` resolves to an existing Source ID.

A Core validator SHOULD warn when:

- anchor type is unknown;
- precision value is unknown;
- anchor type-specific recommended fields are missing;
- ranges are malformed;
- line or page range start is greater than end;
- source metadata is insufficient to make the anchor useful.

Strict mode MAY promote warnings to errors.
