#!/usr/bin/env python3
"""
Generate a highlighted-changes version of the paper.

Compares a baseline .tex file against the current version and produces
a new .tex file with yellow-highlighted additions. Uses the `soul` package
(\hl{}) for inline changes and `framed` (\begin{shaded}) for block-level
additions (new paragraphs, new subsections, new list items).

Usage:
    python3 generate_changes_pdf.py [baseline] [current] [output]

Defaults:
    baseline = /tmp/paper-pre-session24.tex
    current  = paper/full/arxiv/paper.tex  (relative to repo root)
    output   = paper/full/arxiv/paper-changes.tex
"""

import sys
import difflib
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent  # aIware root

BASELINE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/paper-pre-session24.tex")
CURRENT = Path(sys.argv[2]) if len(sys.argv) > 2 else REPO / "paper" / "full" / "arxiv" / "paper.tex"
OUTPUT = Path(sys.argv[3]) if len(sys.argv) > 3 else REPO / "paper" / "full" / "arxiv" / "paper-changes.tex"

# Preamble additions (inserted after \usepackage{setspace})
PREAMBLE_ADDITIONS = r"""
% === Changes highlighting (auto-generated) ===
\usepackage{soul}
\usepackage{framed}
\definecolor{shadecolor}{rgb}{1.0, 1.0, 0.75}  % light yellow
\sethlcolor{yellow!40}
% Yellow shaded boxes mark new/changed content since the baseline version.
"""


def is_latex_command_line(line):
    """Check if a line is primarily a LaTeX structural command."""
    stripped = line.strip()
    return (stripped.startswith(r'\begin{') or
            stripped.startswith(r'\end{') or
            stripped.startswith(r'\section') or
            stripped.startswith(r'\subsection') or
            stripped.startswith(r'\subsubsection') or
            stripped.startswith(r'\item') or
            stripped == '')


def find_changed_blocks(baseline_lines, current_lines):
    """
    Return list of (start, end) line ranges (0-indexed, inclusive)
    in current_lines that are new or changed relative to baseline.
    """
    sm = difflib.SequenceMatcher(None, baseline_lines, current_lines, autojunk=False)
    changed_lines = set()

    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ('insert', 'replace'):
            for j in range(j1, j2):
                changed_lines.add(j)

    if not changed_lines:
        return []

    # Group consecutive changed lines into blocks
    sorted_lines = sorted(changed_lines)
    blocks = []
    block_start = sorted_lines[0]
    prev = sorted_lines[0]

    for line_num in sorted_lines[1:]:
        # Allow gaps of up to 2 blank/command lines to merge blocks
        if line_num - prev <= 3:
            prev = line_num
        else:
            blocks.append((block_start, prev))
            block_start = line_num
            prev = line_num
    blocks.append((block_start, prev))

    return blocks


def generate_highlighted(baseline_path, current_path, output_path):
    baseline_lines = baseline_path.read_text().splitlines()
    current_lines = current_path.read_text().splitlines()

    blocks = find_changed_blocks(baseline_lines, current_lines)

    if not blocks:
        print("No changes detected.")
        return

    print(f"Found {len(blocks)} changed block(s):")
    for start, end in blocks:
        preview = current_lines[start].strip()[:60]
        print(f"  Lines {start+1}-{end+1}: {preview}...")

    # Build the output: insert shaded environment around changed blocks
    # We need to be careful not to put \begin{shaded} inside other environments
    # improperly. Strategy: wrap at paragraph level.

    changed_set = set()
    for start, end in blocks:
        for i in range(start, end + 1):
            changed_set.add(i)

    output_lines = []
    in_shaded = False
    preamble_inserted = False

    for i, line in enumerate(current_lines):
        # Insert preamble additions after \usepackage{setspace}
        if not preamble_inserted and r'\usepackage{setspace}' in line:
            output_lines.append(line)
            output_lines.append(PREAMBLE_ADDITIONS)
            preamble_inserted = True
            continue

        if i in changed_set:
            if not in_shaded:
                # Don't wrap pure structural commands, start shading at content
                output_lines.append(r'\begin{shaded}')
                in_shaded = True
            output_lines.append(line)
        else:
            if in_shaded:
                output_lines.append(r'\end{shaded}')
                in_shaded = False
            output_lines.append(line)

    if in_shaded:
        output_lines.append(r'\end{shaded}')

    output_path.write_text('\n'.join(output_lines))
    print(f"\nWritten to: {output_path}")
    print(f"Compile with: pdflatex {output_path}")


if __name__ == '__main__':
    generate_highlighted(BASELINE, CURRENT, OUTPUT)
