#!/usr/bin/env python3
"""Build individual design PDFs (1-4) with embedded diagrams and full documentation."""

import base64
import subprocess
import tempfile
from pathlib import Path

BASE = Path(__file__).parent
PNG_DIR = BASE / "png"
README_DIR = BASE.parent

DESIGNS = [
    {
        "num": "01",
        "slug": "01-dual-stream-llm",
        "title": "Design 1: Dual-Stream LLM",
        "readme_dir": "01-dual-stream-llm",
        "intro": (
            "The Dual-Stream LLM design uses two continuously-running LLM inference "
            "streams to implement the four-model architecture. LLM #1 handles implicit "
            "processing (IWM/ISM), encoding world and self knowledge in its weights and "
            "maintaining state through its KV-cache. LLM #2 runs the explicit simulation "
            "(EWM/ESM), generating the virtual world and self models as continuous token "
            "streams. A permeability gate based on attention masking and temperature "
            "modulation controls information flow between the implicit and explicit sides. "
            "A third LLM handles external communication, and a SQLite knowledge graph "
            "provides persistent memory. This is the most immediately buildable design "
            "(implementation difficulty 2/5, 4-8 weeks to prototype), but its critical "
            "weakness is the absence of genuine Class 4 dynamics -- LLM autoregressive "
            "generation is fundamentally feedforward, not the parallel edge-of-chaos "
            "computation the theory requires."
        ),
    },
    {
        "num": "02",
        "slug": "02-cellular-automaton",
        "title": "Design 2: Cellular Automaton Substrate",
        "readme_dir": "02-cellular-automaton",
        "intro": (
            "The Cellular Automaton design places a genuine cellular automaton at the "
            "core of the architecture -- a 3D grid of approximately 1 million cells "
            "running at Class 4 criticality. The CA transition rules, which are "
            "parameterized and learnable, encode the implicit models (IWM/ISM). Neural "
            "readout networks sample the CA state at ~20 Hz to decode explicit world "
            "and self simulations (EWM/ESM). A criticality controller actively maintains "
            "edge-of-chaos dynamics by monitoring branching ratio, avalanche statistics, "
            "and correlation length. The ESM readout output is fed back into the CA, "
            "creating genuine self-referential closure through the substrate dynamics. "
            "This is the only design that directly and genuinely addresses the criticality "
            "requirement (implementation difficulty 4/5, 3-5 months to prototype), but "
            "it starts with zero pre-trained world knowledge and faces open research "
            "questions around training CA transition rules."
        ),
    },
    {
        "num": "03",
        "slug": "03-recurrent-substrate",
        "title": "Design 3: Recurrent Neural Substrate",
        "readme_dir": "03-recurrent-substrate",
        "intro": (
            "The Recurrent Neural Substrate design uses recurrent neural networks or "
            "state-space models (e.g., Mamba) whose continuous dynamics naturally "
            "exhibit edge-of-chaos behavior. The RNN's weight matrices encode implicit "
            "knowledge (IWM/ISM), while decoder heads project the hidden state into "
            "world and self simulations (EWM/ESM). Criticality is controlled through "
            "the spectral radius of the recurrent weight matrix -- at spectral radius "
            "= 1.0, the network operates at the edge of chaos with maximal information "
            "retention and sensitivity. The self-referential closure loop feeds ESM "
            "decoder output back as RNN input, and a gating network controls "
            "permeability. This design combines well-understood criticality mathematics "
            "(spectral radius) with end-to-end differentiable training "
            "(implementation difficulty 3.5/5, ~3 months to prototype), though it "
            "faces questions about whether spectral radius = 1 truly produces Class 4 "
            "dynamics equivalent to the theory's requirements."
        ),
    },
    {
        "num": "04",
        "slug": "04-hybrid-knowledge-graph",
        "title": "Design 4: Hybrid Knowledge-Graph + Simulation",
        "readme_dir": "04-hybrid-knowledge-graph",
        "intro": (
            "The Hybrid Knowledge-Graph design uses a structured knowledge graph "
            "(implementing proven design patterns) as the implicit models (IWM/ISM), "
            "with small LLMs or learned simulators running the explicit models "
            "(EWM/ESM). The knowledge graph stores world and self knowledge as entities "
            "with multi-dimensional weighted relations, vector embeddings for semantic "
            "retrieval, and a SELF entity rooted subgraph for the self-model. A context "
            "assembly pipeline (vector retrieval, graph expansion, self-model merge, "
            "budget allocation) feeds assembled context to the simulators at ~20 Hz. "
            "Variable permeability maps to retrieval depth in the graph. A criticality "
            "controller attempts to push the coupled graph-simulation system toward "
            "edge-of-chaos behavior through stochastic activation spreading and "
            "temperature modulation. This is the fastest path to a running system "
            "(implementation difficulty 2/5, 6-10 weeks) with the richest memory "
            "architecture, but its criticality is bolted on rather than intrinsic."
        ),
    },
]

CSS = """
@page {
    size: A4;
    margin: 2cm 2cm 2.5cm 2cm;
}
body {
    font-family: "Liberation Sans", "Helvetica Neue", Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #1a1a1a;
    max-width: 100%;
}
h1 {
    font-size: 22pt;
    color: #1A5276;
    border-bottom: 3px solid #1A5276;
    padding-bottom: 8px;
    margin-top: 0;
}
h2 {
    font-size: 16pt;
    color: #2C3E50;
    border-bottom: 1px solid #BDC3C7;
    padding-bottom: 4px;
    margin-top: 1.5em;
    page-break-after: avoid;
}
h3 {
    font-size: 13pt;
    color: #34495E;
    margin-top: 1.2em;
    page-break-after: avoid;
}
h4 {
    font-size: 11pt;
    color: #34495E;
    margin-top: 1em;
    page-break-after: avoid;
}
.legend {
    font-size: 10pt;
    color: #666;
    margin-bottom: 1em;
    padding: 6px 12px;
    background: #f8f9fa;
    border-radius: 4px;
    border: 1px solid #dee2e6;
}
.legend .iwm { color: #1A5276; font-weight: bold; }
.legend .ism { color: #1E8449; font-weight: bold; }
.legend .ewm { color: #B7950B; font-weight: bold; }
.legend .esm { color: #C0392B; font-weight: bold; }
img {
    max-width: 100%;
    display: block;
    margin: 1em auto;
}
.diagram-container {
    text-align: center;
    margin: 1em 0;
    page-break-inside: avoid;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
    font-size: 10pt;
    page-break-inside: auto;
}
th, td {
    border: 1px solid #BDC3C7;
    padding: 6px 10px;
    text-align: left;
    vertical-align: top;
}
th {
    background: #2C3E50;
    color: white;
    font-weight: bold;
}
tr:nth-child(even) {
    background: #F8F9FA;
}
code {
    font-family: "Liberation Mono", "Courier New", monospace;
    font-size: 9.5pt;
    background: #F4F6F7;
    padding: 1px 4px;
    border-radius: 3px;
}
pre {
    background: #F4F6F7;
    padding: 10px 14px;
    border-radius: 4px;
    border: 1px solid #D5D8DC;
    font-size: 9pt;
    line-height: 1.4;
    overflow-wrap: break-word;
    white-space: pre-wrap;
    page-break-inside: auto;
}
pre code {
    background: none;
    padding: 0;
}
hr {
    border: none;
    border-top: 1px solid #BDC3C7;
    margin: 1.5em 0;
}
blockquote {
    border-left: 3px solid #1A5276;
    margin-left: 0;
    padding-left: 1em;
    color: #555;
}
p {
    margin: 0.6em 0;
}
ul, ol {
    margin: 0.5em 0;
    padding-left: 1.5em;
}
li {
    margin: 0.2em 0;
}
strong {
    color: #1a1a1a;
}
"""


def png_to_uri(path):
    data = Path(path).read_bytes()
    return f"data:image/png;base64,{base64.b64encode(data).decode()}"


def readme_to_html(readme_path):
    """Convert README.md to HTML body snippet via pandoc."""
    result = subprocess.run(
        ["pandoc", str(readme_path), "--to", "html5", "--no-highlight"],
        capture_output=True, text=True, check=True
    )
    return result.stdout


def build_html(design):
    num = design["num"]
    simple_png = PNG_DIR / f"design-{num}-simple.png"
    detail_png = PNG_DIR / f"design-{num}.png"
    readme_path = README_DIR / design["readme_dir"] / "README.md"

    simple_uri = png_to_uri(simple_png)
    detail_uri = png_to_uri(detail_png)

    # Convert README to HTML, skip the first heading (we provide our own)
    body_html = readme_to_html(readme_path)
    # Remove the first <h1> from the body since we already have it
    if "<h1" in body_html:
        # Find end of first h1 block
        h1_start = body_html.index("<h1")
        h1_end = body_html.index("</h1>") + len("</h1>")
        body_html = body_html[:h1_start] + body_html[h1_end:]

    # Remove the one-line summary paragraph (it's in the intro)
    if "<strong>One-line summary:" in body_html:
        p_start = body_html.index("<p><strong>One-line summary:")
        p_end = body_html.index("</p>", p_start) + len("</p>")
        body_html = body_html[:p_start] + body_html[p_end:]

    # Also remove leading <hr> if present
    body_html = body_html.lstrip()
    while body_html.startswith("<hr"):
        hr_end = body_html.index(">") + 1
        if body_html[hr_end:hr_end+1] == "\n":
            hr_end += 1
        body_html = body_html[hr_end:].lstrip()

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{design['title']}</title>
<style>
{CSS}
</style>
</head>
<body>

<h1>{design['title']}</h1>

<div class="legend">
    <span class="iwm">&#9632; IWM (blue)</span> &nbsp;|&nbsp;
    <span class="ism">&#9632; ISM (green)</span> &nbsp;|&nbsp;
    <span class="ewm">&#9632; EWM (grey/yellow)</span> &nbsp;|&nbsp;
    <span class="esm">&#9632; ESM (red)</span>
</div>

<h2>Overview</h2>

<div class="diagram-container">
<img src="{simple_uri}" alt="High-level architecture overview" style="max-height: 400px;" />
</div>

<p>{design['intro']}</p>

<h2>Detailed Architecture</h2>

<div class="diagram-container">
<img src="{detail_uri}" alt="Detailed architecture diagram" />
</div>

<h2>Full Documentation</h2>

{body_html}

</body>
</html>
"""
    return html


def main():
    for design in DESIGNS:
        slug = design["slug"]
        html_path = BASE / f"{slug}.html"
        pdf_path = BASE / f"{slug}.pdf"

        print(f"Building {slug}...")

        # Generate HTML
        html_content = build_html(design)
        html_path.write_text(html_content, encoding="utf-8")

        # Convert to PDF
        subprocess.run(
            ["weasyprint", str(html_path), str(pdf_path)],
            check=True
        )

        # Clean up HTML
        html_path.unlink()

        print(f"  -> {pdf_path.name} done")

    print("\nAll 4 design PDFs built successfully.")


if __name__ == "__main__":
    main()
