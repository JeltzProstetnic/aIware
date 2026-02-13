# Figure 1: The Four-Model Architecture

## Description for Paper

**Figure 1. The Four-Model Architecture.** The four models are arranged along two axes: scope (everything/world vs. self only) and mode (implicit/learned vs. explicit/simulated). The implicit models (IWM, ISM) constitute the substrate-level "real side" — learned, structural, non-conscious. The explicit models (EWM, ESM) constitute the simulation-level "virtual side" — transient, generated, phenomenal. Arrows indicate generation: implicit models generate explicit models in real time, constrained by current sensory input. The dashed line represents the implicit-explicit boundary, whose permeability varies across states (increased in psychedelic states, locally decreased in anosognosia). Self-referential closure (the ESM modeling the system that generates it) is indicated by the reflexive arrow.

## Layout Specification (for graphic designer or TikZ)

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│              SCOPE →                                │
│         Everything (world)    Self only              │
│                                                     │
│  M   ┌──────────────────┬──────────────────┐        │
│  O   │                  │                  │        │
│  D   │   Implicit       │   Implicit       │        │
│  E   │   World Model    │   Self Model     │  REAL  │
│      │   (IWM)          │   (ISM)          │  SIDE  │
│  ↓   │                  │                  │        │
│      │  • Synaptic      │  • Body schema   │  Non-  │
│  I   │    weights        │  • Habits        │  con-  │
│  m   │  • All learned   │  • Personality   │  scious│
│  p   │    knowledge      │  • Autobio.     │        │
│  l   │  • Causal         │    memory        │  "Lights│
│  i   │    models         │  • Motor skills │   off" │
│  c   │                  │                  │        │
│  i   ├─ ─ ─ ─ ─ ─ ─ ─ ─┼─ ─ ─ ─ ─ ─ ─ ─ ┤        │
│  t   │  PERMEABILITY BOUNDARY              │        │
│      │  (variable: ↑ psychedelics,          │        │
│  →   │   ↓ anosognosia)                    │        │
│      ├──────────────────┼──────────────────┤        │
│  E   │                  │                  │        │
│  x   │   Explicit       │   Explicit       │ VIRTUAL│
│  p   │   World Model    │   Self Model     │  SIDE  │
│  l   │   (EWM)          │   (ESM)          │        │
│  i   │                  │       ↺          │  Phe-  │
│  c   │  • Perceived     │  [self-referential│ nomenal│
│  i   │    world          │   closure]       │        │
│  t   │  • Sensory        │  • "I"           │  "Lights│
│      │    experience     │  • Perspective   │   on"  │
│      │  • THE conscious  │  • Agency sense  │        │
│      │    world          │  • THE conscious │        │
│      │                  │    self           │        │
│      └──────────────────┴──────────────────┘        │
│                                                     │
│  ─────► Generation (implicit → explicit)            │
│  - - -  Permeability boundary (variable)            │
│    ↺    Self-referential closure                    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## Key Visual Elements

1. **2×2 grid** — the central structure
2. **Clear horizontal division** — real side (top) vs virtual side (bottom), marked with distinct shading:
   - Real side: muted/gray background ("lights off")
   - Virtual side: bright/colored background ("lights on")
3. **Dashed permeability boundary** between implicit and explicit rows
4. **Downward arrows** from IWM→EWM and ISM→ESM showing generation
5. **Sensory input arrow** entering from the left, feeding into EWM
6. **Reflexive arrow** on ESM indicating self-referential closure
7. **Labels on axes**: vertical = Mode (Implicit → Explicit), horizontal = Scope (World → Self)

## Color Scheme Recommendation

- IWM: Dark blue-gray (learned, stable, vast)
- ISM: Dark green-gray (self-knowledge, stable)
- EWM: Bright blue (the conscious world — vivid, phenomenal)
- ESM: Bright green/gold (the conscious self — the "I")
- Permeability boundary: Orange dashed line (dynamic, variable)
- Background: Light gray for real side, white for virtual side

## For LaTeX/TikZ

A TikZ implementation would use:
- `\draw` for the 2×2 grid
- `\fill[opacity=0.1]` for background shading
- `\draw[dashed, orange]` for the permeability boundary
- `\draw[->, thick]` for generation arrows
- `\draw[->, thick, bend right]` for the self-referential closure arrow on ESM
- `\node` for all labels

## For SVG/Web

An SVG version should be roughly 800×600px with:
- Clean sans-serif font (Helvetica, Arial, or similar)
- Generous padding between cells
- Hover tooltips explaining each model (for web version)
