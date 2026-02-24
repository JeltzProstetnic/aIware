#!/usr/bin/env python3
"""PDF verification tests (Tier 4).

These tests verify that compiled PDFs have correct structure:
page counts, extractable text, section headings, no unresolved refs,
images present, no blank pages.

Run with: python3 -m pytest tmp/test_pdf_verification.py -v -m slow
Requires: PyMuPDF (fitz) and compiled PDFs on disk.
"""

import os
import re
import sys
import pytest

try:
    import fitz  # PyMuPDF
except ImportError:
    pytest.skip("PyMuPDF (fitz) not installed", allow_module_level=True)

REPO_ROOT = "/home/jeltz/aIware"

# Expected ranges — calibrated 2026-02-23
FMT_PDF_PATH = os.path.join(REPO_ROOT, "paper/full/biorxiv/paper.pdf")
FMT_PAGE_RANGE = (50, 70)       # current ~61 pages (grew with 2026 additions)
FMT_MIN_WORDS = 10_000          # at least 10k extractable words

INTEL_PDF_PATH = os.path.join(REPO_ROOT, "paper/intelligence/paper.pdf")
INTEL_PAGE_RANGE = (12, 30)     # current ~20 pages
INTEL_MIN_WORDS = 5_000         # at least 5k extractable words


def extract_all_text(pdf_path: str) -> str:
    """Extract all text from a PDF using PyMuPDF."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text


def get_page_texts(pdf_path: str) -> list[str]:
    """Get per-page text for a PDF."""
    doc = fitz.open(pdf_path)
    texts = [page.get_text() for page in doc]
    doc.close()
    return texts


def count_images(pdf_path: str) -> int:
    """Count total images across all pages."""
    doc = fitz.open(pdf_path)
    total = 0
    for page in doc:
        total += len(page.get_images())
    doc.close()
    return total


# =============================================================================
# FMT Paper — PDF Verification
# =============================================================================

@pytest.mark.slow
class TestFmtPdfVerification:
    """Tier 4: FMT paper PDF structural checks."""

    @pytest.fixture(autouse=True)
    def _require_pdf(self):
        if not os.path.exists(FMT_PDF_PATH):
            pytest.skip(f"FMT PDF not found: {FMT_PDF_PATH}")
        doc = fitz.open(FMT_PDF_PATH)
        pages = doc.page_count
        doc.close()
        if pages == 0:
            pytest.skip(f"FMT PDF unreadable by PyMuPDF (0 pages): {FMT_PDF_PATH}")

    def test_page_count_in_range(self):
        doc = fitz.open(FMT_PDF_PATH)
        pages = doc.page_count
        doc.close()
        lo, hi = FMT_PAGE_RANGE
        assert lo <= pages <= hi, \
            f"FMT PDF has {pages} pages, expected [{lo}, {hi}]"

    def test_text_extractable(self):
        text = extract_all_text(FMT_PDF_PATH)
        words = len(text.split())
        assert words >= FMT_MIN_WORDS, \
            f"FMT PDF has {words} extractable words, expected >= {FMT_MIN_WORDS}"

    def test_section_headings_present(self):
        text = extract_all_text(FMT_PDF_PATH)
        required = [
            "Introduction",
            "Eight Requirements",
            "Four-Model Theory",
            "Philosophical Commitments",
            "Binding",
            "Explanatory Range",
            "Comparative Analysis",
            "Testable Predictions",
            "Open Questions",
            "Discussion",
            "Conclusion",
        ]
        for heading in required:
            assert heading in text, \
                f"Section heading '{heading}' not found in PDF text"

    def test_no_unresolved_references(self):
        text = extract_all_text(FMT_PDF_PATH)
        # LaTeX unresolved refs show as "??" in PDF
        double_q = text.count("??")
        assert double_q == 0, \
            f"FMT PDF has {double_q} instances of '??' — unresolved LaTeX refs (bibtex likely failed)"

    def test_images_present(self):
        img_count = count_images(FMT_PDF_PATH)
        assert img_count >= 3, \
            f"FMT PDF has {img_count} images, expected >= 3"

    def test_no_blank_pages(self):
        texts = get_page_texts(FMT_PDF_PATH)
        for i, text in enumerate(texts):
            words = len(text.split())
            assert words >= 5, \
                f"FMT PDF page {i+1} appears blank ({words} words)"


# =============================================================================
# Intel Paper — PDF Verification
# =============================================================================

@pytest.mark.slow
class TestIntelPdfVerification:
    """Tier 4: Intelligence paper PDF structural checks."""

    @pytest.fixture(autouse=True)
    def _require_pdf(self):
        if not os.path.exists(INTEL_PDF_PATH):
            pytest.skip(f"Intel PDF not found: {INTEL_PDF_PATH}")

    def test_page_count_in_range(self):
        doc = fitz.open(INTEL_PDF_PATH)
        pages = doc.page_count
        doc.close()
        lo, hi = INTEL_PAGE_RANGE
        assert lo <= pages <= hi, \
            f"Intel PDF has {pages} pages, expected [{lo}, {hi}]"

    def test_text_extractable(self):
        text = extract_all_text(INTEL_PDF_PATH)
        words = len(text.split())
        assert words >= INTEL_MIN_WORDS, \
            f"Intel PDF has {words} extractable words, expected >= {INTEL_MIN_WORDS}"

    def test_section_headings_present(self):
        text = extract_all_text(INTEL_PDF_PATH)
        required = [
            "Curious Omission",
            "Status Quo",
            "Recursive",
            "Operational Knowledge",
            "AI",
            "Learnab",
            "Discussion",
            "Conclusion",
        ]
        for heading in required:
            assert heading in text, \
                f"Section heading '{heading}' not found in PDF text"

    def test_no_unresolved_references(self):
        text = extract_all_text(INTEL_PDF_PATH)
        double_q = text.count("??")
        assert double_q == 0, \
            f"Intel PDF has {double_q} instances of '??' — unresolved LaTeX refs (bibtex likely failed)"

    def test_no_blank_pages(self):
        texts = get_page_texts(INTEL_PDF_PATH)
        for i, text in enumerate(texts):
            words = len(text.split())
            assert words >= 5, \
                f"Intel PDF page {i+1} appears blank ({words} words)"


# =============================================================================
# Entry point
# =============================================================================

if __name__ == "__main__":
    args = sys.argv[1:] if len(sys.argv) > 1 else ["-v", "-m", "slow"]
    pytest.main([__file__] + args)
