# Merge Tool Requirements

The merge tool composes multiple IdeaMark patterns into a new YAML file. Requirements derive from [merge_tool_spec.md](../merge_tool_spec.md).

## Inputs
- Accept **two or more** `.ref.yaml` files from `refs/`.
- For each ref, load the full pattern from the path specified by its `access.uri`.
- Optional arguments specify a **merge intent** (`intersection`, `union`, `hybrid`, `synthesis`) and a **conflict strategy** (`manual`, `prefer-a`, `prefer-b`, `annotate`).

## Processing
- Validate that referenced pattern files exist and conform to `schema/ideamark.schema.yaml`.
- Detect conflicts in `problem.summary`, `solution.approach`, and shared `metadata`. Conflict evaluation may vary by chosen strategy.
- Apply the selected merge strategy, producing combined `context`, `problem`, `solution`, and `metadata` sections.
- Generate a new unique pattern `id` and update `linked_patterns` with source IDs.

## Outputs
- Write the merged pattern to a destination file or directory specified via CLI.
- Create an optional summary report (Markdown or JSON) describing:
  - Source pattern IDs and titles
  - Detected conflicts and resolutions
  - Merge intent and strategy
  - Linked pattern IDs

## Validation
- Validate the final YAML with the IdeaMark schema before saving.

These requirements ensure the tool can merge patterns consistently while preserving the semantic intent of the originals.
