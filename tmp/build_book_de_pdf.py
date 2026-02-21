#!/usr/bin/env python3
"""Convert book-manuscript-de.md to a review-ready LaTeX book PDF (German).

Based on build_book_pdf.py (English version), adapted for:
  - German babel hyphenation
  - German typographical quotes („ ")
  - German chapter/section detection
  - German title page and front matter
"""

import re
import os
import subprocess
import shutil

MANUSCRIPT = "/home/jeltz/aIware/pop-sci/book-manuscript-de.md"
FIGURES_DIR = "/home/jeltz/aIware/figures"
OUTPUT_DIR = "/home/jeltz/aIware/pop-sci"

# Figure insertion points: insert AFTER these line patterns
FIGURE_INSERTIONS = {
    # Figure 3: After "Bewusstsein ist kein Lichtschalter. Es ist ein Dimmer."
    "Bewusstsein ist kein Lichtschalter": {
        "file": "figure3-phenomenological-content-bw.png",
        "caption": "Phänomenologischer Gehalt im Tagesverlauf. Routinetätigkeiten führen zu "
                   "niedrigem phänomenologischem Gehalt (Autopilot). Auffällige Ereignisse "
                   "(Bedrohungen, soziale Signale) erzeugen hohen Gehalt. Bewusstsein verfolgt, "
                   "was wichtig ist, nicht alles.",
        "label": "fig:phenomenological",
        "position": "after",
    },
}


def make_figure_latex(fig_info):
    """Generate LaTeX for a figure insertion."""
    fig_path = os.path.join(FIGURES_DIR, fig_info["file"])
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
    math_spans = []
    def _save_math(m):
        math_spans.append(m.group(0))
        return f'\x00MATH{len(math_spans)-1}\x00'
    text = re.sub(r'\$[^$]+\$', _save_math, text)
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('$', '\\$')
    # Greek letters
    text = text.replace('Φ', '$\\Phi$')
    text = text.replace('φ', '$\\phi$')
    # Arrows and special Unicode
    text = text.replace('→', '$\\rightarrow$')
    text = text.replace('↑', '$\\uparrow$')
    text = text.replace('↓', '$\\downarrow$')
    text = text.replace('₂', '$_2$')
    # Restore preserved inline math spans
    for i, span in enumerate(math_spans):
        text = text.replace(f'\x00MATH{i}\x00', span)
    return text


def convert_inline(text):
    """Convert inline markdown formatting to LaTeX."""
    # Bold+italic (***text***)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'\\textbf{\\textit{\1}}', text)
    # Bold (**text**)
    text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)
    # Italic (*text*)
    text = re.sub(r'(?<![\\])\*(.+?)\*', r'\\textit{\1}', text)
    # Em-dashes
    text = text.replace('—', '---')
    # En-dashes
    text = text.replace('–', '--')
    # German quotes: "text" → \glqq{}text\grqq{}
    text = re.sub(r'"([^"]+)"', r'\\glqq{}\1\\grqq{}', text)
    # Remaining straight double quotes
    text = text.replace('"', "\\grqq{}")
    # Ellipsis
    text = text.replace('...', '\\ldots{}')
    return text


def parse_table_alignment(separator_line):
    """Parse a markdown table separator row to determine column alignments."""
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
    """Convert a single table cell's content."""
    text = escape_latex(text)
    text = convert_inline(text)
    return text


def convert_spread_table(table_lines, data_start, header_cells, num_cols):
    """Convert Appendix A visual processing hierarchy table into a two-page spread."""
    data_rows = []
    for row_line in table_lines[data_start:]:
        cells = parse_table_row(row_line)
        while len(cells) < num_cols:
            cells.append('')
        cells = cells[:num_cols]
        data_rows.append([convert_table_cell(c) for c in cells])

    lines = []
    lines.append('')
    lines.append('\\clearpage')
    lines.append('\\ifodd\\value{page}\\hbox{}\\thispagestyle{empty}\\clearpage\\fi')
    lines.append('')

    # LEFT PAGE: Areal, Rezeptives Feld, Normale Funktion
    lines.append('{\\footnotesize')
    lines.append('\\noindent')
    lines.append('\\begin{tabularx}{\\linewidth}{>{\\hsize=0.7\\hsize}X X X}')
    lines.append('\\toprule')
    left_headers = ['\\textbf{Areal}',
                    '\\textbf{Rezeptives Feld}', '\\textbf{Normale Funktion}']
    lines.append(' & '.join(left_headers) + ' \\\\')
    lines.append('\\midrule')
    for row in data_rows:
        lines.append(f'{row[0]} & {row[1]} & {row[2]} \\\\')
        lines.append('[6pt]')
    lines.append('\\bottomrule')
    lines.append('\\end{tabularx}')
    lines.append('}')

    # RIGHT PAGE: Areal, Psychedelische Signatur
    lines.append('\\clearpage')
    lines.append('')
    lines.append('{\\footnotesize')
    lines.append('\\noindent')
    lines.append('\\begin{tabularx}{\\linewidth}{>{\\hsize=0.7\\hsize}X X}')
    lines.append('\\toprule')
    right_headers = ['\\textbf{Areal}', '\\textbf{Psychedelische Signatur}']
    lines.append(' & '.join(right_headers) + ' \\\\')
    lines.append('\\midrule')
    for row in data_rows:
        lines.append(f'{row[0]} & {row[3]} \\\\')
        lines.append('[6pt]')
    lines.append('\\bottomrule')
    lines.append('\\end{tabularx}')
    lines.append('}')
    lines.append('')
    return '\n'.join(lines)


def convert_fiveclass_table(table_lines, data_start, header_cells, num_cols, alignments):
    """Convert five-class mapping table with footnotesize font."""
    data_rows = []
    for row_line in table_lines[data_start:]:
        cells = parse_table_row(row_line)
        while len(cells) < num_cols:
            cells.append('')
        cells = cells[:num_cols]
        data_rows.append([convert_table_cell(c) for c in cells])

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
    """Convert markdown table lines to a LaTeX tabularx table."""
    if len(table_lines) < 2:
        return ''

    header_cells = parse_table_row(table_lines[0])
    num_cols = len(header_cells)
    header_text = ' '.join(header_cells)

    if len(table_lines) >= 2 and is_separator_row(table_lines[1]):
        alignments = parse_table_alignment(table_lines[1])
        data_start = 2
    else:
        alignments = ['l'] * num_cols
        data_start = 1

    # Detect Appendix A spread table (4 columns with Psychedelische Signatur + Rezeptives Feld)
    if 'Psychedelische Signatur' in header_text and 'Rezeptives Feld' in header_text:
        return convert_spread_table(table_lines, data_start, header_cells, num_cols)

    # Detect five-class tables
    if 'Fünf-Klassen' in header_text or 'Fünf Klassen' in header_text or 'Was sich ändert' in header_text or 'Berechnet' in header_text or 'Wolfram-Klasse' in header_text:
        return convert_fiveclass_table(table_lines, data_start, header_cells, num_cols, alignments)

    while len(alignments) < num_cols:
        alignments.append('l')
    alignments = alignments[:num_cols]

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
    lines.append('{\\small')
    lines.append('\\noindent')
    lines.append('\\begin{tabularx}{\\linewidth}{' + col_spec + '}')
    lines.append('\\toprule')

    converted_headers = ['\\textbf{' + convert_table_cell(c) + '}' for c in header_cells]
    lines.append(' & '.join(converted_headers) + ' \\\\')
    lines.append('\\midrule')

    for row_line in table_lines[data_start:]:
        cells = parse_table_row(row_line)
        while len(cells) < num_cols:
            cells.append('')
        cells = cells[:num_cols]
        converted_cells = [convert_table_cell(c) for c in cells]
        lines.append(' & '.join(converted_cells) + ' \\\\[4pt]')

    lines.append('\\bottomrule')
    lines.append('\\end{tabularx}')
    lines.append('}')
    lines.append('')
    return '\n'.join(lines)


def markdown_to_latex(md_text):
    """Convert German markdown manuscript to LaTeX body."""
    lines = md_text.split('\n')
    latex_lines = []
    in_blockquote = False
    in_list = False
    pending_figures_before = {}
    pending_figures_after = {}

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

        # Check for "before" figure insertions
        for trigger, fig_latex in list(pending_figures_before.items()):
            if trigger in stripped:
                latex_lines.append(fig_latex)
                del pending_figures_before[trigger]
                break

        # Skip [FIGURE:] placeholders
        if stripped.startswith('[FIGURE:'):
            i += 1
            continue

        # Skip HTML comments
        if stripped.startswith('<!--'):
            if '-->' in stripped:
                i += 1
                continue
            i += 1
            while i < len(lines) and '-->' not in lines[i]:
                i += 1
            if i < len(lines):
                i += 1
            continue

        # Markdown image: ![alt](path)
        img_match = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$', stripped)
        if img_match:
            alt_text = img_match.group(1)
            img_path = img_match.group(2)
            caption = ''
            if i + 1 < len(lines) and i + 2 < len(lines):
                next_stripped = lines[i + 1].strip()
                if next_stripped == '' and lines[i + 2].strip().startswith('*') and lines[i + 2].strip().endswith('*'):
                    caption = lines[i + 2].strip()[1:-1]
                    caption = convert_inline(escape_latex(caption))
                    i += 2
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

        # Markdown table detection
        if stripped.startswith('|') and not in_blockquote and not in_list:
            table_lines_block = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines_block.append(lines[i])
                i += 1
            latex_lines.append(convert_table_to_latex(table_lines_block))
            continue

        # Skip the title line
        if stripped.startswith('# Die Simulation') and not stripped.startswith('## '):
            i += 1
            continue

        # Skip subtitle line
        if stripped.startswith('## Die Architektur von Bewusstsein'):
            i += 1
            continue

        # Skip author line
        if stripped == '**Matthias Gruber**':
            i += 1
            continue

        # Skip dedication line (handled in preamble front matter)
        if stripped.startswith('*Für alle, die sich je gefragt'):
            i += 1
            continue

        # Skip table of contents section
        if stripped == '## Inhalt':
            i += 1
            while i < len(lines) and lines[i].strip() != '---':
                i += 1
            i += 1  # skip the ---
            continue

        # Horizontal rules -> skip
        if stripped == '---':
            i += 1
            continue

        # Chapter headings (## Kapitel N: Title or ## Vorwort: or ## Über or etc.)
        chapter_match = re.match(r'^## (.+)$', stripped)
        if chapter_match:
            raw_title = chapter_match.group(1)

            # Insert \mainmatter before first numbered chapter
            if raw_title.startswith('Kapitel 1:'):
                latex_lines.append('\\mainmatter')
                latex_lines.append('\\pagestyle{fancy}')

            # Insert \backmatter before back matter sections
            if raw_title.startswith('Danksagung'):
                latex_lines.append('\\backmatter')

            title = convert_inline(escape_latex(raw_title))

            # Unnumbered chapters
            if any(raw_title.startswith(w) for w in [
                'Vorwort', 'Über', 'Danksagung', 'Anmerkungen', 'Coda', 'Anhang'
            ]):
                latex_lines.append(f'\\chapter*{{{title}}}')
                latex_lines.append(f'\\addcontentsline{{toc}}{{chapter}}{{{title}}}')
                latex_lines.append(f'\\markboth{{{title}}}{{}}')
            else:
                # Extract chapter number and title (Kapitel N: Title)
                ch_match = re.match(r'Kapitel \d+:\s*(.+)', title)
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
        num_match = re.match(r'^(\d+)\.\s+(.+)$', stripped)
        if num_match:
            if not in_list:
                latex_lines.append('\\begin{enumerate}')
                in_list = True
            item_text = convert_inline(escape_latex(num_match.group(2)))
            latex_lines.append(f'  \\item {item_text}')
            i += 1
            continue

        # End list
        if in_list and (stripped == '' or (not stripped.startswith('- ') and not stripped.startswith('* ') and not re.match(r'^\d+\.', stripped))):
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

    if in_blockquote:
        latex_lines.append('\\end{quote}')
    if in_list:
        latex_lines.append('\\end{itemize}')

    return '\n'.join(latex_lines)


def build_latex_document(body):
    """Wrap the body in a complete LaTeX document for German book."""
    preamble = r"""\documentclass[11pt, twoside, openright]{book}

% Trim size: 6" x 9" (US Trade paperback)
\usepackage[
  paperwidth=6in, paperheight=9in, inner=0.875in, outer=0.75in, top=0.75in, bottom=0.75in
]{geometry}

% German language support
\usepackage[ngerman]{babel}

% Typography
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{palatino}
\usepackage{microtype}
\emergencystretch=1em
\usepackage{setspace}
\setstretch{1.15}

% Graphics
\usepackage{graphicx}
\graphicspath{{../figures/}{../figures/book/}}

% Links (hidden for print)
\usepackage{xcolor}
\usepackage[hidelinks, bookmarks=false]{hyperref}
\hypersetup{
  pdftitle={Die Simulation namens Ich},
  pdfauthor={Matthias Gruber},
  pdfsubject={Bewusstsein, Berechnung und Kosmos},
}

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
\fancyhead[LE]{\small\itshape Die Simulation namens Ich}
\fancyhead[RO]{\small\itshape\leftmark}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}

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
\renewcommand{\lightrulewidth}{0.8pt}
\usepackage{longtable}
\usepackage{array}
\usepackage{tabularx}

% Figure placement
\usepackage{float}

% Landscape pages
\usepackage{pdflscape}
\renewcommand{\textfraction}{0.1}
\renewcommand{\topfraction}{0.9}
\renewcommand{\bottomfraction}{0.9}

% Blank pages truly blank
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
{\Huge\bfseries Die Simulation\\[0.3cm] namens Ich\par}
\end{center}
\cleardoublepage

% ---- Full title page (recto) ----
\vspace*{2in}
\begin{center}
{\Huge\bfseries Die Simulation\\[0.3cm] namens Ich\par}
\vspace{0.8cm}
{\Large Die Architektur von\\[0.2cm] Bewusstsein, Berechnung und Kosmos\par}
\vspace{2cm}
{\large Matthias Gruber\par}
\end{center}
\clearpage

% ---- Copyright page (verso of title) ----
\thispagestyle{empty}
\vspace*{\fill}
{\small
\noindent \textcopyright\ 2026 Matthias Gruber. Alle Rechte vorbehalten.\par
\vspace{0.5cm}
\noindent Kein Teil dieser Publikation darf ohne vorherige schriftliche Genehmigung
des Autors reproduziert, verteilt oder übertragen werden, außer für kurze Zitate
in Rezensionen und bestimmte nichtkommerzielle Nutzungen, die das Urheberrecht erlaubt.\par
\vspace{0.5cm}
\noindent ISBN: [TBD]\par
\vspace{0.5cm}
\noindent Erste Ausgabe, 2026\par
\vspace{0.5cm}
\noindent www.matthiasgruber.com\par
}
\cleardoublepage

% ---- Dedication page (recto) ----
\thispagestyle{empty}
\vspace*{3in}
\begin{center}
\textit{Für alle, die sich je gefragt haben, warum sich irgendetwas nach irgendetwas anfühlt.}
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


def main():
    tex_file = os.path.join(OUTPUT_DIR, "book-manuscript-de.tex")
    pdf_file = os.path.join(OUTPUT_DIR, "book-manuscript-de.pdf")

    print("Reading German manuscript...")
    with open(MANUSCRIPT, 'r', encoding='utf-8') as f:
        md_text = f.read()

    print("Converting to LaTeX...")
    body = markdown_to_latex(md_text)

    print("Building document...")
    document = build_latex_document(body)

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
    r1 = subprocess.run(
        ['pdflatex', '-interaction=nonstopmode', '-output-directory', OUTPUT_DIR, tex_file],
        capture_output=True, cwd=OUTPUT_DIR, timeout=120
    )

    print("Compiling PDF (pass 2 for TOC)...")
    r2 = subprocess.run(
        ['pdflatex', '-interaction=nonstopmode', '-output-directory', OUTPUT_DIR, tex_file],
        capture_output=True, cwd=OUTPUT_DIR, timeout=120
    )

    if os.path.exists(pdf_file):
        size_mb = os.path.getsize(pdf_file) / (1024 * 1024)
        print(f"\nSUCCESS: {pdf_file} ({size_mb:.1f} MB)")

        # Copy to Windows desktop
        win_path = "/mnt/c/Users/Matthias/Desktop/book-manuscript-de.pdf"
        try:
            shutil.copy2(pdf_file, win_path)
            print(f"Copied to: {win_path}")
        except Exception as e:
            print(f"Note: Could not copy to Windows desktop: {e}")
    else:
        print(f"\nFAILED - checking log...")
        log_path = tex_file.replace('.tex', '.log')
        if os.path.exists(log_path):
            with open(log_path, 'r', errors='replace') as f:
                log = f.read()
            errors = [l for l in log.split('\n') if l.startswith('!')]
            for e in errors[:10]:
                print(f"  ERROR: {e}")


if __name__ == '__main__':
    main()
