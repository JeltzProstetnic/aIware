#!/usr/bin/env python3
"""Build a review PDF of the full FMT paper with changed portions highlighted in yellow."""

import subprocess
import sys
from pathlib import Path

SRC = Path("/home/jeltz/aIware/paper/full/four-model-theory-full.md")
OUT_MD = Path("/home/jeltz/aIware/tmp/fmt-review-highlighted.md")
OUT_PDF = Path("/home/jeltz/aIware/tmp/fmt-review-highlighted.pdf")
CSS = Path("/home/jeltz/aIware/tmp/review-highlight.css")

# Each highlight: (start_substring, end_substring)
# The script finds start, then finds end AFTER start, wraps everything between in <mark>.
HIGHLIGHTS = [
    # Section 1.3 — tradition-locating paragraph
    (
        "The theory belongs to the self-modeling tradition in consciousness studies,",
        "(real/virtual) that dissolves the Hard Problem."
    ),
    # Section 1.3 — updated prediction count
    (
        "the theory generates four novel testable predictions",
        "under five principles."
    ),
    # Section 1.3 — updated roadmap
    (
        "Section 8 presents the empirical convergence evidence and four predictions.",
        "Section 8 presents the empirical convergence evidence and four predictions."
    ),
    # Section 3.1 — rewritten opening
    (
        "Consciousness — the capacity for subjective experience — is constituted",
        "Consciousness is not a property the brain possesses but a process the brain performs."
    ),
    # Section 3.1 — bridging paragraph
    (
        "This definition centers on the mechanism — self-simulation —",
        "all of which define consciousness through the self-modeling mechanism that constitutes it."
    ),
    # Section 8 — entire restructured section (title through end of Prediction 4)
    (
        "## 8. Predictions and Empirical Convergence",
        "is unique to the Four-Model Theory."
    ),
    # Section 7.4 — updated cross-ref
    (
        "Unique mechanism for identity-content determination during ego dissolution (Predictions 1 and 2) and for connecting psychedelics to anosognosia.",
        "Unique mechanism for identity-content determination during ego dissolution (Predictions 1 and 2) and for connecting psychedelics to anosognosia."
    ),
    # Section 10.2 — updated priorities
    (
        "1. **Investigate the psychedelic-anosognosia connection** (Prediction 1)",
        "4. **Measure criticality at lucid dream onset** (Prediction 4) — achievable with established lucid-dreamer paradigms and high-density EEG."
    ),
    # Section 11 — updated conclusion
    (
        "The theory generates four novel testable predictions, each with clear falsification criteria:",
        "have been independently confirmed by subsequent empirical work (Section 8.1)."
    ),
]


def highlight_text(md_text: str) -> str:
    """Wrap changed portions with <mark> tags."""
    result = md_text
    for start_str, end_str in HIGHLIGHTS:
        start_idx = result.find(start_str)
        if start_idx == -1:
            print(f"WARNING: Could not find highlight start: {start_str[:80]}...")
            continue
        end_idx = result.find(end_str, start_idx)
        if end_idx == -1:
            print(f"WARNING: Could not find highlight end: {end_str[:80]}...")
            continue
        end_idx += len(end_str)
        chunk = result[start_idx:end_idx]
        result = result[:start_idx] + "<mark>" + chunk + "</mark>" + result[end_idx:]
    return result


def write_css():
    CSS.write_text("""\
@page {
    size: A4;
    margin: 2cm;
}
body {
    font-family: "Linux Libertine", "Times New Roman", serif;
    font-size: 11pt;
    line-height: 1.5;
    max-width: 100%;
}
h1 { font-size: 18pt; margin-top: 1.5em; }
h2 { font-size: 14pt; margin-top: 1.2em; }
h3 { font-size: 12pt; margin-top: 1em; }
mark {
    background-color: #FFFF00 !important;
    padding: 0 2px;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
    font-size: 10pt;
}
th, td {
    border: 1px solid #333;
    padding: 4px 8px;
    text-align: left;
}
th { background-color: #f0f0f0; }
blockquote {
    border-left: 3px solid #ccc;
    padding-left: 1em;
    margin-left: 0;
    color: #555;
}
code { font-size: 10pt; }
""")


def main():
    print("Reading source .md...")
    md_text = SRC.read_text()

    print("Applying highlights...")
    highlighted = highlight_text(md_text)

    header = (
        "---\n"
        "title: 'REVIEW COPY — Changed Portions Highlighted in Yellow'\n"
        "---\n\n"
        "> **This is a review copy.** All text highlighted in yellow is new or changed "
        "relative to the previous version. Changes: (1) definition framing — "
        "front-loading subjective experience, locating FMT in the self-modeling tradition; "
        "(2) prediction restructuring — empirical convergence section for confirmed claims, "
        "four novel predictions with clear falsification criteria.\n\n---\n\n"
    )
    highlighted = header + highlighted

    print(f"Writing highlighted .md to {OUT_MD}...")
    OUT_MD.write_text(highlighted)

    print("Writing CSS...")
    write_css()

    print("Building PDF with pandoc + weasyprint...")
    cmd = [
        "pandoc",
        str(OUT_MD),
        "-o", str(OUT_PDF),
        "--pdf-engine=weasyprint",
        f"--css={CSS}",
        "--from=markdown+raw_html",
        "--metadata", "title=FMT Review Copy — Changes Highlighted",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: pandoc failed:\n{result.stderr}")
        sys.exit(1)

    print(f"Done! PDF at: {OUT_PDF}")


if __name__ == "__main__":
    main()
