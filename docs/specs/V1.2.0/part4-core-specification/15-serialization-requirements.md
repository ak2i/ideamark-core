# 15. Serialization Requirements

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 15.1 Purpose

Serialization requirements define how IdeaMark Core documents should be written, parsed, formatted, and preserved as interoperable YAML documents.

The goal is reliable exchange among humans, LLMs, CLI tools, validators, formatters, migration tools, and authoring systems.

## 15.2 Primary Format

YAML is the primary human-authored serialization format for IdeaMark Core v1.2.0.

A conforming YAML document MUST parse into a single top-level mapping.

Required namespaces MUST appear as top-level mapping keys.

## 15.3 JSON-equivalent Representation

Tools MAY expose a JSON-equivalent normalized representation.

The JSON-equivalent representation SHOULD preserve:

- required Core namespaces;
- object arrays;
- object IDs;
- references;
- optional fields;
- extension fields;
- unknown namespaces where possible.

JSON-equivalent output MUST NOT require a different Core data model.

## 15.4 YAML Feature Restrictions

For interoperability, documents SHOULD avoid advanced YAML features whose behavior may differ across parsers or round-trip tools.

Documents SHOULD NOT rely on:

- YAML anchors and aliases;
- custom tags;
- merge keys;
- parser-specific implicit typing;
- multi-document streams;
- comments as machine-readable data.

Tools MAY reject these features in strict mode.

Tools SHOULD preserve comments when possible, but comments MUST NOT be required for Core semantics.

## 15.5 Scalar Values

Required IDs and references MUST be strings.

Authors SHOULD quote IDs when there is any chance that a YAML parser may reinterpret them as numbers, booleans, timestamps, or null.

Recommended:

```yaml
id: "ent-001"
```

Also acceptable when unambiguous:

```yaml
id: ent-001
```

## 15.6 Timestamps

Timestamp fields SHOULD use ISO 8601 strings.

Example:

```yaml
updated_at: 2026-07-07T00:00:00Z
```

Core validators MAY treat timestamps as strings in Core mode.

Strict mode or profiles MAY require stricter timestamp validation.

## 15.7 Ordering

Array order SHOULD be preserved by formatters unless a canonical ordering mode is explicitly requested.

The following arrays may carry meaningful authoring or reconstruction order:

- `sources[]`
- `sections[]`
- `sections[].occurrences[]`
- `occurrences[]`
- `entities[]`
- `structure.sections[]`

When reconstruction order matters, authors SHOULD express it explicitly using Section occurrence lists or `structure.sections`.

## 15.8 Formatting

Formatters SHOULD:

- preserve required Core data;
- preserve extension data;
- preserve unknown fields;
- preserve unknown namespaces;
- preserve array order by default;
- avoid rewriting IDs;
- avoid converting arrays into keyed maps;
- avoid dropping nulls unless a normalization mode declares that behavior.

Formatters MAY offer canonical formatting.

Canonical formatting MUST be explicit and documented.

## 15.9 Round-trip Behavior

Round-trip processing means reading and writing a document without intentional semantic transformation.

A round-trip formatter SHOULD NOT drop:

- unknown namespaces;
- extension fields;
- optional fields;
- comments, when the tool supports comment preservation;
- ordering;
- approximate anchors;
- unsupported profile declarations.

A tool MUST NOT silently remove data that it does not understand during normal round-trip processing.

## 15.10 Encoding

Documents SHOULD be encoded as UTF-8.

Tools SHOULD read and write UTF-8 by default.

A tool MAY reject documents that cannot be decoded as UTF-8.

## 15.11 File Extension

The recommended file extensions are:

- `.ideamark.yaml`
- `.ideamark.yml`

Markdown-embedded or hybrid formats may be defined by companion specifications, but this Part 4 Core serialization is expressed as YAML document structure.

## 15.12 Serialization Boundary

Serialization requirements do not define:

- storage engine schema;
- database indexing;
- retrieval pipeline representation;
- authoring engine internal IR;
- UI component format;
- Projection Library storage format.

Implementations MAY map Core documents to other internal representations as long as they can preserve and emit conforming Core documents when required.
