#!/usr/bin/env python3
"""Generic assembler: python3 assemble_generic.py <task-output.json> <dest.md> [field]
Reads a translate-workflow output file and concatenates the per-chunk translations in id order."""
import json, re, sys

OUT_FILE, DEST = sys.argv[1], sys.argv[2]
FIELD = sys.argv[3] if len(sys.argv) > 3 else "t"

raw = open(OUT_FILE, encoding="utf-8").read()
try:
    data = json.loads(raw)
except json.JSONDecodeError:
    i = raw.find("{"); data, _ = json.JSONDecoder().raw_decode(raw[i:])
results = (data.get("result") or data)["results"]
results.sort(key=lambda r: r["id"])
failed = [r["id"] for r in results if not r.get(FIELD)]

def clean(s):
    s = s.strip()
    s = re.sub(r"^```[a-zA-Z]*\n", "", s)
    s = re.sub(r"\n```$", "", s)
    return s.strip()

parts = []
for r in results:
    v = r.get(FIELD)
    parts.append(clean(v) if v else f"<!-- MISSING CHUNK {r['id']:03d} — translation failed, re-run -->")
body = re.sub(r"\n{3,}", "\n\n", "\n\n".join(parts)) + "\n"
open(DEST, "w", encoding="utf-8").write(body)
print(f"wrote {DEST}: {body.count(chr(10))} lines, {len(body)} chars, headings={len(re.findall(r'(?m)^## ', body))}")
print(f"failed/missing chunks: {failed if failed else 'none'}")
