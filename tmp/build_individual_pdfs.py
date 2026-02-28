#!/usr/bin/env python3
"""Build individual design PDFs for all 16 AC architecture designs.

For each design: simple diagram + intro + detailed diagram + full docs (sans ASCII art).
Uses neutral Mermaid theme and base64-embedded images for weasyprint.

Usage: python3 tmp/build_individual_pdfs.py
"""

import base64
import re
import subprocess
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
DESIGNS_DIR = PROJECT / "docs" / "engineering" / "designs"
PDF_DIR = DESIGNS_DIR / "pdf"
MMD_DIR = PDF_DIR / "mmd"
PNG_DIR = PDF_DIR / "png"

# Model colors (same as overview)
MODEL_COLORS = {
    "IWM": {"fill": "#D6EAF8", "stroke": "#1A5276"},
    "ISM": {"fill": "#D5F5E3", "stroke": "#1E8449"},
    "EWM": {"fill": "#EAECEE", "stroke": "#B7950B"},
    "ESM": {"fill": "#FADBD8", "stroke": "#C0392B"},
}

# Design metadata
DESIGNS = [
    {"num": 1, "slug": "01-dual-stream-llm", "title": "Dual-Stream LLM",
     "readme": "01-dual-stream-llm/README.md"},
    {"num": 2, "slug": "02-cellular-automaton", "title": "Cellular Automaton Substrate",
     "readme": "02-cellular-automaton/README.md"},
    {"num": 3, "slug": "03-recurrent-substrate", "title": "Recurrent Neural Substrate",
     "readme": "03-recurrent-substrate/README.md"},
    {"num": 4, "slug": "04-hybrid-knowledge-graph", "title": "Hybrid Knowledge-Graph + Simulation",
     "readme": "04-hybrid-knowledge-graph/README.md"},
    {"num": 5, "slug": "05-multi-agent", "title": "Multi-Agent Consciousness",
     "readme": "05-multi-agent/README.md"},
    {"num": 6, "slug": "06-four-model-llm-pipeline", "title": "Four-Model LLM Pipeline",
     "readme": "06-four-model-llm-pipeline/README.md"},
    {"num": 7, "slug": "07-staged-architecture", "title": "Staged Architecture",
     "readme": "07-staged-architecture/README.md"},
    {"num": 8, "slug": "08-coupled-dual-field", "title": "Coupled Dual-Field Dynamics",
     "readme": "08-coupled-dual-field/README.md"},
    {"num": 9, "slug": "09-stochastic-manifold", "title": "Stochastic Model Density on Riemannian Manifold",
     "readme": "09-stochastic-manifold/README.md"},
    {"num": 10, "slug": "10-predictive-coding-hierarchy", "title": "Predictive Coding Hierarchy",
     "readme": "10-predictive-coding-hierarchy/README.md"},
    {"num": 11, "slug": "11-spectral-decomposition", "title": "Spectral Decomposition",
     "readme": "11-spectral-decomposition/README.md"},
    {"num": 12, "slug": "12-gauge-field", "title": "Neural Gauge Field with Symmetry Breaking",
     "readme": "12-gauge-field/README.md"},
    {"num": 13, "slug": "13-reservoir-gated-recurrent", "title": "Reservoir-Gated Recurrent LLM",
     "readme": None, "source": "new-proposals-13-15.md", "start": 36, "end": 326},
    {"num": 14, "slug": "14-neural-field-automaton", "title": "Neural Field Automaton",
     "readme": None, "source": "new-proposals-13-15.md", "start": 327, "end": 633},
    {"num": 15, "slug": "15-dual-timescale-spiking", "title": "Dual-Timescale Spiking Reservoir + LLM Canopy",
     "readme": None, "source": "new-proposals-13-15.md", "start": 634, "end": 9999},
    {"num": 16, "slug": "16-quick-win-mirror-box", "title": "The Mirror Box (Quick-Win Pseudo-AC)",
     "readme": "16-quick-win-pseudo-ac/README.md"},
]

# Simple diagram Mermaid code (5-8 nodes each)
SIMPLE_DIAGRAMS = {
    1: """graph LR
    SENS[Sensory Input] --> IWM[IWM<br/>LLM #1 weights]
    SELF[Self-state] --> ISM[ISM<br/>LLM #1 weights]
    IWM --> GATE[Permeability<br/>Gate]
    ISM --> GATE
    GATE --> EWM[EWM<br/>LLM #2 generation]
    GATE --> ESM[ESM<br/>LLM #2 generation]
    ESM -->|self-ref loop| ESM
    EWM --> COMM[Communication LLM]
    ESM --> COMM""",
    2: """graph LR
    SENS[Sensory Input] --> IWM[IWM Region<br/>CA transition rules]
    IWM --> CA[3D Cellular Automaton<br/>Class 4 criticality]
    ISM[ISM Region<br/>CA transition rules] --> CA
    CA --> PERM[Permeability]
    PERM --> EWM[EWM Readout<br/>World decoder]
    PERM --> ESM[ESM Readout<br/>Self decoder]
    ESM -->|self-ref| CA
    ESM --> COMM[Communication LLM]""",
    3: """graph LR
    SENS[Sensory Input] --> RNN[Recurrent Substrate<br/>spectral radius = 1.0]
    RNN --> GATE[Gating Network]
    GATE --> EWM[EWM Decoder]
    GATE --> ESM[ESM Decoder]
    ESM -->|self-ref feedback| RNN
    ESM --> COMM[Communication LLM]
    IWM[IWM in weights] -.-> RNN
    ISM[ISM in weights] -.-> RNN""",
    4: """graph LR
    SENS[Sensory Input] --> IWM[IWM<br/>World subgraph]
    IWM --> CTX[Context Assembly]
    ISM[ISM<br/>SELF subgraph] --> CTX
    CTX --> PERM[Permeability Gate]
    PERM --> EWM[EWM Simulator<br/>3B LLM]
    PERM --> ESM[ESM Simulator<br/>3B LLM]
    ESM -->|self-ref| ESM
    ESM --> COMM[Communication LLM]""",
    5: """graph LR
    SENS[Sensory Input] --> IWMP[IWM Pool<br/>2-4 LLMs]
    IWMP --> SS[Shared State Space]
    ISMP[ISM Pool<br/>2-4 LLMs] --> SS
    SS --> SCHED[Scheduling +<br/>Permeability]
    SCHED --> EWMP[EWM Pool<br/>2-4 LLMs]
    SCHED --> ESMP[ESM Pool<br/>2-4 LLMs]
    ESMP -->|self-ref| ESMP
    EWMP --> SPOKE[Spokesperson LLM]
    ESMP --> SPOKE""",
    6: """graph LR
    SENS[Sensory Input] --> IWM[IWM Store<br/>Knowledge Graph]
    ISM[ISM Store<br/>SELF entity] --> CTX[Context Assembly]
    IWM --> CTX
    CTX --> PERM[Permeability Gate]
    PERM --> EWM[EWM Generator<br/>7B LLM]
    PERM --> ESM[ESM Generator<br/>7B LLM]
    ESM -->|self-ref closure| ESM
    EWM --> COMM[Communication LLM]
    ESM --> COMM""",
    7: """graph TD
    S1[Stage 1: LLM Pipeline<br/>No criticality, 6-10 wk] --> S2[Stage 2: + Reservoir<br/>Near-critical, 3-4 mo]
    S2 --> S3[Stage 3: Critical Substrate<br/>Full CA/neural net]
    S1 --> SHARED[Same 4-model architecture<br/>EWM + ESM + IWM + ISM]
    S2 --> SHARED
    S3 --> SHARED
    SHARED --> TEST[Compare criticality<br/>levels across stages]""",
    8: """graph LR
    SENS[Sensory Input] --> R[Implicit Field R<br/>Persistent knowledge]
    R --> BOUND[Ontological Boundary<br/>Variable permeability]
    BOUND --> V[Explicit Field V<br/>Transient simulation]
    V --> BOUND
    V --> EWM[EWM peaks<br/>sigma near 0]
    V --> ESM[ESM peaks<br/>sigma near 1]
    ESM -->|self-ref| ESM
    EWM --> COMM[Communication LLM]
    ESM --> COMM""",
    9: """graph LR
    SENS[Sensory Input] --> PDE[Fokker-Planck PDE<br/>on Riemannian manifold]
    PDE --> MV[M_virtual density]
    PDE --> MNV[M_nonvirtual density]
    MV --> EWM[EWM Peak]
    MV --> ESM[ESM Peak]
    MNV --> IWM[IWM Peak]
    MNV --> ISM[ISM Peak]
    ESM -->|self-ref closure| PDE
    EWM --> COMM[Communication LLM]
    ESM --> COMM""",
    10: """graph TD
    IO[Input/Output] --> TOP[Top Layer: Pre-trained LLM<br/>IWM + ESM + Communication]
    TOP -->|predictions: VIRTUAL| MID[Middle Layers<br/>Recurrent modules]
    MID -->|errors: NON-VIRTUAL| TOP
    MID --> L0[Sensory Layer]
    L0 --> MID
    CRIT[Multi-scale criticality<br/>Branching ratio = 1.0] -.-> MID
    TOP -->|self-ref: predict own errors| TOP""",
    11: """graph LR
    SENS[Sensory Input] --> SUB[Recurrent Substrate<br/>Weight matrix W]
    SUB --> DECOMP[Eigenmode<br/>Decomposition]
    DECOMP --> EWM[phi_1: EWM-like<br/>World mode]
    DECOMP --> ESM[phi_2: ESM-like<br/>Self mode]
    DECOMP --> HIGHER[Higher modes<br/>Continuous spectrum]
    ESM -->|self-ref feedback| SUB
    EWM --> COMM[Communication LLM]
    ESM --> COMM
    IWM[IWM + ISM<br/>in weights W] -.-> SUB""",
    12: """graph TD
    INPUT[Sensory Input] --> FIELD[Computational Field<br/>Langevin dynamics]
    FIELD --> TC[Phase Transition at T_c]
    TC --> PHI0[Order Parameter Phi_0<br/>NON-VIRTUAL: IWM/ISM]
    TC --> GOLD[Goldstone Fluctuations<br/>VIRTUAL: EWM/ESM]
    GOLD -->|self-ref coupling| FIELD
    GOLD --> COMM[Communication LLM]
    CRIT[Criticality IS the design<br/>divergent xi, chi] -.-> TC""",
    13: """graph LR
    SENS[Sensory Input] --> RES[Critical Reservoir<br/>50K units, SR=1.0]
    RES --> GATE[Gate signal g]
    GATE --> LLM[Recurrent LLM<br/>Mamba-2, 40 Hz]
    LLM --> MAPPER[Model Space Mapper<br/>scope, mode manifold]
    LLM -->|self-ref readout| RES
    IWM[IWM: LLM weights] -.-> LLM
    ISM[ISM: LoRA adapters] -.-> LLM
    MAPPER --> DENSITY[Density peaks:<br/>EWM + ESM + IWM + ISM]""",
    14: """graph LR
    INIT[LLM Init<br/>one-time] -->|set kernels| FIELD[Neural Field<br/>256x256 toroidal lattice]
    SENS[Sensory Input] --> FIELD
    FIELD --> IWM[IWM kernels<br/>world-scope]
    FIELD --> ISM[ISM kernels<br/>self-scope]
    FIELD --> EWM[EWM activations<br/>world, explicit]
    FIELD --> ESM[ESM activations<br/>self, explicit]
    ESM -->|self-ref feedback| FIELD
    FIELD --> COMM[Communication LLM]""",
    15: """graph TD
    SENS[Sensory Input] --> SNN[SNN Reservoir<br/>100K LIF neurons, 40 Hz]
    SNN -->|spike rates| INTERFACE[Spike-Rate Interface]
    INTERFACE -->|bottom-up errors| LLM[LLM Canopy<br/>Mamba-2 2.8B, 20 Hz]
    LLM -->|top-down predictions| INTERFACE
    INTERFACE -->|modulatory currents| SNN
    LLM -->|self-ref: predict own errors| LLM
    SNN -->|SNN self-ref: self pops| SNN
    LLM --> IO[Language I/O]""",
    16: """graph TD
    SENS[Sensory Input] --> IWM[IWM: Frozen LLM encoder]
    TEL[Telemetry] --> ISM[ISM: LoRA encoder]
    IWM --> DYN[Substrate Dynamics<br/>approx. criticality]
    ISM --> DYN
    DYN --> PERM[Permeability Gate<br/>Wake/Sleep/Dream/Altered]
    PERM --> EWM[EWM: world hidden state]
    PERM --> ESM[ESM: self hidden state]
    ESM -->|self-ref loop| ESM
    EWM --> LLM[LLM: narratives +<br/>self-reports + Q&A]
    ESM --> LLM""",
}

# Node -> model type mapping for coloring simple diagrams
SIMPLE_NODE_MAP = {
    1:  {"IWM": ["IWM"], "ISM": ["ISM"], "EWM": ["EWM"], "ESM": ["ESM"]},
    2:  {"IWM": ["IWM"], "ISM": ["ISM"], "EWM": ["EWM"], "ESM": ["ESM"]},
    3:  {"IWM": ["IWM"], "ISM": ["ISM"], "EWM": ["EWM"], "ESM": ["ESM"]},
    4:  {"IWM": ["IWM"], "ISM": ["ISM"], "EWM": ["EWM"], "ESM": ["ESM"]},
    5:  {"IWM": ["IWMP"], "ISM": ["ISMP"], "EWM": ["EWMP"], "ESM": ["ESMP"]},
    6:  {"IWM": ["IWM"], "ISM": ["ISM"], "EWM": ["EWM"], "ESM": ["ESM"]},
    7:  {},
    8:  {"EWM": ["EWM"], "ESM": ["ESM"]},
    9:  {"IWM": ["IWM"], "ISM": ["ISM"], "EWM": ["EWM"], "ESM": ["ESM"]},
    10: {},
    11: {"IWM": ["IWM"], "EWM": ["EWM"], "ESM": ["ESM"]},
    12: {},
    13: {"IWM": ["IWM"], "ISM": ["ISM"]},
    14: {"IWM": ["IWM"], "ISM": ["ISM"], "EWM": ["EWM"], "ESM": ["ESM"]},
    15: {},
    16: {"IWM": ["IWM"], "ISM": ["ISM"], "EWM": ["EWM"], "ESM": ["ESM"]},
}

CSS = """
@page { size: A4; margin: 2cm 2cm 2.5cm 2cm; }
body { font-family: "Liberation Sans", "Helvetica Neue", Arial, sans-serif;
       font-size: 11pt; line-height: 1.5; color: #1a1a1a; }
h1 { font-size: 22pt; color: #1A5276; border-bottom: 3px solid #1A5276;
     padding-bottom: 8px; margin-top: 0; }
h2 { font-size: 16pt; color: #2C3E50; border-bottom: 1px solid #BDC3C7;
     padding-bottom: 4px; margin-top: 1.5em; page-break-after: avoid; }
h3 { font-size: 13pt; color: #34495E; margin-top: 1.2em; page-break-after: avoid; }
h4 { font-size: 11pt; color: #34495E; margin-top: 1em; page-break-after: avoid; }
.legend { font-size: 10pt; color: #666; margin-bottom: 1em; padding: 6px 12px;
          background: #f8f9fa; border-radius: 4px; border: 1px solid #dee2e6; }
.legend .iwm { color: #1A5276; font-weight: bold; }
.legend .ism { color: #1E8449; font-weight: bold; }
.legend .ewm { color: #B7950B; font-weight: bold; }
.legend .esm { color: #C0392B; font-weight: bold; }
img { max-width: 100%; height: auto; display: block; margin: 1em auto; }
table { width: 100%; border-collapse: collapse; margin: 1em 0; font-size: 10pt; }
th, td { border: 1px solid #BDC3C7; padding: 6px 10px; text-align: left; vertical-align: top; }
th { background: #2C3E50; color: white; font-weight: bold; }
tr:nth-child(even) { background: #F8F9FA; }
code { font-family: "Liberation Mono", monospace; font-size: 9.5pt;
       background: #F4F6F7; padding: 1px 4px; border-radius: 3px; }
pre { background: #F4F6F7; padding: 10px 14px; border-radius: 4px;
      border: 1px solid #D5D8DC; font-size: 9pt; line-height: 1.4;
      overflow-wrap: break-word; white-space: pre-wrap; }
pre code { background: none; padding: 0; }
hr { border: none; border-top: 1px solid #BDC3C7; margin: 1.5em 0; }
blockquote { border-left: 3px solid #1A5276; margin-left: 0; padding-left: 1em; color: #555; }
p { margin: 0.6em 0; }
ul, ol { margin: 0.5em 0; padding-left: 1.5em; }
li { margin: 0.2em 0; }
"""


def png_to_uri(path):
    return f"data:image/png;base64,{base64.b64encode(Path(path).read_bytes()).decode()}"


def style_lines(node_map):
    lines = []
    for model, nodes in node_map.items():
        c = MODEL_COLORS[model]
        for n in nodes:
            lines.append(f"    style {n} fill:{c['fill']},stroke:{c['stroke']},stroke-width:2px")
    return "\n".join(lines)


def get_readme_content(design):
    """Get markdown content for a design."""
    if design.get("readme"):
        return (DESIGNS_DIR / design["readme"]).read_text()
    else:
        # Extract section from combined file
        source = (DESIGNS_DIR / design["source"]).read_text().splitlines()
        start = design["start"] - 1  # 0-indexed
        end = min(design["end"], len(source))
        return "\n".join(source[start:end])


def strip_ascii_diagrams(html):
    """Remove code blocks that contain ASCII architecture diagrams."""
    # Remove ```mermaid blocks (already have rendered diagrams)
    html = re.sub(r'<pre><code class="language-mermaid">.*?</code></pre>', '', html, flags=re.DOTALL)
    # Remove ``` blocks that look like ASCII diagrams (contain box-drawing chars or arrows)
    def is_ascii_diagram(match):
        content = match.group(0)
        indicators = ['──', '│', '┌', '└', '├', '┤', '┬', '┴', '╔', '║',
                       '-->>', '-->', '===', '---', '|||', '+--', '|  ', '<->']
        count = sum(1 for ind in indicators if ind in content)
        return count >= 3
    # Check pre blocks
    def maybe_strip(match):
        if is_ascii_diagram(match):
            return ''
        return match.group(0)
    html = re.sub(r'<pre><code>.*?</code></pre>', maybe_strip, html, flags=re.DOTALL)
    html = re.sub(r'<pre><code class="">.*?</code></pre>', maybe_strip, html, flags=re.DOTALL)
    return html


def extract_intro(md_content):
    """Extract first paragraph after the title as intro."""
    lines = md_content.strip().splitlines()
    in_intro = False
    intro_lines = []
    for line in lines:
        if line.startswith("**One-line summary"):
            continue
        if line.startswith("#"):
            if in_intro:
                break
            continue
        if line.startswith("---"):
            if in_intro:
                break
            continue
        stripped = line.strip()
        if not stripped:
            if in_intro and intro_lines:
                break
            continue
        in_intro = True
        intro_lines.append(stripped)
    return " ".join(intro_lines) if intro_lines else ""


def md_to_html_body(md_content):
    """Convert markdown to HTML body via pandoc, strip ASCII diagrams."""
    result = subprocess.run(
        ["pandoc", "--from", "markdown", "--to", "html5", "--no-highlight"],
        input=md_content, capture_output=True, text=True, check=True
    )
    html = result.stdout
    # Remove first h1/h2 (we provide our own title)
    for tag in ["h1", "h2"]:
        if f"<{tag}" in html:
            start = html.index(f"<{tag}")
            end = html.index(f"</{tag}>") + len(f"</{tag}>")
            html = html[:start] + html[end:]
            break
    html = strip_ascii_diagrams(html)
    return html


def render_mmd(mmd_path, png_path, width=1600, height=900):
    result = subprocess.run(
        ["mmdc", "-i", str(mmd_path), "-o", str(png_path),
         "-w", str(width), "-H", str(height), "-b", "white", "-t", "neutral"],
        capture_output=True, text=True, timeout=60
    )
    return result.returncode == 0


def build_one(design):
    num = design["num"]
    nn = f"{num:02d}"
    slug = design["slug"]

    print(f"  [{nn}] {design['title']}...")

    # 1. Write simple .mmd with colors
    simple_mmd = MMD_DIR / f"design-{nn}-simple.mmd"
    simple_code = SIMPLE_DIAGRAMS[num].strip()
    smap = SIMPLE_NODE_MAP.get(num, {})
    if smap:
        simple_code += "\n" + style_lines(smap)
    simple_mmd.write_text(simple_code + "\n")

    # 2. Render simple PNG
    simple_png = PNG_DIR / f"design-{nn}-simple.png"
    if not render_mmd(simple_mmd, simple_png, 1400, 600):
        print(f"    WARN: simple diagram render failed for {nn}")

    # 3. Detailed PNG already rendered by overview script
    detail_png = PNG_DIR / f"design-{nn}.png"
    if not detail_png.exists():
        detail_mmd = MMD_DIR / f"design-{nn}.mmd"
        if detail_mmd.exists():
            render_mmd(detail_mmd, detail_png)

    # 4. Get content
    md_content = get_readme_content(design)
    intro = extract_intro(md_content)
    body_html = md_to_html_body(md_content)

    # 5. Build HTML
    simple_uri = png_to_uri(simple_png) if simple_png.exists() else ""
    detail_uri = png_to_uri(detail_png) if detail_png.exists() else ""

    simple_img = f'<img src="{simple_uri}" />' if simple_uri else "<p>[Simple diagram unavailable]</p>"
    detail_img = f'<img src="{detail_uri}" />' if detail_uri else "<p>[Detailed diagram unavailable]</p>"

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<title>Design {num}: {design['title']}</title>
<style>{CSS}</style></head><body>
<h1>Design {num}: {design['title']}</h1>
<div class="legend">
    <span class="esm">&#9632; ESM (red)</span> &nbsp;|&nbsp;
    <span class="ewm">&#9632; EWM (dark yellow)</span> &nbsp;|&nbsp;
    <span class="iwm">&#9632; IWM (blue)</span> &nbsp;|&nbsp;
    <span class="ism">&#9632; ISM (green)</span>
</div>
<h2>Overview</h2>
{simple_img}
<p>{intro}</p>
<h2>Detailed Architecture</h2>
{detail_img}
<h2>Full Documentation</h2>
{body_html}
</body></html>"""

    # 6. Write HTML and convert to PDF
    html_path = PDF_DIR / f"{slug}.html"
    pdf_path = PDF_DIR / f"{slug}.pdf"
    html_path.write_text(html)
    subprocess.run(["weasyprint", str(html_path), str(pdf_path)],
                   capture_output=True, check=True, timeout=120)
    html_path.unlink()
    print(f"    -> {pdf_path.name} ({pdf_path.stat().st_size // 1024} KB)")


def main():
    MMD_DIR.mkdir(parents=True, exist_ok=True)
    PNG_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Building {len(DESIGNS)} individual design PDFs...\n")
    for d in DESIGNS:
        build_one(d)
    print(f"\nDone. PDFs in {PDF_DIR}")


if __name__ == "__main__":
    main()
