#!/usr/bin/env python3
"""Check that a directory is a conformant OKF v0.2 bundle (SPEC.md section 11).

Usage: python3 scripts/check_okf.py [bundle_dir]   (default: knowledge)
"""
import re
import sys
from pathlib import Path

RESERVED = {"index.md", "log.md"}


def frontmatter(text):
    """Return the raw frontmatter block, or None if the file has none."""
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else None


def check(bundle):
    errors = []
    for path in sorted(bundle.rglob("*.md")):
        rel = path.relative_to(bundle)
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if path.name == "index.md":
            if fm is not None and (path.parent != bundle or not re.fullmatch(r'okf_version:\s*"?[\d.]+"?', fm.strip())):
                errors.append(f"{rel}: only the root index.md may have frontmatter, and only okf_version")
        elif path.name == "log.md":
            if fm is not None:
                errors.append(f"{rel}: log.md must not have frontmatter")
            dates = re.findall(r"^## (.+)$", text, re.M)
            for d in dates:
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d.strip()):
                    errors.append(f"{rel}: date heading '{d}' is not YYYY-MM-DD")
            if dates != sorted(dates, reverse=True):
                errors.append(f"{rel}: date headings must be newest first")
        elif fm is None:
            errors.append(f"{rel}: missing YAML frontmatter")
        elif not re.search(r"^type:\s*\S", fm, re.M):
            errors.append(f"{rel}: frontmatter has no non-empty 'type'")
    return errors


def main():
    bundle = Path(sys.argv[1] if len(sys.argv) > 1 else "knowledge")
    if not bundle.is_dir():
        sys.exit(f"{bundle} is not a directory")
    errors = check(bundle)
    for e in errors:
        print(e)
    concepts = [p for p in bundle.rglob("*.md") if p.name not in RESERVED]
    print(f"{len(concepts)} concepts, {len(errors)} problems")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
