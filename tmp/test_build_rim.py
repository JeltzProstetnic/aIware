#!/usr/bin/env python3
"""Tests for RIM paper build script — citation verification.

Run: pytest tmp/test_build_rim.py -v
"""

import os
import sys
import tempfile

import pytest

# Add tmp/ to path so we can import the build script
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_rim_pdf import verify_citations


@pytest.fixture
def tex_with_matching_citations(tmp_path):
    """A .tex file where all cite keys match bibitem keys."""
    content = r"""
\documentclass{article}
\usepackage{natbib}
\begin{document}
As shown by \citet{Smith2020}, and confirmed by \citep{Jones2021}.
Also \citeauthor{Brown2019}'s \citeyearpar{Brown2019} work.

\begin{thebibliography}{3}
\bibitem[Smith, 2020]{Smith2020}
Smith, J. (2020). Title. \emph{Journal}, 1, 1--10.

\bibitem[Jones, 2021]{Jones2021}
Jones, A. (2021). Title. \emph{Journal}, 2, 20--30.

\bibitem[Brown, 2019]{Brown2019}
Brown, B. (2019). Title. \emph{Journal}, 3, 30--40.
\end{thebibliography}
\end{document}
"""
    f = tmp_path / "good.tex"
    f.write_text(content)
    return str(f)


@pytest.fixture
def tex_with_missing_bibitem(tmp_path):
    """A .tex file where a cite key has no matching bibitem."""
    content = r"""
\documentclass{article}
\usepackage{natbib}
\begin{document}
\citet{Smith2020} and \citet{Ghost2025}.

\begin{thebibliography}{1}
\bibitem[Smith, 2020]{Smith2020}
Smith, J. (2020). Title. \emph{Journal}, 1, 1--10.
\end{thebibliography}
\end{document}
"""
    f = tmp_path / "missing.tex"
    f.write_text(content)
    return str(f)


@pytest.fixture
def tex_with_unused_bibitem(tmp_path):
    """A .tex file where a bibitem is defined but never cited."""
    content = r"""
\documentclass{article}
\usepackage{natbib}
\begin{document}
\citet{Smith2020}.

\begin{thebibliography}{2}
\bibitem[Smith, 2020]{Smith2020}
Smith, J. (2020). Title. \emph{Journal}, 1, 1--10.

\bibitem[Orphan, 2023]{Orphan2023}
Orphan, X. (2023). Title. \emph{Journal}, 5, 50--60.
\end{thebibliography}
\end{document}
"""
    f = tmp_path / "unused.tex"
    f.write_text(content)
    return str(f)


@pytest.fixture
def tex_with_etal_needed(tmp_path):
    """A .tex file where a 3+ author bibitem uses & instead of et al."""
    content = r"""
\documentclass{article}
\usepackage{natbib}
\begin{document}
\citet{Multi2020}.

\begin{thebibliography}{1}
\bibitem[Alpha \& Gamma, 2020]{Multi2020}
Alpha, A., Beta, B., \& Gamma, G. (2020). Title. \emph{Journal}, 1, 1--10.
\end{thebibliography}
\end{document}
"""
    f = tmp_path / "etal.tex"
    f.write_text(content)
    return str(f)


@pytest.fixture
def tex_with_etal_correct(tmp_path):
    """A .tex file where 3+ author bibitem correctly uses et al."""
    content = r"""
\documentclass{article}
\usepackage{natbib}
\begin{document}
\citet{Multi2020}.

\begin{thebibliography}{1}
\bibitem[Alpha et~al., 2020]{Multi2020}
Alpha, A., Beta, B., \& Gamma, G. (2020). Title. \emph{Journal}, 1, 1--10.
\end{thebibliography}
\end{document}
"""
    f = tmp_path / "etal_ok.tex"
    f.write_text(content)
    return str(f)


class TestVerifyCitations:
    """Tests for the citation verification function."""

    def test_matching_citations_pass(self, tex_with_matching_citations):
        ok, errors = verify_citations(tex_with_matching_citations)
        assert ok is True
        assert errors == []

    def test_missing_bibitem_detected(self, tex_with_missing_bibitem):
        ok, errors = verify_citations(tex_with_missing_bibitem)
        assert ok is False
        assert any("CITE WITHOUT BIBITEM: Ghost2025" in e for e in errors)

    def test_unused_bibitem_detected(self, tex_with_unused_bibitem):
        ok, errors = verify_citations(tex_with_unused_bibitem)
        assert ok is False
        assert any("BIBITEM NEVER CITED: Orphan2023" in e for e in errors)

    def test_etal_needed_detected(self, tex_with_etal_needed):
        ok, errors = verify_citations(tex_with_etal_needed)
        assert ok is False
        assert any("LABEL NEEDS et al." in e for e in errors)

    def test_etal_correct_passes(self, tex_with_etal_correct):
        ok, errors = verify_citations(tex_with_etal_correct)
        assert ok is True
        assert errors == []

    def test_real_rim_paper_passes(self):
        """The actual RIM paper .tex should have zero citation issues."""
        tex_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "paper", "intelligence", "paper.tex",
        )
        if not os.path.exists(tex_path):
            pytest.skip("RIM paper.tex not found")
        ok, errors = verify_citations(tex_path)
        assert ok is True, f"Citation issues in paper.tex:\n" + "\n".join(errors)


class TestVerifyCitationsEdgeCases:
    """Edge cases for citation key extraction."""

    def test_citealp_keys_extracted(self, tmp_path):
        content = r"""
\documentclass{article}
\begin{document}
\citealp{KeyA,KeyB}

\begin{thebibliography}{2}
\bibitem[A, 2020]{KeyA}
A. (2020). Title.
\bibitem[B, 2021]{KeyB}
B. (2021). Title.
\end{thebibliography}
\end{document}
"""
        f = tmp_path / "citealp.tex"
        f.write_text(content)
        ok, errors = verify_citations(str(f))
        assert ok is True

    def test_multiple_keys_in_single_cite(self, tmp_path):
        content = r"""
\documentclass{article}
\begin{document}
\citep{A2020,B2021,C2022}

\begin{thebibliography}{3}
\bibitem[A, 2020]{A2020}
A. (2020). Title.
\bibitem[B, 2021]{B2021}
B. (2021). Title.
\bibitem[C, 2022]{C2022}
C. (2022). Title.
\end{thebibliography}
\end{document}
"""
        f = tmp_path / "multi.tex"
        f.write_text(content)
        ok, errors = verify_citations(str(f))
        assert ok is True
