# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-07-04T12:35Z — WSL (home PC)
**Goal:** Present a low-scroll overview of open book/paper work, then update the book on KDP (most pressing). Parallelize with Opus subagents (Fable 5 geo-blocked — unavailable to fleet).
**Completed:**
- Private-remote sync; cfg-agent-fleet dirty file reviewed (benign AIW-100 ref, needs cfg session to commit)
- Surveyed all papers + books; built compact overview
- KDP state: next-edition EN+DE content DONE+committed (08d34169) but NOT live; gated on AIW-93
- MG chose: voice pass first, then publish
- Phase 1 DONE: 12 Opus reviewers → ~386 DE tells → `docs/aiw93-de-tell-inventory.md` (worklist)
- MG rulings: sensitive passages = light-touch + side-by-side compare before commit; address = keep close direct, fix drift
- Sensitive side-by-side produced (7 fixes) → `tmp/aiw93/de-sensitive-sidebyside.md`, opened for MG
**Key Decisions:**
- Fable 5 is geo-blocked outside US → route all "hard" subagent work to Opus, not Fable.
- KDP update is NOT a quick push: HC/EU PDFs stale (Jun 18, pre-AIW-92), covers stale (Mar/Apr), AIW-93 voice pass is MG-flagged gate ("AI slop" DE), AIW-60 cover QA still open.
**Recovery/Next session:**
- Book next-edition content: committed in `pop-sci/book-manuscript{,-de}.md`. Paperback PDFs rebuilt Jun 22 (have AIW-92); `-hc`/`-eu`/`-de-hc` PDFs are Jun 18 (pre-AIW-92, STALE).
- Voice-pass pipeline spec: `docs/pending-book-next-edition-polish.md` (AIW-93). Revision context: `docs/pending-book-revision.md` (AIW-87/88).
- KDP specs: `.claude/knowledge/kdp-specs.md`. Build: `python3 tmp/build_book_pdf.py` (+ `_de`, `_epub*`, `_cover*`).

### 2026-07-01T09:30Z — WSL (home PC)
**Goal:** S237 — AIW-99 (Zenodo footgun fix) + Bach prior-art citations (inbox item 1) + Friston Inference-500 check (inbox item 5). COMPLETE.
**Completed:**
- Startup: global + private/main ff-merge up to date; confirmed "conversation-log lag 23" is the known cfg-hook false positive (S225); S236 shut down cleanly.
- MG confirmed ResearchGate v11 upload DONE (last S236 manual item cleared).
- **AIW-99 (P0) DONE + committed 4c57f7e5** — `scripts/zenodo_version.py` + 11 tests `scripts/test_zenodo_version.py` (TDD); `zenodo-upload.sh` resolves version up-front from authoritative `$LATEST_VERSION`/`ZENODO_VERSION`, fails fast, ignores draft's stale field. No manual `ZENODO_VERSION` needed on happy path.
- **Inbox item 5 (Friston-500) DONE** — MG NOT on the 500-name list (`subjects.csv`, 548 entries, Gmail `19edc186afb382d9`). Population = sincere-but-unvetted outsiders (~0% crank, 0 establishment academics), 42% FEP, ~4% self-model/recursive (FMT niche). Strategy → `docs/friston-500-smoc-opportunity.md`; **AIW-100 (P1, MG-confirmed)**.
- **Inbox item 1 (Bach prior-art) DONE (drafted)** — FMT already cites Metzinger/Dennett + Bach&Sorensen convergence (premise stale for FMT → no-op, MG agreed). RIM gap: drafted §3.4 convergence paragraph + 6 verified refs → `drafts/rim-priorart-convergence.md` (+ `drafts/rim-priorart-citations-verification.md`). Folded into AIW-81/86; NOT inserted into `paper/intelligence/paper.md` yet (awaits the RIM rebuild + MG final read). Committed dd4cde22.
**Key Decisions:**
- AIW-99 fix derives the version from the authoritative latest *published* version (`$LATEST_VERSION`), never the draft's inherited field; explicit `ZENODO_VERSION` overrides; fail-fast if unresolvable.
- FMT prior-art = no-op (already cites Metzinger/Dennett + Bach convergence). The genuine gap is RIM's missing *motivation-architecture* lineage (Dörner/Bach/Sun/Sloman) — the inbox premise was stale for FMT.
- Friston-500 play = convene the self-model/recursive cluster under the existing "Standard Model of Consciousness" brand with FMT's falsifiability bar as filter; Friston's forward-offer = distribution multiplier; Bildstein symposium = the differentiator. AIW-100 elevated to **P1** ("shot this year"). Guardrail: lead the indie community, publish to the establishment — keep separate.
**Recovery/Next session:**
- Both commits pushed (see git log). Live priorities menu for next session (MG directs): **AIW-91** (P0, minimal critical spiking substrate — sequenced to resume now), **AIW-100** (P1, SMoC Phase-0 charter), **RIM rebuild** (AIW-81/86 + prior-art passage), **AIW-96** §8 metacog integration (coordinate w/ any FMT paper churn).
- RIM prior-art passage is drafted and ready to drop into `paper/intelligence/paper.md` §3.4 when the RIM rebuild runs — see `drafts/rim-priorart-convergence.md`.

### 2026-06-29T19:30Z — WSL (home PC)
**Goal:** S236 — execute AIW-92 (FMT paper integration), then MG-reviewed sharpening edits, commit+push, Zenodo v11, ResearchGate prep. COMPLETE.
**Completed:**
- AIW-92 FMT paper integration: P1–P7 in `.md`+`.tex` (two criticality dimensions §3.7; route-independent seizure §3.7/§10.3; presence→access §3.4.6; new §4.2.3 Two Causal Roles + renumber; §5.1 energy governor; §9 metacog double-dissociation) + 8 verified bib entries. 3 Phase-1 prep agents + 2 Phase-4 review agents (all GO).
- MG-reviewed edits: A §3.4.5 two-limits (instantiation vs extraction/legibility); B removed unbacked fighters sentence §3.4.4 (kept in book); C §4.2.3 inner≫I/O cite upgrade (Stringer2019/ZhengMeister2025/Fiser2004/Raichle2010, cf. Gruber2015 — 4 bib); D §9 focal-lesion→selective-dissociation (anti-modular).
- Build clean: 111pp, 0 undefined cites, 0 LaTeX errors, 0 overfull>2pt. 12 new web-verified bib entries total.
- Committed (b4fb3b63) + filtered-push (private full + origin filtered). Fixed WSL `~/.git-credentials` (added missing `JeltzProstetnic` line — covers all personal repos here).
- **Zenodo v11 PUBLISHED**: version DOI `10.5281/zenodo.21041760`, concept `10.5281/zenodo.18669891`. (Script auto-bump mislabeled it v5 from a stale draft field; corrected to v11 via metadata edit→publish API → AIW-99.)
- ResearchGate upload folder prepared + opened: `tmp/researchgate-upload/` (v11 PDF + UPLOAD-NOTES.md). RG has no API — manual upload by MG.
- `docs/references.md` updated (12 refs). Credential RCA + Zenodo-bug footgun filed (cfg inbox + AIW-99).
**Key Decisions:**
- AIW-92 run as manual parallel Agent calls (not Workflow — no opt-in): 3 read-only prep agents → integrator writing → 2 adversarial review agents. Locked S233 scope held (NO Prediction 5, route-indep seizure, §8 untouched/P7 is §9, no Table rows, un-numbered §3.7 block).
- Zenodo published autonomously (routine tested tooling, reviewed content, metadata editable post-publish). **Lesson: always pass `ZENODO_VERSION=vN` — the script's draft-derived auto-bump is unreliable (AIW-99).**
- §3.4.5/§4.2.3/§9 wording sharpenings made the paper anti-modular + convergence-forward (self-cite → mainstream support); book versions deferred to ed. 3 (AIW-98).
- Credential durable fix (JeltzProstetnic line) applied on WSL; systemic auto-fix escalated to cfg (3 same-day hits: furkansim, p0rn, aIware).
**Recovery/Next session:**
- Paper is live: committed (b4fb3b63), pushed both remotes, Zenodo v11 (`10.5281/zenodo.21041760`). Nothing pending on the paper.
- ResearchGate = the one open MANUAL step for MG: upload `tmp/researchgate-upload/Four-Model-Theory-of-Consciousness-v11.pdf` per its UPLOAD-NOTES.md.
- New backlog: AIW-98 (book ed-3 propagation, P3), AIW-99 (fix zenodo-upload.sh auto-bump, P3) — both pending MG priority confirm.

