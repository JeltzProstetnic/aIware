#!/usr/bin/env python3
"""Content integrity tests for the publication pipeline (Tiers 1-3).

Tier 1: Structural Parity — .md vs .tex section/table/figure counts
Tier 2: Content Volume Guards — word counts and reference counts in plausible ranges
Tier 3: Canary Phrases — hand-picked phrases that must survive conversion

Run with: python3 -m pytest tmp/test_content_integrity.py -v
"""

import os
import re
import sys
import pytest
from conftest import REPO_ROOT


# =============================================================================
# Utility functions
# =============================================================================

def extract_tex_body(tex: str) -> str:
    """Extract body text between end of abstract and bibliography.

    Returns the portion of the .tex after \\end{abstract} and before
    \\bibliography{} or \\begin{thebibliography}.
    """
    abs_end = tex.find(r"\end{abstract}")
    if abs_end == -1:
        return tex  # fallback: whole document
    abs_end += len(r"\end{abstract}")

    bib_start = tex.find(r"\bibliography{")
    if bib_start == -1:
        bib_start = tex.find(r"\begin{thebibliography}")
    if bib_start == -1:
        bib_start = len(tex)

    return tex[abs_end:bib_start]


def count_tex_words(tex_body: str) -> int:
    """Count words after stripping LaTeX commands, braces, and comments."""
    # Remove comments
    stripped = re.sub(r"%.*$", "", tex_body, flags=re.MULTILINE)
    # Remove \command[opt]{arg} → keep arg
    stripped = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?\{([^}]*)\}", r"\2", stripped)
    # Remove remaining \commands
    stripped = re.sub(r"\\[a-zA-Z]+\*?", "", stripped)
    # Remove braces and backslashes
    stripped = re.sub(r"[{}\\]", "", stripped)
    # Remove LaTeX environments markers
    stripped = re.sub(r"begin|end", "", stripped)
    return len(stripped.split())


def extract_tex_references(tex: str) -> int:
    """Count references: \\bibitem in .tex or .bbl, or entries in thebibliography."""
    bibitems = len(re.findall(r"\\bibitem", tex))
    if bibitems > 0:
        return bibitems
    # For external .bbl: count \bibliography command presence, return 0 as
    # we can't read the .bbl from the .tex alone — Tier 2 will use a different approach
    return 0


# =============================================================================
# Tier 2 Calibration Constants
# =============================================================================
# Calibrated 2026-02-23 against current .md sources.
# Update only when cumulative edits exceed ±25%.

# FMT paper: md body = 17,205 words; tex body ≈ 16,106 words
FMT_BODY_WORD_RANGE = (13_000, 21_000)
# FMT: .bbl has 81 bibitems
FMT_REFERENCE_RANGE = (65, 110)
# FMT: 87 \citep + 17 \citet = 104
FMT_CITATION_CMD_MIN = 50

# Intel paper: md body = 7,428 words; tex body ≈ 8,108 words
INTEL_BODY_WORD_RANGE = (5_500, 10_500)
# Intel: 51 bibitems in thebibliography
INTEL_REFERENCE_RANGE = (35, 70)
# Intel: 24 \citep + 20 \citet = 44
INTEL_CITATION_CMD_MIN = 25


# =============================================================================
# Tier 3 Canary Phrases
# =============================================================================
# Selection criteria:
# - At least one from each numbered section
# - Phrases near float injection anchors
# - Phrases with conversion-hazardous characters (& umlauts em dashes)
# - Core theoretical terms that will never be removed

FMT_CANARY_PHRASES = [
    # Section 1 — Introduction
    "pre-paradigm state",
    "COGITATE adversarial collaboration",
    "decisive empirical or theoretical superiority",
    # Section 2 — Eight Requirements
    "Explanatory Gap",
    "Boundary Problem",
    "Meta-Problem",
    "Unity and Binding",
    # Section 3 — The Four-Model Theory (core concepts)
    "Implicit World Model",
    "Explicit Self Model",
    "virtual qualia",
    "category error",
    "Cortical Automaton",
    "Five-System Hierarchy",
    "Two Thresholds for Consciousness",
    # Section 3 — key claim (long phrase survives regex?)
    "simulation does, and within the simulation",
    # Section 4 — Philosophical Commitments
    "Process Physicalism",
    "substrate independence",
    "weak emergence",
    # Section 5 — Binding & Criticality (near Table 2 anchor)
    "edge of chaos",
    "Holographic Storage",
    "Patchwork Principle",
    "critical dynamics",
    # Section 6 — Explanatory Range (near Table 3 anchor)
    "ego dissolution",
    "psychedelic phenomenology",
    "split-brain",
    "animal consciousness",
    "Clinical Psychology Bridge",
    # Section 7 — Comparative Analysis (IS a float anchor)
    "Scoring Matrix",
    "theory-by-theory",
    "Emerging Frameworks",
    # Section 8 — Testable Predictions
    "testable predictions",
    "fMRI Signatures",
    "Anosognosia",
    "Sleep Architecture",
    "DID Alters",
    "Ultimate Prediction",
    # Section 9 + 10
    "open questions",
    "Artificial Consciousness",
    # Near hazardous characters
    "Hengen",              # near & in "Hengen & Shew"
    "Albantakis",          # near et al.
    "IIT pseudoscientific",  # controversial phrase with special conversion
]

INTEL_CANARY_PHRASES = [
    # Section 1 — Introduction
    "Curious Omission",
    "sustained drive to learn",
    "opened a book since leaving school",
    # Section 2 — Status Quo
    "Cattell-Horn-Carroll",
    "CHC taxonomy",
    "investment theory",
    "triarchic theory",
    "Multiple Intelligences",
    "Wechsler",
    # Section 3 — Recursive System
    "recursive",
    "self-reinforcing system",
    "closed amplification loop",
    "three-component",
    # Section 4 — Operational Knowledge
    "operational knowledge",
    "learning strategies",
    "strategic thinking",
    "Hidden Multiplier",
    # Section 5 — AI Implication
    "artificial intelligence",
    "vast knowledge and computational performance",
    "intrinsic motivation",
    # Section 6 — Learnability
    "intelligence is, to a large extent",
    "compounding effects",
    "School Grade Disaster",
    "Performance Is Not the Bottleneck",
    # Section 7 — Discussion
    "stereotype threat",
    "self-reinforcing",
    "testable predictions",
    "Historical Note",
    # Section 8 — Conclusion
    "learning ability",
    # Near hazardous characters
    "Steele",              # near & in Steele & Aronson
    "Dignath",             # near & in Dignath & Büttner
    "von Stumm",           # lowercase "von"
]


# =============================================================================
# TIER 1: Structural Parity — FMT Paper
# =============================================================================

class TestFmtStructuralParity:
    """Tier 1: Verify .md structure is preserved in generated .tex."""

    def test_section_count_matches(self, fmt_md, fmt_generated_tex):
        """Every ## N. in .md must produce a \\section in .tex."""
        md_sections = re.findall(r"^## \d+\.", fmt_md, re.MULTILINE)
        tex_sections = re.findall(r"\\section\{", fmt_generated_tex)
        assert len(tex_sections) >= len(md_sections), \
            f"md has {len(md_sections)} sections, tex has {len(tex_sections)}"

    def test_subsection_count_matches(self, fmt_md, fmt_generated_tex):
        """### in .md must produce \\subsection in .tex (±2 tolerance)."""
        md_sub = len(re.findall(r"^### ", fmt_md, re.MULTILINE))
        tex_sub = len(re.findall(r"\\subsection\{", fmt_generated_tex))
        assert abs(tex_sub - md_sub) <= 2, \
            f"md has {md_sub} subsections, tex has {tex_sub} (diff > 2)"

    def test_section_titles_preserved(self, fmt_md, fmt_generated_tex):
        """Every section title text from .md appears somewhere in .tex."""
        md_titles = re.findall(r"^## \d+\.\s+(.+)$", fmt_md, re.MULTILINE)
        for title in md_titles:
            clean = title.strip()
            # Title may have em dashes converted
            variants = [clean, clean.replace(" — ", "---"), clean.replace(" — ", " --- ")]
            found = any(v in fmt_generated_tex for v in variants)
            assert found, f"Section title '{clean}' not found in .tex"

    def test_table_count_matches(self, fmt_md, fmt_generated_tex):
        """Table count: **Table N in .md vs \\begin{table} in .tex (exact match)."""
        md_tables = len(re.findall(r"\*\*Table \d+", fmt_md))
        tex_tables = len(re.findall(r"\\begin\{table", fmt_generated_tex))
        assert tex_tables == md_tables, \
            f"md has {md_tables} tables, tex has {tex_tables} — float injection likely failed"

    def test_figure_count(self, fmt_generated_tex):
        """At least 3 figures expected (known FLOAT_FIG constants)."""
        tex_figs = len(re.findall(r"\\begin\{figure", fmt_generated_tex))
        assert tex_figs >= 3, f"Expected >=3 figures, got {tex_figs}"

    def test_all_cite_keys_have_bib_entries(self, fmt_generated_tex):
        """Every \\cite key in .tex must exist in references.bib."""
        bib_path = os.path.join(REPO_ROOT, "paper/full/biorxiv/references.bib")
        if not os.path.exists(bib_path):
            pytest.skip("references.bib not found")
        bib_text = open(bib_path).read()
        bib_keys = set(re.findall(r"@\w+\{(\w+),", bib_text))
        # Extract all citation keys from \cite, \citep, \citet, \citealt, \citealp, \citeauthor, \citeyearpar
        cite_keys = set()
        for match in re.finditer(r"\\cite[a-z]*\{([^}]+)\}", fmt_generated_tex):
            for key in match.group(1).split(","):
                cite_keys.add(key.strip())
        missing = cite_keys - bib_keys
        assert len(missing) == 0, \
            f"{len(missing)} citation keys missing from .bib: {sorted(missing)}"

    def test_unnumbered_sections_preserved(self, fmt_generated_tex):
        """Acknowledgments, Data Availability, Funding must exist."""
        for section_name in ["Acknowledgments", "Data Availability", "Funding"]:
            assert section_name in fmt_generated_tex, \
                f"Unnumbered section '{section_name}' not found in .tex"

    def test_no_empty_sections(self, fmt_generated_tex):
        """Every \\section must be followed by ≥50 words before the next section."""
        body = extract_tex_body(fmt_generated_tex)
        sections = re.split(r"\\section\{", body)
        for i, sec in enumerate(sections[1:], 1):  # skip pre-first-section
            # Get text up to next \section or end
            next_sec = re.search(r"\\section\{", sec)
            chunk = sec[:next_sec.start()] if next_sec else sec
            words = count_tex_words(chunk)
            assert words >= 50, \
                f"Section #{i} has only {words} words (expected ≥50)"


# =============================================================================
# TIER 1: Structural Parity — Intel Paper
# =============================================================================

class TestIntelStructuralParity:
    """Tier 1: Verify .md structure is preserved in generated .tex."""

    def test_section_count_matches(self, intel_md, intel_generated_tex):
        md_sections = re.findall(r"^## \d+\.", intel_md, re.MULTILINE)
        tex_sections = re.findall(r"\\section\{", intel_generated_tex)
        assert len(tex_sections) >= len(md_sections), \
            f"md has {len(md_sections)} sections, tex has {len(tex_sections)}"

    def test_subsection_count_matches(self, intel_md, intel_generated_tex):
        md_sub = len(re.findall(r"^### ", intel_md, re.MULTILINE))
        tex_sub = len(re.findall(r"\\subsection\{", intel_generated_tex))
        assert abs(tex_sub - md_sub) <= 2, \
            f"md has {md_sub} subsections, tex has {tex_sub} (diff > 2)"

    def test_section_titles_preserved(self, intel_md, intel_generated_tex):
        md_titles = re.findall(r"^## \d+\.\s+(.+)$", intel_md, re.MULTILINE)
        for title in md_titles:
            clean = title.strip()
            variants = [clean, clean.replace(" — ", "---"), clean.replace(" — ", " --- ")]
            found = any(v in intel_generated_tex for v in variants)
            assert found, f"Section title '{clean}' not found in .tex"

    def test_unnumbered_sections_preserved(self, intel_generated_tex):
        assert "Acknowledgments" in intel_generated_tex or \
               "Acknowledgements" in intel_generated_tex, \
            "Acknowledgments section not found in .tex"

    def test_no_empty_sections(self, intel_generated_tex):
        body = extract_tex_body(intel_generated_tex)
        sections = re.split(r"\\section\{", body)
        for i, sec in enumerate(sections[1:], 1):
            next_sec = re.search(r"\\section\{", sec)
            chunk = sec[:next_sec.start()] if next_sec else sec
            words = count_tex_words(chunk)
            assert words >= 50, \
                f"Section #{i} has only {words} words (expected ≥50)"


# =============================================================================
# TIER 2: Content Volume Guards — FMT Paper
# =============================================================================

class TestFmtContentVolume:
    """Tier 2: Word counts and reference counts in plausible fixed ranges."""

    def test_body_word_count_in_range(self, fmt_generated_tex):
        body = extract_tex_body(fmt_generated_tex)
        words = count_tex_words(body)
        lo, hi = FMT_BODY_WORD_RANGE
        assert lo <= words <= hi, \
            f"FMT body words = {words}, expected [{lo}, {hi}]"

    def test_citation_commands_minimum(self, fmt_generated_tex):
        citep = len(re.findall(r"\\citep\{", fmt_generated_tex))
        citet = len(re.findall(r"\\citet\{", fmt_generated_tex))
        total = citep + citet
        assert total >= FMT_CITATION_CMD_MIN, \
            f"FMT cite commands = {total}, expected >= {FMT_CITATION_CMD_MIN}"

    def test_bold_count_approximate(self, fmt_md, fmt_generated_tex):
        """\\textbf{} count ≈ ** count ±40%."""
        md_bold = len(re.findall(r"\*\*[^*]+\*\*", fmt_md))
        tex_bold = len(re.findall(r"\\textbf\{", fmt_generated_tex))
        if md_bold > 0:
            ratio = tex_bold / md_bold
            assert 0.4 <= ratio <= 1.6, \
                f"Bold ratio tex/md = {ratio:.2f} ({tex_bold}/{md_bold})"


# =============================================================================
# TIER 2: Content Volume Guards — Intel Paper
# =============================================================================

class TestIntelContentVolume:
    """Tier 2: Word counts and reference counts in plausible fixed ranges."""

    def test_body_word_count_in_range(self, intel_generated_tex):
        body = extract_tex_body(intel_generated_tex)
        words = count_tex_words(body)
        lo, hi = INTEL_BODY_WORD_RANGE
        assert lo <= words <= hi, \
            f"Intel body words = {words}, expected [{lo}, {hi}]"

    def test_reference_count_in_range(self, intel_generated_tex):
        refs = len(re.findall(r"\\bibitem", intel_generated_tex))
        lo, hi = INTEL_REFERENCE_RANGE
        assert lo <= refs <= hi, \
            f"Intel references = {refs}, expected [{lo}, {hi}]"

    def test_citation_commands_minimum(self, intel_generated_tex):
        citep = len(re.findall(r"\\citep\{", intel_generated_tex))
        citet = len(re.findall(r"\\citet\{", intel_generated_tex))
        total = citep + citet
        assert total >= INTEL_CITATION_CMD_MIN, \
            f"Intel cite commands = {total}, expected >= {INTEL_CITATION_CMD_MIN}"

    def test_bold_count_approximate(self, intel_md, intel_generated_tex):
        md_bold = len(re.findall(r"\*\*[^*]+\*\*", intel_md))
        tex_bold = len(re.findall(r"\\textbf\{", intel_generated_tex))
        if md_bold > 0:
            ratio = tex_bold / md_bold
            assert 0.4 <= ratio <= 1.6, \
                f"Bold ratio tex/md = {ratio:.2f} ({tex_bold}/{md_bold})"


# =============================================================================
# TIER 3: Canary Phrases — FMT Paper
# =============================================================================

class TestFmtCanaryPhrases:
    """Tier 3: Hand-picked phrases from .md must survive in generated .tex.

    Each canary is a phrase that:
    - Exists in the .md source (verified at calibration time)
    - Will never be intentionally removed from the paper
    - Tests a specific vulnerability (section boundary, float anchor, special char)

    If a canary fails, the conversion likely has a bug — these phrases don't
    get edited out during normal authoring.
    """

    @pytest.mark.parametrize("phrase", FMT_CANARY_PHRASES)
    def test_canary_survives_conversion(self, phrase, fmt_md, fmt_generated_tex):
        # First verify the canary exists in source
        assert phrase in fmt_md, \
            f"STALE CANARY: '{phrase}' no longer in .md — update canary list"
        # Then verify it survived conversion (possibly with LaTeX escaping)
        # Try direct match, then with common LaTeX transformations
        variants = [
            phrase,
            phrase.replace("&", r"\&"),
            phrase.replace(" — ", "---"),
            phrase.replace(" — ", " --- "),
        ]
        found = any(v in fmt_generated_tex for v in variants)
        assert found, \
            f"CANARY DEAD: '{phrase}' is in .md but NOT in .tex — conversion bug!"


# =============================================================================
# TIER 3: Canary Phrases — Intel Paper
# =============================================================================

class TestIntelCanaryPhrases:
    """Tier 3: Hand-picked phrases from .md must survive in generated .tex."""

    @pytest.mark.parametrize("phrase", INTEL_CANARY_PHRASES)
    def test_canary_survives_conversion(self, phrase, intel_md, intel_generated_tex):
        assert phrase in intel_md, \
            f"STALE CANARY: '{phrase}' no longer in .md — update canary list"
        variants = [
            phrase,
            phrase.replace("&", r"\&"),
            phrase.replace(" — ", "---"),
            phrase.replace(" — ", " --- "),
            phrase.replace("ü", r"\"{u}"),
            phrase.replace("å", r"\r{a}"),
            phrase.replace("é", r"\'{e}"),
        ]
        found = any(v in intel_generated_tex for v in variants)
        assert found, \
            f"CANARY DEAD: '{phrase}' is in .md but NOT in .tex — conversion bug!"


# =============================================================================
# Entry point
# =============================================================================

if __name__ == "__main__":
    args = sys.argv[1:] if len(sys.argv) > 1 else ["-v"]
    pytest.main([__file__] + args)
