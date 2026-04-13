#!/usr/bin/env python3
"""Build .docx from German book manuscript with proper formatting."""
import subprocess
import sys
import re
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "pop-sci/book-manuscript-de.md")
OUT = os.path.join(BASE, "tmp/book-manuscript-de.docx")
TMP = os.path.join(BASE, "tmp/book-manuscript-de-preprocessed.md")

with open(SRC, "r") as f:
    content = f.read()

# Remove the initial --- ... --- block (lines 7-11) that pandoc misreads as YAML
# The pattern: line starting with ---, some content, line starting with ---
# Replace first two --- with nothing (they're decorative separators around the dedication)
lines = content.split("\n")
new_lines = []
hr_count = 0
for i, line in enumerate(lines):
    if line.strip() == "---":
        hr_count += 1
        if hr_count <= 2:
            # First two --- are around the dedication - replace with blank lines
            new_lines.append("")
            continue
        else:
            # Chapter separators - replace with a page break marker for pandoc
            # Use a raw openxml page break in a div
            new_lines.append("")
            new_lines.append("\\newpage")
            new_lines.append("")
            continue
    new_lines.append(line)

preprocessed = "\n".join(new_lines)

with open(TMP, "w") as f:
    f.write(preprocessed)

# Build with pandoc
cmd = [
    "pandoc", TMP,
    "-o", OUT,
    "--from", "markdown",
    "--to", "docx",
    f"--resource-path={os.path.join(BASE, 'pop-sci')}",
    "--toc",
    "--toc-depth=2",
]

result = subprocess.run(cmd, capture_output=True, text=True)
if result.stderr:
    print(f"Warnings: {result.stderr}", file=sys.stderr)
if result.returncode != 0:
    print(f"FAILED: {result.stderr}", file=sys.stderr)
    sys.exit(1)

# Clean up
os.remove(TMP)
print(f"Built: {OUT}")
