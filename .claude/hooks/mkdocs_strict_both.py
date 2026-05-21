#!/usr/bin/env python3
"""PostToolUse hook: when mkdocs*.yml is edited, run both strict builds.

CI runs `mkdocs build --strict` against BOTH mkdocs.yml (zh) and
mkdocs.en.yml (en). Local users tend to only check zh and discover
broken-link failures on push. This hook short-circuits that.

Skips silently if `mkdocs` is not on PATH (e.g. venv not activated) —
the goal is to assist, not to gate every edit.
"""
import json
import os
import shutil
import subprocess
import sys

WATCHED = {"mkdocs.yml", "mkdocs.en.yml"}

data = json.load(sys.stdin)
path = (data.get("tool_input") or {}).get("file_path", "") or ""
if os.path.basename(path) not in WATCHED:
    sys.exit(0)

cwd = data.get("cwd") or os.getcwd()

if shutil.which("mkdocs") is None:
    sys.stderr.write(
        "[mkdocs-strict] skipped: `mkdocs` not on PATH. "
        "Activate your venv and run manually:\n"
        "  mkdocs build --strict && mkdocs build --strict -f mkdocs.en.yml\n"
    )
    sys.exit(0)

def run(label, args):
    return label, subprocess.run(args, cwd=cwd, capture_output=True, text=True)

results = [
    run("zh", ["mkdocs", "build", "--strict"]),
    run("en", ["mkdocs", "build", "--strict", "-f", "mkdocs.en.yml"]),
]

failed = [(n, r) for n, r in results if r.returncode != 0]
if not failed:
    sys.stderr.write("[mkdocs-strict] both zh + en strict builds passed\n")
    sys.exit(0)

sys.stderr.write("[mkdocs-strict] FAILED: " + ", ".join(n for n, _ in failed) + "\n")
for n, r in failed:
    tail = (r.stderr or r.stdout or "")[-2000:]
    sys.stderr.write(f"--- {n} ---\n{tail}\n")
sys.exit(2)
