# Skills — machine-readable markdown

This folder contains skill definitions written as Markdown files with YAML frontmatter so both humans and AI agents can read and index them easily.

Location: docs/skills/

Included files:

- skill-format.md — schema and best practices for skill files.
- example-skill.md — a complete example skill you can copy and edit.

How AI agents should read these files

- Read the YAML frontmatter first — it contains the machine-readable metadata (id, name, inputs, outputs, tags, version, format_version).
- Use the body of the document for human-friendly explanations and examples. Prefer explicit example blocks for parsing.
- Filenames SHOULD be kebab-case and unique (e.g., summarize-text.md).

Adding new skills

- Add a new file under docs/skills/ with a unique id in the frontmatter.
- Follow the schema documented in skill-format.md.
- Commit to the default branch; if you want GitHub Pages to publish them, set Pages source to "Branch: <default> / Folder: /docs" in repository settings.

Why this layout

- Storing skills in docs/ makes them easy to publish with GitHub Pages and easy for crawlers and AI agents to find (raw URLs and the Pages site both work).
- YAML frontmatter gives a stable structure; the rest of the markdown provides examples and human context.
