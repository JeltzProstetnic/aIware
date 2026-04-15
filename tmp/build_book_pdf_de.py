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

MANUSCRIPT = "/home/jeltz/aIware/pop-sci/book-manuscript-de.md"
FIGURES_DIR = "/home/jeltz/aIware/figures"
OUTPUT_DIR = "/home/jeltz/aIware/pop-sci"

# Edition-specific configuration
EDITIONS = {
    "us": {
        "label": "DE Paperback 6\"×9\" (KDP)",
        "suffix": "",
        "geometry": r"paperwidth=6in, paperheight=9in, inner=0.875in, outer=0.75in, top=0.75in, bottom=0.75in",
        "geometry_comment": "% Trim size: 6\" x 9\" (KDP-Taschenbuch)",
        "gutter_note": "Bundsteg für ~270-Seiten-Buch",
        "isbn_line": r"\noindent ISBN: 9798257520600\par",
        "edition_line": r"\noindent Erste deutsche Ausgabe, 2026\par",
    },
    "us-hc": {
        "label": "DE Hardcover 6\"×9\" (KDP)",
        "suffix": "-hc",
        "geometry": r"paperwidth=6in, paperheight=9in, inner=0.875in, outer=0.75in, top=0.75in, bottom=0.75in",
        "geometry_comment": "% Trim size: 6\" x 9\" (KDP-Hardcover)",
        "gutter_note": "Bundsteg für ~270-Seiten-Buch",
        "isbn_line": r"\noindent ISBN: 9798257524424 (hardcover)\par",
        "edition_line": r"\noindent Erste deutsche Ausgabe, 2026\par",
    },
    "eu": {
        "label": "DE European 15.5×23cm (IngramSpark)",
        "suffix": "-eu",
        "geometry": r"paperwidth=155mm, paperheight=230mm, inner=22mm, outer=19mm, top=19mm, bottom=19mm",
        "geometry_comment": "% Trim size: 15.5 x 23 cm (Europäisches Taschenbuch)",
        "gutter_note": "Bundsteg für ~270-Seiten-Buch",
        "isbn_line": r"",
        "edition_line": r"\noindent Erste deutsche Ausgabe, 2026\par",
    },
}

# Figure insertion points: insert AFTER these line patterns
FIGURE_INSERTIONS = {
    # Figure 1: Now embedded directly in the markdown (Ch2, "Your Brain's Four Representations")
    # so no FIGURE_INSERTIONS entry needed — avoids duplication.
    # Figure 2: Also embedded directly in the markdown (Ch2, "The Real Side and the Virtual Side")
    # so no FIGURE_INSERTIONS entry needed — avoids duplication.
    # Figure 3: Nach "Bewusstsein ist kein Lichtschalter. Es ist ein Dimmer."
    "Bewusstsein ist kein Lichtschalter": {
        "file": "figure3-phenomenological-content-bw-de.png",
        "caption": "Phänomenaler Gehalt im Verlauf eines Morgens. Routinehandlungen erzeugen "
                   "niedrigen phänomenalen Gehalt (Autopilot). Auffällige Ereignisse (Bedrohungen, "
                   "soziale Signale) erzeugen hohen phänomenalen Gehalt. Bewusstsein verfolgt, "
                   "was zählt, nicht alles.",
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
    """Convert a single table cell's content: escape LaTeX chars, then apply inline formatting.
    Also inserts explicit soft hyphens into long German compounds that don't hyphenate
    automatically inside narrow tabularx columns.
    """
    text = escape_latex(text)
    text = convert_inline(text)
    # Soft hyphen insertion for stubborn long German compounds in table cells
    # \- is LaTeX's discretionary hyphen — breaks only when needed
    soft_hyphens = {
        'Kritisch/überkritisch': r'Kritisch/\-überkritisch',
        'Selbstbewusstsein': r'Selbst\-be\-wusst\-sein',
        'Bewegungsverarbeitung': r'Bewegungs\-ver\-ar\-bei\-tung',
        'Bewegungswahrnehmung': r'Be\-we\-gungs\-wahr\-neh\-mung',
        'Bewegungsgrenzen': r'Be\-we\-gungs\-gren\-zen',
        'Skalenverarbeitung': r'Ska\-len\-ver\-ar\-bei\-tung',
        'Formverarbeitung': r'Form\-ver\-ar\-bei\-tung',
        'Objektunterscheidung': r'Ob\-jekt\-un\-ter\-schei\-dung',
        'Szenenkonstruktion': r'Sze\-nen\-kon\-struk\-ti\-on',
        'Textursegmentierung': r'Tex\-tur\-seg\-men\-tie\-rung',
        'Texturwahrnehmung': r'Tex\-tur\-wahr\-neh\-mung',
        'Richtungskodierung': r'Rich\-tungs\-ko\-die\-rung',
        'Gesichtserkennung': r'Ge\-sichts\-er\-ken\-nung',
        'Wiederholungsstruktur': r'Wie\-der\-ho\-lungs\-struk\-tur',
        'kaleidoskopische': r'ka\-lei\-do\-sko\-pi\-sche',
        'Halluzinationen': r'Hal\-lu\-zi\-na\-tio\-nen',
    }
    for word, broken in soft_hyphens.items():
        text = text.replace(word, broken)
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
    lines.append('{\\scriptsize')
    lines.append('\\noindent')
    lines.append('\\begin{tabularx}{\\linewidth}{>{\\hsize=0.7\\hsize}Y Y Y}')
    lines.append('\\toprule')
    left_headers = ['\\textbf{Areal}',
                    '\\textbf{Rezeptives Feld}', '\\textbf{Normale Funktion}']
    lines.append(' & '.join(left_headers) + ' \\\\')
    lines.append('\\midrule')
    for row in data_rows:
        lines.append(f'{row[0]} & {row[1]} & {row[2]} \\\\[3pt]')
    lines.append('\\bottomrule')
    lines.append('\\end{tabularx}')
    lines.append('}')

    # === RIGHT PAGE (recto): Area, Psychedelic signature ===
    lines.append('\\clearpage')
    lines.append('')
    lines.append('{\\scriptsize')
    lines.append('\\noindent')
    lines.append('\\begin{tabularx}{\\linewidth}{>{\\hsize=0.7\\hsize}Y Y}')
    lines.append('\\toprule')
    right_headers = ['\\textbf{Areal}', '\\textbf{Psychedelische Signatur}']
    lines.append(' & '.join(right_headers) + ' \\\\')
    lines.append('\\midrule')
    for row in data_rows:
        lines.append(f'{row[0]} & {row[3]} \\\\[3pt]')
    lines.append('\\bottomrule')
    lines.append('\\end{tabularx}')
    lines.append('}')
    lines.append('')

    return '\n'.join(lines)


def convert_landscape_table(table_lines, data_start, header_cells, num_cols, alignments):
    """Convert a wide table to a sideways rotation on a normal portrait page.
    Uses \\rotatebox{90}{...} around a fixed-width minipage so the content
    stays within the physical page bounds (KDP preflight-safe, unlike pdflscape
    which stores content at rotated coordinates that exceed page width)."""
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
            col_types.append('Z')
        elif a == 'r':
            col_types.append(r'>{\raggedleft\arraybackslash\hspace{0pt}}X')
        else:
            col_types.append('Y')
    col_spec = ' '.join(col_types)

    lines = []
    lines.append('')
    lines.append('\\clearpage')
    lines.append('\\thispagestyle{plain}')
    lines.append('\\vspace*{\\fill}')
    lines.append('\\begin{center}')
    lines.append('\\rotatebox{90}{%')
    # Minipage width = landscape text area length = portrait textheight (~7.5in)
    lines.append('\\begin{minipage}{7.25in}%')
    lines.append('{\\small')
    lines.append('\\noindent')
    lines.append('\\begin{tabularx}{\\linewidth}{' + col_spec + '}')
    lines.append('\\toprule')
    converted_headers = ['\\textbf{' + convert_table_cell(c) + '}' for c in header_cells]
    lines.append(' & '.join(converted_headers) + ' \\\\')
    lines.append('\\midrule')
    for row in data_rows:
        lines.append(' & '.join(row) + ' \\\\[6pt]')
    lines.append('\\bottomrule')
    lines.append('\\end{tabularx}')
    lines.append('}')
    lines.append('\\end{minipage}%')
    lines.append('}')
    lines.append('\\end{center}')
    lines.append('\\vspace*{\\fill}')
    lines.append('\\clearpage')
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

    # Map alignments to tabularx column types (Y/Z allow hyphenation of German compounds)
    col_types = []
    for a in alignments[:num_cols]:
        if a == 'c':
            col_types.append('Z')
        elif a == 'r':
            col_types.append(r'>{\raggedleft\arraybackslash\hspace{0pt}}X')
        else:
            col_types.append('Y')
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
    # Must have 4 columns (Areal, Rezeptives Feld, Normale Funktion, Psychedelische Signatur)
    # The Chapter 6 condensed version has only 3 columns and should NOT be a spread.
    if 'Psychedelische Signatur' in header_text and 'Rezeptives Feld' in header_text:
        return convert_spread_table(table_lines, data_start, header_cells, num_cols)

    # Wide tables → rotate to landscape for readability
    # Applies to: the 6-col Fünf-Klassen comparison (Berechnet/Reduzierbar)
    #             the 4-col Wolfram classes table (Wolfram-Klasse header)
    if (num_cols >= 5 and ('Berechnet' in header_text or 'Reduzierbar' in header_text)) \
            or 'Wolfram-Klasse' in header_text:
        return convert_landscape_table(table_lines, data_start, header_cells, num_cols, alignments)

    # Detect narrow five-class mapping → use footnotesize
    if 'Fünf-Klassen' in header_text or 'Was sich änderte' in header_text:
        return convert_fiveclass_table(table_lines, data_start, header_cells, num_cols, alignments)

    # Ensure alignment list matches column count
    while len(alignments) < num_cols:
        alignments.append('l')
    alignments = alignments[:num_cols]

    # Map alignments to tabularx column types (Y/Z allow hyphenation of German compounds)
    col_types = []
    for a in alignments:
        if a == 'c':
            col_types.append('Z')
        elif a == 'r':
            col_types.append(r'>{\raggedleft\arraybackslash\hspace{0pt}}X')
        else:
            col_types.append('Y')

    col_spec = ' '.join(col_types)

    lines = []
    lines.append('')

    # German tables use \footnotesize so long compounds fit in narrow columns
    lines.append('{\\footnotesize')

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

        # Skip the title (# Die Simulation namens Ich) - handled in preamble
        if stripped.startswith('# Die Simulation namens Ich') and not stripped.startswith('## '):
            i += 1
            continue

        # Skip author line
        if stripped == '**Matthias Gruber**':
            i += 1
            continue

        # Skip German dedication paragraph — handled in preamble front matter
        if stripped.startswith('*Gerichtet an alle, die sich je gefragt haben'):
            i += 1
            continue

        # Skip table of contents section
        if stripped == '## Inhalt':
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

        # Chapter headings (## Kapitel N: Titel oder ## Vorwort / ## Coda / ## Anhang ...)
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

            # Clean up title for LaTeX
            title = convert_inline(escape_latex(raw_title))

            # Use \chapter* for non-numbered chapters
            if any(raw_title.startswith(w) for w in [
                'Bewusstsein und Kosmos', 'Vorwort', 'Der Autor',
                'Coda', 'Danksagung', 'Anmerkungen', 'Anhang'
            ]):
                # For titles with em-dash subtitles, use shortened form in TOC
                # and running header — keep full title in chapter heading.
                if ' — ' in raw_title:
                    short_raw = raw_title.split(' — ')[0]
                    toc_title = convert_inline(escape_latex(short_raw))
                else:
                    toc_title = title
                latex_lines.append(f'\\chapter*{{{title}}}')
                latex_lines.append(f'\\addcontentsline{{toc}}{{chapter}}{{{toc_title}}}')
                latex_lines.append(f'\\markboth{{{toc_title}}}{{}}')
            else:
                # Extract chapter number and title
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
            # Line-break overrides for long German section titles that overflow
            title = title.replace(
                'Warum das Gehirn die Fähigkeit zur Selbstmodellierung hat',
                'Warum das Gehirn die Fähigkeit\\\\zur Selbstmodellierung hat'
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
\usepackage[ngerman]{babel}    % German hyphenation and typography
\renewcommand{\contentsname}{Inhalt}
\renewcommand{\chaptername}{Kapitel}
\usepackage{palatino}          % Elegant serif font
\usepackage{microtype}         % Better typography (protrusion + expansion)
% German typesetting: loose tolerance + generous stretch for long compounds
\tolerance=3000
\emergencystretch=4em
\hyphenpenalty=50
\hbadness=10000                % suppress underfull-hbox warnings
\usepackage{ragged2e}          % \RaggedRight for hyphenated tabularx cells
% Manual hyphenation hints for stubborn long German compounds
\hyphenation{%
  Bio-me-di-zi-ni-sche Bio-me-di-zi-ni-schen%
  Si-mu-la-ti-ons-ba-sier-ter Si-mu-la-ti-ons-ba-sier-ten%
  Sach-ver-stän-di-ger Sach-ver-stän-di-gen%
  Pro-zess-ma-na-ge-ment Pro-jekt-ma-na-ge-ment%
  Soft-ware-ent-wick-lung%
  Quan-ten-me-cha-ni-ker%
  Sym-me-trie-for-scher%
  KI-Trans-for-ma-ti-on%
  Selbst-re-fe-ren-zi-ell Selbst-re-fe-ren-zi-el-le%
  Selbst-be-wusst-sein Selbst-mo-del-lie-rung%
  In-for-ma-ti-ons-ver-ar-bei-tung%
  Pho-to-re-zep-tor-zel-len%
  Be-wusst-seins-for-schung%
  Neu-ro-wis-sen-schaft Neu-ro-wis-sen-schaf-ten Neu-ro-wis-sen-schaft-ler%
  Wahr-neh-mungs-phi-lo-soph%
  Be-we-gungs-ver-ar-bei-tung Be-we-gungs-wahr-neh-mung%
  Be-we-gungs-gren-zen Be-we-gungs-grö-ße%
  Wie-der-ho-lungs-struk-tur Wie-der-ho-lend%
  Ska-len-ver-ar-bei-tung Ska-len-in-va-ri-anz%
  Ob-jekt-un-ter-schei-dung Ob-jekt-in-va-ri-ant%
  Szenen-kon-struk-ti-on%
  Tex-tur-seg-men-tie-rung Tex-tur-wahr-neh-mung%
  Form-ver-ar-bei-tung Form-kon-stan-ten%
  Kan-ten-er-ken-nung%
  Kon-tur-in-te-gra-ti-on%
  Ge-sichts-er-ken-nung%
  Ge-schwin-dig-keits-%
  Rich-tungs-ko-die-rung%
  Hal-lu-zi-na-ti-o-nen%
  Psy-che-de-lisch Psy-che-de-li-sche Psy-che-de-li-schen%
  ka-lei-do-sko-pisch ka-lei-do-sko-pi-sche%
  at-men-de schim-mern-de%
  in-te-r-agie-ren-de per-sis-ten-te%
  be-we-gungs-ab-ge-stimmt%
  dar-stell-bar un-be-kannt%
}
\usepackage{setspace}
\setstretch{1.15}              % Standard book leading

% Graphics
\usepackage{graphicx}
\graphicspath{{../figures/}{../figures/book/}}

% Links (hidden for print - no colored text)
\usepackage{xcolor}
\usepackage[hidelinks, bookmarks=false]{hyperref}
\hypersetup{
  pdftitle={Die Simulation namens Ich},
  pdfauthor={Matthias Gruber},
  pdfsubject={Die Architektur von Bewusstsein, Berechnung und Kosmos},
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
\renewcommand{\lightrulewidth}{0.8pt}   % KDP minimum line weight is 0.75pt
\usepackage{longtable}
\usepackage{array}
\usepackage{tabularx}
% Hyphenating column types (long German compound words in tables)
% Force hyphenation: hyphenpenalty=0, exhyphenpenalty=0 lets long compounds break
\newcolumntype{Y}{>{\RaggedRight\arraybackslash\hyphenpenalty=0\exhyphenpenalty=0\hspace{0pt}}X}
\newcolumntype{Z}{>{\centering\arraybackslash\hspace{0pt}}X}
% Tighter table cell padding to give more room to content
\setlength{\tabcolsep}{4pt}

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
\noindent Kein Teil dieser Veröffentlichung darf ohne vorherige schriftliche
Genehmigung des Autors in irgendeiner Form oder mit irgendwelchen Mitteln
reproduziert, verbreitet oder übertragen werden, ausgenommen kurze Zitate
in Rezensionen und bestimmte nichtkommerzielle Nutzungen, die das
Urheberrecht gestattet.\par
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
\begin{minipage}{0.75\textwidth}
\centering
\textit{Gerichtet an alle, die sich je gefragt haben, warum wir unser Selbst
wahrnehmen können, warum sich Dinge nach etwas anfühlen, warum wir uns
gedanklich alles Mögliche vorstellen können, und wie dieses Kino im Kopf
zustandekommt.}
\end{minipage}
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
    tex_file = os.path.join(OUTPUT_DIR, f"book-manuscript-de{suffix}.tex")
    pdf_file = os.path.join(OUTPUT_DIR, f"book-manuscript-de{suffix}.pdf")
    win_name = f"book-manuscript-de{suffix}.pdf"

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
    parser.add_argument('--edition', choices=['us', 'us-hc', 'eu', 'all'], default='us',
                        help='Edition to build: us (paperback), us-hc (hardcover), eu (IngramSpark), all (all three)')
    args = parser.parse_args()

    print("Reading manuscript...")
    with open(MANUSCRIPT, 'r', encoding='utf-8') as f:
        md_text = f.read()

    print("Converting to LaTeX...")
    body = markdown_to_latex(md_text)

    editions = ['us', 'us-hc', 'eu'] if args.edition == 'all' else [args.edition]
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
