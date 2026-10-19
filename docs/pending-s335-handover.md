<!-- Action: await-user-decision -->
<!-- Tracked-by: AIW-275, AIW-276, AIW-277, AIW-278, AIW-279, AIW-280, AIW-281, AIW-282, AIW-283, AIW-284 -->
# S334 → S335 handover — post-MoC7 papers, FMT v19 published, Camilo mail pending

Overall report of S334: `docs/s334-report.md` (sections 1–8). Rulings with MG's verbatim words: `docs/decisions.md`
"2026-10-16 (S334)". Reviews: `docs/reviews/2026-10-1[67]-*.md`.

## Shipped in S334 — do not redo
- **FMT v19 on Zenodo** `10.5281/zenodo.23427746` (concept `10.5281/zenodo.18669891`), 167 pp, changelog
  `docs/zenodo-changelog-fmt-v19.md` (thanks Kleiner). Public GitHub mirror pushed (drafts/docs verified absent).
  Content: closure falsifier reworded; minimal consciousness + two axes; accessible/accessed; sleep rows; RPT;
  six new comparisons; consciousness = process; sufficient conditions; self-model criterion; white-box decision
  procedure (Table 1b); identity bridge with three refuters (functional twin primary); panpsychism "requires none,
  cannot exclude". Edit list: `docs/s334-v19-master-edits.md`.
- **Definitions A** (`drafts/papers-moc7/definitions-not-settled.md`, 8,999 words): Fable referee ×2, readability
  pass, Fable citation audit applied (`docs/reviews/2026-10-17-fable-citation-audit-definitions-A.md`),
  impersonal voice, AI declaration, honest FMT footnote. PDF: `drafts/papers-moc7/Gruber - Pointing Is Not
  Defining (draft).pdf` and `~/Desktop/` on Deck 2.
- **Definitions B, minimal self, robot plea, theory map, prediction map** drafted and reviewed (see report §3–4);
  Definitions B now scores FMT on Paper A's C1–C9. Assessment: `docs/reviews/2026-10-17-fmt-definition-vs-C1-C9.md`.
- **Deck 2 tooling:** TeX Live 2026 (TinyTeX, scheme-full upgrade ran in tmux `texfull`, log `/tmp/texfull.log`),
  pandoc 3.6.4, latexdiff, git-lfs (aIware figures were LFS pointers before), PyMuPDF in `~/.venvs/simbook`.
  Zenodo token now at `aIware/.env.zenodo` (from vault key `zenodo`, field `api_token`; gitignored, 600).
- **lrn (MG-approved):** no Gmail drafts before MG's signal (aIware CLAUDE.md amended; global part in cfg inbox
  [rule]); Gmail-connector hook + MCP drift check (cfg inbox [work] + [rule]; analysis
  `docs/reviews/2026-10-17-lrn-gmail-connector-mcp-drift.md`).

## MG's own to-do
- **Send the Camilo mail.** Gmail draft r5719103773991706508 "A draft for the consensus project's map of
  definitions" to camilo.miguel.signorelli@gmail.com — attach `~/Desktop/Gruber - Pointing Is Not Defining
  (draft).pdf`, check From = matthias@matthiasgruber.com, send. Then the next session reads the sent copy and
  updates `contacts.md` #42 + `docs/conversation-log.md`.
- **Find the consensus-group video** (reports of all groups asking for a definitions map; Signorelli naming THE MAP
  as first project) — evidence for Definitions A §5 once citable.
- **Four older Gmail drafts** (Negru, van der Vlag, Yu, Chen) from early S334 — still unsent? Check Sent first.
- **Antonova** LinkedIn texts `drafts/moc7-antonova-linkedin.txt` — sent or not (carried from S333).

## Next concrete action
Check Gmail Sent for the Camilo mail and the four older drafts; record what went out (atomic tracking); then ask
the open decisions below one at a time.

## Open decisions (re-verify premises, ask one at a time with AskUserQuestion, recommended first)
1. **Backlog priorities AIW-275..284** were only proposed (`backlog.md` lines tagged "proposed"). Options: *accept
   as proposed (Rec.)* / *re-rank*.
2. **Journal pause for Definitions A** (S324 pause, `docs/decisions.md`): route is now via Camilo/consensus project.
   Options: *keep pause until Camilo answers (Rec.)* / *lift for JCS now*. JCS needs anonymisation, single quotes,
   150-word summary, AI statement, and a findable 2015 book (Zenodo DOI or Lulu link) — citation audit row "JCS".
3. **Definitions A title** "Pointing Is Not Defining…": *keep (Rec.)* / *version without negation*.
4. **Insect "only a now, no how"** rendered as present tense with no modelled past/future and no model of its own
   modelling (`drafts/papers-moc7/deriving-the-fmt-definition.md`): *correct (Rec.)* / *weaken to master's "basic,
   if present"* (master now says "minimal, if present").
5. **Minimal self:** cite MoC7 talks/posters (Allen n=49 preliminary): *ask authors first (Rec.)* / *cite as
   conference abstracts*. Name Zahavi (MoC7 advisory board) in the self-contradiction reply: *yes (Rec.)* / *no*.
   Empirical co-author for the "minimal-self blindness" experiment: *look for one later (Rec.)* / *now* / *no*.
6. **Robot plea** (`robot-consciousness-plea.md`): competing-interests self-binding for the crucible robot —
   *logging + pre-registered stop rules (Rec.)* / *no aversive valence in closure-on runs* / *capped valence*;
   "servitude" vs "slavery": *servitude (Rec.)* / *slavery*; title: *keep "Silent suffering…" (Rec.)* / *"Look at
   the robots…"*.
7. **Theory map:** PRM verdict "function absorbed, constitution contradicted": *confirm (Rec.)* / *revise*. Format
   order: *wiki page first, then paper (Rec.)* / *SMoC chapter (AIW-146)*. Align `theory-map-paper.md` C3, §4.1,
   frame "Second" ("phenomenality at the basic rung" → "minimal and basic"): *yes (Rec.)*.
8. **Prediction map (AIW-276):** route *draft map to Niccolò Negro, cc Mudrik (Rec.)* / *Mudrik directly*. Needs one
   demo-map export from xk29y8.csb.app in a desktop browser (no browser on Deck 2). E3 ranks highest though only a
   signature prediction: *explain in the cover note (Rec.)* / *revisit §8.5*.
9. **Eric Platon** repo access (ties to crucible open-sourcing): *wait for cru open-source prep (Rec.)* / *give
   access now*.
10. **Primer disclosure** (`drafts/contribute-primer/wiki-contribute-index.md` quotes unpublished CRU-70/78):
    *publish after crucible clears the results (Rec.)* / *publish with the results redacted now*.
11. **Zenodo FMT description link** to `matthiasgruber.com/moc7/` (outward edit, AIW-283): *add now (Rec.)* /
    *after the landing page is richer*.
12. **Thompson social post:** which CS claims were wrong, and the forgotten speaker's name — MG input needed.
13. **Vukovic (#120, AIW-277):** what input did she ask theories for — MG input needed.
14. **AIW-218 / AIW-156** publish-gate deferrals (deferred again for v19): *schedule now that MoC7 is over (Rec.)* /
    *leave*.
15. **P56 posters:** did MG meet Mudrik, Yu, Chen, van der Vlag — anything agreed (affects the four drafts)?
16. **10-09 mp4 self-notes** — what are they?
17. **aIware leftover git stash** (`stash@{0}` git-sync-check auto-stash): *drop after a look (Rec.)* / *keep*.

## Waiting on others
- **Camilo Signorelli:** answer on how to proceed / co-authorship / citing the consensus reports.
- **cfg-agent-fleet:** google-workspace MCP on Deck 2; Gmail-connector hook; MCP drift check; Deck 2 machine-file
  update (TeX/pandoc/git-lfs); idle-compaction setting; global draft-timing rule.
- **crucible:** open-sourcing prep, primer + registration, A#6 re-analysis (carried from S333).
- **infrastructure:** `/moc7/` landing page with SJÄLV + contribute sections; wiki redeploy (AIW-271).
- **social:** new MoC7 persons + Thompson post.
