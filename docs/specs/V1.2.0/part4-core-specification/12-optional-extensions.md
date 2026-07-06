# 12. Optional Extensions

**Version:** IdeaMark Core v1.2.0  
**Status:** Draft

## 12.1 Purpose

IdeaMark Core must remain small enough to be interoperable while allowing profiles, domains, tools, and companion specifications to add data that Core does not define.

Extensions provide that boundary.

Extension data may be useful, but it MUST NOT be required to interpret minimum Core semantics unless a profile explicitly declares that requirement.

## 12.2 Extension Locations

Extension data MAY appear in three places:

1. top-level extension namespaces;
2. the top-level `extensions` namespace;
3. extension fields inside Core objects.

Core mode validators SHOULD preserve extension data in all three locations.

Strict mode MAY reject extension data that is not declared by a profile.

## 12.3 Top-level Extension Namespaces

A document MAY include top-level namespaces outside the required Core namespaces.

Example:

```yaml
meta:
  spec_version: ideamark-core-v1.2.0
  document_id: example-extension
  status: draft
sources: []
sections: []
occurrences: []
entities: []
relations: []
```

Core mode validators SHOULD warn about unknown top-level namespaces unless declared by a profile or extension declaration.

Core mode validators SHOULD preserve them during round-trip formatting.

## 12.4 `extensions` Namespace

The `extensions` namespace MAY be used for namespaced extension data.

Example:

```yaml
extensions:
  example.org/review:
    reviewer: domain-specialist
    state: needs-review
```

`extensions` SHOULD be a mapping when present.

Keys under `extensions` SHOULD be stable namespace identifiers such as domain names, URI-like identifiers, or profile identifiers.

## 12.5 Object-level Extension Fields

Core objects MAY include extension fields.

Example:

```yaml
entities:
  - id: ent-001
    content: Example reusable material.
    x-example-org:
      review_state: accepted
```

Object-level extension fields SHOULD be clearly namespaced.

The `x-` prefix is RECOMMENDED for ad hoc extension fields.

Profile-declared fields MAY use profile-defined names without the `x-` prefix.

## 12.6 Extension Declaration

A profile MAY declare supported extension namespaces and fields.

A document MAY also include extension declarations in `meta.profiles` or `extensions`.

Example:

```yaml
meta:
  profiles:
    - example.org/review-profile-v1
extensions:
  example.org/review:
    schema: example.org/review-profile-v1
```

Core does not define a universal extension declaration schema.

Companion specifications MAY define one.

## 12.7 Preservation Requirement

Tools that read and write IdeaMark Core documents SHOULD preserve extension data by default.

This includes:

- unknown top-level namespaces;
- `extensions` namespace data;
- unknown fields inside Core objects;
- namespaced extension fields;
- profile-declared fields not understood by the current tool.

Tools MUST NOT silently drop extension data during normal round-trip formatting.

A tool MAY drop extension data only in an explicit destructive normalization, export, or sanitization mode.

## 12.8 Extension Boundary

Extension data MUST NOT change the meaning of required Core fields for Core validators.

For example:

- an extension field cannot make a missing `id` valid;
- an extension namespace cannot replace the required `entities` namespace;
- a profile-specific relation graph cannot replace `sections[].occurrences` for Core reconstruction;
- extension provenance cannot replace required Source references when anchors point to sources.

Profiles MAY add requirements, but they do not weaken Core requirements.

## 12.9 Optional Core-adjacent Namespaces

The following namespaces are common candidates for optional or profile-defined use:

- `relations`
- `perspectives`
- `provenance`
- `structure`
- `extensions`

`structure` is described separately because it has a recommended Core-adjacent ordering role.

`relations`, `perspectives`, and `provenance` are not required Core namespaces in v1.2.0.

## 12.10 Validation Requirements

A Core validator SHOULD:

- preserve extension data;
- warn about undeclared unknown top-level namespaces;
- warn about undeclared object-level extension fields when they are not clearly namespaced;
- validate required Core fields regardless of extension data.

A strict validator MAY:

- reject unknown namespaces;
- reject unknown fields;
- reject undeclared extensions;
- require profile declarations for extension data.

A validator MUST NOT treat extension data as required Core semantics unless running in a profile mode that explicitly defines that behavior.
