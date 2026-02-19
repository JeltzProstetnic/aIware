#!/usr/bin/env python3
"""Build cosmology papers from .md to .tex to .pdf using pandoc and pdflatex."""

import os
import sys
import subprocess
import shutil

REPO_ROOT = "/home/jeltz/aIware"

# Paper definitions
PAPERS = {
    "paper3": {
        "name": "Paper 3: SB-HC4A",
        "md": os.path.join(REPO_ROOT, "paper/cosmology/sb-hc4a.md"),
        "unicode_header": os.path.join(REPO_ROOT, "paper/cosmology/unicode-header.tex"),
        "tex": os.path.join(REPO_ROOT, "paper/cosmology/sb-hc4a.tex"),
        "pdf": os.path.join(REPO_ROOT, "paper/cosmology/sb-hc4a.pdf"),
        "output_dir": os.path.join(REPO_ROOT, "paper/cosmology"),
    },
    "paper6": {
        "name": "Paper 6: SB-HC4A Formalization",
        "md": os.path.join(REPO_ROOT, "paper/cosmology_formal/sb-hc4a-formalization.md"),
        "unicode_header": os.path.join(REPO_ROOT, "paper/cosmology_formal/unicode-header.tex"),
        "tex": os.path.join(REPO_ROOT, "paper/cosmology_formal/sb-hc4a-formalization.tex"),
        "pdf": os.path.join(REPO_ROOT, "paper/cosmology_formal/sb-hc4a-formalization.pdf"),
        "output_dir": os.path.join(REPO_ROOT, "paper/cosmology_formal"),
    },
}


def check_dependencies():
    """Check that pandoc and pdflatex are available."""
    missing = []

    if shutil.which("pandoc") is None:
        missing.append("pandoc")

    if shutil.which("pdflatex") is None:
        missing.append("pdflatex")

    if missing:
        print(f"ERROR: Missing required tools: {', '.join(missing)}")
        print("Install with: sudo apt install pandoc texlive-latex-base texlive-latex-extra")
        return False

    return True


def build_paper(paper_id, keep_aux=False):
    """Build a single paper from .md to .pdf.

    Args:
        paper_id: "paper3" or "paper6"
        keep_aux: If True, keep auxiliary files (.aux, .log, .out)

    Returns:
        True if successful, False otherwise
    """
    paper = PAPERS[paper_id]

    print(f"\n{'='*60}")
    print(f"Building {paper['name']}")
    print(f"{'='*60}")

    # Check source files exist
    if not os.path.exists(paper["md"]):
        print(f"ERROR: Source file not found: {paper['md']}")
        return False

    if not os.path.exists(paper["unicode_header"]):
        print(f"ERROR: Unicode header not found: {paper['unicode_header']}")
        return False

    # Step 1: Convert .md to .tex using pandoc
    print(f"\n[1/3] Converting .md to .tex with pandoc...")
    pandoc_cmd = [
        "pandoc",
        paper["md"],
        "-H", paper["unicode_header"],
        "--standalone",
        "-o", paper["tex"]
    ]

    try:
        result = subprocess.run(
            pandoc_cmd,
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0:
            print(f"ERROR: pandoc failed:")
            print(result.stderr)
            return False

        print(f"  Created: {paper['tex']}")

    except subprocess.TimeoutExpired:
        print("ERROR: pandoc timed out")
        return False
    except Exception as e:
        print(f"ERROR: pandoc failed: {e}")
        return False

    # Step 2: Compile .tex to .pdf (first pass)
    print(f"\n[2/3] Compiling .tex to .pdf (pass 1)...")
    pdflatex_cmd = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-output-directory", paper["output_dir"],
        paper["tex"]
    ]

    try:
        result = subprocess.run(
            pdflatex_cmd,
            capture_output=True,
            text=True,
            cwd=paper["output_dir"],
            timeout=120
        )

        if result.returncode != 0:
            print(f"ERROR: pdflatex pass 1 failed")
            # Show relevant errors from log
            log_file = paper["tex"].replace(".tex", ".log")
            if os.path.exists(log_file):
                with open(log_file, 'r', errors='replace') as f:
                    log = f.read()
                errors = [l for l in log.split('\n') if l.startswith('!')]
                for e in errors[:10]:
                    print(f"  {e}")
            return False

        print(f"  Pass 1 complete")

    except subprocess.TimeoutExpired:
        print("ERROR: pdflatex timed out")
        return False
    except Exception as e:
        print(f"ERROR: pdflatex failed: {e}")
        return False

    # Step 3: Compile again for cross-references
    print(f"\n[3/3] Compiling .tex to .pdf (pass 2 for cross-references)...")

    try:
        result = subprocess.run(
            pdflatex_cmd,
            capture_output=True,
            text=True,
            cwd=paper["output_dir"],
            timeout=120
        )

        if result.returncode != 0:
            print(f"ERROR: pdflatex pass 2 failed")
            return False

        print(f"  Pass 2 complete")

    except subprocess.TimeoutExpired:
        print("ERROR: pdflatex timed out")
        return False
    except Exception as e:
        print(f"ERROR: pdflatex failed: {e}")
        return False

    # Step 4: Clean up auxiliary files (unless --keep-aux)
    if not keep_aux:
        aux_extensions = [".aux", ".log", ".out"]
        for ext in aux_extensions:
            aux_file = paper["tex"].replace(".tex", ext)
            if os.path.exists(aux_file):
                os.remove(aux_file)
        print(f"\n  Cleaned up auxiliary files")

    # Check success
    if os.path.exists(paper["pdf"]):
        size_mb = os.path.getsize(paper["pdf"]) / (1024 * 1024)
        print(f"\n{'='*60}")
        print(f"SUCCESS: {paper['pdf']}")
        print(f"Size: {size_mb:.2f} MB")
        print(f"{'='*60}")
        return True
    else:
        print(f"\nERROR: PDF was not created: {paper['pdf']}")
        return False


def main():
    """Main entry point."""
    # Parse arguments
    keep_aux = "--keep-aux" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    # Determine which papers to build
    if not args:
        # Build all papers
        papers_to_build = ["paper3", "paper6"]
    elif len(args) == 1 and args[0] in PAPERS:
        # Build specific paper
        papers_to_build = [args[0]]
    else:
        print("Usage:")
        print(f"  {sys.argv[0]}              # Build both papers")
        print(f"  {sys.argv[0]} paper3       # Build only Paper 3")
        print(f"  {sys.argv[0]} paper6       # Build only Paper 6")
        print(f"  {sys.argv[0]} --keep-aux   # Keep auxiliary files")
        return 1

    # Check dependencies
    if not check_dependencies():
        return 1

    # Build papers
    results = {}
    for paper_id in papers_to_build:
        results[paper_id] = build_paper(paper_id, keep_aux)

    # Summary
    print(f"\n{'='*60}")
    print("BUILD SUMMARY")
    print(f"{'='*60}")

    for paper_id in papers_to_build:
        status = "SUCCESS" if results[paper_id] else "FAILED"
        print(f"{PAPERS[paper_id]['name']}: {status}")

    # Return 0 if all succeeded, 1 if any failed
    return 0 if all(results.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
