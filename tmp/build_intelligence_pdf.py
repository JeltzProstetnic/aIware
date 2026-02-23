#!/usr/bin/env python3
"""Build intelligence paper from .md to .tex to .pdf.

Pipeline: paper/intelligence/paper.md → paper/intelligence/paper.tex → paper/intelligence/paper.pdf
Implements formatting rules from paper/intelligence/paper.formatting-rules.md.
"""

import os
import re
import sys
import subprocess
import shutil

REPO_ROOT = "/home/jeltz/aIware"
MD_PATH = os.path.join(REPO_ROOT, "paper/intelligence/paper.md")
TEX_PATH = os.path.join(REPO_ROOT, "paper/intelligence/paper.tex")
PDF_PATH = os.path.join(REPO_ROOT, "paper/intelligence/paper.pdf")
OUTPUT_DIR = os.path.join(REPO_ROOT, "paper/intelligence")

# ---------------------------------------------------------------------------
# Citation key mapping: display name → BibTeX key
# Built from the existing hand-maintained .tex thebibliography entries.
# Keys follow the convention: LastnameYear (first author only).
# ---------------------------------------------------------------------------

INTEL_CITATION_KEYS = {
    # Single authors
    ("Ackerman", "1996"): "Ackerman1996",
    ("Bandura", "1997"): "Bandura1997",
    ("Binet", "1905"): "Binet1905",
    ("Cacioppo", "1996"): "Cacioppo1996",
    ("Cattell", "1971"): "Cattell1971",
    ("Cronbach", "1949"): "Cronbach1949",
    ("Duckworth", "2007"): "Duckworth2007",
    ("Dweck", "2006"): "Dweck2006",
    ("Frank", "1959"): "Frank1959",
    ("Gardner", "1983"): "Gardner1983",
    ("Gruber", "2015"): "Gruber2015",
    ("Gruber", "2026"): "Gruber2026",
    ("Gruber", "2026a"): "Gruber2026a",
    ("Gruber", "2026b"): "Gruber2026b",
    ("Heckman", "2006"): "Heckman2006",
    ("Huang", "2024"): "Huang2024",
    ("Schiefele", "2017"): "Schiefele2017",
    ("Snow", "1996"): "Snow1996",
    ("Stanovich", "1986"): "Stanovich1986",
    ("Stanovich", "2016"): "Stanovich2016",
    ("Sternberg", "1985"): "Sternberg1985",
    ("Sternberg", "2019"): "Sternberg2019",
    ("Waterhouse", "2006"): "Waterhouse2006",
    ("Wechsler", "1940"): "Wechsler1940",
    ("Wechsler", "1943"): "Wechsler1943",
    ("Zimmerman", "2002"): "Zimmerman2002",
    # Multi-author (first author + year)
    ("Deci", "2000"): "DeciRyan2000",
    ("Deci & Ryan", "2000"): "DeciRyan2000",
    ("Wigfield", "2000"): "WigfieldEccles2000",
    ("Wigfield & Eccles", "2000"): "WigfieldEccles2000",
    ("McGrew", "2009"): "McGrew2009",
    ("Schneider", "2018"): "SchneiderMcGrew2018",
    ("Schneider & McGrew", "2018"): "SchneiderMcGrew2018",
    ("Canivez", "2019"): "CanivezYoungstrom2019",
    ("Canivez and Youngstrom", "2019"): "CanivezYoungstrom2019",
    ("Ziegler", "2012"): "Ziegler2012",
    ("von Stumm", "2013"): "vonStummAckerman2013",
    ("von Stumm & Ackerman", "2013"): "vonStummAckerman2013",
    ("von Stumm", "2011"): "vonStumm2011",
    ("Murayama", "2013"): "Murayama2013",
    ("Crede", "2008"): "CredeKuncel2008",
    ("Credé", "2008"): "CredeKuncel2008",
    ("Carr", "2019"): "CarrDweck2019",
    ("Carr & Dweck", "2019"): "CarrDweck2019",
    ("Rosenthal", "1968"): "RosenthalJacobson1968",
    ("Rosenthal & Jacobson", "1968"): "RosenthalJacobson1968",
    ("Steele", "1995"): "SteeleAronson1995",
    ("Steele & Aronson", "1995"): "SteeleAronson1995",
    ("Yeager", "2012"): "YeagerDweck2012",
    ("Yeager & Dweck", "2012"): "YeagerDweck2012",
    ("Macnamara", "2023"): "MacnamaraBurgoyne2023",
    ("Macnamara & Burgoyne", "2023"): "MacnamaraBurgoyne2023",
    ("Melby-Lervåg", "2013"): "MelbyLervag2013",
    ("Melby-Lervåg & Hulme", "2013"): "MelbyLervag2013",
    ("Melby-Lervag", "2013"): "MelbyLervag2013",  # without diacritics fallback
    ("Merton", "1948"): "Merton1948",
    ("van Geert", "2020"): "vanGeert2020",
    ("Hilger", "2020"): "Hilger2020",
    ("Sternberg", "2021"): "Sternberg2021",
    # Multi-author with &
    ("Dignath", "2008"): "DignathButtner2008",
    ("Dignath & Büttner", "2008"): "DignathButtner2008",
    ("Jaeggi", "2008"): "Jaeggi2008",
    ("Chase", "1973"): "ChaseSimon1973",
    ("Chase & Simon", "1973"): "ChaseSimon1973",
    ("Bloom", "1968"): "Bloom1968",
    ("Flavell", "1979"): "Flavell1979",
    # "et al." forms → same first-author key
}


def generate_preamble():
    """Generate LaTeX preamble matching formatting rules."""
    return r"""\documentclass[12pt,a4paper]{article}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{mathpazo}
\usepackage[margin=1in]{geometry}
\usepackage{setspace}
\usepackage{natbib}
\usepackage{microtype}
\usepackage{hyperref}
\usepackage{url}
\usepackage{enumitem}

\onehalfspacing
\emergencystretch=1em

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    citecolor=blue,
    urlcolor=blue
}
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
    # Try with & variant
    if " & " in author:
        first = author.split(" & ")[0].strip()
        if (first, year) in keys:
            return keys[(first, year)]
    # Fallback: construct from first author + year
    # Remove spaces, hyphens, special chars for key
    key_author = re.sub(r'[^A-Za-z]', '', author_clean.split(",")[0].split(" ")[-1] if "," in author_clean else author_clean)
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
    # Covers diacritics: é, ü, å, ö, ø, etc.
    _L = r'a-zà-öø-ÿ'  # lowercase letters including diacritics
    _U = r'A-ZÀ-ÖØ-Þ'  # uppercase letters including diacritics
    _S = r'[^\S\n]'      # whitespace but NOT newline — prevents cross-line matching
    # Single surname: Capitalized, may be hyphenated (Melby-Lervåg, Saint-Hilaire)
    _SURNAME = rf'[{_U}][{_L}]{{2,}}(?:-[{_U}][{_L}]{{2,}})*'
    # Author name: optional lowercase particle (von, van, de, di, le, la) + surname
    _PARTICLE = rf'(?:(?:von|van|de|di|le|la|du|el|al){_S}+)'
    _NAME = rf'(?:{_PARTICLE})?{_SURNAME}'
    # Author group: Name (& Name)* (et al.)?
    _AUTHORS = rf'{_NAME}(?:{_S}+(?:&{_S}+)?{_SURNAME})*(?:{_S}+et{_S}+al\.?)?'
    # Author group allowing & with diacritics on second author too
    _AUTHORS_AMP = rf'{_NAME}(?:(?:{_S}+(?:&{_S}+)?(?:{_PARTICLE})?{_SURNAME}))*(?:{_S}+et{_S}+al\.?)?'

    # --- Pass 1: Possessive citations: Author's (Year) ---
    # e.g., "Sternberg's (1985)" → "\citeauthor{Sternberg1985}'s \citeyearpar{Sternberg1985}"
    def replace_possessive(m):
        author = m.group(1)
        year = m.group(2)
        key = _lookup_key(author, year, keys)
        return f"\\citeauthor{{{key}}}'s \\citeyearpar{{{key}}}"

    result = re.sub(
        rf"({_NAME}(?:{_S}+{_SURNAME})*)'s{_S}+\((\d{{4}}[a-z]?)\)",
        replace_possessive,
        result
    )

    # --- Pass 2: Textual citations: Author (Year) or Author (Year, Year) ---
    # Must come before parenthetical to avoid double-matching
    def replace_textual(m):
        author = m.group(1)
        years_str = m.group(2)
        years = [y.strip() for y in years_str.split(",")]
        cite_keys = [_lookup_key(author, y, keys) for y in years]
        return f"\\citet{{{','.join(cite_keys)}}}"

    # Author (Year) or Author (Year, Year) — NOT inside parentheses
    # Use [^\S\n]+ to prevent matching across line boundaries
    result = re.sub(
        rf"(?<!\()({_AUTHORS_AMP}){_S}+\((\d{{4}}[a-z]?(?:{_S}*,{_S}*\d{{4}}[a-z]?)*)\)",
        replace_textual,
        result
    )

    # --- Pass 3: Parenthetical citations: (Author, Year; ...) ---
    def replace_parenthetical(m):
        inner = m.group(1)
        # Check if this looks like actual citations vs model names
        # Citations have: AuthorName, 4-digit year
        if not re.search(r'\d{4}', inner):
            return m.group(0)  # Not a citation, leave as-is

        # Split by semicolons for multiple citations
        parts = [p.strip() for p in inner.split(";")]
        cite_keys = []
        non_citation_parts = []

        for part in parts:
            # Try to find: Author(s), Year anywhere in the part
            # Allow lowercase particles (von, van, de) and & between authors
            # Allow diacritics in all author name positions
            # Allow free text before (e.g., "for exceptions, see", "though see")
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
                cite_keys.append(key)
                # Check for additional years: ", Year"
                rest = part[cm.end():]
                extra_years = re.findall(r',\s*(\d{4}[a-z]?)', rest)
                for ey in extra_years:
                    ekey = _lookup_key(author, ey, keys)
                    cite_keys.append(ekey)
                # Check if there's meaningful non-citation text before/after
                prefix = part[:cm.start()].strip()
                # Strip "see", "see also", "though see", "for X, see" prefixes
                prefix_clean = re.sub(r'(?:for\s+\w+,?\s*)?(?:though\s+)?(?:see\s+(?:also\s+)?)?$', '', prefix).strip()
                suffix = rest.strip().lstrip(',').strip()
                # Remove year-only suffixes already captured
                suffix = re.sub(r'^(?:\d{4}[a-z]?\s*,?\s*)*', '', suffix).strip()
                if prefix_clean or suffix:
                    non_citation_parts.append(part[:cm.start()].strip() if prefix_clean else '')
            else:
                non_citation_parts.append(part)

        if cite_keys and not non_citation_parts:
            return f"\\citep{{{','.join(cite_keys)}}}"
        elif cite_keys:
            # Mixed: some citations, some text
            cite_str = f"\\citealp{{{','.join(cite_keys)}}}"
            text_parts = "; ".join(non_citation_parts)
            return f"({text_parts}; {cite_str})"
        else:
            return m.group(0)

    # Match parenthetical groups that contain at least one year
    result = re.sub(
        r'\(([^)]*\d{4}[^)]*)\)',
        replace_parenthetical,
        result
    )

    return result


def convert_body(text):
    """Convert markdown body text to LaTeX.

    Handles headings, emphasis, lists, special characters, horizontal rules.
    Does NOT handle citations (call convert_citations separately).
    """
    lines = text.split("\n")
    output = []
    in_list = False
    list_type = None  # 'enumerate' or 'itemize'
    in_sublist = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # --- Horizontal rules ---
        if re.match(r'^---+\s*$', line):
            i += 1
            continue

        # --- Headings ---
        h1_match = re.match(r'^#\s+(.+)$', line)
        if h1_match:
            # H1 is the title — skip it (handled in title block)
            i += 1
            continue

        h2_match = re.match(r'^##\s+(?:\d+\.\s+)?(.+)$', line)
        if h2_match:
            if in_list:
                output.append(f"\\end{{{list_type}}}")
                in_list = False
            title = h2_match.group(1).strip()
            # Check for unnumbered sections (Acknowledgments, Data Availability, etc.)
            if title.lower() in ("acknowledgments", "acknowledgements",
                                  "data availability", "funding",
                                  "disclosure statement"):
                output.append(f"\\section*{{{title}}}")
            else:
                output.append(f"\\section{{{title}}}")
            i += 1
            continue

        h3_match = re.match(r'^###\s+(?:\d+\.\d+\s+)?(.+)$', line)
        if h3_match:
            if in_list:
                output.append(f"\\end{{{list_type}}}")
                in_list = False
            title = h3_match.group(1).strip()
            output.append(f"\\subsection{{{title}}}")
            i += 1
            continue

        # --- Numbered lists ---
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

        # --- Bullet lists ---
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

        # --- Sub-bullets (indented) ---
        sub_bullet_match = re.match(r'^\s{2,}[-*]\s+(.+)$', line)
        if sub_bullet_match:
            if not in_sublist:
                output.append("\\begin{itemize}")
                in_sublist = True
            item_text = _convert_inline(sub_bullet_match.group(1))
            output.append(f"\\item {item_text}")
            i += 1
            continue

        # End sub-list if we're no longer in one
        if in_sublist and not re.match(r'^\s{2,}[-*]', line):
            output.append("\\end{itemize}")
            in_sublist = False

        # End list if we're at a blank line or non-list content
        if in_list and line.strip() == "" and (
            i + 1 >= len(lines) or not re.match(r'^(?:\d+\.|\s*[-*])\s', lines[i + 1])
        ):
            if in_sublist:
                output.append("\\end{itemize}")
                in_sublist = False
            output.append(f"\\end{{{list_type}}}")
            in_list = False

        # --- Regular text ---
        converted = _convert_inline(line)
        output.append(converted)
        i += 1

    # Close any open lists
    if in_sublist:
        output.append("\\end{itemize}")
    if in_list:
        output.append(f"\\end{{{list_type}}}")

    return "\n".join(output)


def _convert_inline(text):
    """Convert inline markdown to LaTeX."""
    result = text

    # Em dash: — → ---
    result = result.replace(" — ", "---")
    result = result.replace("—", "---")

    # Special characters (must come before emphasis conversion)
    # Escape & but not in already-escaped contexts or \& already present
    result = re.sub(r'(?<!\\)&(?!\\)', r'\\&', result)
    # Escape % but not in already-escaped contexts
    result = re.sub(r'(?<!\\)%', r'\\%', result)
    # Escape # in body text (but not at start of line — headings already handled)
    result = re.sub(r'(?<!\\)(?<!^)#', r'\\#', result)

    # Bold + italic (***text*** or ___text___) → \textbf{\emph{text}}
    result = re.sub(r'\*\*\*(.+?)\*\*\*', r'\\textbf{\\emph{\1}}', result)

    # Bold (**text**) → \textbf{text}
    result = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', result)

    # Italic (*text*) → \emph{text}
    # But NOT inside math mode ($...$) or already-converted LaTeX
    result = re.sub(r'(?<!\$)\*([^*\n]+?)\*(?!\$)', r'\\emph{\1}', result)

    # Inline code (`text`) → \texttt{text}
    result = re.sub(r'`([^`]+)`', r'\\texttt{\1}', result)

    # Smart quotes
    result = re.sub(r'"([^"]*)"', r"``\1''", result)
    result = re.sub(r'"([^"]*)"', r"``\1''", result)

    # Section cross-references: Section N → Section~N
    result = re.sub(r'Section (\d)', r'Section~\1', result)

    # Umlaut preservation
    result = result.replace("ü", r'\"u')
    result = result.replace("ö", r'\"o')
    result = result.replace("ä", r'\"a')
    result = result.replace("å", r'\aa{}')

    return result


def extract_references(md_text):
    """Extract reference entries from the .md references section.

    Returns a list of dicts with 'key', 'display_label', 'entry_text'.
    """
    # Find the references section
    refs_match = re.search(r'^## References\s*\n(.*)', md_text, re.DOTALL | re.MULTILINE)
    if not refs_match:
        return []

    refs_text = refs_match.group(1)
    entries = []
    current_entry = []

    for line in refs_text.strip().split("\n"):
        line = line.strip()
        if not line:
            if current_entry:
                entries.append("\n".join(current_entry))
                current_entry = []
            continue
        current_entry.append(line)

    if current_entry:
        entries.append("\n".join(current_entry))

    result = []
    for entry in entries:
        parsed = _parse_reference(entry)
        if parsed:
            result.append(parsed)

    return result


def _parse_reference(entry_text):
    """Parse a single markdown reference entry into components."""
    # Patterns:
    # Author, A. (Year). Title. *Journal*, vol(issue), pages.
    # Author, A. (Year). *Book title*. Publisher.
    # Author, A., & Author, B. (Year). Title. In Editor (Ed.), *Book* (pp. X-Y). Publisher.

    match = re.match(
        r'^(.+?)\s*\((\d{4}[a-z]?)\)\.\s*(.+)$',
        entry_text,
        re.DOTALL
    )
    if not match:
        return None

    authors_str = match.group(1).strip()
    year = match.group(2)
    rest = match.group(3).strip()

    # Generate citation key
    key = _generate_citation_key(authors_str, year)

    # Generate display label for \bibitem
    display_label = _generate_display_label(authors_str, year)

    # Convert rest to LaTeX
    bib_body = _format_bib_entry(authors_str, rest)

    return {
        "key": key,
        "display_label": display_label,
        "year": year,
        "authors": authors_str,
        "body": bib_body,
        "raw": entry_text,
    }


def _generate_citation_key(authors_str, year):
    """Generate a BibTeX citation key from authors and year."""
    # Get first author's last name
    first_author = authors_str.split(",")[0].strip()
    # Handle "van Geert", "von Stumm", etc.
    parts = first_author.split()
    if len(parts) > 1 and parts[0].lower() in ("van", "von", "de", "di"):
        last_name = "".join(parts[:2])
    else:
        last_name = parts[-1] if parts else first_author

    # Handle multi-author keys that combine names
    if "&" in authors_str:
        # Check for two-author conventions
        authors = re.split(r',\s*&\s*|\s*&\s*', authors_str)
        if len(authors) == 2:
            second_last = authors[1].strip().split(",")[0].strip().split()[-1]
            # Some keys combine both last names: DeciRyan, SteeleAronson, etc.
            combined = re.sub(r'[^A-Za-z]', '', last_name) + re.sub(r'[^A-Za-z]', '', second_last)
            # Check if this matches our known keys
            if (last_name, year) in INTEL_CITATION_KEYS:
                return INTEL_CITATION_KEYS[(last_name, year)]
            return combined + year

    # Clean the last name
    clean_name = re.sub(r'[^A-Za-z]', '', last_name)
    return clean_name + year


def _generate_display_label(authors_str, year):
    """Generate the display label for \\bibitem[label]{key}."""
    # e.g., "Deci & Ryan, 2000", "Sternberg et al., 2021", "Dweck, 2006"
    if "&" in authors_str:
        parts = re.split(r',\s*&\s*|\s*&\s*', authors_str, maxsplit=1)
        first = parts[0].strip().split(",")[0].strip()
        second = parts[1].strip().split(",")[0].strip().split()[-1]
        return f"{first} \\& {second}, {year}"
    elif "," in authors_str:
        # Multiple authors separated by commas
        author_list = [a.strip() for a in re.split(r',\s*(?:&|\band\b)', authors_str)]
        if len(author_list) > 2:
            first = authors_str.split(",")[0].strip()
            return f"{first} et~al., {year}"
        else:
            first = authors_str.split(",")[0].strip()
            return f"{first}, {year}"
    else:
        return f"{authors_str}, {year}"


def _format_bib_entry(authors_str, rest):
    """Format the body of a bibliography entry in LaTeX."""
    result = rest
    # Convert *Title* to {\em Title}
    result = re.sub(r'\*([^*]+)\*', r'{\\em \1}', result)
    # En dashes
    result = result.replace("–", "--")
    # Smart quotes
    result = re.sub(r'"([^"]*)"', r"``\1''", result)
    result = re.sub(r'"([^"]*)"', r"``\1''", result)
    # Umlaut
    result = result.replace("ü", r'\"u')
    result = result.replace("ö", r'\"o')
    result = result.replace("ä", r'\"a')
    result = result.replace("å", r'\aa{}')
    # Escape &
    result = result.replace(" & ", r" \& ")

    return result


def _format_authors_bib(authors_str):
    """Format author names for bibliography entry."""
    result = authors_str
    result = result.replace("&", r"\&")
    result = result.replace("ü", r'\"u')
    result = result.replace("ö", r'\"o')
    result = result.replace("ä", r'\"a')
    result = result.replace("å", r'\aa{}')
    return result


def parse_md():
    """Parse the markdown file into structured components."""
    with open(MD_PATH, "r") as f:
        md_text = f.read()

    # Extract title (first # heading)
    title_match = re.match(r'^#\s+(.+?)$', md_text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Untitled"

    # Extract abstract
    abstract_match = re.search(
        r'^## Abstract\s*\n\n(.+?)(?=\n\n\*\*Keywords\*\*|\n\n---|\n\n## )',
        md_text, re.DOTALL | re.MULTILINE
    )
    abstract = abstract_match.group(1).strip() if abstract_match else ""

    # Extract keywords
    kw_match = re.search(r'\*\*Keywords\*\*:\s*(.+?)(?=\n\n)', md_text, re.DOTALL)
    keywords = kw_match.group(1).strip() if kw_match else ""

    # Extract body (between abstract/keywords and References)
    # Find where body starts: after keywords or after abstract
    body_start = md_text.find("## 1.")
    if body_start == -1:
        body_start = md_text.find("## 1 ")
    refs_start = md_text.find("## References")

    body = md_text[body_start:refs_start].strip() if body_start > 0 and refs_start > 0 else ""

    # Check for special sections after numbered sections but before References
    # (Acknowledgments, Disclosure Statement, etc.)

    return {
        "title": title,
        "abstract": abstract,
        "keywords": keywords,
        "body": body,
        "full_text": md_text,
    }


def generate_tex():
    """Generate complete .tex from .md source."""
    parsed = parse_md()
    md_text = parsed["full_text"]

    # Preamble
    preamble = generate_preamble()

    # Title block (from formatting rules)
    title_tex = parsed["title"].replace(": ", ":\\\\\n\\medskip\n")
    title_block = f"""\\title{{{title_tex}}}
\\author{{Matthias Gruber\\\\
\\small Independent Researcher\\\\
\\small ORCID: 0009-0005-9697-1665\\\\
\\small \\href{{mailto:matthias@matthiasgruber.com}}{{matthias@matthiasgruber.com}}}}
\\date{{}}
"""

    # Abstract — convert citations FIRST (before & is escaped to \&)
    abstract_cited = convert_citations(parsed["abstract"], INTEL_CITATION_KEYS)
    abstract_tex = _convert_inline(abstract_cited)
    keywords_tex = _convert_inline(parsed["keywords"])

    abstract_block = f"""\\begin{{abstract}}
{abstract_tex}

\\medskip
\\noindent\\textbf{{Keywords:}} {keywords_tex}
\\end{{abstract}}
"""

    # Body — convert citations FIRST (before & is escaped to \&)
    body_cited = convert_citations(parsed["body"], INTEL_CITATION_KEYS)
    body_tex = convert_body(body_cited)

    # References
    refs = extract_references(md_text)
    refs_block = generate_thebibliography(refs)

    # Assemble
    tex = f"""{preamble}
{title_block}
\\begin{{document}}

\\maketitle

{abstract_block}

{body_tex}

{refs_block}

\\end{{document}}
"""

    return tex


def generate_thebibliography(refs):
    """Generate \\begin{{thebibliography}} block from parsed references."""
    if not refs:
        return ""

    lines = [f"\\begin{{thebibliography}}{{{len(refs)}}}"]
    lines.append("")

    for ref in refs:
        label = ref["display_label"]
        key = ref["key"]
        authors_tex = _format_authors_bib(ref["authors"])
        year = ref["year"]
        body = ref["body"]

        lines.append(f"\\bibitem[{label}]{{{key}}}")
        lines.append(f"{authors_tex} ({year}).")
        # Split body into \newblock segments
        # First segment is the title, second is the journal/publisher
        body_parts = body.split(". ", 1)
        if len(body_parts) > 1:
            lines.append(f"\\newblock {body_parts[0]}.")
            lines.append(f"\\newblock {body_parts[1]}")
        else:
            lines.append(f"\\newblock {body}")
        lines.append("")

    lines.append("\\end{thebibliography}")
    return "\n".join(lines)


def build_tex():
    """Build the .tex file from .md source."""
    tex = generate_tex()
    with open(TEX_PATH, "w") as f:
        f.write(tex)
    print(f"Generated: {TEX_PATH}")
    return True


def build_pdf(keep_aux=False):
    """Compile .tex to .pdf using pdflatex."""
    if not os.path.exists(TEX_PATH):
        build_tex()

    if shutil.which("pdflatex") is None:
        print("ERROR: pdflatex not found")
        return False

    cmd = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-output-directory", OUTPUT_DIR,
        TEX_PATH,
    ]

    for pass_num in range(1, 3):
        print(f"  pdflatex pass {pass_num}...")
        result = subprocess.run(cmd, capture_output=True, text=True,
                                cwd=OUTPUT_DIR, timeout=120,
                                errors='replace')
        if result.returncode != 0:
            print(f"ERROR: pdflatex pass {pass_num} failed")
            log_path = TEX_PATH.replace(".tex", ".log")
            if os.path.exists(log_path):
                with open(log_path, errors="replace") as f:
                    for line in f:
                        if line.startswith("!"):
                            print(f"  {line.rstrip()}")
            return False

    if not keep_aux:
        for ext in [".aux", ".log", ".out"]:
            p = TEX_PATH.replace(".tex", ext)
            if os.path.exists(p):
                os.remove(p)

    if os.path.exists(PDF_PATH):
        size_kb = os.path.getsize(PDF_PATH) / 1024
        print(f"SUCCESS: {PDF_PATH} ({size_kb:.0f} KB)")
        return True
    else:
        print(f"ERROR: PDF not created: {PDF_PATH}")
        return False


def main():
    keep_aux = "--keep-aux" in sys.argv
    tex_only = "--tex-only" in sys.argv

    print("=" * 60)
    print("Building Intelligence Paper")
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
