#!/usr/bin/env python3
"""
Search the German book PDF for cosmology-related content and key references.
"""

import fitz  # PyMuPDF
import re
import os
from collections import defaultdict

PDF_PATH = "/mnt/c/Users/Matthias/Documents/_Eigene/Die Emergenz des Bewusstseins 6x9 lit.pdf"
OUTPUT_PATH = "/home/jeltz/aIware/tmp/book-cosmology-search.txt"

# Search keywords grouped by category
SEARCH_GROUPS = {
    "Holographic / t'Hooft": [
        r"'t\s*Hooft",
        r"\bt\s*Hooft\b",
        r"holograph",  # catches holographic, holographisch, etc.
        r"Holograph",
    ],
    "Metzinger / Self-Model": [
        r"Metzinger",
        r"Selbstmodell",
        r"Self.?Model",
        r"Selbst-Modell",
    ],
    "Cellular Automaton / Wolfram": [
        r"Zellularautomat",
        r"Zellul.{0,5}rer\s+Automat",
        r"cellular\s+automaton",
        r"cellular\s+automata",
        r"Wolfram",
        r"Automat",  # catches Automaten, Automatismus etc.
    ],
    "Cosmology / Universe": [
        r"Kosmo",  # Kosmologie, Kosmologisch, etc.
        r"cosmol",
        r"Universum",
        r"universe",
        r"kosmisch",
        r"cosmic",
    ],
    "Singularity": [
        r"Singulari",  # Singularität, singularity, etc.
    ],
    "Criticality / Edge of Chaos": [
        r"Kritikalit",  # Kritikalität
        r"criticality",
        r"edge\s+of\s+chaos",
        r"Rand\s+des\s+Chaos",
        r"kritisch",  # kritischer Übergang etc.
    ],
    "Big Bang / Black Hole": [
        r"Big\s+Bang",
        r"Urknall",
        r"schwarzes?\s+Loch",
        r"black\s+hole",
        r"Schwarzloch",
    ],
    "Emergence": [
        r"Emergenz",
        r"emergenz",
        r"emergence",
        r"emergent",
        r"emergier",
    ],
    "Dennett / Multiple Draft": [
        r"Dennett",
        r"Multiple\s+Draft",
        r"Vielfach.{0,10}Entwurf",
    ],
}

def extract_context(text, match_start, match_end, context_chars=150):
    """Extract surrounding context around a match."""
    start = max(0, match_start - context_chars)
    end = min(len(text), match_end + context_chars)

    prefix = text[start:match_start]
    matched = text[match_start:match_end]
    suffix = text[match_end:end]

    # Clean up whitespace
    prefix = re.sub(r'\s+', ' ', prefix).strip()
    matched = re.sub(r'\s+', ' ', matched).strip()
    suffix = re.sub(r'\s+', ' ', suffix).strip()

    return prefix, matched, suffix


def main():
    print(f"Opening PDF: {PDF_PATH}")

    if not os.path.exists(PDF_PATH):
        print(f"ERROR: PDF not found at {PDF_PATH}")
        return

    doc = fitz.open(PDF_PATH)
    total_pages = len(doc)
    print(f"Total pages: {total_pages}")

    # Results: dict of category -> list of (page_num, pattern, prefix, match, suffix)
    results = defaultdict(list)

    # Track already-seen matches to avoid duplicates from overlapping patterns
    seen_matches = set()  # (page_num, match_start_approx, category)

    for page_num in range(total_pages):
        page = doc[page_num]
        text = page.get_text()

        if not text.strip():
            continue

        for category, patterns in SEARCH_GROUPS.items():
            for pattern in patterns:
                for m in re.finditer(pattern, text, re.IGNORECASE):
                    # Deduplicate: same page, close position, same category
                    dedup_key = (page_num, m.start() // 50, category)
                    if dedup_key in seen_matches:
                        continue
                    seen_matches.add(dedup_key)

                    prefix, matched, suffix = extract_context(text, m.start(), m.end(), 150)
                    results[category].append({
                        'page': page_num + 1,  # 1-indexed
                        'pattern': pattern,
                        'matched': matched,
                        'prefix': prefix,
                        'suffix': suffix,
                        'full_context': f"...{prefix} [{matched}] {suffix}..."
                    })

    doc.close()

    # Write output
    lines = []
    lines.append("=" * 80)
    lines.append("COSMOLOGY & KEY REFERENCES SEARCH — Die Emergenz des Bewusstseins (2015)")
    lines.append(f"PDF: {PDF_PATH}")
    lines.append(f"Total pages searched: {total_pages}")
    lines.append("=" * 80)
    lines.append("")

    total_matches = sum(len(v) for v in results.values())
    lines.append(f"TOTAL MATCHES FOUND: {total_matches}")
    lines.append("")

    # Summary table
    lines.append("SUMMARY BY CATEGORY:")
    lines.append("-" * 40)
    for category, matches in sorted(results.items()):
        pages = sorted(set(m['page'] for m in matches))
        lines.append(f"  {category}: {len(matches)} matches on pages {pages}")
    lines.append("")

    # Detailed results by category
    for category, matches in sorted(results.items()):
        lines.append("=" * 80)
        lines.append(f"CATEGORY: {category}")
        lines.append(f"  {len(matches)} matches")
        lines.append("=" * 80)

        # Sort by page
        matches_sorted = sorted(matches, key=lambda x: x['page'])

        for m in matches_sorted:
            lines.append(f"\n  [Page {m['page']}] Pattern: {m['pattern']!r}")
            lines.append(f"  Matched: {m['matched']!r}")
            lines.append(f"  Context: {m['full_context']}")
            lines.append("")

    output_text = "\n".join(lines)

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(output_text)

    print(f"\nResults written to: {OUTPUT_PATH}")
    print(f"\nSUMMARY:")
    for category, matches in sorted(results.items()):
        pages = sorted(set(m['page'] for m in matches))
        print(f"  {category}: {len(matches)} matches on pages {pages[:10]}{'...' if len(pages) > 10 else ''}")

    return results


if __name__ == "__main__":
    main()
