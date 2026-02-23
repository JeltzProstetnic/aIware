#!/usr/bin/env python3
"""Baseline calibration script for content integrity tests.

Reads current .md and .tex files, derives word counts / section counts /
reference counts, and prints the constants block for review and copy-paste
into test_content_integrity.py.

Usage: python3 tmp/update_test_baselines.py

This script intentionally does NOT auto-update test files. The developer
must review the output and commit the change deliberately.
"""

import os
import re
import importlib.util

REPO_ROOT = "/home/jeltz/aIware"


def import_module_from_path(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def count_tex_words(tex_body: str) -> int:
    """Count words after stripping LaTeX commands."""
    stripped = re.sub(r"%.*$", "", tex_body, flags=re.MULTILINE)
    stripped = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?\{([^}]*)\}", r"\2", stripped)
    stripped = re.sub(r"\\[a-zA-Z]+\*?", "", stripped)
    stripped = re.sub(r"[{}\\]", "", stripped)
    return len(stripped.split())


def extract_tex_body(tex: str) -> str:
    abs_end = tex.find(r"\end{abstract}")
    if abs_end == -1:
        return tex
    abs_end += len(r"\end{abstract}")
    bib_start = tex.find(r"\bibliography{")
    if bib_start == -1:
        bib_start = tex.find(r"\begin{thebibliography}")
    if bib_start == -1:
        bib_start = len(tex)
    return tex[abs_end:bib_start]


def analyze_paper(label, md_path, build_script_path, tex_path=None, bbl_path=None):
    """Analyze a paper and print calibration data."""
    print(f"\n{'='*60}")
    print(f" {label}")
    print(f"{'='*60}")

    # Read .md
    with open(md_path) as f:
        md = f.read()

    # Section counts
    sections = re.findall(r"^## \d+\.", md, re.MULTILINE)
    subsections = re.findall(r"^### ", md, re.MULTILINE)
    tables = re.findall(r"\*\*Table \d+", md)
    print(f"  Sections (## N.):    {len(sections)}")
    print(f"  Subsections (###):   {len(subsections)}")
    print(f"  Tables (**Table N):  {len(tables)}")

    # MD word count (body only)
    body_start = md.find("## 1.")
    refs_start = md.find("## References")
    if refs_start == -1:
        refs_start = len(md)
    body = md[body_start:refs_start] if body_start >= 0 else md
    md_body_words = len(body.split())
    print(f"  MD body words:       {md_body_words}")

    # Generate .tex
    try:
        build = import_module_from_path("build", build_script_path)
        tex = build.generate_tex()
    except Exception as e:
        print(f"  ERROR generating .tex: {e}")
        tex = None

    if tex:
        # .tex analysis
        tex_body = extract_tex_body(tex)
        tex_body_words = count_tex_words(tex_body)
        citep = len(re.findall(r"\\citep\{", tex))
        citet = len(re.findall(r"\\citet\{", tex))
        bibitems = len(re.findall(r"\\bibitem", tex))
        tex_sections = len(re.findall(r"\\section\{", tex))
        tex_subsections = len(re.findall(r"\\subsection\{", tex))
        tex_tables = len(re.findall(r"\\begin\{table", tex))
        tex_figures = len(re.findall(r"\\begin\{figure", tex))

        print(f"  TEX body words:      {tex_body_words}")
        print(f"  TEX sections:        {tex_sections}")
        print(f"  TEX subsections:     {tex_subsections}")
        print(f"  TEX tables:          {tex_tables}")
        print(f"  TEX figures:         {tex_figures}")
        print(f"  \\citep:              {citep}")
        print(f"  \\citet:              {citet}")
        print(f"  Total cite cmds:     {citep + citet}")
        print(f"  \\bibitem (in .tex):  {bibitems}")

    # Check .bbl if present
    if bbl_path and os.path.exists(bbl_path):
        with open(bbl_path) as f:
            bbl = f.read()
        bbl_bibs = len(re.findall(r"\\bibitem", bbl))
        print(f"  \\bibitem (in .bbl):  {bbl_bibs}")

    # Print recommended constants
    if tex:
        word_center = tex_body_words
        word_lo = int(word_center * 0.75)
        word_hi = int(word_center * 1.25)

        ref_count = bibitems
        if bbl_path and os.path.exists(bbl_path):
            ref_count = bbl_bibs
        ref_lo = max(int(ref_count * 0.75), ref_count - 15)
        ref_hi = int(ref_count * 1.35)

        cite_min = max(int((citep + citet) * 0.5), 25)

        print(f"\n  --- Recommended Constants ---")
        print(f"  BODY_WORD_RANGE = ({word_lo:,}, {word_hi:,})  # center ~{word_center:,}")
        print(f"  REFERENCE_RANGE = ({ref_lo}, {ref_hi})")
        print(f"  CITATION_CMD_MIN = {cite_min}")


def main():
    print("Content Integrity Baseline Calibration")
    print(f"Date: 2026-02-23")
    print(f"Repo: {REPO_ROOT}")

    analyze_paper(
        "FMT Full Paper",
        os.path.join(REPO_ROOT, "paper/full/four-model-theory-full.md"),
        os.path.join(REPO_ROOT, "tmp/build_fmt_full_pdf.py"),
        bbl_path=os.path.join(REPO_ROOT, "paper/full/biorxiv/paper.bbl"),
    )

    analyze_paper(
        "Intelligence Paper",
        os.path.join(REPO_ROOT, "paper/intelligence/paper.md"),
        os.path.join(REPO_ROOT, "tmp/build_intelligence_pdf.py"),
    )

    print(f"\n{'='*60}")
    print("Review above values. If they differ significantly from")
    print("test_content_integrity.py constants, update manually.")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
