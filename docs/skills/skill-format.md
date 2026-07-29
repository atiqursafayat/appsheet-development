# Skill file format and best practices

This document defines the recommended, machine-readable skill Markdown format used under docs/skills/.

Required YAML frontmatter fields
- id: unique slug for the skill (string). Use kebab-case, e.g., `summarize-text`.
- name: human-friendly name (string).
- description: short summary (string).
- version: semantic version, e.g., `1.0.0` (string).
- format_version: integer or string indicating the frontmatter schema version (e.g., `1`).
- tags: list of strings (at least an empty array `[]` if none).
- inputs: list of input descriptors. Each input is an object with keys: name (string), type (string), required (bool), description (string).
- outputs: list of output descriptors. Each is an object with keys: name (string), type (string), description (string).

Optional fields
- category: top-level category (string) — used for shallow grouping in paths.
- subcategory: second-level group (string) — optional.
- author, license, examples

JSON-LD embedding (recommended)

Embedding a brief JSON-LD block in the skill body helps web crawlers and some agents discover stable metadata without parsing frontmatter. Example:

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Summarize text",
  "description": "Produce a short summary of a given text",
  "identifier": "summarize-text",
  "keywords": "nlp, summarization"
}
```

Storage and path depth
- Keep at most two directory levels under docs/skills (category/subcategory/skill.md). Example: docs/skills/text/summarization/summarize-text.md.

Validation
- Use the provided GitHub Actions workflow (validate-skills.yml) to validate frontmatter on pushes and PRs.
- The build-skills-index workflow regenerates docs/skills/skills-index.json automatically.

Best practices summary
- Keep skills shallow (<=2 levels under docs/skills).
- Include at least one example block per skill.
- Use semver for `version` and bump `format_version` when schema changes.
- Keep the YAML frontmatter authoritative; use the Markdown body for examples and human notes.
