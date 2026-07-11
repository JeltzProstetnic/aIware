# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-07-11T11:15Z — WSL (home PC)
**Goal:** AIW-109 — apply ALL cross-edition QA fixes across all 8 book editions (EN/DE/ES/FR/PT/IT/JA/ZH). Hidden-defect QA cleanup, NOT theory revision. Work-list = `drafts/aiw108-cross-edition-qa-findings.md`.
**Completed:**
- Startup: sync check (both remotes up-to-date), read handoff + work-list + publication-build.md, persona=Bartl
- §0 WebSearch DONE: Hengen/Shew + Algom/Shriki ConCrit = REAL (no fabrication, no escalation); IIT letter = PsyArXiv Sept 2023 (fixed); Kanzi dance=verified, ice-cream=unverifiable (FLAG MG); Bach=Joscha Bach @Plinz X-post, verbatim unverifiable via search (FLAG MG)
- EN source-shared fixes DONE: #1-17 factual + #37/#40/#41/#42 artifacts + TOC clean (#43) + "automata" grammar. All verified count==1, defects gone. Paragraph-merge from comment-deletion caught+fixed. Line count 2475.
- EN: ALL source-shared + aphorism (keep 1) + automata. DONE, verified.
- DE: ALL source-shared (Opus German rewrites) + aphorism + §2 typography (222 quote-pairs→„…", 852 dashes→spaced en-dash) + calques/register. DONE, verified. Line 2368.
- ES/FR/PT/IT/JA/ZH: source-shared + §2 + BLOCKERs applied via Fable per-language agents (spec: `drafts/aiw109-fix-spec.md`). FR BLOCKERs (L1088 English note, L636 garbled, L554 unclosed italic) resolved; PT L518 corrupted-para reconstructed + free-will meaning-inversion fixed. All verified (grep, line counts sane, no merges).
- Checkpoint commit of all 8 manuscripts.
**Key Decisions:**
- Fix EN/DE `.md` first for source-level items, then re-propagate (AIW-109 non-divergence rule).
- Method: verified find→replace, `count==1` per file, never parallel-write one file.
- Model conflict to resolve with MG: handoff says "Fable is back / cost-free" (S254); agent-roster config still shows Fable COST HOLD from 2026-07-08. Default to Opus for fix work unless MG confirms Fable.
**Recovery/Next session:**
Read `docs/pending-aiw108-fix-all-editions.md` + `drafts/aiw108-cross-edition-qa-findings.md`. Editions file: `pop-sci/book-manuscript{,-de,-es,-fr,-pt,-it,-ja,-zh}.md`. Verify each line number in-file before editing.

### 2026-07-11T07:56Z — WSL
**Goal:** AIW-108 — final Fable review of all book editions, EN+DE first (highest multiplier), then token-check → translations as budget allows.
**Completed:**
- Startup: private ff-merge (up to date), context parsed, session-context populated
- Fable gate: MG chose "Fable EN+DE then reassess" → then all 8; probe confirmed claude-fable-5 reachable + no content gate on consciousness material
- Purpose corrected (MG): hidden-defect QA sweep, NOT theory revision; crucible results optional upside only
- EN QA (probe + 5 reviewers) → `drafts/aiw108-en-fable-final-review.md`
- DE QA (5) → `drafts/aiw108-de-fable-final-review.md`
- ZH / ES / JA / FR / PT / IT QA (5 each, native-quality + CJK/typography axes + source-shared cross-check) — 41 reviewers total, no failures
- Consolidated ALL findings → `drafts/aiw108-cross-edition-qa-findings.md` (source-shared matrix + edition-specific + verify-first)
- Fix handover → `docs/pending-aiw108-fix-all-editions.md`; retired inverted-framing `pending-aiw108-fable-final-review.md`; backlog AIW-109 updated
**Key Decisions:**
- **REVIEW PURPOSE CORRECTED (MG, S255):** this is a LAST-LINE QA sweep for defects that have HIDDEN WELL (factual errors, contradictions, broken cross-refs, coherence, prose tells) — NOT a theory revision. Crucible results are optional upside only ("already confirmed experimentally in a model"), never a reason to rewrite published claims. Reviewer brief = hidden-issue hunt; prediction-mismatch axis DROPPED.
- **SIGN-INVERSION ERROR (S255, owned):** I propagated a handoff/inbox framing that read the CRU-36 null as a falsification ("book's sufficiency claim contradicted; 'none falsified' now dishonest"). WRONG. Ground truth `crucible/docs/decisions.md` 2026-07-08: null is FMT-CONSISTENT (mis-wired blob probe); real Closure-1 loop DOES real work (closure ON≫OFF, recursion-specific); criticality computes (CRU-27); 2026-07-11 CS/CG PASS + gridworld all-green (preliminary, no GO/NO-GO). NOTHING falsified → book's "none has been falsified" STANDS. Upstream handoff (docs/pending-aiw108-fable-final-review.md) + inbox items carry the same inverted framing → correct before they misinform the next session.
- Resume S254 handoff (AIW-108). EN+DE source editions → fix source-level findings upstream, re-propagate (never per-language patch structural issues; AIW-109 method).
- Known errors (neuron→85k, Ch10→Ch8, Leibniz→Ch13, anosognosia=Ch6, separators=45) already fixed in all 8 editions S254 → verify-and-move-on, don't re-hunt.
**Recovery/Next session:**
- Handoff/plan: `docs/pending-aiw108-fable-final-review.md`. Backlog: AIW-108 (translations→published), AIW-109 (structural/ed.3 rebuild+KDP re-upload).
- Reviewer context per edition: manuscript `pop-sci/book-manuscript{,-de,...}.md` + current FMT paper `paper/full/four-model-theory-full.md` + `.claude/knowledge/prediction-framing.md` + revised crucible predictions (in handoff §Crucible results).
- Serialize Workflow fan-outs — never 2 large runs concurrently (S253 rate-limits killed 37 agents).

### 2026-07-10T11:10Z — WSL (DESKTOP-32ILURB)
**Goal:** Resume AIW-108 multilingual book program. MG priority order: DE/EN → already-translated (ES/FR/PT) → partial (IT/JA) → open (ZH). MG decision this session: SKIP to IT/JA/ZH (DE/EN coherence+DE-voice already shipped; AIW-93 EN voice DEFERRED). Fable confirmed LIVE (probe ALIVE) → available for ZH.
**Completed:**
- Startup: private synced, additionalContext surfaced, state mapped.
- Verified: EN/DE coherence fixes DONE+committed (afd14701), interiors rebuilt (12b30076). DE voice done; EN voice (AIW-93) deferred per MG.
- Verified propagation: anosognosia Ch8→Ch6 fix present in ES/FR/PT/JA; MISSING in IT.
- Fixed IT bug: `(Capitolo 8)` → `(Capitolo 6)` line 1254 (root cause: stale source chunks predate afd14701; IT translated S253 carried it; single isolated instance).
- Prepped IT Kalk rerun: FAIL1=[21,27,35], FAIL2=[39,44,52,54].
- IT Kalk rerun (7 segs): 29 findings (15A+14B) → 18 applied; 11 not-found ALL confirmed already-fixed by overlapping first-run edits. findings-all.json=520.
- JA Kalk (439 findings): 323 applied + 96 em-dash `―→——` normalization + 3 separators. 68 not-applied = overlap-duplicates (twin fixed, spot-verified); 1 genuine miss + 1 ambiguous → reviewer draft.
- JA coherence (13): 8 ja-only applied (salvia ×3, TOC↔heading ×3, HIGH stutter-dup bug, オチ→明かされるもの); 5 structural → AIW-109 (cross-confirms IT's 4 + new item G "German book's analysis" ref).
- JA = publish-candidate. Reviewer draft: drafts/aiw108-ja-kalk-findings.md. COMMIT next.
- ZH translated (Fable 60/60, high quality) → assembled (2473 ln, 32 headings, 0 missing) → typography normalized (straight "→curly "" for CJK-content: 160→2 residual Latin citations; 0 「」/«» leakage) → chunked (zh-kalk 36 + zh-kalk2 54).
- ZH Kalk (354 findings): 288 applied + 16 half-width→full-width comma normalization + 3 separators (now 45). 44 not-applied = overlap-duplicates (twin-fixed, verified: signature/十亿倍/社交本领/half-colon all gone). No em-dash issue (Fable used —— here). Reviewer draft: drafts/aiw108-zh-kalk-findings.md.
- ZH coherence (18): 10 zh-only single-fixes applied (TOC↔heading ×8, Dr.Strangelove→奇爱博士) + chapter-numbering unified (38 refs → 第N章 Arabic). 5 structural → AIW-109 (THIRD confirmation of IT+JA). Deferred to reviewer: 预言/预测 + real/virtual-side term (diffuse).
- ZH = publish-candidate. Reviewer draft: drafts/aiw108-zh-kalk-findings.md. COMMIT next.
- ALL 3 LANGS DONE: IT, JA, ZH = publish-candidates. AIW-108 program: EN/DE live, ES/FR/PT/IT/JA/ZH = publish-candidates (human-native gates pending).
- MG "fix everything everywhere" (AIW-109): all wrong-fact/wrong-ref errors fixed in ALL 8 editions .md — neuron→85,000, Ch.10→Ch.8, Leibniz→Ch.13, anosognosia=Ch.6, separator parity=45. Commit after f51863a3.
- Corrigendum note for ed.2 print copies (friends/family giveaways) → drafts/corrigendum-ed2.pdf (EN+DE), built clean.
- Next-session handoff written: docs/pending-aiw108-fable-final-review.md (final Fable review, EN+DE FIRST per MG, then token-check → translations).
**Key Decisions:**
- MG priority (2026-07-10): DE EN → already-translated → partial → open. MG chose "Skip to IT/JA/ZH" — DE/EN treated as done-enough, AIW-93 EN voice pass deferred.
- Fable re-enabled: MG "fable is back and the limit seems reset" + live probe → use Fable for ZH translation (Tier 4). All Kalk/coherence = Opus (matches applied IT 392 fixes + FR/PT precedent).
- HARD RULE: never run two large Workflow fan-outs concurrently — serialize.
- ZH: local-Qwen REJECTED (MG S253). Translator = Fable (now available).
**Pending at shutdown:** 11 aIware inbox tasks (research/outreach lane — Sandamirskaya/Seth/NoC/Safron/Bildstein/Wittmann/Metzinger-no-recruit/VM-tax) — NOT touched this session.
**Recovery/Next session:**
- Handover (superseded by this session's progress): `docs/pending-aiw108-it-ja-finish.md`.
- IT pipeline: `tmp/it-pipeline/` (rerun script edited: FAIL1/FAIL2 set). Findings so far: `tmp/it-kalk/findings-all.json` (491). Apply chain: rerun workflow → append to findings-all.json → `screen_findings.py` → `kalk_apply.py --report`.
- JA: clone `tmp/it-pipeline/aiw108-kalk-it.js` → ja, GLOSS/CULT = `tmp/ja-pipeline/{glossary,culture-guide}-ja.md`. Chunk with `kalk_chunk.py pop-sci/book-manuscript-ja.md tmp/ja-kalk ja 70` + `... tmp/ja-kalk2 ja 46`.
- ZH prep exists: `tmp/zh-pipeline/{glossary-zh,culture-guide-zh}.md`. Source chunks: `tmp/es-pipeline/chunks/` (62, skip 7,62) — NOTE these are STALE (pre-afd14701); ZH will inherit the anosognosia Ch8 ref → fix in ZH coherence.

