#!/usr/bin/env python3
"""Convert book-manuscript.md to a POD-ready LaTeX book PDF.

Supports two editions:
  --edition us   6"x9" US Trade (KDP)         [default]
  --edition eu   15.5x23cm European (IngramSpark Germany)
  --edition all  Build both editions
"""

import argparse
import re
import os
import subprocess
import shutil

MANUSCRIPT = "/home/jeltz/aIware/pop-sci/book-manuscript.md"
FIGURES_DIR = "/home/jeltz/aIware/figures"
OUTPUT_DIR = "/home/jeltz/aIware/pop-sci"

# Edition-specific configuration
EDITIONS = {
    "us": {
        "label": "US Trade 6\"×9\" (KDP)",
        "suffix": "",           # book-manuscript.tex/pdf (default, backwards-compatible)
        "geometry": r"paperwidth=6in, paperheight=9in, inner=0.875in, outer=0.75in, top=0.75in, bottom=0.75in",
        "geometry_comment": "% Trim size: 6\" x 9\" (US Trade paperback)",
        "gutter_note": "gutter sized for ~250-page book",
        "isbn_line": r"\noindent ISBN: [TBD-US]\par",
        "edition_line": r"\noindent First US edition, 2026\par",
    },
    "eu": {
        "label": "European 15.5×23cm (IngramSpark)",
        "suffix": "-eu",        # book-manuscript-eu.tex/pdf
        "geometry": r"paperwidth=155mm, paperheight=230mm, inner=22mm, outer=19mm, top=19mm, bottom=19mm",
        "geometry_comment": "% Trim size: 15.5 x 23 cm (European trade paperback)",
        "gutter_note": "gutter sized for ~250-page book",
        "isbn_line": r"\noindent ISBN: [TBD-EU]\par",
        "edition_line": r"\noindent First European edition, 2026\par",
    },
}

# Figure insertion points: insert AFTER these line patterns
FIGURE_INSERTIONS = {
    # Figure 1: Now embedded directly in the markdown (Ch2, "Your Brain's Four Representations")
    # so no FIGURE_INSERTIONS entry needed — avoids duplication.
    # Figure 2: Also embedded directly in the markdown (Ch2, "The Real Side and the Virtual Side")
    # so no FIGURE_INSERTIONS entry needed — avoids duplication.
    # Figure 3: After "consciousness is not a light switch. It's a dimmer."
    "consciousness is not a light switch": {
        "file": "figure3-phenomenological-content-bw.png",
        "caption": "Phenomenological Content Through a Morning. Routine activities lead to low "
                   "phenomenological content (autopilot). Salient events (threats, social signals) "
                   "produce high content. Consciousness tracks what matters, not everything.",
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
        f"  \\includegraphics[width=0.95\\textwidth]{{{rel_path}}}\n"
        f"  \\caption{{{fig_info['caption']}}}\n"
        f"  \\label{{{fig_info['label']}}}\n"
        f"\\end{{figure}}\n\n"
    )

def escape_latex(text):
    """Escape special LaTeX characters in text, preserving intentional LaTeX commands."""
    # Preserve inline math ($...$) before escaping
    math_spans = []
    def _save_math(m):
        math_spans.append(m.group(0))
        return f'\x00MATH{len(math_spans)-1}\x00'
    text = re.sub(r'\$[^$]+\$', _save_math, text)
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
    # Handle Greek letters
    text = text.replace('Φ', '$\\Phi$')
    text = text.replace('φ', '$\\phi$')
    # Handle other Unicode that T1 encoding can't handle
    text = text.replace('→', '$\\rightarrow$')
    text = text.replace('↑', '$\\uparrow$')
    text = text.replace('↓', '$\\downarrow$')
    # Subscript/superscript Unicode
    text = text.replace('₂', '$_2$')
    # Restore preserved inline math spans
    for i, span in enumerate(math_spans):
        text = text.replace(f'\x00MATH{i}\x00', span)
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

def parse_table_alignment(separator_line):
    """Parse a markdown table separator row to determine column alignments.

    Returns a list of alignment characters: 'l', 'c', or 'r'.
    """
    cells = [c.strip() for c in separator_line.strip().strip('|').split('|')]
    alignments = []
    for cell in cells:
        cell = cell.strip()
        if cell.startswith(':') and cell.endswith(':'):
            alignments.append('c')
        elif cell.endswith(':'):
            alignments.append('r')
        else:
            alignments.append('l')
    return alignments


def parse_table_row(row_line):
    """Parse a markdown table row into a list of cell contents."""
    # Strip leading/trailing pipes and split
    row = row_line.strip()
    if row.startswith('|'):
        row = row[1:]
    if row.endswith('|'):
        row = row[:-1]
    return [cell.strip() for cell in row.split('|')]


def is_separator_row(line):
    """Check if a line is a markdown table separator (|---|---|)."""
    stripped = line.strip().strip('|')
    cells = [c.strip() for c in stripped.split('|')]
    return all(re.match(r'^:?-{2,}:?$', c) for c in cells if c)


def convert_table_cell(text):
    """Convert a single table cell's content: escape LaTeX chars, then apply inline formatting."""
    text = escape_latex(text)
    text = convert_inline(text)
    return text


def convert_spread_table(table_lines, data_start, header_cells, num_cols):
    """Convert the Appendix A visual processing hierarchy table into a two-page spread.

    Left page (verso): Area, Receptive field, Normal function
    Right page (recto): Area, Psychedelic signature
    Area column is repeated on both pages for cross-reference.
    """
    # Parse data rows into cells
    data_rows = []
    for row_line in table_lines[data_start:]:
        cells = parse_table_row(row_line)
        while len(cells) < num_cols:
            cells.append('')
        cells = cells[:num_cols]
        data_rows.append([convert_table_cell(c) for c in cells])

    # Column indices: 0=Area, 1=Receptive field, 2=Normal function, 3=Psychedelic
    lines = []

    # Force onto an even (verso/left) page for proper spread layout
    lines.append('')
    lines.append('\\clearpage')
    lines.append('\\ifodd\\value{page}\\hbox{}\\thispagestyle{empty}\\clearpage\\fi')
    lines.append('')

    # === LEFT PAGE (verso): Area, Receptive field, Normal function ===
    lines.append('{\\footnotesize')
    lines.append('\\noindent')
    lines.append('\\begin{tabularx}{\\linewidth}{>{\\hsize=0.7\\hsize}X X X}')
    lines.append('\\toprule')
    left_headers = ['\\textbf{Area}',
                    '\\textbf{Receptive field}', '\\textbf{Normal function}']
    lines.append(' & '.join(left_headers) + ' \\\\')
    lines.append('\\midrule')
    for row in data_rows:
        lines.append(f'{row[0]} & {row[1]} & {row[2]} \\\\')
        lines.append('[6pt]')  # extra vertical space between rows
    lines.append('\\bottomrule')
    lines.append('\\end{tabularx}')
    lines.append('}')

    # === RIGHT PAGE (recto): Area, Psychedelic signature ===
    lines.append('\\clearpage')
    lines.append('')
    lines.append('{\\footnotesize')
    lines.append('\\noindent')
    lines.append('\\begin{tabularx}{\\linewidth}{>{\\hsize=0.7\\hsize}X X}')
    lines.append('\\toprule')
    right_headers = ['\\textbf{Area}', '\\textbf{Psychedelic signature}']
    lines.append(' & '.join(right_headers) + ' \\\\')
    lines.append('\\midrule')
    for row in data_rows:
        lines.append(f'{row[0]} & {row[3]} \\\\')
        lines.append('[6pt]')  # match left page row spacing
    lines.append('\\bottomrule')
    lines.append('\\end{tabularx}')
    lines.append('}')
    lines.append('')

    return '\n'.join(lines)


def convert_fiveclass_table(table_lines, data_start, header_cells, num_cols, alignments):
    """Convert the five-class mapping table with footnotesize font."""
    # Parse data rows
    data_rows = []
    for row_line in table_lines[data_start:]:
        cells = parse_table_row(row_line)
        while len(cells) < num_cols:
            cells.append('')
        cells = cells[:num_cols]
        data_rows.append([convert_table_cell(c) for c in cells])

    # Map alignments to tabularx column types
    col_types = []
    for a in alignments[:num_cols]:
        if a == 'c':
            col_types.append(r'>{\centering\arraybackslash}X')
        elif a == 'r':
            col_types.append(r'>{\raggedleft\arraybackslash}X')
        else:
            col_types.append('X')
    col_spec = ' '.join(col_types)

    lines = []
    lines.append('')
    lines.append('{\\footnotesize')
    lines.append('\\noindent')
    lines.append('\\begin{tabularx}{\\linewidth}{' + col_spec + '}')
    lines.append('\\toprule')
    converted_headers = ['\\textbf{' + convert_table_cell(c) + '}' for c in header_cells]
    lines.append(' & '.join(converted_headers) + ' \\\\')
    lines.append('\\midrule')
    for row in data_rows:
        lines.append(' & '.join(row) + ' \\\\[4pt]')
    lines.append('\\bottomrule')
    lines.append('\\end{tabularx}')
    lines.append('}')
    lines.append('')
    return '\n'.join(lines)


def convert_table_to_latex(table_lines):
    """Convert a list of markdown table lines to a LaTeX tabularx table.

    Uses tabularx with X columns for automatic text wrapping, which prevents
    overflow on the page. Reduces font size for wider tables.
    The Appendix A visual processing hierarchy table (detected by 'Brodmann area'
    in header) is split across a two-page spread for readability.

    table_lines[0] = header row
    table_lines[1] = separator row (alignment indicators)
    table_lines[2:] = data rows
    """
    if len(table_lines) < 2:
        return ''

    header_cells = parse_table_row(table_lines[0])
    num_cols = len(header_cells)
    header_text = ' '.join(header_cells)

    # Parse alignment from separator row
    if len(table_lines) >= 2 and is_separator_row(table_lines[1]):
        alignments = parse_table_alignment(table_lines[1])
        data_start = 2
    else:
        alignments = ['l'] * num_cols
        data_start = 1

    # Detect the Appendix A visual processing hierarchy table → two-page spread
    # Must have 4 columns (Area, Receptive field, Normal function, Psychedelic signature)
    # The Chapter 6 condensed version has only 3 columns and should NOT be a spread.
    if 'Psychedelic signature' in header_text and 'Receptive field' in header_text:
        return convert_spread_table(table_lines, data_start, header_cells, num_cols)

    # Detect five-class tables → use footnotesize
    # Matches both the mapping table (Five-class | Wolfram | What changed) and
    # the full comparison table (Class | Rules | Period | Structure | Reducible | Computes)
    if 'Five-class' in header_text or 'What changed' in header_text or 'Computes' in header_text:
        return convert_fiveclass_table(table_lines, data_start, header_cells, num_cols, alignments)

    # Ensure alignment list matches column count
    while len(alignments) < num_cols:
        alignments.append('l')
    alignments = alignments[:num_cols]

    # Map alignments to tabularx column types (X = auto-wrap)
    col_types = []
    for a in alignments:
        if a == 'c':
            col_types.append(r'>{\centering\arraybackslash}X')
        elif a == 'r':
            col_types.append(r'>{\raggedleft\arraybackslash}X')
        else:
            col_types.append('X')

    col_spec = ' '.join(col_types)

    lines = []
    lines.append('')

    # Use \small for all tables (consistent sizing)
    lines.append('{\\small')

    lines.append('\\noindent')
    lines.append('\\begin{tabularx}{\\linewidth}{' + col_spec + '}')
    lines.append('\\toprule')

    # Header row (bold)
    converted_headers = ['\\textbf{' + convert_table_cell(c) + '}' for c in header_cells]
    lines.append(' & '.join(converted_headers) + ' \\\\')
    lines.append('\\midrule')

    # Data rows
    for row_line in table_lines[data_start:]:
        cells = parse_table_row(row_line)
        # Pad or trim to match column count
        while len(cells) < num_cols:
            cells.append('')
        cells = cells[:num_cols]
        converted_cells = [convert_table_cell(c) for c in cells]
        lines.append(' & '.join(converted_cells) + ' \\\\[4pt]')

    lines.append('\\bottomrule')
    lines.append('\\end{tabularx}')

    lines.append('}')  # close font size group

    lines.append('')

    return '\n'.join(lines)


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

        # --- Skip [FIGURE:] placeholders ---
        if stripped.startswith('[FIGURE:'):
            i += 1
            continue

        # --- Skip HTML comments (<!-- ... -->) ---
        if stripped.startswith('<!--'):
            # Single-line comment
            if '-->' in stripped:
                i += 1
                continue
            # Multi-line comment: skip until closing -->
            i += 1
            while i < len(lines) and '-->' not in lines[i]:
                i += 1
            if i < len(lines):
                i += 1  # skip the closing line
            continue

        # --- Markdown image: ![alt](path) ---
        img_match = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$', stripped)
        if img_match:
            alt_text = img_match.group(1)
            img_path = img_match.group(2)
            # Path is relative to manuscript dir (pop-sci/) — same as .tex output dir, keep as-is
            # Check if next line is an italic caption
            caption = ''
            if i + 1 < len(lines) and i + 2 < len(lines):
                next_stripped = lines[i + 1].strip()
                if next_stripped == '' and lines[i + 2].strip().startswith('*') and lines[i + 2].strip().endswith('*'):
                    caption = lines[i + 2].strip()[1:-1]  # strip surrounding *
                    caption = convert_inline(escape_latex(caption))
                    i += 2  # skip blank line and caption
            latex_lines.append('')
            latex_lines.append('\\begin{figure}[htbp]')
            latex_lines.append('  \\centering')
            latex_lines.append(f'  \\includegraphics[width=0.95\\textwidth]{{{img_path}}}')
            if caption:
                latex_lines.append(f'  \\caption{{{caption}}}')
            latex_lines.append('\\end{figure}')
            latex_lines.append('')
            i += 1
            continue

        # --- Markdown table detection ---
        if stripped.startswith('|') and not in_blockquote and not in_list:
            # Collect all consecutive lines that are part of this table
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i])
                i += 1
            # Convert table block to LaTeX
            latex_lines.append(convert_table_to_latex(table_lines))
            continue

        # Skip the title (# The Simulation You Call "I") - handled in preamble
        if stripped.startswith('# The Simulation') and not stripped.startswith('## '):
            i += 1
            continue

        # Skip subtitle line (## The Architecture of Consciousness...)
        if stripped.startswith('## The Architecture of Consciousness, Computation, and the Cosmos'):
            i += 1
            continue

        # Skip author line
        if stripped == '**Matthias Gruber**':
            i += 1
            continue

        # Dedication line — skip (now in preamble front matter)
        if stripped.startswith('*For everyone who has ever wondered'):
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
            raw_title = chapter_match.group(1)

            # Insert \mainmatter before first numbered chapter
            if raw_title.startswith('Chapter 1:'):
                latex_lines.append('\\mainmatter')
                latex_lines.append('\\pagestyle{fancy}')

            # Insert \backmatter before back matter sections
            if raw_title.startswith('Acknowledgments'):
                latex_lines.append('\\backmatter')

            # Clean up title for LaTeX
            title = convert_inline(escape_latex(raw_title))

            # Use \chapter* for non-numbered chapters
            if any(raw_title.startswith(w) for w in [
                'Preface', 'About', 'Acknowledgments', 'Notes', 'Coda', 'Appendix'
            ]):
                latex_lines.append(f'\\chapter*{{{title}}}')
                latex_lines.append(f'\\addcontentsline{{toc}}{{chapter}}{{{title}}}')
                latex_lines.append(f'\\markboth{{{title}}}{{}}')
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
            # Line break overrides for long section titles
            title = title.replace(
                'Why Your Brain Has the Capacity for Self-Modeling',
                'Why Your Brain Has the Capacity\\\\for Self-Modeling'
            )
            title = title.replace(
                "Psychedelic Visuals Reveal the Brain's Processing Layers",
                "Psychedelic Visuals Reveal\\\\the Brain's Processing Layers"
            )
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

def build_latex_document(body, edition="us"):
    """Wrap the body in a complete LaTeX document for POD printing."""
    ed = EDITIONS[edition]
    preamble = r"""\documentclass[11pt, twoside, openright]{book}

""" + ed["geometry_comment"] + "\n" + r"""\usepackage[
  """ + ed["geometry"] + r"""
]{geometry}

% Typography
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{palatino}          % Elegant serif font
\usepackage{microtype}         % Better typography
\emergencystretch=1em          % Allow extra stretch to avoid overflow with hyphenated/apostrophe words
\usepackage{setspace}
\setstretch{1.15}              % Standard book leading

% Graphics
\usepackage{graphicx}
\graphicspath{{../figures/}{../figures/book/}}

% Links (hidden for print - no colored text)
\usepackage{xcolor}
\usepackage[hidelinks]{hyperref}

% Chapter styling
\usepackage{titlesec}
\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries}
  {\chaptertitlename\ \thechapter}{20pt}{\Huge\raggedright}
\titleformat{name=\chapter,numberless}[display]
  {\normalfont\huge\bfseries}
  {}{0pt}{\Huge\raggedright}
\titlespacing*{\chapter}{0pt}{50pt}{40pt}

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

% For plain pages (chapter starts, front matter)
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

% Tables
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{tabularx}

% Figure placement
\usepackage{float}

% Landscape pages for wide tables
\usepackage{pdflscape}
\renewcommand{\textfraction}{0.1}
\renewcommand{\topfraction}{0.9}
\renewcommand{\bottomfraction}{0.9}

% Make blank pages (from \cleardoublepage) truly blank
\makeatletter
\def\cleardoublepage{\clearpage\if@twoside \ifodd\c@page\else
  \thispagestyle{empty}\hbox{}\newpage
  \if@twocolumn\hbox{}\newpage\fi\fi\fi}
\makeatother

\begin{document}

% ==== FRONT MATTER ====
\frontmatter
\pagestyle{empty}

% ---- Half-title page (recto) ----
\vspace*{3in}
\begin{center}
{\Huge\bfseries The Simulation\\[0.3cm] You Call ``I''\par}
\end{center}
\cleardoublepage

% ---- Full title page (recto) ----
\vspace*{2in}
\begin{center}
{\Huge\bfseries The Simulation\\[0.3cm] You Call ``I''\par}
\vspace{0.8cm}
{\Large The Architecture of\\[0.2cm] Consciousness, Computation, and the Cosmos\par}
\vspace{2cm}
{\large Matthias Gruber\par}
\end{center}
\clearpage

% ---- Copyright page (verso of title) ----
\thispagestyle{empty}
\vspace*{\fill}
{\small
\noindent \textcopyright\ 2026 Matthias Gruber. All rights reserved.\par
\vspace{0.5cm}
\noindent No part of this publication may be reproduced, distributed, or transmitted
in any form or by any means without the prior written permission of the author,
except for brief quotations in reviews and certain noncommercial uses
permitted by copyright law.\par
\vspace{0.5cm}
""" + ed["isbn_line"] + r"""
\vspace{0.5cm}
""" + ed["edition_line"] + r"""
\vspace{0.5cm}
\noindent www.matthiasgruber.com\par
}
\cleardoublepage

% ---- Dedication page (recto) ----
\thispagestyle{empty}
\vspace*{3in}
\begin{center}
\textit{For everyone who has ever wondered why anything feels like anything.}
\end{center}
\cleardoublepage

% ---- Table of contents ----
\pagestyle{plain}
\tableofcontents
\cleardoublepage

"""

    postamble = r"""
\end{document}
"""
    return preamble + body + postamble

def build_edition(edition, md_text, body):
    """Build a single edition (us or eu)."""
    ed = EDITIONS[edition]
    suffix = ed["suffix"]
    tex_file = os.path.join(OUTPUT_DIR, f"book-manuscript{suffix}.tex")
    pdf_file = os.path.join(OUTPUT_DIR, f"book-manuscript{suffix}.pdf")
    win_name = f"book-manuscript{suffix}.pdf"

    print(f"\n{'='*60}")
    print(f"Building: {ed['label']}")
    print(f"{'='*60}")

    print("Building document...")
    document = build_latex_document(body, edition)

    print(f"Writing {tex_file}...")
    with open(tex_file, 'w', encoding='utf-8') as f:
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
    subprocess.run(
        ['pdflatex', '-interaction=nonstopmode', '-output-directory', OUTPUT_DIR, tex_file],
        capture_output=True, cwd=OUTPUT_DIR, timeout=120
    )

    print("Compiling PDF (pass 2 for TOC)...")
    subprocess.run(
        ['pdflatex', '-interaction=nonstopmode', '-output-directory', OUTPUT_DIR, tex_file],
        capture_output=True, cwd=OUTPUT_DIR, timeout=120
    )

    if os.path.exists(pdf_file):
        size_mb = os.path.getsize(pdf_file) / (1024 * 1024)
        print(f"\nSUCCESS: {pdf_file} ({size_mb:.1f} MB)")

        # Copy to Windows desktop
        win_path = f"/mnt/c/Users/Matthias/Desktop/{win_name}"
        try:
            shutil.copy2(pdf_file, win_path)
            print(f"Copied to: {win_path}")
        except Exception as e:
            print(f"Note: Could not copy to Windows desktop: {e}")
        return True
    else:
        print(f"\nFAILED - checking log...")
        log_path = tex_file.replace('.tex', '.log')
        if os.path.exists(log_path):
            with open(log_path, 'r', errors='replace') as f:
                log = f.read()
            errors = [l for l in log.split('\n') if l.startswith('!')]
            for e in errors[:10]:
                print(f"  ERROR: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Build POD-ready book PDF")
    parser.add_argument('--edition', choices=['us', 'eu', 'all'], default='us',
                        help='Edition to build: us (6"x9" KDP), eu (15.5x23cm IngramSpark), all (both)')
    args = parser.parse_args()

    print("Reading manuscript...")
    with open(MANUSCRIPT, 'r', encoding='utf-8') as f:
        md_text = f.read()

    print("Converting to LaTeX...")
    body = markdown_to_latex(md_text)

    editions = ['us', 'eu'] if args.edition == 'all' else [args.edition]
    results = {}
    for ed in editions:
        results[ed] = build_edition(ed, md_text, body)

    print(f"\n{'='*60}")
    for ed, ok in results.items():
        status = "OK" if ok else "FAILED"
        print(f"  {EDITIONS[ed]['label']}: {status}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
