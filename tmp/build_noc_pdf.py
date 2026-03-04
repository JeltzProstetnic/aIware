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


def build_docx():
    """Build .docx from .tex via pandoc."""
    tex_file = os.path.join(BUILD_DIR, "paper.tex")
    bib_file = os.path.join(BUILD_DIR, "references.bib")

    if not os.path.exists(tex_file):
        print("ERROR: Run PDF build first (need build directory)")
        sys.exit(1)

    csl_file = os.path.join(BUILD_DIR, "apa.csl")
    cmd = [
        "pandoc",
        tex_file,
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
