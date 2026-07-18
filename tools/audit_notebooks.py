#!/usr/bin/env python3
"""Audit Jupyter notebooks for common portability and review issues."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    ".ipynb_checkpoints",
}

PATTERNS: dict[str, re.Pattern[str]] = {
    "Windows absolute path": re.compile(r"""(?<![A-Za-z0-9_])[A-Za-z]:[\\/][^\s"'`]+"""),
    "Colab Drive path": re.compile(r"""/content/(?:drive|gdrive)/[^\s"'`]+"""),
    "Drive mount": re.compile(r"""drive\.mount\s*\("""),
    "Graphviz/pydotplus": re.compile(
        r"""pydotplus|export_graphviz|graph\.write_png"""
    ),
    "Shell package installation": re.compile(
        r"""(?m)^\s*(?:!|%pip\s+|pip\s+install|conda\s+install)"""
    ),
    "Shell download command": re.compile(
        r"""(?m)^\s*(?:!|%%bash).*?(?:wget|curl|gdown)"""
    ),
}

MAX_OUTPUT_BYTES = 500_000


def iter_notebooks(root: Path):
    for path in sorted(root.rglob("*.ipynb")):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        yield path


def source_text(cell: dict[str, Any]) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(source)
    return str(source)


def output_size(output: dict[str, Any]) -> int:
    try:
        return len(
            json.dumps(
                output,
                ensure_ascii=False,
                separators=(",", ":"),
            ).encode("utf-8")
        )
    except (TypeError, ValueError):
        return 0


def audit_notebook(path: Path, root: Path) -> list[str]:
    issues: list[str] = []

    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"INVALID NOTEBOOK JSON: {exc}"]

    cells = notebook.get("cells", [])
    if not isinstance(cells, list):
        return ["INVALID NOTEBOOK STRUCTURE: 'cells' is not a list"]

    code_cells = 0
    markdown_cells = 0
    output_count = 0
    total_output_bytes = 0

    for index, cell in enumerate(cells, start=1):
        cell_type = cell.get("cell_type")
        text = source_text(cell)

        if cell_type == "code":
            code_cells += 1

            for label, pattern in PATTERNS.items():
                if pattern.search(text):
                    issues.append(f"cell {index}: {label}")

            outputs = cell.get("outputs", [])
            if isinstance(outputs, list):
                output_count += len(outputs)
                total_output_bytes += sum(
                    output_size(output)
                    for output in outputs
                    if isinstance(output, dict)
                )

        elif cell_type == "markdown":
            markdown_cells += 1

    if code_cells and markdown_cells == 0:
        issues.append("no Markdown teaching/documentation cells")

    if output_count:
        issues.append(
            f"{output_count} saved output(s), "
            f"approximately {total_output_bytes / 1024:.1f} KiB"
        )

    if total_output_bytes > MAX_OUTPUT_BYTES:
        issues.append("large saved notebook outputs")

    try:
        relative = path.relative_to(root)
    except ValueError:
        relative = path

    return issues


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()

    if not root.exists():
        print(f"Repository path does not exist: {root}", file=sys.stderr)
        return 2

    notebooks = list(iter_notebooks(root))
    print(f"Repository: {root}")
    print(f"Notebooks found: {len(notebooks)}")
    print()

    notebooks_with_issues = 0

    for path in notebooks:
        issues = audit_notebook(path, root)
        if not issues:
            continue

        notebooks_with_issues += 1
        print(f"[REVIEW] {path.relative_to(root)}")
        for issue in issues:
            print(f"  - {issue}")
        print()

    print(
        f"Audit complete: {notebooks_with_issues} of "
        f"{len(notebooks)} notebook(s) require review."
    )

    # This is an advisory audit, so findings do not produce a failing exit code.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
