#!/usr/bin/env python3
"""Build Hugging Face dataset JSONL from FMT wiki articles + papers."""

import json
import os
import re
import sys
from pathlib import Path

WIKI_DIR = Path("/home/jeltz/aIware/wiki")
OUTPUT = Path("/home/jeltz/aIware/tmp/huggingface-dataset/dataset.jsonl")

EXCLUDE_FILES = {"STYLE-GUIDE.md", "INFRASTRUCTURE-SPEC.md"}
EXCLUDE_DIRS = {"assets"}

SITE_BASE = "https://fmt.matthiasgruber.com"

# Papers to include (no YAML frontmatter)
PAPERS = [
    {
        "path": Path("/home/jeltz/aIware/paper/full/four-model-theory-full.md"),
        "id": "paper-fmt",
        "title": "The Four-Model Theory of Consciousness: A Simulation-Based Framework Unifying the Hard Problem, Binding, and Altered States",
        "section": "Research Papers",
        "source": "paper",
        "url": "https://doi.org/10.5281/zenodo.18669891",
    },
    {
        "path": Path("/home/jeltz/aIware/paper/intelligence/paper.md"),
        "id": "paper-rim",
        "title": "Why Intelligence Models Must Include Motivation: A Recursive Framework",
        "section": "Research Papers",
        "source": "paper",
        "url": "https://osf.io/preprints/osf/kctvg",
    },
]


def parse_yaml_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and return (metadata, body)."""
    if not text.startswith("---"):
        return {}, text

    end = text.find("\n---", 3)
    if end == -1:
        return {}, text

    frontmatter = text[3:end].strip()
    body = text[end + 4:].strip()

    meta = {}
    for line in frontmatter.split("\n"):
        line = line.strip()
        if ":" in line and not line.startswith("-") and not line.startswith("["):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if key in ("title", "section", "description", "article_number"):
                meta[key] = val
    return meta, body


def wiki_url(rel_path: str) -> str:
    """Convert relative path like 'basics/qualia.md' to site URL."""
    # MkDocs uses directory/filename without .md
    url_path = rel_path.replace(".md", "/")
    return f"{SITE_BASE}/{url_path}"


def collect_wiki_articles() -> list[dict]:
    """Collect all wiki articles with metadata."""
    entries = []

    for root, dirs, files in os.walk(WIKI_DIR):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for fname in sorted(files):
            if not fname.endswith(".md"):
                continue
            if fname in EXCLUDE_FILES:
                continue

            fpath = Path(root) / fname
            rel = fpath.relative_to(WIKI_DIR)

            text = fpath.read_text(encoding="utf-8")
            meta, body = parse_yaml_frontmatter(text)

            # Derive ID from path
            article_id = str(rel).replace("/", "-").replace(".md", "")

            title = meta.get("title", fname.replace(".md", "").replace("-", " ").title())
            section = meta.get("section", rel.parent.name.replace("-", " ").title() if rel.parent.name else "Index")

            entries.append({
                "id": article_id,
                "title": title,
                "section": section,
                "text": body,
                "source": "wiki",
                "url": wiki_url(str(rel)),
            })

    return entries


def collect_papers() -> list[dict]:
    """Collect research papers."""
    entries = []
    for paper in PAPERS:
        text = paper["path"].read_text(encoding="utf-8")
        # Papers have no YAML frontmatter -- strip any leading metadata lines
        # but keep all markdown content
        _, body = parse_yaml_frontmatter(text)
        # If no frontmatter was found, body == text (the full content)
        if body == text:
            body = text.strip()

        entries.append({
            "id": paper["id"],
            "title": paper["title"],
            "section": paper["section"],
            "text": body,
            "source": paper["source"],
            "url": paper["url"],
        })
    return entries


def validate(entries: list[dict]) -> bool:
    """Validate dataset integrity."""
    ok = True

    # Check all fields present
    for e in entries:
        for key in ["id", "title", "section", "text", "source", "url"]:
            if key not in e:
                print(f"ERROR: Missing key '{key}' in {e.get('id', '?')}")
                ok = False

    # Check for empty texts
    empty = [e["id"] for e in entries if not e["text"].strip()]
    if empty:
        print(f"ERROR: Empty text in: {empty}")
        ok = False

    # Check for duplicate IDs
    ids = [e["id"] for e in entries]
    seen = set()
    for x in ids:
        if x in seen:
            print(f"ERROR: Duplicate ID: {x}")
            ok = False
        seen.add(x)

    # Check source values
    bad_source = [e["id"] for e in entries if e["source"] not in ("wiki", "paper")]
    if bad_source:
        print(f"ERROR: Invalid source in: {bad_source}")
        ok = False

    if ok:
        print("Validation passed.")
    return ok


def main():
    wiki = collect_wiki_articles()
    papers = collect_papers()
    all_entries = wiki + papers

    with open(OUTPUT, "w", encoding="utf-8") as f:
        for entry in all_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"Wrote {len(all_entries)} entries to {OUTPUT}")
    print(f"  Wiki articles: {len(wiki)}")
    print(f"  Papers: {len(papers)}")

    # Summary by section
    sections = {}
    for e in all_entries:
        sections[e["section"]] = sections.get(e["section"], 0) + 1
    print("\nBy section:")
    for sec, count in sorted(sections.items()):
        print(f"  {sec}: {count}")

    # Total text size
    total_chars = sum(len(e["text"]) for e in all_entries)
    print(f"\nTotal text: {total_chars:,} chars (~{total_chars // 4:,} tokens)")

    # Validate
    print()
    validate(all_entries)


if __name__ == "__main__":
    main()
