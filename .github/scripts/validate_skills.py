#!/usr/bin/env python3
"""Validate skill Markdown files under docs/skills.

Rules enforced:
- Files must contain YAML frontmatter delimited by '---' on top.
- Required fields in frontmatter: id, name, description, version, format_version, inputs, outputs, tags
- inputs and outputs must be lists with required keys
- Directory nesting under docs/skills must be at most 2 levels deep (e.g., docs/skills/<level1>/<level2>/file.md)

Exit with non-zero status if any validation fails.
"""
import os
import sys
import re
import yaml

ROOT = 'docs/skills'
REQUIRED = ['id','name','description','version','format_version','inputs','outputs','tags']

errors = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    for fname in filenames:
        if not fname.endswith('.md'):
            continue
        full = os.path.join(dirpath, fname)
        # check nesting depth under docs/skills
        rel = os.path.relpath(full, ROOT)
        parts = rel.split(os.sep)
        # parts includes possible subdirs and filename
        # allowed: filename (['file.md']), 1 level (['cat','file.md']), 2 levels (['cat','sub','file.md'])
        if len(parts) - 1 > 2:  # subtract filename
            errors.append(f"Too deep: {full} (more than 2 directory levels under docs/skills)")
            continue
        with open(full, 'r', encoding='utf-8') as f:
            text = f.read()
        # parse YAML frontmatter
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            errors.append(f"No YAML frontmatter in {full}")
            continue
        yf = m.group(1)
        try:
            data = yaml.safe_load(yf)
        except Exception as e:
            errors.append(f"YAML parse error in {full}: {e}")
            continue
        if not isinstance(data, dict):
            errors.append(f"Frontmatter is not a mapping in {full}")
            continue
        for k in REQUIRED:
            if k not in data:
                errors.append(f"Missing required field '{k}' in {full}")
        # inputs/outputs structure
        for side in ('inputs','outputs'):
            val = data.get(side)
            if not isinstance(val, list):
                errors.append(f"Field '{side}' must be a list in {full}")
            else:
                for i, item in enumerate(val):
                    if not isinstance(item, dict):
                        errors.append(f"{side}[{i}] must be an object in {full}")
                    else:
                        if 'name' not in item:
                            errors.append(f"{side}[{i}] missing 'name' in {full}")
                        if side == 'inputs' and 'type' not in item:
                            errors.append(f"{side}[{i}] missing 'type' in {full}")

# report
if errors:
    print('Validation failed with the following issues:')
    for e in errors:
        print('- ' + e)
    sys.exit(1)
else:
    print('All skill files validated successfully.')
