#!/usr/bin/env python3
"""Convert book-manuscript.md to a beautiful LaTeX book PDF with illustrations."""

import re
import os
import subprocess
import shutil

MANUSCRIPT = "/home/jeltz/aIware/pop-sci/book-manuscript.md"
FIGURES_DIR = "/home/jeltz/aIware/figures"
OUTPUT_DIR = "/home/jeltz/aIware/pop-sci"
TEX_FILE = os.path.join(OUTPUT_DIR, "book-manuscript.tex")

# Figure insertion points: insert AFTER these line patterns
FIGURE_INSERTIONS = {
    # Figure 1: After ESM description, before "The Real Side and the Virtual Side"
    "### The Real Side and the Virtual Side": {
        "file": "figure1-four-model-architecture.png",
        "caption": "The Four-Model Architecture. The four models are arranged along two axes: "
                   "scope (world vs.\\ self) and mode (implicit/learned vs.\\ explicit/simulated). "
                   "The implicit models (IWM, ISM) constitute the substrate-level ``real side'' --- "
                   "learned, structural, non-conscious. The explicit models (EWM, ESM) constitute "
                   "the simulation-level ``virtual side'' --- transient, generated, phenomenal.",
        "label": "fig:four-models",
        "position": "before",  # Insert figure BEFORE this heading
    },
    # Figure 2: After "That's the key. Let me spell it out."
    "That's the key. Let me spell it out.": {
        "file": "figure2-real-virtual-split.png",
        "caption": "The Real/Virtual Split. The substrate (real side) does not experience. "
                   "The simulation (virtual side) does. Asking why neurons ``feel'' commits "
                   "a category error --- neurons generate the simulation; the simulation feels.",
        "label": "fig:real-virtual",
        "position": "after",
    },
    # Figure 3: After "consciousness is not a light switch. It's a dimmer."
    "consciousness is not a light switch": {
        "file": "figure3-phenomenological-content.png",
        "caption": "Phenomenological Content Through a Morning. ESM updates produce peaks in "
                   "phenomenological content. Routine activities lead to low content (autopilot). "
                   "Salient events (threats, social signals) produce high content. Consciousness "
                   "tracks what matters, not everything.",
        "label": "fig:phenomenological",
        "position": "after",
    },
}

def make_figure_latex(fig_info):
    """Generate LaTeX for a figure insertion."""
    fig_path = os.path.join(FIGURES_DIR, fig_info["file"])
    # Use relative path from output dir
    rel_path = os.path.relpath(fig_path, OUTPUT_DIR)
    return (
        f"\n\\begin{{figure}}[htbp]\n"
        f"  \\centering\n"
        f"  \\includegraphics[width=0.85\\textwidth]{{{rel_path}}}\n"
        f"  \\caption{{{fig_info['caption']}}}\n"
        f"  \\label{{{fig_info['label']}}}\n"
        f"\\end{{figure}}\n\n"
    )

def escape_latex(text):
    """Escape special LaTeX characters in text, preserving intentional LaTeX commands."""
    # Don't escape inside our figure blocks (they have their own LaTeX)
    # Handle ampersands
    text = text.replace('&', '\\&')
    # Handle percent signs
    text = text.replace('%', '\\%')
    # Handle hash/pound signs (but not markdown headings - those are handled separately)
    # Handle underscores in running text (not in URLs or intentional formatting)
    # This is tricky - we need to be careful
    # Handle dollar signs
    text = text.replace('$', '\\$')
    return text

def convert_inline(text):
    """Convert inline markdown formatting to LaTeX."""
    # Bold+italic (***text*** or ___text___)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'\\textbf{\\textit{\1}}', text)
    # Bold (**text**)
    text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)
    # Italic (*text*) - careful not to match already-converted
    text = re.sub(r'(?<![\\])\*(.+?)\*', r'\\textit{\1}', text)
    # Em-dashes (already as — or as ---)
    text = text.replace('—', '---')
    # En-dashes
    text = text.replace('–', '--')
    # Smart quotes - convert "text" to ``text''
    # This is a simplified approach
    text = re.sub(r'"([^"]+)"', r"``\1''", text)
    # Remaining straight double quotes
    text = text.replace('"', "''")
    # Ellipsis
    text = text.replace('...', '\\ldots{}')
    return text

def markdown_to_latex(md_text):
    """Convert markdown manuscript to LaTeX body."""
    lines = md_text.split('\n')
    latex_lines = []
    in_blockquote = False
    in_list = False
    pending_figures_before = {}  # heading text -> figure latex
    pending_figures_after = {}   # text fragment -> figure latex

    # Prepare figure insertion lookup
    for trigger, fig_info in FIGURE_INSERTIONS.items():
        fig_latex = make_figure_latex(fig_info)
        if fig_info["position"] == "before":
            pending_figures_before[trigger] = fig_latex
        else:
            pending_figures_after[trigger] = fig_latex

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Check for "before" figure insertions (insert figure before this heading)
        for trigger, fig_latex in list(pending_figures_before.items()):
            if trigger in stripped:
                latex_lines.append(fig_latex)
                del pending_figures_before[trigger]
                break

        # Skip the title (# The Simulation You Call "I") - handled in preamble
        if stripped.startswith('# The Simulation') and not stripped.startswith('## '):
            i += 1
            continue

        # Skip subtitle line (## How Your Brain...)
        if stripped.startswith('## How Your Brain Creates Consciousness'):
            i += 1
            continue

        # Skip author line
        if stripped == '**Matthias Gruber**':
            i += 1
            continue

        # Dedication line
        if stripped.startswith('*For everyone who has ever wondered'):
            latex_lines.append('\\vspace*{2cm}')
            latex_lines.append('\\begin{center}')
            latex_lines.append(convert_inline(escape_latex(stripped)))
            latex_lines.append('\\end{center}')
            latex_lines.append('\\vspace{1cm}')
            i += 1
            continue

        # Skip table of contents section
        if stripped == '## Contents':
            # Skip until next ---
            i += 1
            while i < len(lines) and lines[i].strip() != '---':
                i += 1
            i += 1  # skip the ---
            continue

        # Horizontal rules -> skip (we use chapter breaks instead)
        if stripped == '---':
            i += 1
            continue

        # Chapter headings (## Chapter N: Title or ## Preface: or ## About or ## Acknowledgments or ## Notes)
        chapter_match = re.match(r'^## (.+)$', stripped)
        if chapter_match:
            title = chapter_match.group(1)
            # Clean up title for LaTeX
            title = convert_inline(escape_latex(title))
            # Use \chapter* for non-numbered chapters
            if any(title.startswith(w) for w in ['Preface', 'About', 'Acknowledgments', 'Notes', 'Coda']):
                latex_lines.append(f'\\chapter*{{{title}}}')
                latex_lines.append(f'\\addcontentsline{{toc}}{{chapter}}{{{title}}}')
            else:
                # Extract chapter number and title
                ch_match = re.match(r'Chapter \d+:\s*(.+)', title)
                if ch_match:
                    ch_title = ch_match.group(1)
                    latex_lines.append(f'\\chapter{{{ch_title}}}')
                else:
                    latex_lines.append(f'\\chapter{{{title}}}')
            i += 1
            continue

        # Section headings (### )
        section_match = re.match(r'^### (.+)$', stripped)
        if section_match:
            title = convert_inline(escape_latex(section_match.group(1)))
            latex_lines.append(f'\\section*{{{title}}}')
            i += 1
            continue

        # Subsection headings (#### )
        subsection_match = re.match(r'^#### (.+)$', stripped)
        if subsection_match:
            title = convert_inline(escape_latex(subsection_match.group(1)))
            latex_lines.append(f'\\subsection*{{{title}}}')
            i += 1
            continue

        # Block quotes
        if stripped.startswith('> '):
            if not in_blockquote:
                latex_lines.append('\\begin{quote}')
                in_blockquote = True
            quote_text = convert_inline(escape_latex(stripped[2:]))
            latex_lines.append(quote_text)
            i += 1
            continue
        elif in_blockquote and stripped == '':
            latex_lines.append('\\end{quote}')
            in_blockquote = False
            latex_lines.append('')
            i += 1
            continue
        elif in_blockquote and not stripped.startswith('>'):
            latex_lines.append('\\end{quote}')
            in_blockquote = False
            # Don't increment - reprocess this line
            continue

        # List items
        if stripped.startswith('- ') or stripped.startswith('* '):
            if not in_list:
                latex_lines.append('\\begin{itemize}')
                in_list = True
            item_text = convert_inline(escape_latex(stripped[2:]))
            latex_lines.append(f'  \\item {item_text}')
            i += 1
            continue
        # Numbered list items
        num_match = re.match(r'^(\d+)\.\s+(.+)$', stripped)
        if num_match:
            if not in_list:
                latex_lines.append('\\begin{enumerate}')
                in_list = True
            item_text = convert_inline(escape_latex(num_match.group(2)))
            latex_lines.append(f'  \\item {item_text}')
            i += 1
            continue

        # End list if we hit a non-list, non-empty line or empty line
        if in_list and (stripped == '' or (not stripped.startswith('- ') and not stripped.startswith('* ') and not re.match(r'^\d+\.', stripped))):
            # Check if it was enumerate or itemize by looking back
            for prev in reversed(latex_lines):
                if '\\begin{enumerate}' in prev:
                    latex_lines.append('\\end{enumerate}')
                    break
                elif '\\begin{itemize}' in prev:
                    latex_lines.append('\\end{itemize}')
                    break
            in_list = False
            if stripped == '':
                latex_lines.append('')
                i += 1
                continue
            # Fall through to process the line normally

        # Empty line
        if stripped == '':
            latex_lines.append('')
            i += 1
            continue

        # Regular paragraph text
        text = convert_inline(escape_latex(stripped))
        latex_lines.append(text)

        # Check for "after" figure insertions
        for trigger, fig_latex in list(pending_figures_after.items()):
            if trigger in stripped:
                latex_lines.append(fig_latex)
                del pending_figures_after[trigger]
                break

        i += 1

    # Close any open environments
    if in_blockquote:
        latex_lines.append('\\end{quote}')
    if in_list:
        latex_lines.append('\\end{itemize}')

    return '\n'.join(latex_lines)

def build_latex_document(body):
    """Wrap the body in a complete LaTeX document."""
    preamble = r"""\documentclass[11pt, a5paper, openany]{book}

% Page geometry - A5 for comfortable book reading
\usepackage[a5paper, margin=1.8cm, top=2.2cm, bottom=2.2cm]{geometry}

% Typography
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{palatino}          % Elegant serif font
\usepackage{microtype}         % Better typography
\usepackage{setspace}
\onehalfspacing

% Graphics
\usepackage{graphicx}
\graphicspath{{../figures/}}

% Colors and links
\usepackage[dvipsnames]{xcolor}
\usepackage[
  colorlinks=true,
  linkcolor=BrickRed,
  urlcolor=NavyBlue,
  citecolor=OliveGreen
]{hyperref}

% Chapter styling
\usepackage{titlesec}
\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries}
  {\chaptertitlename\ \thechapter}{20pt}{\Huge}
\titleformat{name=\chapter,numberless}[display]
  {\normalfont\huge\bfseries}
  {}{0pt}{\Huge}
\titlespacing*{\chapter}{0pt}{30pt}{20pt}

% Section styling
\titleformat{\section}
  {\normalfont\Large\bfseries}{}{0pt}{}
\titlespacing*{\section}{0pt}{20pt}{10pt}

% Headers and footers
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\small\itshape The Simulation You Call ``I''}
\fancyhead[RO]{\small\itshape\leftmark}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}

% For plain pages (chapter starts)
\fancypagestyle{plain}{
  \fancyhf{}
  \fancyfoot[C]{\thepage}
  \renewcommand{\headrulewidth}{0pt}
}

% Quote formatting
\usepackage{csquotes}
\renewenvironment{quote}
  {\list{}{\leftmargin=1.5em\rightmargin=1.5em}\item\relax\itshape}
  {\endlist}

% Prevent widows and orphans
\widowpenalty=10000
\clubpenalty=10000

% Figure placement
\usepackage{float}
\renewcommand{\textfraction}{0.1}
\renewcommand{\topfraction}{0.9}
\renewcommand{\bottomfraction}{0.9}

\begin{document}

% Title page
\begin{titlepage}
\centering
\vspace*{3cm}
{\Huge\bfseries The Simulation\\[0.3cm] You Call ``I''\par}
\vspace{1cm}
{\Large How Your Brain Creates Consciousness\\[0.2cm]
--- and Why That Means We Can Build One\par}
\vspace{2cm}
{\large\itshape Matthias Gruber\par}
\vfill
{\small Draft manuscript --- \today\par}
\end{titlepage}

% Table of contents
\tableofcontents
\newpage

"""

    postamble = r"""
\end{document}
"""
    return preamble + body + postamble

def main():
    print("Reading manuscript...")
    with open(MANUSCRIPT, 'r', encoding='utf-8') as f:
        md_text = f.read()

    print("Converting to LaTeX...")
    body = markdown_to_latex(md_text)

    print("Building document...")
    document = build_latex_document(body)

    print(f"Writing {TEX_FILE}...")
    with open(TEX_FILE, 'w', encoding='utf-8') as f:
        f.write(document)

    # Copy figures to output directory for compilation
    for fig_info in FIGURE_INSERTIONS.values():
        src = os.path.join(FIGURES_DIR, fig_info["file"])
        dst = os.path.join(OUTPUT_DIR, fig_info["file"])
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.copy2(src, dst)
            print(f"  Copied {fig_info['file']}")

    # Compile with pdflatex (run twice for TOC)
    print("Compiling PDF (pass 1)...")
    result1 = subprocess.run(
        ['pdflatex', '-interaction=nonstopmode', '-output-directory', OUTPUT_DIR, TEX_FILE],
        capture_output=True, text=True, cwd=OUTPUT_DIR, timeout=120
    )

    print("Compiling PDF (pass 2 for TOC)...")
    result2 = subprocess.run(
        ['pdflatex', '-interaction=nonstopmode', '-output-directory', OUTPUT_DIR, TEX_FILE],
        capture_output=True, text=True, cwd=OUTPUT_DIR, timeout=120
    )

    pdf_path = TEX_FILE.replace('.tex', '.pdf')
    if os.path.exists(pdf_path):
        size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
        print(f"\nSUCCESS: {pdf_path} ({size_mb:.1f} MB)")

        # Also copy to Windows desktop for easy access
        win_path = "/mnt/c/Users/Matthias/Desktop/book-manuscript.pdf"
        try:
            shutil.copy2(pdf_path, win_path)
            print(f"Copied to: {win_path}")
        except Exception as e:
            print(f"Note: Could not copy to Windows desktop: {e}")
    else:
        print("\nFAILED - checking log...")
        log_path = TEX_FILE.replace('.tex', '.log')
        if os.path.exists(log_path):
            with open(log_path, 'r') as f:
                log = f.read()
            # Find errors
            errors = [l for l in log.split('\n') if l.startswith('!')]
            for e in errors[:10]:
                print(f"  ERROR: {e}")

if __name__ == '__main__':
    main()
