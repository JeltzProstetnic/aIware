#!/usr/bin/env python3
"""Build pipeline for the NoC (trimmed) paper.

Produces:
  tmp/noc-paper.pdf        — review-quality PDF from LaTeX
  tmp/noc-paper.docx       — submission-quality .docx from LaTeX via pandoc

Usage:
  python3 tmp/build_noc_pdf.py            # PDF only
  python3 tmp/build_noc_pdf.py --docx     # PDF + .docx
  python3 tmp/build_noc_pdf.py --highlight # PDF with yellow-highlighted changes
"""

import argparse
import os
import shutil
import subprocess
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = os.path.join(PROJECT_ROOT, "paper", "trimmed", "noc")
BUILD_DIR = os.path.join(PROJECT_ROOT, "tmp", "build-noc")
OUTPUT_PDF = os.path.join(PROJECT_ROOT, "tmp", "noc-paper.pdf")
OUTPUT_DOCX = os.path.join(PROJECT_ROOT, "tmp", "noc-paper.docx")


def run(cmd, cwd=None, check=True):
    """Run a command, printing it first."""
    print(f"  >> {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0 and check:
        print(f"STDOUT:\n{result.stdout}")
        print(f"STDERR:\n{result.stderr}")
        sys.exit(1)
    return result


def build_pdf(highlight=False):
    """Build PDF via pdflatex + bibtex."""
    # Clean and prepare build directory
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.makedirs(BUILD_DIR)

    # Copy source files
    for f in os.listdir(SOURCE_DIR):
        src = os.path.join(SOURCE_DIR, f)
        if os.path.isfile(src) and (
            f.endswith(".tex")
            or f.endswith(".bib")
            or f.endswith(".png")
            or f.endswith(".jpg")
            or f.endswith(".pdf")
            or f.endswith(".svg")
            or f.endswith(".css")
            or f.endswith(".csl")
        ):
            shutil.copy2(src, BUILD_DIR)

    tex_file = os.path.join(BUILD_DIR, "paper.tex")

    if highlight:
        # Add soul package for highlighting and enable it
        with open(tex_file, "r") as fh:
            content = fh.read()
        content = content.replace(
            r"\usepackage{microtype}",
            r"\usepackage{microtype}" + "\n" + r"\usepackage{soul}",
        )
        with open(tex_file, "w") as fh:
            fh.write(content)

    # pdflatex pass 1
    run(["pdflatex", "-interaction=nonstopmode", "paper.tex"], cwd=BUILD_DIR)

    # bibtex (may warn about missing citations on first pass — that's normal)
    run(["bibtex", "paper"], cwd=BUILD_DIR, check=False)

    # pdflatex pass 2 + 3
    run(["pdflatex", "-interaction=nonstopmode", "paper.tex"], cwd=BUILD_DIR)
    run(["pdflatex", "-interaction=nonstopmode", "paper.tex"], cwd=BUILD_DIR)

    # Copy output
    built_pdf = os.path.join(BUILD_DIR, "paper.pdf")
    if os.path.exists(built_pdf):
        shutil.copy2(built_pdf, OUTPUT_PDF)
        print(f"\nPDF ready: {OUTPUT_PDF}")
    else:
        print("ERROR: paper.pdf not found in build directory")
        sys.exit(1)


def _preprocess_tex_for_pandoc(tex_file):
    """Preprocess .tex for pandoc: convert tabularx to tabular.

    pandoc silently drops complex tabularx tables. This converts them
    to plain tabular so all tables survive in the .docx output.
    Also adds explicit 'Table N.' prefixes to captions since pandoc
    doesn't auto-number tables in .docx.
    """
    import re

    with open(tex_file, "r") as fh:
        content = fh.read()

    # Replace tabularx environments with tabular
    # \begin{tabularx}{\textwidth}{cols} → \begin{tabular}{cols}
    content = re.sub(
        r"\\begin\{tabularx\}\{[^}]*\}",
        r"\\begin{tabular}",
        content,
    )
    content = content.replace(r"\end{tabularx}", r"\end{tabular}")

    # Replace X column type with l (left-aligned) for pandoc
    # This is a rough fix — X columns become left-aligned instead of
    # auto-width, but it preserves the table content in .docx
    # Handle X that appears in column specs (after \begin{tabular}{...})
    def replace_x_columns(match):
        spec = match.group(1)
        spec = re.sub(r"(?<![A-Za-z])X(?![A-Za-z])", "l", spec)
        return r"\begin{tabular}{" + spec + "}"

    content = re.sub(
        r"\\begin\{tabular\}\{([^}]*)\}",
        replace_x_columns,
        content,
    )

    # Add explicit "Table N." to captions for pandoc (it doesn't auto-number)
    table_num = 0

    def add_table_number(match):
        nonlocal table_num
        table_num += 1
        caption_text = match.group(1)
        return rf"\caption{{Table {table_num}. {caption_text}}}"

    # Only number captions inside table environments
    parts = re.split(r"(\\begin\{table\}.*?\\end\{table\})", content, flags=re.DOTALL)
    result = []
    for part in parts:
        if part.startswith(r"\begin{table}"):
            part = re.sub(r"\\caption\{([^}]+)\}", add_table_number, part, count=1)
        result.append(part)
    content = "".join(result)

    pandoc_tex = tex_file.replace(".tex", "-pandoc.tex")
    with open(pandoc_tex, "w") as fh:
        fh.write(content)
    print(f"  Preprocessed {os.path.basename(pandoc_tex)} for pandoc (tabularx→tabular, table numbering)")
    return pandoc_tex


def build_docx():
    """Build .docx from .tex via pandoc."""
    tex_file = os.path.join(BUILD_DIR, "paper.tex")
    bib_file = os.path.join(BUILD_DIR, "references.bib")

    if not os.path.exists(tex_file):
        print("ERROR: Run PDF build first (need build directory)")
        sys.exit(1)

    # Preprocess .tex for pandoc compatibility
    pandoc_tex = _preprocess_tex_for_pandoc(tex_file)

    csl_file = os.path.join(BUILD_DIR, "apa.csl")
    cmd = [
        "pandoc",
        pandoc_tex,
        "--from=latex",
        "--to=docx",
        f"--bibliography={bib_file}",
        "--citeproc",
        f"--resource-path={BUILD_DIR}",
        f"--output={OUTPUT_DOCX}",
    ]
    if os.path.exists(csl_file):
        cmd.append(f"--csl={csl_file}")
    run(cmd, cwd=BUILD_DIR)
    print(f"DOCX ready: {OUTPUT_DOCX}")


def main():
    parser = argparse.ArgumentParser(description="Build NoC paper")
    parser.add_argument("--docx", action="store_true", help="Also build .docx")
    parser.add_argument(
        "--highlight", action="store_true", help="Enable yellow highlighting"
    )
    args = parser.parse_args()

    print("=== Building NoC paper (LaTeX pipeline) ===\n")
    build_pdf(highlight=args.highlight)

    if args.docx:
        print("\n=== Building .docx submission copy ===\n")
        build_docx()

    print("\nDone.")


if __name__ == "__main__":
    main()
