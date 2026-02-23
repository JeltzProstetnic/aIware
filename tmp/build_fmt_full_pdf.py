#!/usr/bin/env python3
"""Build FMT full paper from .md to .tex to .pdf.

Pipeline: paper/full/four-model-theory-full.md → paper/full/biorxiv/paper.tex → paper/full/biorxiv/paper.pdf
Implements formatting rules from paper/full/four-model-theory-full.formatting-rules.md.
"""

import os
import re
import sys
import subprocess
import shutil

REPO_ROOT = "/home/jeltz/aIware"
MD_PATH = os.path.join(REPO_ROOT, "paper/full/four-model-theory-full.md")
TEX_PATH = os.path.join(REPO_ROOT, "paper/full/biorxiv/paper.tex")
PDF_PATH = os.path.join(REPO_ROOT, "paper/full/biorxiv/paper.pdf")
BIB_PATH = os.path.join(REPO_ROOT, "paper/full/biorxiv/references.bib")
OUTPUT_DIR = os.path.join(REPO_ROOT, "paper/full/biorxiv")

# ---------------------------------------------------------------------------
# Citation key mapping: (author_display, year) → BibTeX key
# Built from references.bib. Keys follow: LastnameYear (first author).
# ---------------------------------------------------------------------------

FMT_CITATION_KEYS = {
    # Single authors
    ("Aaronson", "2014"): "Aaronson2014",
    ("Albantakis", "2023"): "Albantakis2023",
    ("Aldrich", "1987"): "Aldrich1987",
    ("Alkire", "2000"): "Alkire2000",
    ("Anton", "1899"): "Anton1899",
    ("Baars", "1988"): "Baars1988",
    ("Bayne", "2010"): "Bayne2010",
    ("Beggs", "2003"): "Beggs2003",
    ("Birch", "2025"): "Birch2025",
    ("Block", "1995"): "Block1995",
    ("Block", "2007"): "Block2007",
    ("Boly", "2012"): "Boly2012",
    ("Brodmann", "1909"): "Brodmann1909",
    ("Butlin", "2023"): "Butlin2023",
    ("Butlin", "2025"): "Butlin2025",
    ("Casali", "2013"): "Casali2013",
    ("Casarotto", "2016"): "Casarotto2016",
    ("Chalmers", "1995"): "Chalmers1995",
    ("Chalmers", "1996"): "Chalmers1996",
    ("Chalmers", "2016"): "Chalmers2016",
    ("Chalmers", "2018"): "Chalmers2018",
    ("Coleman", "2014"): "Coleman2014",
    ("Corlett", "2011"): "Corlett2011",
    ("Cybenko", "1989"): "Cybenko1989",
    ("Dennett", "1991"): "Dennett1991",
    ("Engel", "2001"): "Engel2001",
    ("Fleming", "2024"): "Fleming2024",
    ("Frankish", "2016"): "Frankish2016",
    ("Fries", "2005"): "Fries2005",
    ("Fries", "2015"): "Fries2015",
    ("Friston", "2010"): "Friston2010",
    ("Gazzaniga", "1962"): "Gazzaniga1962",
    ("Gazzaniga", "1965"): "Gazzaniga1965",
    ("Gazzaniga", "2000"): "Gazzaniga2000",
    ("Goff", "2019"): "Goff2019",
    ("Gray", "1989"): "Gray1989",
    ("Graziano", "2013"): "Graziano2013",
    ("Graziano", "2024"): "Graziano2024",
    ("Gruber", "2015"): "Gruber2015",
    ("Gruber", "2026"): "Gruber2026intelligence",
    ("Hinton", "1986"): "Hinton1986",
    ("Hornik", "1989"): "Hornik1989",
    ("Huxley", "1874"): "Huxley1874",
    ("Jackson", "1982"): "Jackson1982",
    ("James", "1890"): "James1890",
    ("Kim", "1993"): "Kim1993",
    ("Kuhn", "1962"): "Kuhn1962",
    ("LaBerge", "1985"): "LaBerge1985",
    ("Lamme", "2006"): "Lamme2006",
    ("Lamme", "2010"): "Lamme2010",
    ("Lashley", "1950"): "Lashley1950",
    ("Levine", "1983"): "Levine1983",
    ("Libet", "1985"): "Libet1985",
    ("Long", "2024"): "Long2024",
    ("Metzinger", "2003"): "Metzinger2003",
    ("Metzinger", "2009"): "Metzinger2009",
    ("Monti", "2010"): "Monti2010",
    ("Nagel", "1974"): "Nagel1974",
    ("Owen", "2006"): "Owen2006",
    ("Pribram", "1991"): "Pribram1991",
    ("Revonsuo", "1999"): "Revonsuo1999",
    ("Rosenthal", "2005"): "Rosenthal2005",
    ("Schwitzgebel", "2025"): "Schwitzgebel2025",
    ("Seth", "2021"): "Seth2021",
    ("Strawson", "2006"): "Strawson2006",
    ("Tegmark", "2000"): "Tegmark2000",
    ("Tononi", "2004"): "Tononi2004",
    ("Treisman", "1996"): "Treisman1996",
    ("Wegner", "2002"): "Wegner2002",
    ("Weiskrantz", "1986"): "Weiskrantz1986",
    ("Wolfram", "2002"): "Wolfram2002",
    # Multi-author (first-author key)
    ("Algom", "2026"): "AlgomShriki2026",
    ("Algom & Shriki", "2026"): "AlgomShriki2026",
    ("Carhart-Harris", "2012"): "CarhartHarris2012",
    ("Carhart-Harris", "2014"): "CarhartHarris2014",
    ("Carhart-Harris", "2016"): "CarhartHarris2016",
    ("COGITATE", "2025"): "COGITATE2025",
    ("COGITATE Consortium", "2025"): "COGITATE2025",
    ("Dehaene", "2011"): "Dehaene2011",
    ("Dehaene & Changeux", "2011"): "Dehaene2011",
    ("Doerig", "2019"): "Doerig2019",
    ("Ellia", "2025"): "Ellia2025",
    ("Ellia & Tsuchiya", "2025"): "Ellia2025",
    ("Gomez-Marin", "2025"): "GomezMarin2025",
    ("Gomez-Marin & Seth", "2025"): "GomezMarin2025",
    ("Güntürkün", "2016"): "Gunturkun2016",
    ("Gunturkun", "2016"): "Gunturkun2016",
    ("Güntürkün & Bugnyar", "2016"): "Gunturkun2016",
    ("Hengen", "2025"): "HengenShew2025",
    ("Hengen & Shew", "2025"): "HengenShew2025",
    ("IIT-Concerned", "2025"): "IITConcerned2025",
    ("Kirkeby-Hinrup", "2025"): "KirkebyHinrup2025",
    ("Klüver", "1966"): "Kluver1966",
    ("Kluver", "1966"): "Kluver1966",
    ("Lau", "2011"): "Lau2011",
    ("Lau & Rosenthal", "2011"): "Lau2011",
    ("Llinas", "1993"): "Llinas1993",
    ("Llinás", "1993"): "Llinas1993",
    ("Llinás", "1998"): "Llinas1998",
    ("Melloni", "2023"): "Melloni2023",
    ("Milinkovic", "2025"): "Milinkovic2025",
    ("NatNeuro", "2025"): "NatNeuro2025IIT",
    ("Penrose", "1994"): "PenroseHameroff1994",
    ("Penrose & Hameroff", "1994"): "PenroseHameroff1994",
    ("Pinto", "2017"): "Pinto2017",
    ("Priesemann", "2013"): "Priesemann2013",
    ("Priesemann", "2014"): "Priesemann2014",
    ("Reinders", "2003"): "Reinders2003",
    ("Reinders", "2008"): "Reinders2008",
    ("Rodriguez", "1999"): "Rodriguez1999",
    ("Schartner", "2017"): "Schartner2017",
    ("Schurger", "2012"): "Schurger2012",
    ("Singer", "1995"): "Singer1995",
    ("Singer & Gray", "1995"): "Singer1995",
    ("Tagliazucchi", "2012"): "Tagliazucchi2012",
    ("Tagliazucchi", "2016"): "Tagliazucchi2016",
    ("Timmermann", "2019"): "Timmermann2019",
    ("Timmermann", "2023"): "Timmermann2023",
    ("Tononi, Albantakis", "2025"): "TononiAlbantakis2025",
    ("Treisman", "1980"): "Treisman1980",
    ("Treisman & Gelade", "1980"): "Treisman1980",
    ("Van Rullen", "2003"): "VanRullen2003",
    ("Van Rullen & Koch", "2003"): "VanRullen2003",
    ("von Neumann", "1932"): "vonNeumann1932",
    ("Wigner", "1961"): "Wigner1961",
    ("Zurek", "2003"): "Zurek2003",
    ("Anthropic", "2025"): "Anthropic2025",
    # Display form variants
    ("Dehaene-Naccache", "2011"): "DehaeneNaccache2011",
    ("DehaeneNaccache", "2011"): "DehaeneNaccache2011",
    # Frontiers/Acta special entries (not real citations in bib)
    ("Frontiers in Psychology", "2025"): None,
    ("Acta Analytica", "2024"): None,
    # Fallback forms: regex-misparses of multi-word/org names and CamelCase splits
    ("Consortium", "2025"): "COGITATE2025",    # COGITATE Consortium
    ("Concerned", "2025"): "IITConcerned2025", # IIT-Concerned
    ("Psychology", "2025"): None,               # Frontiers in Psychology
    ("Plenz", "2003"): "Beggs2003",            # Beggs and Plenz
    ("Clelland", "1986"): "Hinton1986",        # McClelland split
    ("Tsuchiya", "2025"): "Ellia2025",         # Ellia and Tsuchiya
    ("Shea", "2024"): "Fleming2024",           # Fleming and Shea
    ("Berge", "1985"): "LaBerge1985",          # LaBerge split
    ("Shew", "2025"): "HengenShew2025",        # Hengen and Shew
    ("Shriki", "2025"): "AlgomShriki2026",     # Algom and Shriki (year variant)
    ("Shriki", "2026"): "AlgomShriki2026",     # Algom and Shriki
    ("Anthropic", "2026"): "Anthropic2025",    # Safety: old year in case of stale refs
}


def generate_preamble():
    """Generate LaTeX preamble matching formatting rules."""
    return r"""\documentclass[12pt]{article}

% === Packages ===
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{xcolor}
\usepackage[round]{natbib}
\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=blue!60!black,urlcolor=blue!60!black]{hyperref}
\usepackage{microtype}
\usepackage{setspace}
\usepackage{parskip}

% === Formatting ===
\onehalfspacing
"""


def _lookup_key(author, year, keys):
    """Look up a citation key for an author-year pair."""
    # Direct lookup
    if (author, year) in keys:
        return keys[(author, year)]
    # Strip "et al." suffix
    author_clean = re.sub(r'\s+et\s+al\.?$', '', author).strip()
    if (author_clean, year) in keys:
        return keys[(author_clean, year)]
    # Try with & variant (handles both "X & Y" and "X and Y")
    for sep in (" & ", " and "):
        if sep in author_clean:
            # Try the full "X & Y" form in keys (normalize "and" to "&")
            normalized = author_clean.replace(" and ", " & ")
            if (normalized, year) in keys:
                return keys[(normalized, year)]
            # Try first author only
            first = author_clean.split(sep)[0].strip()
            if (first, year) in keys:
                return keys[(first, year)]
    # Try without accents
    author_ascii = author_clean.replace("é", "e").replace("ü", "u").replace("ö", "o")
    if (author_ascii, year) in keys:
        return keys[(author_ascii, year)]
    # Fallback: construct from first author + year
    key_author = re.sub(r'[^A-Za-z]', '', author_clean.split(",")[0].split(" ")[-1] if "," in author_clean else author_clean.split()[-1] if author_clean.split() else author_clean)
    return key_author + year


def convert_citations(text, keys):
    """Convert markdown-style citations to natbib LaTeX commands.

    Handles:
    - (Author, Year) → \\citep{Key}
    - (Author, Year; Author, Year) → \\citep{Key1,Key2}
    - Author (Year) → \\citet{Key}
    - Author's (Year) → \\citeauthor{Key}'s \\citeyearpar{Key}
    - (Author et al., Year) → \\citep{Key}
    - Author (Year, Year) → \\citet{Key1,Key2}
    """
    result = text

    # Unicode-aware character classes for author names
    _L = r'a-zà-öø-ÿ'
    _U = r'A-ZÀ-ÖØ-Þ'
    _S = r'[^\S\n]'      # whitespace but NOT newline — prevents cross-line matching
    # Surname: handles normal (Chalmers) and CamelCase (McClelland, LaBerge)
    _SURNAME_NORMAL = rf'[{_U}][{_L}]{{2,}}'
    _SURNAME_CAMEL = rf'[{_U}][{_L}]{{1,}}(?:[{_U}][{_L}]{{2,}})+'
    _SURNAME = rf'(?:{_SURNAME_CAMEL}|{_SURNAME_NORMAL})(?:-[{_U}][{_L}]{{2,}})*'
    _PARTICLE = rf'(?:(?:von|van|de|di|le|la|du|el|al){_S}+)'
    _NAME = rf'(?:{_PARTICLE})?{_SURNAME}'
    _AND = rf'(?:&|and)'  # both "X & Y" and "X and Y"
    _AUTHORS_AMP = rf'{_NAME}(?:(?:{_S}+(?:{_AND}{_S}+)?(?:{_PARTICLE})?{_SURNAME}))*(?:{_S}+et{_S}+al\.?)?'

    # --- Pass 1: Possessive citations: Author's (Year) ---
    def replace_possessive(m):
        author = m.group(1)
        year = m.group(2)
        key = _lookup_key(author, year, keys)
        if key is None:
            return m.group(0)
        return f"\\citeauthor{{{key}}}'s \\citeyearpar{{{key}}}"

    result = re.sub(
        rf"({_NAME}(?:{_S}+(?:{_AND}{_S}+)?{_SURNAME})*)'s{_S}+\((\d{{4}}[a-z]?)\)",
        replace_possessive,
        result
    )

    # --- Pass 2: Textual citations: Author (Year) or Author (Year, Year) ---
    def replace_textual(m):
        author = m.group(1)
        years_str = m.group(2)
        years = [y.strip() for y in years_str.split(",")]
        cite_keys = []
        for y in years:
            key = _lookup_key(author, y, keys)
            if key is not None:
                cite_keys.append(key)
        if not cite_keys:
            return m.group(0)
        return f"\\citet{{{','.join(cite_keys)}}}"

    # Use [^\S\n]+ to prevent matching across line boundaries
    result = re.sub(
        rf"(?<!\()({_AUTHORS_AMP}){_S}+\((\d{{4}}[a-z]?(?:{_S}*,{_S}*\d{{4}}[a-z]?)*)\)",
        replace_textual,
        result
    )

    # --- Pass 3: Parenthetical citations: (Author, Year; ...) ---
    def replace_parenthetical(m):
        inner = m.group(1)
        if not re.search(r'\d{4}', inner):
            return m.group(0)

        parts = [p.strip() for p in inner.split(";")]
        cite_keys = []
        non_citation_parts = []

        for part in parts:
            cm = re.search(
                rf'({_NAME}'
                rf'(?:(?:[\s,]+(?:&\s+)?(?:{_PARTICLE})?{_SURNAME}))*'
                rf'(?:{_S}+et{_S}+al\.?)?)'
                r'(?:,\s*|\s+)'
                r'(\d{4}[a-z]?)',
                part
            )
            if cm:
                author = cm.group(1).strip().rstrip(",")
                year = cm.group(2)
                key = _lookup_key(author, year, keys)
                if key is not None:
                    cite_keys.append(key)
                else:
                    non_citation_parts.append(part)
                rest = part[cm.end():]
                extra_years = re.findall(r',\s*(\d{4}[a-z]?)', rest)
                for ey in extra_years:
                    ekey = _lookup_key(author, ey, keys)
                    if ekey is not None:
                        cite_keys.append(ekey)
                # Check for meaningful non-citation text
                prefix = part[:cm.start()].strip()
                prefix_clean = re.sub(r'(?:for\s+\w+,?\s*)?(?:though\s+)?(?:see\s+(?:also\s+)?)?$', '', prefix).strip()
                if prefix_clean:
                    non_citation_parts.append(prefix_clean)
            else:
                non_citation_parts.append(part)

        if cite_keys and not non_citation_parts:
            return f"\\citep{{{','.join(cite_keys)}}}"
        elif cite_keys:
            cite_str = f"\\citealp{{{','.join(cite_keys)}}}"
            text_parts = "; ".join(non_citation_parts)
            return f"({text_parts}; {cite_str})"
        else:
            return m.group(0)

    result = re.sub(
        r'\(([^)]*\d{4}[^)]*)\)',
        replace_parenthetical,
        result
    )

    return result


def convert_body(text):
    """Convert markdown body text to LaTeX."""
    lines = text.split("\n")
    output = []
    in_list = False
    list_type = None
    in_sublist = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Markdown pipe tables — skip entirely (LaTeX tables injected as floats)
        # Matches: | header | header | and |---|---| separator lines
        if re.match(r'^\|', line):
            i += 1
            continue

        # Bold table captions: **Table N. Title** — skip (float has its own caption)
        if re.match(r'^\*\*Table\s+\d+', line):
            i += 1
            continue

        # Horizontal rules
        if re.match(r'^---+\s*$', line):
            i += 1
            continue

        # H1 — title, skip
        if re.match(r'^#\s+', line):
            i += 1
            continue

        # H2 — section
        h2_match = re.match(r'^##\s+(?:\d+\.\s+)?(.+)$', line)
        if h2_match:
            if in_list:
                output.append(f"\\end{{{list_type}}}")
                in_list = False
            title = h2_match.group(1).strip()
            if title.lower() in ("acknowledgments", "acknowledgements",
                                  "data availability", "funding",
                                  "disclosure statement", "references"):
                if title.lower() == "references":
                    i += 1
                    continue  # References handled separately
                output.append(f"\n%{'='*77}")
                output.append(f"\\section*{{{title}}}")
                output.append(f"%{'='*77}")
            else:
                output.append(f"\n%{'='*77}")
                output.append(f"\\section{{{title}}}")
                output.append(f"%{'='*77}")
            i += 1
            continue

        # H3 — subsection
        h3_match = re.match(r'^###\s+(?:\d+\.\d+\s+)?(.+)$', line)
        if h3_match:
            if in_list:
                output.append(f"\\end{{{list_type}}}")
                in_list = False
            title = h3_match.group(1).strip()
            output.append(f"\n\\subsection{{{title}}}")
            i += 1
            continue

        # Numbered lists
        num_match = re.match(r'^(\d+)\.\s+(.+)$', line)
        if num_match:
            if not in_list:
                output.append("\\begin{enumerate}")
                in_list = True
                list_type = "enumerate"
            item_text = _convert_inline(num_match.group(2))
            output.append(f"\\item {item_text}")
            i += 1
            continue

        # Bullet lists
        bullet_match = re.match(r'^[-*]\s+(.+)$', line)
        if bullet_match:
            if not in_list:
                output.append("\\begin{itemize}")
                in_list = True
                list_type = "itemize"
            item_text = _convert_inline(bullet_match.group(1))
            output.append(f"\\item {item_text}")
            i += 1
            continue

        # Sub-bullets
        sub_match = re.match(r'^\s{2,}[-*]\s+(.+)$', line)
        if sub_match:
            if not in_sublist:
                output.append("\\begin{itemize}")
                in_sublist = True
            item_text = _convert_inline(sub_match.group(1))
            output.append(f"\\item {item_text}")
            i += 1
            continue

        if in_sublist and not re.match(r'^\s{2,}[-*]', line):
            output.append("\\end{itemize}")
            in_sublist = False

        if in_list and line.strip() == "" and (
            i + 1 >= len(lines) or not re.match(r'^(?:\d+\.|\s*[-*])\s', lines[i + 1])
        ):
            if in_sublist:
                output.append("\\end{itemize}")
                in_sublist = False
            output.append(f"\\end{{{list_type}}}")
            in_list = False

        # Markdown footnotes: [^name] reference and [^name]: definition
        if re.match(r'^\[\^(\w+)\]:', line):
            # Footnote definition — skip (handled inline)
            # Collect multi-line footnote
            while i + 1 < len(lines) and lines[i + 1].startswith("  "):
                i += 1
            i += 1
            continue

        converted = _convert_inline(line)
        output.append(converted)
        i += 1

    if in_sublist:
        output.append("\\end{itemize}")
    if in_list:
        output.append(f"\\end{{{list_type}}}")

    return "\n".join(output)


def _convert_inline(text):
    """Convert inline markdown to LaTeX."""
    result = text

    # Em dash: allow line break after em dashes (zero-width space prevents overfull lines)
    result = result.replace(" — ", "---\\hspace{0pt}")
    result = result.replace("—", "---\\hspace{0pt}")

    # Special characters
    result = re.sub(r'(?<!\\)&(?!\\)', r'\\&', result)
    result = re.sub(r'(?<!\\)%', r'\\%', result)

    # Bold + italic
    result = re.sub(r'\*\*\*(.+?)\*\*\*', r'\\textbf{\\emph{\1}}', result)

    # Bold
    result = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', result)

    # Italic (avoid false matches inside math or LaTeX)
    result = re.sub(r'(?<!\$)\*([^*\n]+?)\*(?!\$)', r'\\emph{\1}', result)

    # Inline code
    result = re.sub(r'`([^`]+)`', r'\\texttt{\1}', result)

    # Smart quotes
    result = re.sub(r'"([^"]*)"', r"``\1''", result)
    result = re.sub(r'"([^"]*)"', r"``\1''", result)

    # Section cross-refs
    result = re.sub(r'Section (\d)', r'Section~\1', result)

    # Footnote references: [^quantum] → handled specially
    def replace_footnote_ref(m):
        return ""  # Footnote text injected from definition
    # (Footnotes are injected from the formatting-rules or extracted from .md)

    # Umlaut preservation
    result = result.replace("ü", r'\"u')
    result = result.replace("ö", r'\"o')
    result = result.replace("ä", r'\"a')
    result = result.replace("å", r'\aa{}')
    result = result.replace("Φ", r"$\Phi$")
    result = result.replace("×", r"$\times$")
    result = result.replace("≈", r"$\approx$")
    result = result.replace("↑", r"$\uparrow$")
    result = result.replace("→", r"$\to$")

    # Unicode symbols used in comparison table
    result = result.replace("●", r"$\bullet$")
    result = result.replace("◐", r"$\odot$")
    result = result.replace("○", r"$\circ$")

    # Greek letters
    result = result.replace("α", r"$\alpha$")
    result = result.replace("β", r"$\beta$")
    result = result.replace("γ", r"$\gamma$")
    result = result.replace("δ", r"$\delta$")

    return result


def extract_references(md_text):
    """Extract reference entries from the .md references section."""
    refs_match = re.search(r'^## References\s*\n(.*)', md_text, re.DOTALL | re.MULTILINE)
    if not refs_match:
        # Look for reference list at end
        refs_match = re.search(r'\n\n((?:[A-Z].+?\(\d{4}\).*\n?)+)$', md_text, re.DOTALL)
        if not refs_match:
            return []

    refs_text = refs_match.group(1)
    entries = []
    current = []

    for line in refs_text.strip().split("\n"):
        line = line.strip()
        if not line:
            if current:
                entries.append("\n".join(current))
                current = []
            continue
        current.append(line)

    if current:
        entries.append("\n".join(current))

    return entries


def extract_footnotes(md_text):
    """Extract markdown footnotes [^name]: text."""
    footnotes = {}
    pattern = re.compile(r'^\[\^(\w+)\]:\s*(.+?)(?=\n\[\^|\n\n[^[\s]|\Z)', re.MULTILINE | re.DOTALL)
    for m in pattern.finditer(md_text):
        name = m.group(1)
        text = m.group(2).strip()
        # Remove continuation indentation
        text = re.sub(r'\n\s{2,}', ' ', text)
        footnotes[name] = text
    return footnotes


# ---------------------------------------------------------------------------
# LaTeX float blocks (figures and tables from the hand-maintained .tex)
# These are NOT in the .md source and must be injected at correct positions.
# ---------------------------------------------------------------------------

FLOAT_TABLE_FOUR_MODELS = r"""
\begin{table}[htbp]
\centering
\caption{The Four-Model Architecture}
\label{tab:four-models}
\begin{tabularx}{\textwidth}{lXX}
\toprule
& \textbf{Everything (world)} & \textbf{Self only} \\
\midrule
\textbf{Implicit} (learned, substrate-level) & Implicit World Model (IWM) & Implicit Self Model (ISM) \\
\textbf{Explicit} (simulated, phenomenal) & Explicit World Model (EWM) & Explicit Self Model (ESM) \\
\bottomrule
\end{tabularx}
\end{table}
"""

FLOAT_FIG_FOUR_MODELS = r"""
\begin{figure}[htbp]
\centering
\includegraphics[width=0.85\textwidth]{figure1-four-model-architecture.png}
\caption{The four-model architecture. The two orthogonal axes---scope (world vs.\ self) and mode (implicit vs.\ explicit)---define four functionally distinct models. Implicit models (bottom) are substrate-level, learned, and non-conscious. Explicit models (top) are virtual, transient, and phenomenal.}
\label{fig:four-models}
\end{figure}
"""

FLOAT_FIG_REAL_VIRTUAL = r"""
\begin{figure}[htbp]
\centering
\includegraphics[width=0.85\textwidth]{figure2-real-virtual-split.png}
\caption{The ontological split between the real substrate (physical, structural, non-conscious---``lights off'') and the virtual phenomenal world (simulated, transient, experiential---``lights on''). Qualia exist only on the virtual side.}
\label{fig:real-virtual}
\end{figure}
"""

FLOAT_TABLE_CRITICALITY = r"""
\begin{table}[htbp]
\centering
\caption{Independent Convergence on Criticality}
\label{tab:criticality-convergence}
\begin{tabularx}{\textwidth}{lXl}
\toprule
\textbf{Year} & \textbf{Development} & \textbf{Path} \\
\midrule
2002 & Wolfram publishes \textit{A New Kind of Science} & Computational theory \\
2003 & Beggs \& Plenz---neuronal avalanches, self-organized criticality & Empirical neuroscience \\
2014 & Carhart-Harris---Entropic Brain Hypothesis & Empirical neuroscience \\
\textbf{2015} & \textbf{Gruber---Class~4 / edge of chaos requirement for consciousness} & \textbf{Theoretical (via Wolfram)} \\
2016 & Tagliazucchi et al.---LSD and criticality & Empirical neuroscience \\
2022 & ``Self-organized criticality as a framework for consciousness'' (review) & Empirical neuroscience \\
2025 & Hengen \& Shew---meta-analysis of 140 datasets confirms criticality & Empirical neuroscience \\
\textbf{2025--26} & \textbf{ConCrit framework (Algom \& Shriki)---criticality as unifying mechanism for consciousness theories} & \textbf{Theoretical/empirical synthesis} \\
\bottomrule
\end{tabularx}
\end{table}
"""

FLOAT_FIG_PHENOMENOLOGICAL = r"""
\begin{figure}[htbp]
\centering
\includegraphics[width=0.85\textwidth]{figure3-phenomenological-content.png}
\caption{The structure of phenomenological content: what appears in the virtual world (EWM) and how the virtual self (ESM) experiences it. The boundary between implicit and explicit determines what reaches conscious awareness.}
\label{fig:phenomenological}
\end{figure}
"""

FLOAT_TABLE_CONSCIOUSNESS_STATES = r"""
\begin{table}[htbp]
\centering
\caption{Consciousness States and Criticality}
\label{tab:consciousness-states}
\small
\renewcommand{\arraystretch}{1.4}
\begin{tabularx}{\textwidth}{>{\raggedright}p{1.9cm} >{\raggedright}p{1.7cm} >{\raggedright}p{3.2cm} X >{\raggedright\arraybackslash}p{2cm}}
\toprule
\textbf{State} & \textbf{Criticality} & \textbf{Four-model status} & \textbf{Consciousness prediction} & \textbf{Key evidence} \\
\midrule
Normal waking & At/near critical & All four active & Full consciousness & High PCI \\
REM sleep & Near-critical & EWM/ESM on internal input & Degraded (dream) & Moderate PCI \\
Deep NREM & Subcritical & EWM/ESM collapse & Absent & Low PCI \\
Propofol & Forced subcritical & EWM/ESM suppressed & Absent & PCI $\approx$ 0 \\
Ketamine & NOT subcritical & EWM/ESM on wrong input & Present but disconnected & Increased entropy \\
Psychedelics & At/past critical & All active, permeability $\uparrow$ & Present, altered & Enhanced complexity \\
Vegetative state & Typically subcritical & EWM/ESM collapsed & Absent (usually) & Low metabolism \\
Covert awareness & At criticality & EWM/ESM intact, output damaged & Present but unexpressible & Owen et al.\ \\
MCS & Fluctuating & Intermittent EWM/ESM & Intermittent & Fluctuating PCI \\
\bottomrule
\end{tabularx}
\end{table}
"""

FLOAT_TABLE_COMPARISON = r"""
\textbf{Assessment criteria}: \textit{Addresses} = the theory provides a substantive, defended account of this requirement. \textit{Partial} = the theory provides a relevant account that leaves significant aspects unresolved. \textit{Minimal} = the theory touches on this requirement but does not develop a full treatment. \textit{Silent} = the theory does not address this requirement (which may reflect deliberate scope limitation rather than failure). \textit{N/A} = the requirement does not apply given the theory's ontological commitments.

Ratings: $\bullet$ = addresses, $\odot$ = partial, $\circ$ = minimal, --- = silent, n/a = not applicable.

\begin{table}[htbp]
\centering
\caption{Theory Comparison Across Eight Requirements}
\label{tab:comparison}
\small
\begin{tabular}{lccccccc}
\toprule
\textbf{Requirement} & \textbf{FMT} & \textbf{IIT} & \textbf{GNW} & \textbf{HOT} & \textbf{PP} & \textbf{AST} & \textbf{RPT} \\
\midrule
Hard Problem & $\bullet$ & $\bullet^\dagger$ & ---$^\ddagger$ & $\odot$ & ---$^\ddagger$ & $\odot$ & --- \\
Expl.\ Gap & $\bullet$ & $\bullet^\dagger$ & ---$^\ddagger$ & $\odot$ & ---$^\ddagger$ & $\odot$ & --- \\
Boundary & $\bullet$ & $\bullet$ & $\odot$ & $\circ$ & $\odot$ & $\odot$ & $\odot$ \\
Structure & $\bullet$ & $\bullet$ & $\odot$ & $\odot$ & $\bullet$ & $\odot$ & $\odot$ \\
Binding & $\bullet$ & $\bullet$ & $\odot$ & $\circ$ & $\odot$ & $\circ$ & $\odot$ \\
Combination & $\bullet$ & $\circ^{\dagger\dagger}$ & n/a & n/a & n/a & n/a & n/a \\
Causal Role & $\bullet$ & $\odot$ & $\odot$ & $\odot$ & $\bullet$ & $\odot$ & $\bullet$ \\
Meta-Problem & $\bullet$ & $\circ$ & $\odot$ & $\odot$ & $\odot$ & $\bullet$ & $\circ$ \\
\bottomrule
\end{tabular}

\smallskip
\raggedright\footnotesize
$^\dagger$~IIT addresses the Hard Problem through its axioms, identifying consciousness with $\Phi$. Whether this constitutes a solution or a redefinition is debated (see \S7.2).
$^{\dagger\dagger}$~IIT's panpsychist commitments lead to the Combination Problem \citep{Chalmers2016}, which remains unresolved within the framework.
$^\ddagger$~GNW and PP proponents argue these theories address the ``real problem'' of consciousness \citep{Seth2021}---explaining the structure and contents of experience---even if they do not address the Hard Problem as Chalmers defines it. This is a legitimate methodological choice, not a deficiency; the ``silent'' rating reflects the scope of the requirement as defined in Section~2, not a judgment on overall merit.
\end{table}
"""

# Float injection anchors: (text_anchor_in_converted_body, float_latex)
# The anchor is a snippet of converted text that appears BEFORE the float.
FLOAT_INJECTIONS = [
    # Table 1 + Figure 1: after the taxonomy paragraph in Section 3.1
    ("functionally distinct processes, not anatomically localized regions",
     FLOAT_TABLE_FOUR_MODELS + FLOAT_FIG_FOUR_MODELS),
    # Figure 2: after "This division is the foundation"
    ("This division is the foundation",
     FLOAT_FIG_REAL_VIRTUAL),
    # Table 2 + Figure 3: after ConCrit framework mention
    ("ConCrit",
     FLOAT_TABLE_CRITICALITY + FLOAT_FIG_PHENOMENOLOGICAL),
    # Table 3: after "position relative to the critical point"
    ("position relative to the critical point",
     FLOAT_TABLE_CONSCIOUSNESS_STATES),
    # Table 4: before "Theory-by-Theory Comparison" subsection
    ("systematically assesses each theory",
     FLOAT_TABLE_COMPARISON),
]


def inject_floats(tex_body):
    """Inject LaTeX float blocks at anchor positions in the body."""
    result = tex_body
    for anchor, float_latex in FLOAT_INJECTIONS:
        idx = result.find(anchor)
        if idx >= 0:
            # Find end of the paragraph containing the anchor
            para_end = result.find("\n\n", idx)
            if para_end < 0:
                para_end = result.find("\n\\", idx)
            if para_end < 0:
                para_end = len(result)
            result = result[:para_end] + "\n" + float_latex + "\n" + result[para_end:]
    return result


def parse_md():
    """Parse the markdown file into structured components."""
    with open(MD_PATH, "r") as f:
        md_text = f.read()

    # Title
    title_match = re.match(r'^#\s+(.+?)$', md_text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Untitled"

    # Abstract
    abstract_match = re.search(
        r'^## Abstract\s*\n\n(.+?)(?=\n\n\*\*Keywords\*\*)',
        md_text, re.DOTALL | re.MULTILINE
    )
    abstract = abstract_match.group(1).strip() if abstract_match else ""

    # Keywords
    kw_match = re.search(r'\*\*Keywords\*\*:\s*(.+?)(?=\n\n)', md_text, re.DOTALL)
    keywords = kw_match.group(1).strip() if kw_match else ""

    # Body: from first section to References
    body_start = md_text.find("## 1.")
    if body_start == -1:
        body_start = md_text.find("## 1 ")

    # Find end of body (References section or end of numbered sections)
    # The .md has refs as an unlabeled list at the end (no "## References" header)
    # Find where numbered sections end
    refs_pattern = re.search(r'\n\n(?=[A-Z][a-z]+,?\s+[A-Z]\.?\s+(?:&|\()\s*)', md_text[body_start:])
    # Better: find the last ## section, then the reference list starts after
    all_sections = list(re.finditer(r'^## ', md_text, re.MULTILINE))
    if all_sections:
        last_section = all_sections[-1]
        # Check if there's content after the last section that looks like references
        body_end = len(md_text)
        # Find where references start (first line that looks like "Author, A. (Year)")
        ref_list_match = re.search(
            r'\n\n([A-Z][a-z]+.*?\(\d{4}\)\.)',
            md_text[last_section.start():],
            re.MULTILINE
        )
        if ref_list_match:
            body_end = last_section.start() + ref_list_match.start()

    body = md_text[body_start:body_end].strip() if body_start > 0 else ""

    # Footnotes
    footnotes = extract_footnotes(md_text)

    return {
        "title": title,
        "abstract": abstract,
        "keywords": keywords,
        "body": body,
        "footnotes": footnotes,
        "full_text": md_text,
    }


def generate_tex():
    """Generate complete .tex from .md source."""
    parsed = parse_md()

    preamble = generate_preamble()

    # Title (formatting rule: line break after colon)
    title_tex = parsed["title"]
    title_tex = title_tex.replace(": ", ":\\\\")

    title_block = f"""% === Title ===
\\title{{{title_tex}}}
\\author{{Matthias Gruber\\\\
\\textit{{Independent researcher}}\\\\
ORCID: \\href{{https://orcid.org/0009-0005-9697-1665}}{{0009-0005-9697-1665}}\\\\
\\texttt{{matthias@matthiasgruber.com}}}}
\\date{{}}
"""

    # Abstract — convert citations FIRST (before & is escaped to \&)
    abstract_cited = convert_citations(parsed["abstract"], FMT_CITATION_KEYS)
    abstract_tex = _convert_inline(abstract_cited)

    keywords_tex = _convert_inline(parsed["keywords"])

    abstract_block = f"""\\begin{{abstract}}\\singlespacing
{abstract_tex}
\\end{{abstract}}

\\noindent\\textbf{{Keywords}}: {keywords_tex}
"""

    # Body — convert citations FIRST (before & is escaped to \&)
    body_cited = convert_citations(parsed["body"], FMT_CITATION_KEYS)
    body_tex = convert_body(body_cited)

    # Inject footnotes
    footnotes = parsed["footnotes"]
    for fn_name, fn_text in footnotes.items():
        fn_cited = convert_citations(fn_text, FMT_CITATION_KEYS)
        fn_tex = _convert_inline(fn_cited)
        # Replace [^name] reference with \footnote{text}
        body_tex = body_tex.replace(f"[^{fn_name}]", f"\\footnote{{{fn_tex}}}")

    # Inject floats
    body_tex = inject_floats(body_tex)

    # Bibliography
    bib_block = """\\bibliographystyle{plainnat}
\\bibliography{references}"""

    # Assemble
    tex = f"""{preamble}
{title_block}
% === Document ===
\\begin{{document}}
\\maketitle

{abstract_block}

{body_tex}

{bib_block}

\\end{{document}}
"""

    return tex


def build_tex():
    """Build the .tex file from .md source."""
    tex = generate_tex()
    with open(TEX_PATH, "w") as f:
        f.write(tex)
    print(f"Generated: {TEX_PATH}")
    return True


def build_pdf(keep_aux=False):
    """Compile .tex to .pdf using pdflatex + bibtex."""
    if not os.path.exists(TEX_PATH):
        build_tex()

    for tool in ["pdflatex", "bibtex"]:
        if shutil.which(tool) is None:
            print(f"ERROR: {tool} not found")
            return False

    pdflatex_cmd = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-output-directory", OUTPUT_DIR,
        TEX_PATH,
    ]
    bibtex_cmd = ["bibtex", os.path.join(OUTPUT_DIR, "paper")]

    # Pass 1: pdflatex
    print("  pdflatex pass 1...")
    result = subprocess.run(pdflatex_cmd, capture_output=True, text=True,
                            cwd=OUTPUT_DIR, timeout=120, errors='replace')
    if result.returncode != 0:
        print("ERROR: pdflatex pass 1 failed")
        _print_tex_errors(TEX_PATH.replace(".tex", ".log"))
        return False

    # bibtex
    print("  bibtex...")
    result = subprocess.run(bibtex_cmd, capture_output=True, text=True,
                            cwd=OUTPUT_DIR, timeout=60, errors='replace')
    if result.returncode != 0:
        print(f"WARNING: bibtex returned {result.returncode}")
        if result.stderr:
            print(f"  {result.stderr[:200]}")

    # Pass 2 & 3: pdflatex (resolve references)
    for pass_num in [2, 3]:
        print(f"  pdflatex pass {pass_num}...")
        result = subprocess.run(pdflatex_cmd, capture_output=True, text=True,
                                cwd=OUTPUT_DIR, timeout=120, errors='replace')
        if result.returncode != 0:
            print(f"ERROR: pdflatex pass {pass_num} failed")
            _print_tex_errors(TEX_PATH.replace(".tex", ".log"))
            return False

    if not keep_aux:
        for ext in [".aux", ".log", ".out", ".blg"]:
            p = os.path.join(OUTPUT_DIR, "paper" + ext)
            if os.path.exists(p):
                os.remove(p)

    if os.path.exists(PDF_PATH):
        size_kb = os.path.getsize(PDF_PATH) / 1024
        print(f"SUCCESS: {PDF_PATH} ({size_kb:.0f} KB)")
        return True
    else:
        print(f"ERROR: PDF not created: {PDF_PATH}")
        return False


def _print_tex_errors(log_path):
    """Print relevant errors from a .log file."""
    if not os.path.exists(log_path):
        return
    with open(log_path, errors="replace") as f:
        for line in f:
            if line.startswith("!"):
                print(f"  {line.rstrip()}")


def main():
    keep_aux = "--keep-aux" in sys.argv
    tex_only = "--tex-only" in sys.argv

    print("=" * 60)
    print("Building FMT Full Paper")
    print("=" * 60)

    print("\n[1/2] Generating .tex from .md...")
    build_tex()

    if not tex_only:
        print("\n[2/2] Compiling .tex to .pdf...")
        success = build_pdf(keep_aux)
        return 0 if success else 1
    else:
        print("\n[2/2] Skipped PDF compilation (--tex-only)")
        return 0


if __name__ == "__main__":
    sys.exit(main())
