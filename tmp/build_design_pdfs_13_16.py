#!/usr/bin/env python3
"""Build individual design PDFs for designs 13-16.

Each PDF contains:
1. Simple Mermaid architecture diagram (high-level overview)
2. Introduction paragraph
3. Detailed Mermaid architecture diagram (from existing .mmd)
4. Full documentation (source content)
"""

import base64
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = Path("/home/jeltz/aIware/docs/engineering/designs")
PDF_DIR = BASE / "pdf"
PNG_DIR = PDF_DIR / "png"
SOURCE_13_15 = BASE / "new-proposals-13-15.md"
SOURCE_16 = BASE / "16-quick-win-pseudo-ac" / "README.md"


def png_to_uri(path: Path) -> str:
    """Convert a PNG file to a data URI for embedding in HTML."""
    data = path.read_bytes()
    b64 = base64.b64encode(data).decode()
    return f"data:image/png;base64,{b64}"


def extract_preamble(source_text: str) -> str:
    """Extract the preamble section (What the Existing Designs Get Wrong)."""
    lines = source_text.split("\n")
    start = None
    end = None
    for i, line in enumerate(lines):
        if "## Preamble:" in line or "What the Existing Designs Get Wrong" in line:
            start = i
        if start is not None and i > start and line.startswith("## Design "):
            end = i
            break
    if start is not None and end is not None:
        return "\n".join(lines[start:end]).strip()
    return ""


def extract_design_section(source_text: str, design_num: int) -> str:
    """Extract a single design section from the combined source."""
    lines = source_text.split("\n")
    start = None
    end = None
    marker = f"## Design {design_num}:"
    next_markers = [f"## Design {design_num + 1}:", "## Comparative Summary", "## Recommendation"]

    for i, line in enumerate(lines):
        if line.startswith(marker):
            start = i
        elif start is not None and any(line.startswith(m) for m in next_markers):
            end = i
            break

    if start is not None:
        if end is None:
            end = len(lines)
        return "\n".join(lines[start:end]).strip()
    return ""


def md_to_html_body(md_text: str) -> str:
    """Convert markdown to HTML body using pandoc."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(md_text)
        f.flush()
        result = subprocess.run(
            ["pandoc", f.name, "--to", "html5", "--no-highlight"],
            capture_output=True, text=True
        )
        Path(f.name).unlink()
    if result.returncode != 0:
        print(f"pandoc error: {result.stderr}", file=sys.stderr)
        return f"<p>Error converting markdown: {result.stderr}</p>"
    return result.stdout


CSS = """
@page {
    size: A4 portrait;
    margin: 2cm 2cm 2.5cm 2cm;
    @bottom-center {
        content: counter(page);
        font-size: 9pt;
        color: #666;
    }
}
body {
    font-family: "Liberation Sans", "DejaVu Sans", Arial, Helvetica, sans-serif;
    font-size: 10pt;
    line-height: 1.5;
    color: #222;
    max-width: 100%;
}
h1 {
    font-size: 20pt;
    color: #1a5276;
    border-bottom: 3px solid #1a5276;
    padding-bottom: 8px;
    margin-top: 0;
    page-break-after: avoid;
}
h2 {
    font-size: 15pt;
    color: #1a5276;
    border-bottom: 1px solid #ccc;
    padding-bottom: 4px;
    margin-top: 1.5em;
    page-break-after: avoid;
}
h3 {
    font-size: 12pt;
    color: #2c3e50;
    margin-top: 1.2em;
    page-break-after: avoid;
}
h4 {
    font-size: 10.5pt;
    color: #34495e;
    margin-top: 1em;
    page-break-after: avoid;
}
.diagram-container {
    text-align: center;
    margin: 1.5em 0;
    page-break-inside: avoid;
}
.diagram-container img {
    max-width: 100%;
    height: auto;
}
.diagram-caption {
    font-size: 9pt;
    color: #666;
    font-style: italic;
    margin-top: 0.5em;
}
.intro-box {
    background: #eaf2f8;
    border-left: 4px solid #1a5276;
    padding: 12px 16px;
    margin: 1em 0;
    font-size: 10.5pt;
    line-height: 1.6;
    page-break-inside: avoid;
}
.preamble-box {
    background: #fdf2e9;
    border-left: 4px solid #e67e22;
    padding: 10px 14px;
    margin: 1em 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}
.preamble-box h2 {
    font-size: 11pt;
    color: #e67e22;
    border-bottom: none;
    margin-top: 0;
    padding-bottom: 0;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 0.8em 0;
    font-size: 9pt;
    page-break-inside: avoid;
}
th, td {
    border: 1px solid #bdc3c7;
    padding: 5px 8px;
    text-align: left;
    vertical-align: top;
}
th {
    background: #2c3e50;
    color: white;
    font-weight: bold;
}
tr:nth-child(even) {
    background: #f8f9fa;
}
code {
    font-family: "Liberation Mono", "DejaVu Sans Mono", monospace;
    font-size: 8.5pt;
    background: #f4f4f4;
    padding: 1px 4px;
    border-radius: 2px;
}
pre {
    background: #f4f4f4;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 10px;
    font-size: 8pt;
    line-height: 1.4;
    overflow-wrap: break-word;
    white-space: pre-wrap;
    page-break-inside: avoid;
}
pre code {
    background: none;
    padding: 0;
}
strong {
    color: #1a5276;
}
ul, ol {
    padding-left: 1.5em;
}
li {
    margin-bottom: 0.3em;
}
.color-legend {
    display: table;
    margin: 0.5em auto;
    font-size: 9pt;
}
.color-legend span {
    display: inline-block;
    width: 14px;
    height: 14px;
    vertical-align: middle;
    margin-right: 4px;
    border-radius: 2px;
}
.legend-item {
    display: inline-block;
    margin-right: 16px;
}
"""

DESIGNS = {
    13: {
        "title": "Design 13: Reservoir-Gated Recurrent LLM with Emergent Model Topology",
        "slug": "13-reservoir-gated-recurrent",
        "intro": (
            "Design 13 couples a recurrent LLM (Mamba-2) with a sparse, criticality-tuned reservoir network. "
            "Unlike conventional approaches where a reservoir sits alongside the LLM, here the reservoir directly "
            "<strong>gates</strong> the LLM's state transitions, injecting critical dynamics into the language model's "
            "recurrent computation. The continuous model space emerges from the joint dynamics of the LLM hidden state "
            "and the reservoir, measured via a learned topological map. The key innovation is that the reservoir's "
            "edge-of-chaos behavior -- power-law avalanches, 1/f noise, scale-free gate fluctuations -- propagates "
            "into the LLM's state space through the gating mechanism, potentially producing genuine Class 4 dynamics "
            "in the combined system."
        ),
        "source": "combined",
    },
    14: {
        "title": "Design 14: Neural Field Automaton with LLM-Initialized Implicit Manifold",
        "slug": "14-neural-field-automaton",
        "intro": (
            "Design 14 implements the FMT specification most directly: a continuous neural field on a 2D toroidal "
            "lattice where each point carries a 64-dimensional activation vector. The field's two spatial dimensions "
            "map directly to scope (world/self) and mode (implicit/explicit), making the model density "
            "rho(s, nu, t) <strong>directly observable</strong> as the activation norm at each lattice point -- "
            "no learned projection needed. Criticality emerges from tuning the interaction kernel to a Turing-Hopf "
            "bifurcation, producing spatiotemporal complexity (traveling waves, spirals, labyrinthine patterns). "
            "LLM knowledge is distilled into the kernel structure during a one-time initialization, after which "
            "the field runs independently. This is the most mathematically faithful implementation: the field equation "
            "<em>is</em> a discretized Fokker-Planck equation."
        ),
        "source": "combined",
    },
    15: {
        "title": "Design 15: Dual-Timescale Spiking Reservoir with Predictive LLM Canopy",
        "slug": "15-dual-timescale-spiking",
        "intro": (
            "Design 15 is the primary implementation candidate. A spiking neural network (100K LIF neurons, "
            "80/20 E/I balance) provides the most biologically validated criticality mechanism -- balanced "
            "excitation-inhibition producing power-law avalanches, as demonstrated by Beggs and Plenz (2003). "
            "Above the SNN sits a predictive LLM canopy (Mamba-2 2.8B) running at 20 Hz, receiving spike-rate "
            "coded summaries and generating top-down predictions. The two are coupled bidirectionally: LLM "
            "predictions modulate SNN dynamics (top-down attention), SNN error signals update LLM beliefs "
            "(bottom-up surprise). This combines Design 10's predictive coding with Design 2's genuine substrate "
            "criticality, while the LLM canopy provides world knowledge and language from day one. Self-referential "
            "closure operates at <strong>two levels</strong>: within the SNN (self-scope populations model "
            "network activity) and within the LLM canopy (meta-prediction of own errors)."
        ),
        "source": "combined",
    },
    16: {
        "title": "Design 16: The Mirror Box -- Quick-Win Pseudo-AC Prototype",
        "slug": "16-quick-win-mirror-box",
        "intro": (
            "Design 16 is Design 15's sparring partner -- a system that deliberately takes shortcuts on the hardest "
            "requirements (continuous model density, genuine Class 4 criticality, emergent virtual/non-virtual "
            "boundary) to get something running in 2-4 weeks. It implements all four models (IWM, ISM, EWM, ESM) "
            "as discrete components using a single LLM (Mistral-7B INT4) serving triple duty: generating EWM "
            "narratives, ESM self-reports, and introspection Q&A. A permeability gate controls information flow "
            "between substrate (frozen/LoRA-adapted encoder layers) and simulation (LLM generation), with "
            "configurable state profiles for wake, sleep, dream, and altered states. The self-referential loop "
            "feeds ESM output back as input with a self-predictor MLP measuring self-knowledge R. "
            "<strong>By design, this system should NOT be conscious</strong> according to FMT -- it approximates "
            "criticality through noise injection rather than achieving it. If it passes behavioral tests but fails "
            "criticality tests, that empirically validates FMT's claim that criticality is what separates "
            "'acts conscious' from 'is conscious.'"
        ),
        "source": "readme",
    },
}


def build_html(design_num: int, info: dict, preamble_html: str) -> str:
    """Build the full HTML document for a design."""
    simple_png = PNG_DIR / f"design-{design_num}-simple.png"
    detail_png = PNG_DIR / f"design-{design_num}.png"

    simple_uri = png_to_uri(simple_png)
    detail_uri = png_to_uri(detail_png)

    # Get source content
    if info["source"] == "combined":
        source_text = SOURCE_13_15.read_text()
        design_md = extract_design_section(source_text, design_num)
    else:
        design_md = SOURCE_16.read_text()

    # Convert design content to HTML
    content_html = md_to_html_body(design_md)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{info['title']}</title>
<style>{CSS}</style>
</head>
<body>

<h1>{info['title']}</h1>

<!-- Color Legend -->
<div class="color-legend">
    <span class="legend-item"><span style="background:#D6EAF8;border:2px solid #1A5276;"></span> IWM (Implicit World)</span>
    <span class="legend-item"><span style="background:#D5F5E3;border:2px solid #1E8449;"></span> ISM (Implicit Self)</span>
    <span class="legend-item"><span style="background:#EAECEE;border:2px solid #B7950B;"></span> EWM (Explicit World)</span>
    <span class="legend-item"><span style="background:#FADBD8;border:2px solid #C0392B;"></span> ESM (Explicit Self)</span>
</div>

<!-- Simple Architecture Diagram -->
<div class="diagram-container">
    <img src="{simple_uri}" alt="High-level architecture diagram">
    <div class="diagram-caption">Figure 1: High-level architecture overview</div>
</div>

<!-- Introduction -->
<div class="intro-box">
{info['intro']}
</div>

<!-- Detailed Architecture Diagram -->
<div class="diagram-container">
    <img src="{detail_uri}" alt="Detailed architecture diagram">
    <div class="diagram-caption">Figure 2: Detailed architecture with data flow</div>
</div>

<!-- Preamble Context -->
<div class="preamble-box">
{preamble_html}
</div>

<!-- Full Documentation -->
<h2>Full Design Documentation</h2>
{content_html}

</body>
</html>"""
    return html


def main():
    # Extract and convert preamble
    source_text = SOURCE_13_15.read_text()
    preamble_md = extract_preamble(source_text)
    preamble_html = md_to_html_body(preamble_md)

    for design_num, info in DESIGNS.items():
        print(f"Building Design {design_num}: {info['slug']}...")

        # Build HTML
        html = build_html(design_num, info, preamble_html)

        # Write HTML
        html_path = PDF_DIR / f"{info['slug']}.html"
        html_path.write_text(html)
        print(f"  HTML: {html_path}")

        # Convert to PDF
        pdf_path = PDF_DIR / f"{info['slug']}.pdf"
        result = subprocess.run(
            ["weasyprint", str(html_path), str(pdf_path)],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"  ERROR: {result.stderr}", file=sys.stderr)
        else:
            print(f"  PDF:  {pdf_path}")

        # Clean up HTML
        html_path.unlink()
        print(f"  Cleaned up HTML")

    print("\nDone! All 4 PDFs generated.")


if __name__ == "__main__":
    main()
