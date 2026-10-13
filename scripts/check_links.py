#!/usr/bin/env python3
"""Check inline local Markdown links without network requests."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def missing_links(root):
    failures = []
    for source in sorted(root.rglob("*.md")):
        if ".git" in source.relative_to(root).parts:
            continue
        body = re.sub(r"```.*?```", "", source.read_text(encoding="utf-8"), flags=re.S)
        for match in re.finditer(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", body):
            target = match.group(1).split(' "', 1)[0].strip("<>")
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            destination = (source.parent / unquote(url.path)).resolve()
            if not destination.is_relative_to(root.resolve()) or not destination.exists():
                failures.append(f"{source.relative_to(root)}: {target}")
    return failures


if __name__ == "__main__":
    errors = missing_links(ROOT)
    if errors:
        print("Missing or out-of-repository links:\n" + "\n".join(errors))
        sys.exit(1)
    print("PASS: local Markdown link targets exist (external URLs and fragments not checked).")
