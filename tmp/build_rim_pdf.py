#!/usr/bin/env python3
"""Build pipeline for the RIM (intelligence) paper.

Produces:
  paper/intelligence/paper.pdf  — canonical PDF (updated in place)
  tmp/rim-paper.pdf             — copy for review

Features:
  - Compiles .tex via tectonic (auto-downloads LaTeX packages)
  - Verifies all citation keys resolve (cite keys ↔ bibitem keys)
  - Reports overfull hbox warnings

Usage:
  python3 tmp/build_rim_pdf.py            # Build PDF
  python3 tmp/build_rim_pdf.py --verify   # Verify citations only (no build)
"""

import argparse
import os
import re
import shutil
import subprocess
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = os.path.join(PROJECT_ROOT, "paper", "intelligence")
BUILD_DIR = os.path.join(PROJECT_ROOT, "tmp", "build-rim")
OUTPUT_PDF = os.path.join(PROJECT_ROOT, "tmp", "rim-paper.pdf")
CANONICAL_PDF = os.path.join(SOURCE_DIR, "paper.pdf")
TECTONIC = os.path.expanduser("~/.local/bin/tectonic")


def detect_engine():
    """Detect available LaTeX engine: pdflatex or tectonic."""
    if shutil.which("pdflatex"):
        return "pdflatex"
    if os.path.exists(TECTONIC) or shutil.which("tectonic"):
        return "tectonic"
    print("ERROR: No LaTeX engine found. Install pdflatex or tectonic.")
    print("  tectonic: curl -sSL https://github.com/tectonic-typesetting/tectonic/"
          "releases/latest/download/tectonic-0.15.0-x86_64-unknown-linux-gnu.tar.gz"
          " | tar xz -C ~/.local/bin/")
    sys.exit(1)


def run(cmd, cwd=None, check=True, capture=True):
    """Run a command, printing it first."""
    print(f"  >> {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=capture, text=True)
    if result.returncode != 0 and check:
        if capture:
            print(f"STDOUT:\n{result.stdout}")
            print(f"STDERR:\n{result.stderr}")
        sys.exit(1)
    return result


def verify_citations(tex_path):
    """Verify all \\cite keys have matching \\bibitem entries and vice versa.

    Returns (ok: bool, errors: list[str]).
    """
    with open(tex_path, "r") as f:
        content = f.read()

    # Extract all cited keys
    cite_pattern = re.compile(
        r"\\(?:cite[tp]?\*?|citeauthor|citeyearpar|citealp|citealt)"
        r"\{([^}]*)\}"
    )
    cited_keys = set()
    for match in cite_pattern.finditer(content):
        for key in match.group(1).split(","):
            key = key.strip()
            if key:
                cited_keys.add(key)

    # Extract all bibitem keys
    bibitem_pattern = re.compile(r"\\bibitem\[[^\]]*\]\{([^}]+)\}")
    defined_keys = set()
    for match in bibitem_pattern.finditer(content):
        defined_keys.add(match.group(1))

    errors = []

    # Keys cited but not defined
    missing = cited_keys - defined_keys
    for key in sorted(missing):
        errors.append(f"CITE WITHOUT BIBITEM: {key}")

    # Keys defined but never cited
    unused = defined_keys - cited_keys
    for key in sorted(unused):
        errors.append(f"BIBITEM NEVER CITED: {key}")

    # Check bibitem labels: 3+ authors should use "et al."
    bibitem_label_pattern = re.compile(
        r"\\bibitem\[([^\]]*)\]\{[^}]+\}\s*\n([^\n]+)"
    )
    for match in bibitem_label_pattern.finditer(content):
        label = match.group(1)
        author_line = match.group(2)
        # Count authors by counting "\&" occurrences + comma-separated
        # authors before the \&. Each \& adds the last author; authors
        # before \& are separated by ", Surname," patterns.
        # Simpler: count capital-letter surname patterns like "Surname, X."
        year_pos = re.search(r"\(\d{4}", author_line)
        author_part = author_line[:year_pos.start()] if year_pos else author_line
        # Count "Surname, I." patterns (uppercase letter followed by comma,
        # then space + initial(s) with period)
        author_count = len(re.findall(
            r"[A-Z][a-zü]+,\s+[A-Z]\.", author_part
        ))
        if author_count >= 3 and "et~al" not in label and "et al" not in label:
            errors.append(
                f"LABEL NEEDS et al. (has {author_count} authors): {label}"
            )

    return len(errors) == 0, errors


def build_pdf():
    """Build PDF via pdflatex or tectonic (auto-detected)."""
    engine = detect_engine()
    print(f"  Using engine: {engine}\n")

    # Clean and prepare build directory
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.makedirs(BUILD_DIR)

    # Copy source .tex
    tex_src = os.path.join(SOURCE_DIR, "paper.tex")
    tex_dst = os.path.join(BUILD_DIR, "paper.tex")
    shutil.copy2(tex_src, tex_dst)

    if engine == "pdflatex":
        # RIM uses thebibliography (no .bib file), so no bibtex needed
        run(["pdflatex", "-interaction=nonstopmode", "paper.tex"], cwd=BUILD_DIR)
        run(["pdflatex", "-interaction=nonstopmode", "paper.tex"], cwd=BUILD_DIR)
        run(["pdflatex", "-interaction=nonstopmode", "paper.tex"], cwd=BUILD_DIR)
        result = None  # no output to parse
    else:
        tectonic_bin = TECTONIC if os.path.exists(TECTONIC) else "tectonic"
        result = run(
            [tectonic_bin, "--reruns", "5", "--print", "paper.tex"],
            cwd=BUILD_DIR,
            check=False,
        )

    # Check for critical issues (tectonic output only — pdflatex logs to file)
    output = ""
    if result is not None:
        output = (result.stdout or "") + (result.stderr or "")

    # Count undefined citations in final output
    undefined = re.findall(r"Citation `([^']+)' .* undefined", output)
    if undefined:
        unique = sorted(set(undefined))
        print(f"\nWARNING: {len(unique)} undefined citation(s):")
        for key in unique:
            print(f"  - {key}")

    # Report overfull boxes
    overfull = re.findall(r"Overfull \\hbox \(([^)]+)\)", output)
    if overfull:
        # Deduplicate (tectonic reports per pass)
        unique_overfull = sorted(set(overfull))
        print(f"\nOverfull hbox warnings ({len(unique_overfull)} unique):")
        for o in unique_overfull:
            print(f"  - {o}")

    # Check for missing characters
    missing_chars = re.findall(r"Missing character: .* \(\"([^\"]+)\)", output)
    if missing_chars:
        unique_chars = sorted(set(missing_chars))
        print(f"\nMISSING CHARACTERS (font issue):")
        for c in unique_chars:
            print(f"  - U+{c}")

    built_pdf = os.path.join(BUILD_DIR, "paper.pdf")
    if not os.path.exists(built_pdf):
        print("ERROR: paper.pdf not produced")
        sys.exit(1)

    # Copy to output locations
    shutil.copy2(built_pdf, OUTPUT_PDF)
    shutil.copy2(built_pdf, CANONICAL_PDF)
    print(f"\nPDF ready: {OUTPUT_PDF}")
    print(f"Canonical: {CANONICAL_PDF}")


def main():
    parser = argparse.ArgumentParser(description="Build RIM (intelligence) paper")
    parser.add_argument(
        "--verify", action="store_true",
        help="Verify citations only (no build)",
    )
    args = parser.parse_args()

    tex_file = os.path.join(SOURCE_DIR, "paper.tex")

    # Always verify citations first
    print("=== Verifying citations ===\n")
    ok, errors = verify_citations(tex_file)
    if errors:
        for e in errors:
            print(f"  ✗ {e}")
        if not args.verify:
            print(f"\n{len(errors)} citation issue(s) found. Building anyway...\n")
    else:
        print("  ✓ All citations verified\n")

    if args.verify:
        sys.exit(0 if ok else 1)

    print("=== Building RIM paper (tectonic) ===\n")
    build_pdf()
    print("\nDone.")


if __name__ == "__main__":
    main()
