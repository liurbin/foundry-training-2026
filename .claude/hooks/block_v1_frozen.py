#!/usr/bin/env python3
"""PreToolUse hook: block edits to v1 frozen docs.

README and CLAUDE.md state v1 docs are no longer maintained. They are kept
only as evolution references. Editing them is almost always a model error.
"""
import json
import sys

FROZEN = (
    "docs/00-training-plan.md",
    "docs/02-instructor-manual.md",
)

data = json.load(sys.stdin)
path = (data.get("tool_input") or {}).get("file_path", "") or ""

if any(path.endswith(f) for f in FROZEN):
    sys.stderr.write(
        f"BLOCKED: {path} is a v1 frozen doc.\n"
        "v1 docs are no longer maintained (see CLAUDE.md / README.md).\n"
        "Edit the v2 counterparts under docs/ instead "
        "(00-training-plan-v2.md / 01-instructor-handbook-v2.md).\n"
    )
    sys.exit(2)

sys.exit(0)
