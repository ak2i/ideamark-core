# 13. Validation Rules

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 13.1 Purpose

Validation determines whether a serialized IdeaMark document satisfies Core structural requirements.

Validation does not determine whether the document is intellectually correct, useful, complete, or faithful to a Projection.

Projection quality, retrieval quality, semantic interpretation, and domain review are outside Core validation.

## 13.2 Validation Modes

Core v1.2.0 defines two initial validation modes:

- Core mode;
- Strict mode.

Profiles MAY define additional validation modes.

## 13.3 Core Mode

Core mode validates the minimum interoperable Core document structure.

Core mode MUST check:

- parseability;
- required top-level namespaces;
- required namespace types;
- required object shape;
- required object IDs;
- duplicate IDs within namespaces;
- required references;
- anchor source references;
- required `meta` fields.

Core mode SHOULD preserve extension data and unknown fields.

Core mode SHOULD warn, rather than fail, for extension data, unknown vocabularies, placeholders, and incomplete draft structures unless a required Core rule is violated.

## 13.4 Strict Mode

Strict mode is intended for controlled exchange, tests, publishing pipelines, or profile-enforced validation.

Strict mode MAY reject:

- unknown top-level namespaces;
- unknown object fields;
- unknown vocabulary values;
- placeholder objects;
- undeclared extensions;
- incomplete structures that Core mode permits;
- unsupported profiles;
- unsupported `spec_version` values.

Strict mode MUST NOT silently reinterpret invalid or unknown data as valid Core data.

## 13.5 Severity Levels

Validators SHOULD report diagnostics using these severity levels:

- `error`
- `warning`
- `info`

An `error` indicates that the document violates a required validation rule.

A `warning` indicates that the document is structurally processable but may be incomplete, ambiguous, unsupported by profile, or likely to cause interoperability problems.

An `info` diagnostic records non-failing observations.

## 13.6 Required Core Errors

A Core validator MUST report an error when:

- the document is not parseable YAML;
- the top-level document is not a mapping;
- a required namespace is missing;
- a required namespace has the wrong type;
- `meta` is missing required fields;
- an object in a required object array is not a mapping;
- a Source, Section, Occurrence, or Entity is missing a valid `id`;
- duplicate IDs occur within a required namespace;
- a non-placeholder Occurrence lacks `entity`;
- a non-placeholder Occurrence lacks `role`;
- an Occurrence references a missing Entity;
- a Section references a missing Occurrence;
- an Anchor references a missing Source;
- an Anchor lacks required `source` or `type` fields.

## 13.7 Recommended Core Warnings

A Core validator SHOULD report a warning when:

- a required namespace is empty in a document that appears intended for exchange;
- an object appears to be a placeholder;
- a Source lacks useful identifying metadata;
- a Section lacks Occurrences;
- an Occurrence is not referenced by any Section;
- an Entity is not referenced by any Occurrence;
- unknown status values appear;
- unknown source types appear;
- unknown anchor types appear;
- unknown top-level namespaces appear without profile or extension declaration;
- unknown object fields appear without clear namespacing;
- `confidence` values are outside 0 to 1;
- `structure.sections` omits known Sections;
- multiple Sections reference the same Occurrence.

## 13.8 Informational Diagnostics

A validator MAY report informational diagnostics for:

- successful profile detection;
- extension preservation;
- recommended ID prefix deviations;
- use of approximate anchors;
- unsupported profile declarations that were ignored in Core mode;
- detected migration opportunities.

## 13.9 Reference Validation

Validators MUST resolve references using the relevant namespace ID scope.

Required Core references are:

| Reference Field | Target Namespace |
| --- | --- |
| `sections[].occurrences[]` | `occurrences[].id` |
| `occurrences[].entity` | `entities[].id` |
| `anchors[].source` | `sources[].id` |
| `structure.sections[]` | `sections[].id` |

`structure.sections[]` validation SHOULD be performed when `structure` exists.

Unresolved `structure.sections[]` references SHOULD be warnings in Core mode unless the validator treats `structure` as a validated optional Core-adjacent namespace.

## 13.10 Placeholder Validation

Placeholder objects MAY be allowed in Core mode.

A placeholder is an object that has an `id` but lacks fields normally needed for reconstruction.

Examples:

- Entity without `content`, `payload`, or `ref`;
- Occurrence without `entity` or `role`;
- Section without `occurrences`;
- Source without identifying metadata beyond `id`.

Core mode SHOULD warn about placeholders.

Strict mode MAY reject placeholders.

Profiles MAY define explicit placeholder rules.

## 13.11 Extension Validation

Core validators SHOULD preserve extension data.

Core validators SHOULD warn about undeclared extension data.

Strict validators MAY reject undeclared extension data.

A validator MUST NOT allow extension data to override or bypass required Core validation rules.

## 13.12 Vocabulary Validation

Core vocabularies are generally recommended rather than closed unless a field is explicitly declared as controlled by a profile.

Core mode SHOULD warn on unknown vocabulary values for:

- document status;
- object status;
- source type;
- anchor type;
- anchor precision;
- Projection role.

Core mode MUST NOT reject unknown vocabulary values solely because they are unknown, unless the field's chapter declares a stricter requirement.

Strict mode MAY reject unknown vocabulary values.

## 13.13 Validation Output

Validator output format is tool-specific or governed by the relevant CLI contract.

A validator SHOULD include enough location information for diagnostics to be actionable.

Recommended diagnostic information:

- severity;
- code;
- message;
- namespace path;
- object ID when available;
- field path when available.

## 13.14 Validation Boundary

Core validation MUST NOT require validators to:

- dereference external source URIs;
- verify source content;
- execute Projection logic;
- judge Entity granularity;
- judge truth of content;
- rank retrieval results;
- execute authoring workflows;
- validate UI layout;
- validate storage engine state.

Companion tools MAY perform stronger checks outside Core validation.
