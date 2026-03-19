Action: act

# Wiki Post-Production — Next Session

## Context
Session 167 produced 99 wiki articles + index page for fmt.matthiasgruber.com. All committed and pushed to private. Infrastructure handover inbox item created.

## Remaining Tasks

### 1. Jargon Scan → Basics Articles (Section XVIII)
Scan all 99 articles for terms non-scientists would struggle with. Create standalone explainer articles in `wiki/basics/`. Can use CC/public domain content. Expected ~20-25 articles. Candidates identified so far:
- Cellular automaton, criticality/edge of chaos, phase transitions
- Panpsychism, Combination Problem
- Default Mode Network, prediction error, synaptic weights
- Qualia, phenomenal consciousness, phenomenology
- Working memory, crystallized vs fluid intelligence
- Neuronal avalanches, Lempel-Ziv complexity
- Callosotomy, anosognosia (medical), ego dissolution
- Recurrent processing, global broadcasting, interoception
- Metacognition, self-determination theory
- Others TBD from scan

### 2. Citation Pass — DOI/PDF Links
Every claim in every article should link to original research (PDF where available). Use `references.md` master list. Format: `[Author et al., Year](DOI-URL)` inline.

### 3. Figure Audit
- Assign anatomical images from `wiki/assets/book-originals/` to specific articles
- Key candidates: cortical homunculus → cortical-automaton.md, medial brain section → five-system-hierarchy.md, neuron diagram → implicit-world-model.md, six cortical layers → cortical-automaton.md, Brodmann areas → cortical-automaton.md, fMRI slices → decoding-virtual.md
- Identify articles needing additional figures beyond Mermaid

### 4. AI Art Briefs → Muse Inbox
Write specific briefs for muse project to generate hero images. ~5-10 images.

### 5. SEO Frontmatter Verification
Some early articles (wave 1) may lack `description:` and `keywords:` in frontmatter. Verify all 100 files have complete SEO fields.

## Files
- Wiki content: `wiki/` (99 articles + index + style guide + infra spec)
- Wiki structure: `docs/wiki-structure-proposal.md`
- Anatomical images: `wiki/assets/book-originals/` (25 images + INDEX.md)
- Infrastructure spec: `wiki/INFRASTRUCTURE-SPEC.md`
- Backlog item: AIW-27
