# Merge Tool Detailed Specifications

This document expands on the high level points in [merge_tool_spec.md](../merge_tool_spec.md) and outlines implementation guidelines.

## CLI Interface
```
python merge_tool.py --refs <A.ref.yaml> <B.ref.yaml> [--intent union] [--strategy prefer-a] [--out <path>]
```
- `--refs` specifies one or more reference files.
- `--intent` indicates how extensively the patterns should be combined (`intersection`, `union`, `hybrid`, `synthesis`).
- `--strategy` controls conflict resolution (`manual`, `prefer-a`, `prefer-b`, `annotate`).
- `--out` may be a filename or directory. When a directory is given, the merged file is named `merged-<uuid>.yaml` and stored there.

## Conflict Detection
The fields checked for conflicting content are:
- `problem.summary`
- `solution.approach`
- any overlapping `metadata` keys

Detection heuristics depend on the merge strategy:
- **manual**: simple text comparison; if different, include TODO placeholders in the output.
- **prefer-a / prefer-b**: conflicts are detected but resolved by selecting the preferred pattern's text.
- **annotate**: embed both versions in a block quote with annotation markers.
- **synthesis**: generate a synthesized text via an LLM prompt tailored to the provider (e.g., OpenAI, Anthropic). Providers may define custom prompt templates.

## Placeholder Format
For `manual` strategy, conflicting fields are replaced with:
```
TODO: resolve conflict between <A.id> and <B.id> for <field>
```
The summary report lists all unresolved fields so a human editor can update them later.

## LLM Prompt Skeleton
When `synthesis` is chosen, the tool constructs prompts of the form:
```
"Combine the following IdeaMark fields using a concise style.\nPattern A:<text>\nPattern B:<text>"
```
Providers can override the wording while keeping the structure.

## Unique ID Generation
A new pattern ID is produced with the format `IdeaMark-<uuid4>`, matching the schema pattern requirement. The Python `uuid` module is recommended.

## Summary Report Schema
The optional report is saved alongside the merged file using `.md` or `.json` extension. Expected fields are:
- `sources`: list of source IDs
- `titles`: mapping of ID to title
- `intent`: chosen merge intent
- `strategy`: conflict resolution strategy
- `conflicts`: list of fields and how they were resolved
- `output`: filename of the merged pattern

## Validation Workflow
1. Load each referenced pattern and validate it against `schema/ideamark.schema.yaml`.
2. After merging, validate the resulting YAML with the same schema.
3. If validation fails at any stage, abort the merge and report the error.

Implementers can extend the tool with additional helpers, but should follow these specifications to ensure compatibility.
