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

# Simple diagram Mermaid code — redesigned for clarity (AIW-15)
# All use TD (top-down) flow with subgraph grouping for implicit/explicit layers,
# matching the mirror-box README ASCII diagram clarity level.
SIMPLE_DIAGRAMS = {
    1: """graph TD
    SENS[Sensory Input] --> IWM
    SELF[Self-state] --> ISM
    subgraph IMPL["Implicit: LLM #1"]
        IWM["IWM<br/>World Knowledge"]
        ISM["ISM<br/>Self Knowledge"]
    end
    IWM --> GATE["Permeability Gate<br/>(attention + temperature)"]
    ISM --> GATE
    GATE --> EWM
    GATE --> ESM
    subgraph EXPL["Explicit: LLM #2"]
        EWM["EWM<br/>World Simulation"]
        ESM["ESM<br/>Self Simulation"]
    end
    ESM -->|self-ref loop| ESM
    EWM --> COMM[Communication LLM]
    ESM --> COMM""",
    2: """graph TD
    SENS[Sensory Input] --> CA
    subgraph IMPL["Implicit: CA Rules"]
        IWM["IWM Region<br/>World rules"]
        ISM["ISM Region<br/>Self rules"]
    end
    IWM --> CA["3D Cellular Automaton<br/>Class 4 Criticality"]
    ISM --> CA
    CA --> PERM["Permeability Barrier"]
    PERM --> EWM
    PERM --> ESM
    subgraph EXPL["Explicit: Decoders"]
        EWM["EWM<br/>World decoder"]
        ESM["ESM<br/>Self decoder"]
    end
    ESM -->|self-ref| CA
    EWM --> COMM[Communication LLM]
    ESM --> COMM""",
    3: """graph TD
    SENS[Sensory Input] --> RNN
    subgraph IMPL["Implicit: RNN"]
        RNN["Recurrent Network<br/>spectral radius = 1.0"]
        IWM["IWM — in weights"]
        ISM["ISM — in weights"]
    end
    IWM -.-> RNN
    ISM -.-> RNN
    RNN --> GATE["Gating Network"]
    GATE --> EWM
    GATE --> ESM
    subgraph EXPL["Explicit Simulation"]
        EWM["EWM Decoder"]
        ESM["ESM Decoder"]
    end
    ESM -->|self-ref feedback| RNN
    EWM --> COMM[Communication LLM]
    ESM --> COMM""",
    4: """graph TD
    SENS[Sensory Input] --> IWM
    subgraph IMPL["Implicit: KG"]
        IWM["IWM<br/>World subgraph"]
        ISM["ISM<br/>Self subgraph"]
    end
    IWM --> CTX["Context Assembly"]
    ISM --> CTX
    CTX --> PERM["Permeability Gate"]
    PERM --> EWM
    PERM --> ESM
    subgraph EXPL["Explicit: 3B LLM"]
        EWM["EWM Simulator"]
        ESM["ESM Simulator"]
    end
    ESM -->|self-ref| ESM
    EWM --> COMM[Communication LLM]
    ESM --> COMM""",
    5: """graph TD
    SENS[Sensory Input] --> IWMP
    subgraph IMPL["Implicit: Agents"]
        IWMP["IWM Pool<br/>2-4 LLMs"]
        ISMP["ISM Pool<br/>2-4 LLMs"]
    end
    IWMP --> SS["Shared State Space"]
    ISMP --> SS
    SS --> SCHED["Scheduling +<br/>Permeability"]
    SCHED --> EWMP
    SCHED --> ESMP
    subgraph EXPL["Explicit: Agents"]
        EWMP["EWM Pool<br/>2-4 LLMs"]
        ESMP["ESM Pool<br/>2-4 LLMs"]
    end
    ESMP -->|self-ref| ESMP
    EWMP --> SPOKE[Spokesperson LLM]
    ESMP --> SPOKE""",
    6: """graph TD
    SENS[Sensory Input] --> IWM
    subgraph IMPL["Implicit: KG Stores"]
        IWM["IWM Store<br/>Knowledge Graph"]
        ISM["ISM Store<br/>Self Entity"]
    end
    IWM --> CTX["Context Assembly"]
    ISM --> CTX
    CTX --> PERM["Permeability Gate"]
    PERM --> EWM
    PERM --> ESM
    subgraph EXPL["Explicit: 7B LLM"]
        EWM["EWM Generator"]
        ESM["ESM Generator"]
    end
    ESM -->|self-ref closure| ESM
    EWM --> COMM[Communication LLM]
    ESM --> COMM""",
    7: """graph TD
    S1["Stage 1: LLM Pipeline<br/>No criticality, 6-10 weeks"]
    S2["Stage 2: + Reservoir<br/>Near-critical, 3-4 months"]
    S3["Stage 3: Critical Substrate<br/>Full CA / neural net"]
    S1 --> S2 --> S3
    S1 -.-> ARCH
    S2 -.-> ARCH
    S3 -.-> ARCH
    ARCH["Same 4-Model Architecture<br/>IWM + ISM --> Gate --> EWM + ESM"]
    ARCH --> TEST["Compare Criticality Metrics<br/>across stages"]""",
    8: """graph TD
    SENS[Sensory Input] --> R["Implicit Field R<br/>Persistent knowledge<br/>(IWM + ISM encoded)"]
    R --> BOUND["Ontological Boundary<br/>Variable Permeability"]
    BOUND --> V
    subgraph EXPL["Explicit: Field V"]
        V["V Field"]
        EWM["EWM peaks<br/>sigma near 0"]
        ESM["ESM peaks<br/>sigma near 1"]
    end
    V --> EWM
    V --> ESM
    V --> BOUND
    ESM -->|self-ref| ESM
    EWM --> COMM[Communication LLM]
    ESM --> COMM""",
    9: """graph TD
    SENS[Sensory Input] --> PDE["Fokker-Planck PDE<br/>on Riemannian Manifold"]
    subgraph NV["Non-Virtual Density"]
        IWM["IWM Peak"]
        ISM["ISM Peak"]
    end
    subgraph VR["Virtual Density"]
        EWM["EWM Peak"]
        ESM["ESM Peak"]
    end
    PDE --> IWM
    PDE --> ISM
    PDE --> EWM
    PDE --> ESM
    ESM -->|self-ref closure| PDE
    EWM --> COMM[Communication LLM]
    ESM --> COMM""",
    10: """graph TD
    IO[Input / Output] --> TOP["Top Layer: Pre-trained LLM<br/>(IWM + ESM + Communication)"]
    TOP -->|predictions: VIRTUAL| MID["Middle Layers<br/>Recurrent modules<br/>branching ratio = 1.0"]
    MID -->|errors: NON-VIRTUAL| TOP
    MID --> L0["Sensory Layer"]
    L0 --> MID
    TOP -->|self-ref: predict own errors| TOP""",
    11: """graph TD
    SENS[Sensory Input] --> SUB
    subgraph IMPL["Implicit: Weights W"]
        SUB["Recurrent Network"]
        IWM["IWM + ISM<br/>encoded in W"]
    end
    IWM -.-> SUB
    SUB --> DECOMP["Eigenmode<br/>Decomposition"]
    subgraph EXPL["Explicit: Eigenmodes"]
        EWM["phi_1: EWM-like<br/>World mode"]
        ESM["phi_2: ESM-like<br/>Self mode"]
        HIGHER["Higher modes<br/>Continuous spectrum"]
    end
    DECOMP --> EWM
    DECOMP --> ESM
    DECOMP --> HIGHER
    ESM -->|self-ref feedback| SUB
    EWM --> COMM[Communication LLM]
    ESM --> COMM""",
    12: """graph TD
    INPUT[Sensory Input] --> FIELD["Neural Field<br/>Langevin Dynamics<br/>Temperature T"]
    FIELD --> TC["Phase Transition at T_c<br/>(divergent xi, chi)"]
    TC --> PHI0["Order Parameter Phi_0<br/>NON-VIRTUAL: IWM / ISM"]
    TC --> GOLD["Goldstone Fluctuations<br/>VIRTUAL: EWM / ESM"]
    GOLD -->|self-ref coupling| FIELD
    GOLD --> COMM[Communication LLM]""",
    13: """graph TD
    SENS[Sensory Input] --> RES
    subgraph IMPL["Implicit Substrate"]
        RES["Critical Reservoir<br/>50K units, SR = 1.0"]
        IWM["IWM: LLM weights"]
        ISM["ISM: LoRA adapters"]
    end
    RES --> GATE["Gate Signal g"]
    IWM -.-> LLM
    ISM -.-> LLM
    GATE --> LLM["Recurrent LLM<br/>Mamba-2, 40 Hz"]
    LLM -->|self-ref readout| RES
    LLM --> MAPPER["Model Space Mapper<br/>scope x mode manifold"]
    MAPPER --> DENSITY["Density Peaks:<br/>EWM + ESM + IWM + ISM"]""",
    14: """graph TD
    INIT["LLM Init (one-time)"] -->|set kernels| FIELD
    SENS[Sensory Input] --> FIELD
    subgraph SUBSTRATE["Neural Field Lattice"]
        FIELD["Field Dynamics"]
        IWM["IWM kernels<br/>world-scope"]
        ISM["ISM kernels<br/>self-scope"]
        EWM["EWM activations<br/>world, explicit"]
        ESM["ESM activations<br/>self, explicit"]
    end
    FIELD --> IWM
    FIELD --> ISM
    FIELD --> EWM
    FIELD --> ESM
    ESM -->|self-ref feedback| FIELD
    FIELD --> COMM[Communication LLM]""",
    15: """graph TD
    SENS[Sensory Input] --> SNN["SNN Reservoir<br/>100K LIF, 40 Hz"]
    IWM["IWM<br/>(in synaptic weights)"] -.-> SNN
    ISM["ISM<br/>(in synaptic weights)"] -.-> SNN
    SNN --> INTF["Spike-Rate Interface<br/>(permeability)"]
    INTF --> LLM["LLM Canopy<br/>Mamba-2 2.8B, 20 Hz"]
    LLM --> EWM["EWM<br/>World predictions"]
    LLM --> ESM["ESM<br/>Self predictions"]
    ESM -->|self-ref| LLM
    LLM -->|feedback| SNN
    LLM --> IO[Language I/O]""",
    16: """graph TD
    SENS[Sensory Input] --> IWM
    TEL[Telemetry] --> ISM
    subgraph IMPL["Implicit Substrate"]
        IWM["IWM<br/>Frozen LLM encoder"]
        ISM["ISM<br/>LoRA encoder"]
    end
    IWM --> DYN["Substrate Dynamics<br/>approx. criticality"]
    ISM --> DYN
    DYN --> PERM["Permeability Gate<br/>Wake / Sleep / Dream / Altered"]
    PERM --> EWM
    PERM --> ESM
    subgraph EXPL["Explicit Simulation"]
        EWM["EWM<br/>World hidden state"]
        ESM["ESM<br/>Self hidden state"]
    end
    ESM -->|self-ref loop| ESM
    EWM --> LLM["LLM: narratives +<br/>self-reports + Q&A"]
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
    15: {"IWM": ["IWM"], "ISM": ["ISM"], "EWM": ["EWM"], "ESM": ["ESM"]},
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
img.overview { max-height: 150mm; width: auto; }
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
    if not render_mmd(simple_mmd, simple_png, 1400, 900):
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

    simple_img = f'<img class="overview" src="{simple_uri}" />' if simple_uri else "<p>[Simple diagram unavailable]</p>"
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
<h2 style="page-break-after:auto">Overview</h2>
{simple_img}
<p>{intro}</p>
<h2 style="page-break-after:auto">Detailed Architecture</h2>
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
