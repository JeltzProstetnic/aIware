#!/usr/bin/env python3
"""Shared fixtures for all paper build/integrity tests.

Used by: test_build_scripts.py, test_content_integrity.py, test_pdf_verification.py
"""

import os
import importlib.util
import pytest

REPO_ROOT = "/home/jeltz/aIware"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def import_module_from_path(name, path):
    """Import a Python file as a module."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# Build script modules
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def fmt_build():
    """Import the FMT build script."""
    path = os.path.join(REPO_ROOT, "tmp", "build_fmt_full_pdf.py")
    return import_module_from_path("build_fmt_full_pdf", path)


@pytest.fixture(scope="session")
def intel_build():
    """Import the intelligence build script."""
    path = os.path.join(REPO_ROOT, "tmp", "build_intelligence_pdf.py")
    return import_module_from_path("build_intelligence_pdf", path)


# ---------------------------------------------------------------------------
# Raw .md content
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def fmt_md():
    """Read the FMT .md source."""
    with open(os.path.join(REPO_ROOT, "paper/full/four-model-theory-full.md")) as f:
        return f.read()


@pytest.fixture(scope="session")
def intel_md():
    """Read the intelligence paper .md source."""
    with open(os.path.join(REPO_ROOT, "paper/intelligence/paper.md")) as f:
        return f.read()


# ---------------------------------------------------------------------------
# Existing .tex content (on disk, possibly hand-maintained or generated)
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def fmt_existing_tex():
    """Read the existing FMT .tex."""
    with open(os.path.join(REPO_ROOT, "paper/full/biorxiv/paper.tex")) as f:
        return f.read()


@pytest.fixture(scope="session")
def intel_existing_tex():
    """Read the existing intelligence .tex."""
    with open(os.path.join(REPO_ROOT, "paper/intelligence/paper.tex")) as f:
        return f.read()


# ---------------------------------------------------------------------------
# Generated .tex content (freshly built from .md each test run)
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def fmt_generated_tex(fmt_build):
    """Generate fresh .tex from the FMT build script."""
    return fmt_build.generate_tex()


@pytest.fixture(scope="session")
def intel_generated_tex(intel_build):
    """Generate fresh .tex from the intelligence build script."""
    return intel_build.generate_tex()


# ---------------------------------------------------------------------------
# pytest configuration
# ---------------------------------------------------------------------------

def pytest_configure(config):
    config.addinivalue_line("markers", "slow: marks tests as slow (PDF compilation)")
