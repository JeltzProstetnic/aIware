#!/usr/bin/env python3
"""AIW-108 Phase-0 chunker: split EN manuscript into ~55-line, paragraph-aligned chunks,
pair each with its proportionally-aligned DE reference span. Writes chunk files + manifest.json."""
import json, os, re

ROOT = "/home/jeltz/aIware"
EN = os.path.join(ROOT, "pop-sci/book-manuscript.md")
DE = os.path.join(ROOT, "pop-sci/book-manuscript-de.md")
OUT = os.path.join(ROOT, "tmp/es-pipeline/chunks")
os.makedirs(OUT, exist_ok=True)

TARGET, HARD_CAP, MIN_CUT, PAD = 55, 65, 40, 12

def load(p):
    with open(p, encoding="utf-8") as f:
        return f.read().split("\n")

en, de = load(EN), load(DE)

def sections(lines):
    """Return list of (start,end) for level-2 (## ) sections; index 0 = preamble before first ##."""
    idx = [i for i, l in enumerate(lines) if l.startswith("## ")]
    bounds = []
    prev = 0
    for i in idx:
        if i > prev:
            bounds.append((prev, i))
        prev = i
    bounds.append((prev, len(lines)))
    return bounds

en_secs, de_secs = sections(en), sections(de)
n = min(len(en_secs), len(de_secs))
if len(en_secs) != len(de_secs):
    print(f"WARN: section count EN={len(en_secs)} DE={len(de_secs)} — pairing first {n}")

def heading(lines, s, e):
    for i in range(s, e):
        if lines[i].startswith("#"):
            return lines[i].lstrip("# ").strip()[:70]
    return f"lines {s}-{e}"

manifest = []
cid = 0
for si in range(n):
    es, ee = en_secs[si]
    ds, dee = de_secs[si]
    en_len = max(1, ee - es)
    de_len = dee - ds
    sec_name = heading(en, es, ee)
    # split EN section into paragraph-aligned chunks
    i = es
    while i < ee:
        j = i
        count = 0
        while j < ee:
            count += 1
            j += 1
            if count >= MIN_CUT and (j >= ee or en[j].strip() == ""):
                if count >= TARGET or count >= HARD_CAP:
                    break
            if count >= HARD_CAP:
                break
        a, b = i, j  # EN chunk [a,b)
        # proportional DE reference with padding, clamped to DE section
        f0, f1 = (a - es) / en_len, (b - es) / en_len
        da = max(ds, int(ds + f0 * de_len) - PAD)
        db = min(dee, int(ds + f1 * de_len) + PAD)
        cid += 1
        en_text = "\n".join(en[a:b])
        de_text = "\n".join(de[da:db])
        fn = f"chunk-{cid:03d}.md"
        with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
            f.write(f"<!-- chunk {cid:03d} | section: {sec_name} | EN lines {a+1}-{b} -->\n\n")
            f.write("=== TRANSLATE THIS (English — primary source) ===\n\n")
            f.write(en_text + "\n\n")
            f.write("=== DE REFERENCE (same passage — consult for meaning/idiom/grandeur; do NOT translate this) ===\n\n")
            f.write(de_text + "\n")
        manifest.append({"id": cid, "file": fn, "section": sec_name,
                          "en_lines": [a + 1, b], "en_count": b - a})
        i = j

with open(os.path.join(ROOT, "tmp/es-pipeline/manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=1)

sizes = [m["en_count"] for m in manifest]
print(f"chunks={len(manifest)}  min={min(sizes)} max={max(sizes)} total_EN_lines={sum(sizes)}")
over = [m['id'] for m in manifest if m['en_count'] > HARD_CAP]
print(f"over-cap chunks: {over if over else 'none'}")
