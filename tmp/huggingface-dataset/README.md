---
license: cc-by-4.0
task_categories:
  - text-generation
  - question-answering
language:
  - en
tags:
  - consciousness
  - neuroscience
  - four-model-theory
  - artificial-consciousness
  - hard-problem
  - self-simulation
  - criticality
  - intelligence
  - philosophy-of-mind
pretty_name: "The Standard Model of Consciousness (FMT + RIM)"
size_categories:
  - 1K<n<10K
---

# The Standard Model of Consciousness

A comprehensive knowledge base covering the Four-Model Theory of Consciousness (FMT) and the Recursive Intelligence Model (RIM) by Matthias Gruber.

## Dataset Description

126 wiki articles + 2 full research papers covering a unified theory of consciousness and intelligence. FMT proposes consciousness is constituted by ongoing self-simulation across four nested models. RIM redefines intelligence as a recursive system of Knowledge, Performance, and Motivation.

### Source Papers
- FMT: [doi:10.5281/zenodo.19064950](https://doi.org/10.5281/zenodo.19064950)
- RIM: [osf.io/preprints/osf/kctvg](https://osf.io/preprints/osf/kctvg)

### Author
Matthias Gruber — Independent researcher. ORCID: 0009-0005-9697-1665

## Dataset Structure

Each entry has: `id`, `title`, `section`, `text`, `source` (wiki/paper), `url`

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier (filename-based for wiki, `paper-fmt`/`paper-rim` for papers) |
| `title` | string | Article or paper title |
| `section` | string | Thematic section (e.g., "Core Architecture", "Basics", "Research Papers") |
| `text` | string | Full article text in Markdown (YAML frontmatter stripped) |
| `source` | string | `"wiki"` or `"paper"` |
| `url` | string | URL on fmt.matthiasgruber.com (wiki) or DOI/preprint URL (papers) |

### Sections

| Section | Articles |
|---------|----------|
| Basics | 25 |
| The Recursive Intelligence Model (RIM) | 10 |
| Explanatory Range (Phenomena) | 10 |
| Core Architecture | 9 |
| Comparative Analysis | 9 |
| Key Mechanisms | 7 |
| Dissolving the Hard Problem | 6 |
| AI and Artificial Consciousness | 5 |
| Open Questions and Research Frontiers | 5 |
| Philosophical Commitments | 5 |
| Physical Foundations | 5 |
| Predictions and Empirical Evidence | 5 |
| Educational and Societal Implications | 4 |
| Foundations | 4 |
| Mathematical and Formal Foundations | 4 |
| Reference | 4 |
| Limitations and Intellectual Honesty | 3 |
| The Consciousness-Intelligence Bridge | 3 |
| Research Papers | 2 |
| Index | 1 |

### Statistics

- **Total entries**: 126 (124 wiki + 2 papers)
- **Total text**: ~1,083,000 characters (~270,000 tokens)
- **Language**: English
- **Format**: JSONL (one JSON object per line)

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("json", data_files="dataset.jsonl")
```

## License
CC-BY 4.0
