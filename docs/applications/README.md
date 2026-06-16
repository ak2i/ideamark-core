# IdeaMark Applications

This section discusses how IdeaMark may be applied in practice.

IdeaMark Core is intentionally application-neutral. The same structure may support many different workflows, domains, and tools.

## Application Areas

### Knowledge Reuse

Organizing reusable traces from discussions, reports, observations, and analyses.

### Research Support

Capturing and recomposing intellectual activity across research projects.

### Planning and Policy

Transforming discussions, observations, and evidence into planning material.

### Business Modeling

Using IdeaMark as a reusable structural layer alongside domain-specific models such as TPCG.

### AI Workflows

Separating:

- extraction
- structuring
- interpretation
- projection
- expression

into reusable stages.

## Relationship to Other Models

IdeaMark Core does not attempt to replace domain-specific representations.

Instead, it provides a reusable meaning-structure layer that can coexist with formats such as:

- OKF
- TPCG
- Markdown
- YAML
- JSON
- future domain-specific representations

## Design Principle

Applications should build on IdeaMark Core without changing the meaning of the Core specification.

The Core specification defines reusable structure. Applications define purpose-specific workflows.
