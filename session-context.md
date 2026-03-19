# Session Context

## Session Info
- **Last Updated**: 2026-03-19T11:45:00+01:00
- **Machine**: WSL
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Gmail triage, FMT wiki content production, Wittmann co-author outreach

## Current State
- **Active Task**: Wiki content production complete, handover to infrastructure
- **Progress** (use `- [x]` checkbox for each completed item):
- [x] Gmail triage — 10 inbox messages processed, 2 Bartl mail ingested+trashed
- [x] PLREV rejection noted, AIW-07 updated → NBSR next
- [x] Perplexity/Ivoclar routed to ivoclar inbox
- [x] Stewart papers evaluated (shallow convergence, archived)
- [x] Blog inbox item confirmed (already exists for social)
- [x] Wiki structure defined — 100 articles across 17+1 sections (`docs/wiki-structure-proposal.md`)
- [x] Style guide created (`wiki/STYLE-GUIDE.md`) — SEO, AI optimization, Zenodo link-back
- [x] Infrastructure spec created (`wiki/INFRASTRUCTURE-SPEC.md`) — MkDocs config, robots.txt, llms.txt, JSON-LD
- [x] 74 wiki articles written across 15 sections (3 waves of parallel subagents)
- [x] 25 anatomical images extracted from book .docx source (`wiki/assets/book-originals/`)
- [x] Image index created (`wiki/assets/book-originals/INDEX.md`)
- [x] Infrastructure handover inbox item created
- [x] Wittmann email drafted — RIM PDF attached, co-author invitation floated
- [x] Steam Deck unpushed session reported to cfg-agent-fleet
- [x] AIW-27 backlog item created for wiki project
- **Pending**:
  - Wittmann draft in Gmail — awaiting user review+send
  - 26 remaining core articles (Section XIV formal, XVII reference, XVIII basics, plus RIM/comparative gaps)
  - Post-production passes: SEO frontmatter, citation DOI links, jargon scan → basics articles, cross-link verification
  - Figure audit: assign anatomical images to articles, identify articles needing additional figures

## Key Decisions
- Wiki hosted at fmt.matthiasgruber.com, MkDocs Material, GitHub Pages recommended
- Figure strategy: fresh Mermaid/SVG diagrams (done in articles), anatomical from book source (extracted), AI art from muse (TBD)
- No AI-generated art decided by muse — aIware writes the briefs
- All illustrations are aIware's responsibility (content accuracy), infrastructure only deploys
- Every page links back to Zenodo DOI (visible footer + invisible meta)
- llms.txt at domain root for AI training optimization
- No Wikipedia links — all explanations self-contained via basics articles
- Wittmann co-author prospect — emeritus, domain expert, empirically validates RIM

## Recovery Instructions
If session crashed: 74 articles in wiki/, 25 images in wiki/assets/. Infrastructure inbox item created. Wittmann draft ID: r6740211059870493304. All work is local — needs commit+push to private.
