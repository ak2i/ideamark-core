# Merge Tool Detailed Specifications

This document expands on the high level points in [merge_tool_spec.md](../merge_tool_spec.md) and outlines implementation guidelines.

## CLI Interface
```
python merge_tool.py --refs <A.ref.yaml> <B.ref.yaml> [<C.ref.yaml> ...] \
    [--intent union] [--strategy prefer] [--priority A B C] [--out <path>]
```
- `--refs` specifies two or more IdeaMark reference files. The order of files sets default priority when no explicit `--priority` is given.
- `--intent` indicates how extensively the patterns should be combined (`intersection`, `union`, `hybrid`, `synthesis`).
- `--strategy` controls conflict resolution (`manual`, `prefer`, `annotate`, `synthesis`). `prefer-a` and `prefer-b` remain accepted aliases when exactly two references are supplied.
- `--priority` lists reference aliases in descending priority for the `prefer` strategy. When omitted, the order passed to `--refs` is used.
- `--out` may be a filename or directory. When a directory is given, the tool creates subfolders `patterns/`, `refs/` and `summary/` and stores output files under them using the common stem `merged-<uuid>`.

## Conflict Detection
The fields checked for conflicting content are:
- `problem.summary`
- `solution.approach`
- any overlapping `metadata` keys

Detection heuristics depend on the merge strategy:
- **manual**: simple text comparison; if different, include TODO placeholders in the output.
- **prefer**: conflicts are detected but resolved according to the priority list. When exactly two references are provided, `prefer-a` and `prefer-b` behave as priority `[A,B]` or `[B,A]`.
- **annotate**: embed all versions in a block quote with annotation markers in their priority order.
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

## Output Directory Structure
When `--out` points to a directory, three files are produced with the same UUID stem:
- `patterns/merged-<uuid>.yaml` – the merged pattern document.
- `refs/merged-<uuid>.ref.yaml` – a machine generated reference capturing provenance.
- `summary/merged-<uuid>.md` – the human readable summary report.
Users are encouraged to publish these three files together in their repository or file share service to allow others to audit how the merge was performed.

## Validation Workflow
1. Load each referenced pattern and validate it against `schema/ideamark.schema.yaml`.
2. After merging, validate the resulting YAML with the same schema.
3. If validation fails at any stage, abort the merge and report the error.

Implementers can extend the tool with additional helpers, but should follow these specifications to ensure compatibility.
