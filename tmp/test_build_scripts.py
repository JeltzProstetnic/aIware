#!/usr/bin/env python3
"""Tests for paper build scripts (FMT full paper + intelligence paper).

TDD: These tests define the expected behavior of the build scripts.
Run with: python3 -m pytest tmp/test_build_scripts.py -v

Fixtures (fmt_build, intel_build, fmt_md, intel_md, etc.) are defined
in conftest.py and shared with test_content_integrity.py.
"""

import os
import sys
import pytest
import re
import subprocess
import tempfile

REPO_ROOT = "/home/jeltz/aIware"


# ===========================================================================
# SHARED: Citation conversion tests
# ===========================================================================

class TestCitationConversion:
    """Test that citation patterns are correctly converted from .md to LaTeX."""

    def test_simple_parenthetical(self, fmt_build):
        """(Chalmers, 1995) → \\citep{Chalmers1995}"""
        text = "as shown (Chalmers, 1995) in the literature"
        result = fmt_build.convert_citations(text, fmt_build.FMT_CITATION_KEYS)
        assert r"\citep{Chalmers1995}" in result

    def test_multiple_parenthetical(self, fmt_build):
        """(Author1, Year; Author2, Year) → \\citep{Key1,Key2}"""
        text = "evidence (Bayne, 2010; Tononi, 2004) supports"
        result = fmt_build.convert_citations(text, fmt_build.FMT_CITATION_KEYS)
        assert r"\citep{Bayne2010,Tononi2004}" in result

    def test_textual_citation(self, fmt_build):
        """Author (Year) → \\citet{AuthorYear}"""
        text = "Levine (1983) identified the Explanatory Gap"
        result = fmt_build.convert_citations(text, fmt_build.FMT_CITATION_KEYS)
        assert r"\citet{Levine1983}" in result

    def test_textual_multiple_years(self, fmt_build):
        """Author (Year1, Year2) → \\citet{Key1,Key2}"""
        text = "Chalmers (1995, 1996) formulated"
        result = fmt_build.convert_citations(text, fmt_build.FMT_CITATION_KEYS)
        assert r"\citet{Chalmers1995,Chalmers1996}" in result

    def test_possessive_citation(self, fmt_build):
        """Author's (Year) → \\citeauthor{Key}'s \\citeyearpar{Key}"""
        text = "Sternberg's (1985) triarchic theory"
        result = fmt_build.convert_citations(text, fmt_build.FMT_CITATION_KEYS)
        # Should NOT remain as plain text
        assert "Sternberg's (1985)" not in result

    def test_et_al_parenthetical(self, fmt_build):
        """(Author et al., Year) → \\citep{AuthorYear}"""
        text = "recent work (Doerig et al., 2019) challenged"
        result = fmt_build.convert_citations(text, fmt_build.FMT_CITATION_KEYS)
        assert r"\citep{Doerig2019}" in result

    def test_ampersand_in_parenthetical(self, fmt_build):
        """(Author1 & Author2, Year) → \\citep{Key}"""
        text = "binding (Singer & Gray, 1995) involves"
        result = fmt_build.convert_citations(text, fmt_build.FMT_CITATION_KEYS)
        assert r"\citep{Singer1995}" in result

    def test_no_false_positive_on_model_names(self, fmt_build):
        """(Implicit World Model, Implicit Self Model) should NOT be treated as citation."""
        text = "The implicit models (Implicit World Model, Implicit Self Model) are substrate-level"
        result = fmt_build.convert_citations(text, fmt_build.FMT_CITATION_KEYS)
        assert "(Implicit World Model, Implicit Self Model)" in result


# ===========================================================================
# INTELLIGENCE: Citation conversion — specific patterns from paper.md
# ===========================================================================

class TestIntelCitationPatterns:
    """Test citation patterns that actually appear in paper/intelligence/paper.md.

    Each test corresponds to a real citation from the .md source that must
    produce a natbib command (linked in PDF), not plain text.
    """

    def test_ampersand_parenthetical_deci_ryan(self, intel_build):
        """(Deci & Ryan, 2000) → \\citep{DeciRyan2000}"""
        text = "Self-Determination Theory (Deci & Ryan, 2000) and"
        keys = intel_build.INTEL_CITATION_KEYS
        result = intel_build.convert_citations(text, keys)
        assert r"\citep{DeciRyan2000}" in result
        assert "(Deci" not in result  # must not remain as plain text

    def test_ampersand_parenthetical_steele_aronson(self, intel_build):
        """(Steele & Aronson, 1995) → \\citep{SteeleAronson1995}"""
        text = "stereotype threat (Steele & Aronson, 1995) undermines"
        keys = intel_build.INTEL_CITATION_KEYS
        result = intel_build.convert_citations(text, keys)
        assert r"\citep{SteeleAronson1995}" in result

    def test_see_also_with_trailing_text(self, intel_build):
        """(see also Ziegler et al., 2012, on the relationship...) →
        should produce \\citealp or \\citep with the trailing text preserved."""
        text = "(see also Ziegler et al., 2012, on the relationship between investment traits and intelligence)"
        keys = intel_build.INTEL_CITATION_KEYS
        result = intel_build.convert_citations(text, keys)
        assert "Ziegler2012" in result
        assert r"\cite" in result  # must be a cite command, not plain text

    def test_lowercase_von_stumm_parenthetical(self, intel_build):
        """(von Stumm et al., 2011; Murayama et al., 2013) → \\citep{vonStumm2011,Murayama2013}"""
        text = "supports this (von Stumm et al., 2011; Murayama et al., 2013) but"
        keys = intel_build.INTEL_CITATION_KEYS
        result = intel_build.convert_citations(text, keys)
        assert "vonStumm2011" in result
        assert "Murayama2013" in result

    def test_umlaut_author_dignath_buttner(self, intel_build):
        """(Dignath & Büttner, 2008) → \\citep{DignathButtner2008}"""
        text = "supports this (Dignath & Büttner, 2008) but"
        keys = intel_build.INTEL_CITATION_KEYS
        result = intel_build.convert_citations(text, keys)
        assert "DignathButtner2008" in result
        assert r"\cite" in result

    def test_mixed_text_and_citation_cronbach(self, intel_build):
        """(what a person *can* do, not what they *will* do; Cronbach, 1949)
        → mixed parenthetical with \\citealp"""
        text = r"(what a person \emph{can} do, not what they \emph{will} do; Cronbach, 1949)"
        keys = intel_build.INTEL_CITATION_KEYS
        result = intel_build.convert_citations(text, keys)
        assert "Cronbach1949" in result
        assert r"\cite" in result

    def test_see_prefix_with_multiple_citations(self, intel_build):
        """(for exceptions, see Murayama et al., 2013; Credé & Kuncel, 2008)"""
        text = r"(for exceptions, see Murayama et al., 2013; Credé & Kuncel, 2008)"
        keys = intel_build.INTEL_CITATION_KEYS
        result = intel_build.convert_citations(text, keys)
        assert "Murayama2013" in result
        assert "CredeKuncel2008" in result

    def test_complex_mixed_jaeggi(self, intel_build):
        """(Jaeggi et al., 2008; though see Melby-Lervåg & Hulme, 2013, for debate about transfer)"""
        text = r"(Jaeggi et al., 2008; though see Melby-Lervåg & Hulme, 2013, for debate about transfer)"
        keys = intel_build.INTEL_CITATION_KEYS
        result = intel_build.convert_citations(text, keys)
        assert "Jaeggi2008" in result
        assert "MelbyLervag2013" in result

    def test_all_intel_citations_become_commands(self, intel_build, intel_md):
        """Every citation in the .md that has a key must produce a \\cite command.

        This is the definitive test: generate .tex and check that no citation
        remains as plain text when it should be a natbib command.
        """
        tex = intel_build.generate_tex()
        # These should all be cite commands, never plain text in parens
        must_be_linked = [
            ("DeciRyan2000", r"\cite"),
            ("Ziegler2012", r"\cite"),
            ("vonStumm2011", r"\cite"),
            ("DignathButtner2008", r"\cite"),
            ("Murayama2013", r"\cite"),
            ("SteeleAronson1995", r"\cite"),
            ("Bandura1997", r"\cite"),
            ("Merton1948", r"\cite"),
            ("Stanovich1986", r"\cite"),
        ]
        for key, cmd_prefix in must_be_linked:
            # The key must appear inside a \cite command
            pattern = r'\\cite[a-z]*\{[^}]*' + re.escape(key) + r'[^}]*\}'
            assert re.search(pattern, tex), \
                f"Citation key '{key}' not found in any \\cite command in generated .tex"


# ===========================================================================
# FMT FULL PAPER: Preamble tests
# ===========================================================================

class TestFmtPreamble:
    """Test FMT paper preamble generation matches formatting rules."""

    def test_preamble_has_documentclass(self, fmt_build):
        preamble = fmt_build.generate_preamble()
        assert r"\documentclass[12pt]{article}" in preamble

    def test_preamble_has_lmodern(self, fmt_build):
        preamble = fmt_build.generate_preamble()
        assert r"\usepackage{lmodern}" in preamble

    def test_preamble_has_margins(self, fmt_build):
        preamble = fmt_build.generate_preamble()
        assert r"\usepackage[margin=1in]{geometry}" in preamble

    def test_preamble_has_onehalfspacing(self, fmt_build):
        preamble = fmt_build.generate_preamble()
        assert r"\onehalfspacing" in preamble

    def test_preamble_has_natbib_round(self, fmt_build):
        preamble = fmt_build.generate_preamble()
        assert r"\usepackage[round]{natbib}" in preamble

    def test_preamble_has_hyperref_blue(self, fmt_build):
        preamble = fmt_build.generate_preamble()
        assert "blue!60!black" in preamble

    def test_preamble_has_all_required_packages(self, fmt_build):
        preamble = fmt_build.generate_preamble()
        for pkg in ["amsmath", "amssymb", "graphicx", "booktabs", "tabularx",
                     "xcolor", "microtype", "parskip", "setspace"]:
            assert pkg in preamble, f"Missing package: {pkg}"


# ===========================================================================
# INTELLIGENCE PAPER: Preamble tests
# ===========================================================================

class TestIntelPreamble:
    """Test intelligence paper preamble generation matches formatting rules."""

    def test_preamble_has_documentclass_a4(self, intel_build):
        preamble = intel_build.generate_preamble()
        assert r"\documentclass[12pt,a4paper]{article}" in preamble

    def test_preamble_has_mathpazo(self, intel_build):
        preamble = intel_build.generate_preamble()
        assert "mathpazo" in preamble

    def test_preamble_has_margins(self, intel_build):
        preamble = intel_build.generate_preamble()
        assert r"\usepackage[margin=1in]{geometry}" in preamble

    def test_preamble_has_natbib(self, intel_build):
        preamble = intel_build.generate_preamble()
        assert r"\usepackage{natbib}" in preamble

    def test_preamble_has_hyperref_blue(self, intel_build):
        preamble = intel_build.generate_preamble()
        assert "colorlinks=true" in preamble
        assert "blue" in preamble

    def test_preamble_has_enumitem(self, intel_build):
        preamble = intel_build.generate_preamble()
        assert "enumitem" in preamble


# ===========================================================================
# MARKDOWN → LATEX CONVERSION
# ===========================================================================

class TestMarkdownConversion:
    """Test markdown → LaTeX body conversion (shared patterns)."""

    def test_h1_becomes_title(self, fmt_build):
        """# Title → used for \\title{}, not \\section."""
        md = "# The Four-Model Theory of Consciousness\n\nSome text."
        result = fmt_build.convert_body(md)
        # H1 should NOT appear as \section
        assert r"\section{The Four-Model Theory" not in result

    def test_h2_becomes_section(self, fmt_build):
        """## Section → \\section{Section}"""
        md = "## 1. Introduction\n\nSome text."
        result = fmt_build.convert_body(md)
        assert r"\section{Introduction}" in result

    def test_h3_becomes_subsection(self, fmt_build):
        """### Subsection → \\subsection{Subsection}"""
        md = "### 1.1 The Pre-Paradigm State\n\nSome text."
        result = fmt_build.convert_body(md)
        assert r"\subsection{The Pre-Paradigm State}" in result

    def test_bold_to_textbf(self, fmt_build):
        """**bold** → \\textbf{bold}"""
        md = "This is **bold text** here."
        result = fmt_build.convert_body(md)
        assert r"\textbf{bold text}" in result

    def test_italic_to_emph(self, fmt_build):
        """*italic* → \\emph{italic}"""
        md = "This is *italic text* here."
        result = fmt_build.convert_body(md)
        assert r"\emph{italic text}" in result

    def test_em_dash(self, fmt_build):
        """ — → ---"""
        md = "first — second"
        result = fmt_build.convert_body(md)
        assert "---" in result

    def test_numbered_list(self, fmt_build):
        """Numbered list → enumerate."""
        md = "1. First item\n2. Second item\n3. Third item"
        result = fmt_build.convert_body(md)
        assert r"\begin{enumerate}" in result
        assert r"\item" in result

    def test_horizontal_rule_stripped(self, fmt_build):
        """--- on its own line should not produce visible output."""
        md = "Before\n\n---\n\nAfter"
        result = fmt_build.convert_body(md)
        # Should not remain as literal ---
        assert "\n---\n" not in result

    def test_special_chars_escaped(self, fmt_build):
        """& and % should be escaped in LaTeX."""
        md = "R&D costs are 50% of revenue."
        result = fmt_build.convert_body(md)
        assert r"R\&D" in result or r"R\&{}D" in result
        assert r"50\%" in result or r"50\%{}" in result

    def test_em_dash_has_break_hint(self, fmt_build):
        """Em dashes must include \\hspace{0pt} to allow line breaks."""
        md = "interventions — environments that support autonomy."
        result = fmt_build.convert_body(md)
        assert r"---\hspace{0pt}" in result
        assert "---environments" not in result  # no bare em dash without break hint


# ===========================================================================
# FMT: Full pipeline integration test
# ===========================================================================

class TestFmtFullPipeline:
    """Integration test: full .md → .tex → .pdf pipeline for FMT paper."""

    def test_generate_tex_from_md(self, fmt_build):
        """Generate .tex from .md and verify it's valid LaTeX."""
        tex = fmt_build.generate_tex()
        # Must start with documentclass
        assert tex.strip().startswith(r"\documentclass")
        # Must end with \end{document}
        assert r"\end{document}" in tex
        # Must have title
        assert r"\title{" in tex
        assert "Four-Model Theory" in tex
        # Must have author
        assert r"\author{" in tex
        assert "Matthias Gruber" in tex
        # Must have abstract
        assert r"\begin{abstract}" in tex
        # Must have bibliography
        assert r"\bibliography{references}" in tex
        # Must have sections
        assert r"\section{Introduction}" in tex

    def test_generated_tex_has_citations(self, fmt_build):
        """Generated .tex must contain natbib citation commands."""
        tex = fmt_build.generate_tex()
        assert r"\citep{" in tex
        assert r"\citet{" in tex

    def test_generated_tex_has_figures(self, fmt_build):
        """Generated .tex must include figure references."""
        tex = fmt_build.generate_tex()
        assert r"\includegraphics" in tex or r"\begin{figure}" in tex

    def test_generated_tex_has_acknowledgments(self, fmt_build):
        """Generated .tex must have acknowledgments section."""
        tex = fmt_build.generate_tex()
        assert "Acknowledgments" in tex or "Acknowledgements" in tex

    def test_build_tex_file(self, fmt_build):
        """Build the .tex file and verify it exists."""
        tex_path = os.path.join(REPO_ROOT, "paper/full/biorxiv/paper.tex")
        # Back up existing
        backup = tex_path + ".bak"
        if os.path.exists(tex_path):
            import shutil
            shutil.copy2(tex_path, backup)
        try:
            fmt_build.build_tex()
            assert os.path.exists(tex_path)
            with open(tex_path) as f:
                content = f.read()
            assert r"\documentclass" in content
            assert r"\end{document}" in content
        finally:
            # Restore backup
            if os.path.exists(backup):
                import shutil
                shutil.copy2(backup, tex_path)
                os.remove(backup)


# ===========================================================================
# INTELLIGENCE: Full pipeline integration test
# ===========================================================================

class TestIntelFullPipeline:
    """Integration test: full .md → .tex → .pdf pipeline for intelligence paper."""

    def test_generate_tex_from_md(self, intel_build):
        """Generate .tex from .md and verify it's valid LaTeX."""
        tex = intel_build.generate_tex()
        # Must start with documentclass
        assert tex.strip().startswith(r"\documentclass")
        # Must end with \end{document}
        assert r"\end{document}" in tex
        # Must have title
        assert r"\title{" in tex
        assert "Intelligence" in tex
        # Must have author
        assert r"\author{" in tex
        assert "Matthias Gruber" in tex
        # Must have abstract
        assert r"\begin{abstract}" in tex
        # Must have sections
        assert r"\section{" in tex
        # Must have bibliography (inline thebibliography)
        assert r"\begin{thebibliography}" in tex or r"\bibliography{" in tex

    def test_generated_tex_has_citations(self, intel_build):
        """Generated .tex must contain natbib citation commands."""
        tex = intel_build.generate_tex()
        assert r"\citep{" in tex or r"\citet{" in tex

    def test_generated_tex_has_keywords(self, intel_build):
        """Generated .tex must have keywords after abstract."""
        tex = intel_build.generate_tex()
        assert "Keywords" in tex or "keywords" in tex

    def test_build_tex_file(self, intel_build):
        """Build the .tex file and verify it exists."""
        tex_path = os.path.join(REPO_ROOT, "paper/intelligence/paper.tex")
        # Back up existing
        backup = tex_path + ".bak"
        if os.path.exists(tex_path):
            import shutil
            shutil.copy2(tex_path, backup)
        try:
            intel_build.build_tex()
            assert os.path.exists(tex_path)
            with open(tex_path) as f:
                content = f.read()
            assert r"\documentclass" in content
            assert r"\end{document}" in content
        finally:
            # Restore backup
            if os.path.exists(backup):
                import shutil
                shutil.copy2(backup, tex_path)
                os.remove(backup)


# ===========================================================================
# REFERENCE EXTRACTION
# ===========================================================================

class TestReferenceExtraction:
    """Test that references are correctly extracted from .md."""

    def test_fmt_extracts_reference_count(self, fmt_build, fmt_md):
        """FMT paper should extract ~70+ references."""
        refs = fmt_build.extract_references(fmt_md)
        assert len(refs) >= 60, f"Expected >=60 refs, got {len(refs)}"

    def test_intel_extracts_reference_count(self, intel_build, intel_md):
        """Intelligence paper should extract ~30+ references."""
        refs = intel_build.extract_references(intel_md)
        assert len(refs) >= 25, f"Expected >=25 refs, got {len(refs)}"


# ===========================================================================
# CONTENT FIDELITY: Key sections present
# ===========================================================================

class TestContentFidelity:
    """Verify that generated .tex preserves all sections from .md."""

    def test_fmt_all_sections_present(self, fmt_build, fmt_md):
        """All ## sections from .md must appear as \\section in .tex."""
        tex = fmt_build.generate_tex()
        # Extract section titles from .md (## N. Title)
        md_sections = re.findall(r'^## \d+\.\s+(.+)$', fmt_md, re.MULTILINE)
        for section in md_sections:
            # Section title should appear in tex (possibly reformatted)
            clean = section.strip()
            assert clean in tex or clean.replace(" — ", "---") in tex, \
                f"Section '{clean}' not found in generated .tex"

    def test_intel_all_sections_present(self, intel_build, intel_md):
        """All ## sections from .md must appear as \\section in .tex."""
        tex = intel_build.generate_tex()
        md_sections = re.findall(r'^## \d+\.\s+(.+)$', intel_md, re.MULTILINE)
        for section in md_sections:
            clean = section.strip()
            assert clean in tex or clean.replace(" — ", "---") in tex, \
                f"Section '{clean}' not found in generated .tex"


# ===========================================================================
# PDF COMPILATION (slow, optional)
# ===========================================================================

@pytest.mark.slow
class TestPdfCompilation:
    """Test that generated .tex actually compiles to PDF.

    Run with: pytest tmp/test_build_scripts.py -v -m slow
    """

    def test_fmt_compiles_to_pdf(self, fmt_build):
        """FMT .tex compiles to .pdf without errors."""
        result = fmt_build.build_pdf()
        assert result is True
        pdf_path = os.path.join(REPO_ROOT, "paper/full/biorxiv/paper.pdf")
        assert os.path.exists(pdf_path)
        assert os.path.getsize(pdf_path) > 10000  # Non-trivial PDF

    def test_intel_compiles_to_pdf(self, intel_build):
        """Intelligence .tex compiles to .pdf without errors."""
        result = intel_build.build_pdf()
        assert result is True
        pdf_path = os.path.join(REPO_ROOT, "paper/intelligence/paper.pdf")
        assert os.path.exists(pdf_path)
        assert os.path.getsize(pdf_path) > 10000


if __name__ == "__main__":
    # Default: skip slow tests
    args = sys.argv[1:] if len(sys.argv) > 1 else ["-v", "-m", "not slow"]
    pytest.main([__file__] + args)
