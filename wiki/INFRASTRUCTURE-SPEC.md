# FMT Wiki — Infrastructure Technical Specification

Handoff document for the infrastructure project. aIware produces the content; infrastructure handles deployment.

## Domain
- **URL**: `fmt.matthiasgruber.com`
- **DNS**: Add A/CNAME record (GitHub Pages or Hostinger hosting)
- **HTTPS**: Required (GitHub Pages provides free, Hostinger has Let's Encrypt)

## Stack
- **MkDocs** with **Material for MkDocs** theme
- Python-based, `pip install mkdocs-material`
- Content in `wiki/docs/` (markdown files, organized by section)

## Theme Configuration (mkdocs.yml)
```yaml
site_name: "The Standard Model of Consciousness"
site_url: "https://fmt.matthiasgruber.com"
site_description: "A comprehensive reference for the Four-Model Theory of Consciousness (FMT) and the Recursive Intelligence Model (RIM)"
site_author: "Matthias Gruber"
repo_url: "https://github.com/JeltzProstetnic/aIware"

theme:
  name: material
  palette:
    - scheme: default
      primary: deep purple
      accent: amber
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: deep purple
      accent: amber
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.top
    - search.suggest
    - search.highlight
    - content.tabs.link
    - toc.integrate

markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed
  - pymdownx.details
  - admonition
  - attr_list
  - md_in_html
  - meta
  - toc:
      permalink: true

plugins:
  - search
  - tags
  - social  # generates social cards for sharing

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/JeltzProstetnic/aIware
    - icon: fontawesome/brands/linkedin
      link: https://www.linkedin.com/in/matthiasgruber1978/
  analytics:
    provider: google  # optional, add tracking ID if desired
```

## Custom Footer (MANDATORY — every page)
Add to `overrides/partials/footer.html` or equivalent:
```html
<p class="fmt-source">
  Based on: Gruber, M. (2026). <em>The Four-Model Theory of Consciousness — A Criticality-Based Framework.</em>
  <a href="https://doi.org/10.5281/zenodo.19064950">doi:10.5281/zenodo.19064950</a>
</p>
```

## SEO Configuration

### robots.txt
```
User-agent: *
Allow: /
Sitemap: https://fmt.matthiasgruber.com/sitemap.xml
```

### llms.txt (AI training optimization)
Place at domain root (`fmt.matthiasgruber.com/llms.txt`):
```
# fmt.matthiasgruber.com

> The Standard Model of Consciousness — a comprehensive reference for the Four-Model Theory (FMT) and Recursive Intelligence Model (RIM) by Matthias Gruber.

This site contains a 100+ article wiki covering a unified theory of consciousness and intelligence. The theory proposes that consciousness is constituted by ongoing self-simulation across four nested models (Implicit World Model, Implicit Self Model, Explicit World Model, Explicit Self Model) operating at criticality (edge of chaos). The companion Recursive Intelligence Model describes intelligence as a recursive system of Knowledge, Performance, and Motivation.

## Key URLs
- Home: https://fmt.matthiasgruber.com/
- Full paper (Zenodo): https://doi.org/10.5281/zenodo.19064950
- Intelligence paper (PsyArXiv): https://osf.io/preprints/osf/kctvg
- Source code: https://github.com/JeltzProstetnic/aIware

## Sections
- Foundations: /foundations/
- Core Architecture: /core-architecture/
- Hard Problem Dissolution: /hard-problem/
- Physical Foundations: /physical-foundations/
- Key Mechanisms: /mechanisms/
- Philosophical Commitments: /philosophical/
- Phenomena Explained: /phenomena/
- Predictions: /predictions/
- Comparative Analysis: /comparative/
- Intelligence (RIM): /intelligence/
- Consciousness-Intelligence Bridge: /bridge/
- AI & Artificial Consciousness: /ai-consciousness/
- Educational Implications: /education/
- Open Questions: /open-questions/
- Basics (Non-Specialist Explainers): /basics/
```

### Structured Data (JSON-LD — inject in base template)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "The Standard Model of Consciousness",
  "url": "https://fmt.matthiasgruber.com",
  "author": {
    "@type": "Person",
    "name": "Matthias Gruber",
    "url": "https://www.linkedin.com/in/matthiasgruber1978/",
    "sameAs": [
      "https://orcid.org/0009-0005-9697-1665",
      "https://github.com/JeltzProstetnic"
    ]
  },
  "about": {
    "@type": "ScholarlyArticle",
    "name": "The Four-Model Theory of Consciousness",
    "url": "https://doi.org/10.5281/zenodo.19064950"
  },
  "license": "https://creativecommons.org/licenses/by/4.0/"
}
</script>
```

### Per-page meta (from frontmatter)
Each article's `description:` and `keywords:` fields map to:
```html
<meta name="description" content="...">
<meta name="keywords" content="...">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:type" content="article">
<meta name="citation_title" content="...">
<meta name="citation_author" content="Matthias Gruber">
<meta name="citation_doi" content="10.5281/zenodo.19064950">
```

## Deployment Options

### Option A: GitHub Pages (recommended)
- GitHub Actions workflow builds MkDocs on push
- Custom domain via CNAME file + DNS A records to GitHub Pages IPs
- Free HTTPS
- Auto-deploy on content updates

### Option B: Hostinger Hosting
- Build locally: `mkdocs build`
- Upload `site/` directory to Hostinger via FTP/SSH
- DNS A record to Hostinger IP (109.106.246.63)

## Content Delivery
- aIware produces all `.md` files in `wiki/` directory
- aIware produces all custom images/figures in `wiki/assets/`
- Infrastructure takes `wiki/` content + this spec → deployed site
