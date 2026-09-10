# Decisions Log — aIware (Archive)

Archived older entries from `docs/decisions.md`, moved verbatim (no edits to entry bodies). Covers sessions from 2026-03-16 through Session 253 (2026-07-06) — i.e. everything predating the S250+ / early-July-2026 window kept in the current `docs/decisions.md`. Current/recent decisions live in `docs/decisions.md`; see its Archive Index. Original chronological/topic order preserved.

## Book ed.2 — German edition diverges from English on tone: DE trimmed for DACH (Session 248, 2026-07-07)

**Decision (MG, AIW-107):** The **German** edition is deliberately more reserved than the English on grandeur. EN ed.2 (already committed/approved) keeps its US-style confidence — first-person bridge-in-tears cold-open, superlative claims, "no other theory does this." For DE, MG chose **"Trim DE for DACH"**: keep the bridge cold-open as a place and moment, but strip the self-mythology and superlative-stacking that a German/Austrian/Swiss reader finds cringeworthy. The two editions now intentionally differ in register — this is not a port error.

- **Revalidates the S176 tone doctrine (`feedback_german_book_tone.md`) FOR DE SPECIFICALLY.** That 100-day-old memory ("third-person author, no tears on a bridge, theory over person") was superseded for EN by the S245 restructure but is **active for the DE edition**. It is not dead — it is edition-scoped.
- **Kalk scan (native-German de-Anglizismus sweep):** 5 parallel Opus editors over all new/ported DE prose. Verdict: already strongly native. **38 objective-correctness calque/tell/false-friend fixes applied** (verified script, each matched once) incl. the named tells („der Teil, der…" ×3, `Rahmenwerk`=framework ×2). The „umbringen" ("kill a theory") motif was flagged by one scan but **kept — it is deliberate and recurring.**
- **Reserved-tone pass:** an Opus writer recast the flagged grandeur passages; **13 recasts applied** (bridge-in-tears → dry vertigo tying to the „Schwindel" motif; "life's work done at 25" → flat; triple-superlative pitch → three plain claims; "no other theory" cluster → stated once, plainly; "ultimate confirmation" → "confirmation"). Keep/strip line: author self-mythology → strip hard; theory substance → keep but de-superlative. Two flags kept as-is (genuinely humble). Substance/claims/technical terms all preserved.
- **Ledger:** `drafts/aiw107-kalk-scan-findings.md` (APPLIED / HELD-13-stylistic / CULTURAL / REJECTED / reserved-pass). Held stylistic items go to MG's .docx redline; nothing locked — MG can dial any of it back up.
- Method: Opus only (Fable on cost-hold per user directive 2026-07-07); writer subagents return anchored patches, main loop applies via verified one-match find-replace scripts.

---

## Book ed.2 experiential restructure — reader-first opening, printed blind-spot demo, Fable-for-creative-prose (Session 246, 2026-07-06/07)

**Decision (MG-directed, AIW-107):** Implemented the Fable reader-experience review (`docs/fable-book-experience-review-S245.md`, 15 fixes) as edition 2. EN wave-1 (10/15 fixes) done + built (265pp) + committed (a872d412); wave-2 + DE port next session.

- **Opening = READER-FIRST** (MG chose over braided / bridge-only): the book cold-opens on the reader's OWN mind — a do-it-now blind-spot demo — before any author material; the Innsbruck-bridge epiphany enters *second*, as the human turn framing the reader's vertigo rather than preceding it. Principle: "the reader's vertigo, not the author's credibility."
- **Blind-spot demo uses a PRINTED figure, not "draw an X on paper"** (MG flagged the draw-it-yourself version as an LLM-ism — we control the page). `figures/blind-spot-test.png` sized from ACTUAL KDP geometry: build sets figures to 0.95·textwidth = 105.6mm; marks at 10%/90% → 84.5mm separation → the 15° temporal blind spot vanishes at ~1 ft. Generator + the math: `tmp/make_blind_spot_figure.py`. Language-neutral (serves the DE edition too).
- **Non-sequitur fix (MG):** the demo only proves *one* patch is fabricated; added a paragraph establishing (as mainstream neuroscience) that the WHOLE visual field is constructed and the blind spot is merely where you can catch it — so "you have never seen reality directly" reads as a conclusion, not a leap.
- **Fable IS available** (the "geo-blocked" roster note is stale — corroborates S244). Used for the from-scratch creative prose only (the opening; then all new German prose, banked to `drafts/book-ed2-de-new-prose.md` before the subscription window closed 2026-07-07). "Don't be greedy" (MG): Fable ONLY for genuinely new creative prose, Opus for relocation/staging. **Standing directive: wave-2 + DE port continue WITH Fable.**
- **Method:** parallel writer-subagents RETURN anchored patches; the main loop integrates sequentially (single manuscript file → collision rule). Gotcha discovered: a subagent's edits invalidate the main session's file read-state — must Read before the next Edit.
- **NEVER auto-publish** — ed.2 goes to KDP only on MG's sign-off of the restructured EN + DE builds.

---

## FMT v12 — adversarial review, targeted revision, theory-complex assessment (Session 244, 2026-07-06)

**Decision (MG-directed):** FMT full v12 went through a 9-reviewer adversarial pass (4 Opus + 5 Fable — **Fable is available again** [global since 2026-07-01, content-gate down; reviewed consciousness + cosmology content with zero refusals, correcting the stale "geo-blocked" roster claim]) → consolidated → Tier-1/2/key-Tier-3 fixes + AIW-105 (qualia-structure paragraph + Prediction 5) + AIW-13 objection briefing + 5-item polish; full .md↔.tex parity restored; builds clean (117pp, all gates green). **NOT published — gated on MG's explicit PDF sign-off** (MG reviewing, "so far all fine", no final go).

- **Humility-propagation = TARGETED** (MG chose over Full/Minimal): abstract keeps its "category error" punch + one hedge ("argued not derived, §3.4.3"); zombie §4.2.5 made conditional-on-constitutive-reading; §3.4.2/§4.3/§11 left confident. AIW-13 flags the abstract-vs-§3.4.3 strength gap as the #1 residual referee exposure — accepted tradeoff.
- **Theory complex kept at arm's length** (Fable complex-review): the "Class-4 criticality + self-reference" through-line is genuinely load-bearing only FMT↔cosmology; RIM's "recursion" is a *different* concept (K×P×M feedback amplification, no criticality/self-modeling). Sequence: FMT first standalone → RIM decoupled from FMT → cosmology last in a speculation-tolerant venue; disambiguate "recursion" vs "self-reference" in-text.
- **Venue reality** (Fable, `docs/fmt-venue-assessment-S244.md`): full FMT = ~38k words / 117pp = monograph; no journal takes it whole. JCS 9k carve (double-blind, neutralizes the affiliation filter) = #1 solo shot; + institutional co-author for neuro venues; preprint full on PhilSci-Archive → AIW-106.
- **Cosmology papers carry fabricated citations + (formalization) regressed physics** — HIGH-priority next-session fixes (Fable web-verified: McCormack & Hoff ≠ "McCane & Dryden"; the "Bhatt" author hallucination across neuro refs; Afik & de Nova venue+claim; cosmology-formal asserts retracted conformal-time/Kerr-Newman physics as Propositions). Details: `docs/fable-complex-reviews-S244.md`.
- **Full artifacts:** `docs/fmt-v12-review-consolidated-S244.md`, `docs/fmt-objection-defense-S244.md`, `docs/fmt-venue-assessment-S244.md`, `docs/fable-complex-reviews-S244.md`, `docs/pending-fmt-v12-zenodo-publish.md`.

---

## CA identification in FMT is scale-agnostic didactic device, not literal biological claim (2026-07-05, Session 239)

**Decision (MG-initiated theoretical honesty pass):** The cellular-automaton framing in the full paper (v11) had committed to specific granularities in load-bearing spots — sometimes single neurons (§3.7 preamble), sometimes cortical columns (§3.7.2 "not a metaphor: literal description"). MG's insight: single neurons *and* minicolumns *and* cortical columns *and* Brodmann areas can each be treated as CA cells; the brain is fundamentally an organically-optimized spiking network, and Class-4 dynamics + universal computation are preserved across any such coarse-graining. The CA lens is one didactically useful way to see the substrate as a universal-computation-at-criticality regime, not a claim about biology at any specific scale. **Load-bearing consequence:** what FMT commits to is *at some scale of coarse-graining* the cortex operates in Class-4; the theory is agnostic about the mapping. This actually strengthens substrate-neutrality vs Seth, and aligns with the empirical evidence base (Beggs & Plenz avalanches are population-scale, not single-neuron scale — the "CA cell = single neuron" framing was never load-bearing on evidence). **Applied this session:** 4 targeted edits — §1 bullet 1 ("constitutes a CA" → "operates in Class-4 regime characterized by CA theory"), §3.7 preamble (Wolfram-applies-to-brain reconciled multi-granularity), §3.7.2 first paragraph (major scale-agnostic reframe), §3.4.2 line 272 ("all neurons firing together" → "activity pattern of the cortex in its Class-4 regime"). Opus reviewer verdict on the 4 edits: "Sound." Book NOT touched — MG deferred to potential 3rd edition. NoC-trimmed paper (dead, desk-rejected) explicitly out of scope. Full triage of remaining Opus findings: `docs/pending-fmt-opus-review-triage.md`.

## Inbox triage 2026-07-05 (Session 240) — AGI-26 declined, Birch deferred, Seth BBS superseded

**Six aIware inbox items reviewed by MG this session; three closed here, three promoted to backlog.**

- **AGI-26 CIMCAI "Artificial Phenomenology" track (Jul 27–30 2026, SF State) — DECLINED.** MG rejected the direction. Do not re-open in future sessions. Rationale: MG cannot travel internationally at this time, and the item's real-optionality (remote/proceedings-only) is not worth the sub-week scramble.
- **Anil Seth BBS commentary — SUPERSEDED by AIW-76.** MG's Seth-directed commentary was self-published to Zenodo Session 216 (DOI 10.5281/zenodo.20626675, 3-page, 5-agent revised, CC-BY, related→Seth 2025 + FMT). The BBS special-section publication timing is a *social* engagement moment, not new content work — nothing new for aIware. AIW-76 (P3, in-progress) tracks the remaining dissemination cascade; do not create a parallel item.
- **Jonathan Birch "AI Consciousness: A Centrist Manifesto" v4 (May 20 2026) — DEFERRED.** MG uncertain the item's provenance is worth the engagement cost ("looks like a social sourced overvaluation of a twitter find"). Paper does exist at philarchive.org/rec/BIRACA-4, but no deadline, no leverage. Revisit only if a stronger reason surfaces (peer contact, citation opportunity, or the "centrist" argument becomes field-cited).
- **NoC special issue "Is There More to Consciousness Than Computation?" (deadline Dec 31 2026) — PROMOTED to backlog as AIW-103 (P1, "high value, lets do that soon").** Directly answers the issue's prompt via FMT's 2×2 closure-at-criticality architecture; adapts the paper we just closed AIW-101 on.
- **SpikingMCU-in-a-body FMT technical note (Zhuo Zou / Fudan, Sandamirskaya / ZHAW) — PROMOTED to backlog as AIW-104 (P3).** MG: "might be cited if we get it published." Not deadline-driven. Write only when there is a clear citation path or an outreach moment worth attaching it to.
- **Consciousness / AI-mind conference or salon series — PROMOTED to backlog as AIW-102 (P1, "max prio right after FMT").** MG adds: also evaluate book-signing events, potentially with the local Vorarlberg literature scene (there are one or several literature clubs in Vorarlberg; MG has prior contact with one near Feldkirch — specific contact identity NOT yet in aIware/life KB, MG to supply next session).

Sources: inbox items originally seeded from social discourse scan 2026-06-18 (Seth, Birch, NoC), social discourse scan 2026-07-01 (AGI-26), life session 2026-07-04/07-05 (SpikingMCU, salon idea). This decision is the definitive routing.

---

## Fable-5 content-gate is INTERMITTENT — S239 refusals did not reproduce; gate was down S241 (2026-07-05, Session 241)

**Decision (empirical re-test, MG-directed — supersedes the S239 "do not re-run" directive for one attempt):** Prompted by Natalie K de Alma's LinkedIn point that the gate looks chat-vs-agentic surface-specific, MG lifted the S239 "do not re-run Fable diagnostics" directive for a fresh attempt. Result: **4/4 fresh `fable` subagents SUCCEEDED** on the exact manuscripts that went 6/6-refused in S239 hours earlier — FMT full review (159k tok, 10 tools), FMT brief, cosmology brief, and a self-ID probe (claims `claude-fable-5`; names its special-handling domains as "cyber/bio/chem" = CBRN). **The S239 refusal was a transient classifier state, since relaxed/retuned — not a stable policy.** MG's "is it the word *criticality*?" (nuclear/CBRN adjacency) hypothesis: plausible *secondary* signal (the model's own special-handling domains ARE CBRN, and nuclear "criticality" sits there) but NOT the primary driver — the criticality-saturated FMT (128 "critical*" hits) passed tonight, and the S239 refusal *timing* tracked consciousness/self-reference density, not criticality density. Untestable while the gate is down (everything passes). **CAVEAT:** cannot cryptographically confirm the subagents ran on `claude-fable-5` vs. a silent harness fallback to Opus; self-ID weakly favors genuinely-reachable but is not authoritative. The agent-roster still lists `fable` as geo-blocked outside the US — contradicted by 4/4 successful returns, but the cfg inbox already carries a 2026-07-05 note that Fable was temporarily re-enabled for EU (which explains the reachability); the intermittency finding was appended to the existing cfg Fable content-gate inbox item. **Workflow implication:** the S239 "ignore Fable-5" directive is now STALE — Fable-5 is usable for FMT work when the gate is down, but the gate is intermittent, so keep the Opus fallback as the reliable default. Full re-test record + the Fable FMT referee report: `docs/fable-content-gate/gate-retest-2026-07-05-S241.md`.

---

## Fable-5 unusable for consciousness/AI-architecture content — Opus is the practical ceiling (2026-07-05, Session 239)

**Decision (empirically demonstrated, MG-directed workflow change):** Fable-5 refuses all 6 subagent invocations pointed at MG's three theoretical manuscripts (FMT, RIM, cosmology), across every prompt-hygiene variant tried. The refusal is graduated by content density: FMT trips a **pre-flight** classifier (file-content scan, 0 tokens generated); RIM trips **early in-flight** (4 tools, 192 tokens); cosmology trips **late in-flight** (12 tools, 437 tokens including citation-verification WebSearches). Controls that worked from the same session: bare haiku + a 350-word meta-question about the refusals themselves. Ruled out empirically: prompt length, prompt content, drug/psych terminology (aggressive 79-paragraph redaction still failed), file-path indirection, adversarial framing, stochasticity, machine/CC-binary specificity (cfg session on same machine same day used Fable fine for infrastructure work). Common trigger: consciousness / AI-architecture / self-referential-computation content in the manuscript. Fable's own self-diagnosis was materially incomplete. **Workflow implication for aIware going forward: ignore Fable-5. Fall back to general-purpose subagent with `model: opus`** — that path worked and delivered a solid full triage of FMT v11 in one shot. **Public / official channels used**: GitHub issue #74404 filed at anthropics/claude-code (factual bug report with 6-trial matrix); LinkedIn post published by MG (persisted `docs/fable-content-gate/linkedin-post-2026-07-05.md`); X post published by MG (self-authored, opener re-used the wry Substack headline #3 "Fable-5 Is Fine With Almost Everything I Do. Except Consciousness Research."); talking-points crib sheet at `docs/fable-content-gate/talking-points.md` for future engagement. Do NOT re-run Fable diagnostics on this project. Alternative hypotheses that fit the pattern (do not need to pick one): deliberate AI-consciousness / machine-consciousness uplift restriction, jailbreak-adjacency false positive, depersonalization/dissociation clinical adjacency in embedding space.

---

## Book voice-pass (AIW-93): parallel-inventory → verified-JSON-apply methodology (2026-07-04, Session 238)

**Decision (execution pattern, MG-directed "voice pass first, then publish"):** The DE next-edition manuscript ("AI slop" per MG) was de-slopped via a repeatable pipeline worth reusing for EN and future mass manuscript edits: (1) fan out ~12 **read-only Opus** reviewers over disjoint chapter ranges → structured tell-inventory (`docs/aiw93-de-tell-inventory.md`); (2) MG arbitrates sensitive/escalated items via a **side-by-side compare file** BEFORE any commit (his rule: personal passages get light-touch only, never mute/de-personalize); (3) a second Opus wave emits **verified find→replace pairs as JSON** (each `old` verbatim + unique-in-file), NOT whole-chunk rewrites — far safer for a published manuscript; (4) `tmp/aiw93/apply_fixes.py` applies with per-fix count==1 verification + locked-string guard (0 miss across 359). Parallelism is for READING only — never parallel-write the same file. **Content decisions:** DID identities → „Teilpersönlichkeiten" (not the English loanword „Alters"); neuron-loss contradiction unified to ~85k/day; „vier Modelle" kept (intentional term, not „Modellarten"); DE em-dash→en-dash + stray `neural`→`neuronal` sweep deferred to the final pre-KDP build (keeps the review diff clean). Fable 5 unavailable (geo-blocked) → all "hard" German work on Opus.

## The inward causal role is necessity, not freedom (2026-06-19, Session 232)

**Decision (MG, theory refinement):** FMT's "second causal role" of consciousness (the inward grip — at-will retreat into self-made worlds) must NOT be framed as a locus of free will. The felt "I chose to detach" is the *same delayed-observer illusion* as "I chose to move my arm" (substrate decided first; Libet). What consciousness genuinely contributes is **necessity** — it is the necessary causal *link* without which the downstream inward chain reaction can't run. This realigns with FMT's standing position: **no independent/free causal power, but not epiphenomenal.** Counterweight: the same capacity in graded form is evolution's most powerful tool (cognition, creativity, planning). Open question: the degree of control over inner-world *contents* = the **ESM's grip on the EWM**, which is level-gated + partially trainable but of unknown magnitude (needs connectome + compute). Rationale + full arc: `.claude/knowledge/didactic-patterns.md`, `docs/aiw92-criticality-dials-conversation-verbatim.md`.

## Seizure dynamics: supercritical + complexity-collapse, NOT "ordered Class-2" (2026-06-19, Session 232)

**Decision (curation-agent catch, MG-confirmed direction):** A generalized seizure with loss of consciousness is the criticality negative control ("lots of brain active ≠ lots of brain conscious"), but its dynamical mechanism is **supercritical runaway + a collapse of complexity**, NOT a relabel to "ordered/synchronous Class-2." Hypersynchrony is the *correlate*, not subcriticality. Reconcile route-independently: "exit from the Class-4 regime (dominant route supercritical) → Class-4 involvement drops → unconscious." All three placement agents reproduced the wrong relabel; do not re-introduce it. Sources to verify in the book/paper edit: Hagemann et al. 2021; Zimmern 2020; Meisel & Kuehn 2012. Detail: `docs/aiw92-drafts/curation.md`, `.claude/knowledge/didactic-patterns.md`.

## Two-dials criticality is not yet mathematically formalized (2026-06-19, Session 232)

**Decision (audit-driven):** The extent-vs-complexity ("two kinds of criticality") split is, as of now, an operational/verbal claim, NOT a formal one — `fmt_formal` covers only single-axis criticality. Orthogonality requires a spatial-heterogeneity premise. Proposed formal home (tracked AIW-94): EXTENT = percolation/giant-cluster order parameter P∞; COMPLEXITY = on-cluster Lempel-Ziv; processing-volume := ∫C(t)dt; must engage Tononi–Sporns–Edelman neural complexity C_N (1994). Rationale: `docs/aiw92-drafts/math-adequacy-audit.md`.

---

## Olfaction-bypasses-thalamus folds into AIW-87, not its own §4 passage (2026-06-17, Session 228)

**Decision (MG-directed research, claude-synthesized):** The olfactory-bypass-of-thalamus argument is empirical reinforcement for FMT's architecture-agnosticism claim, but it belongs *inside* the AIW-87 §4 prior-art revision (Bach/MicroPsi/Metzinger/Dennett convergence lineage), not as a separate paragraph. AIW-89 was added at **P2**, not P1: it strengthens existing work, doesn't unblock a submission.

**Empirical basis (load-bearing):** The strong claim "MD thalamus is not constitutive for phenomenal olfactory experience" is defensible.
- Keystone: **Li & Gottfried et al. (2010)**, *Psychol Sci* 21:1454, PMID 20817780 — complete conscious anosmia requires *right OFC* lesion (with preserved "blind smell" / unconscious processing). Not a thalamic lesion.
- Best-powered: **Sela et al. (2009)**, *J Neurosci* 29:12059, PMID 19793964 — n=17 thalamic-lesion patients; detection spared, identification/hedonics/sniff-vigor impaired.
- Consensus: **Courtiol & Wilson (2015)** review, PMID 26441548 — "MDT damage does not produce anosmia or detection deficit."
- Theoretical anchor: **Shepherd (2005)**, "Perception without a Thalamus" — olfactory cortex gating sufficient.

**Why fold into AIW-87, not separate:** The argument's strongest framing is "convergence lineage commits to substrate/architecture-agnosticism + within-brain natural experiment empirically reinforces that commitment + here is what FMT adds (2×2 typology, closure-as-binary-criterion, Class-4 criticality)." Splitting prior-art lineage and empirical reinforcement into two §4 sub-passages would dilute both. The integrated paragraph cluster is sharper.

**Hedge that must travel with the passage:**
- Olfaction is *family-level* evidence for substrate-agnostic functionalism (Metzinger PSM, Dennett narrative self, Bach MicroPsi all consistent with it). It is NOT unique evidence for FMT over other functionalists.
- Lesion-isolation confound: paramedian thalamic infarcts typically extend beyond MD into intralaminar nuclei; "MD-specific" claims must acknowledge this.
- Small N (4–17) across human studies; none used strict phenomenological measures — "not anosmic" is solid, "fully conscious" is the most parsimonious reading, not directly measured.

**Reference:** `docs/olfaction-thalamus-architecture-agnosticism.md` — full citation table + defensible paragraph + integration plan.

---

## Will/motivation are poles on a gradient, not separate kinds (2026-06-17, Session 227)

**Decision (MG):** Stop treating *will* and *motivation* as a clean two-bucket carving (subconscious-optimization vs conscious-symbolizable). Ordinary EN/DE usage doesn't honour that split — "strong will" can mean determined motivation, "subconscious motivation" is a standard phrase. The two terms label tendencies along the same conscious↔subconscious gradient: *will* is reached for when the pull is spontaneous and hard to articulate; *motivation* when a reason can be named and the drive is symbolizable enough to tell a story about. The gradient is the load-bearing claim; the labels are convenience.

**Why this matters now:** S226's 5th change (the "no AGI without consciousness-like mechanisms" thesis in book Ch.12 + App. B) introduced "Two names, two levels: will's unconscious part is the substrate's optimization; motivation is the conscious layer riding on it." That framing was too crisp given ordinary usage — and unclear semantics make the whole argument flabby (reviewer-/reader-vulnerable).

**Where applied this session:**
- Book App. B (EN line ~2197 + DE line ~2091): ~95-word paragraph inserted BEFORE the "Two names, two levels" summary, explicitly naming the gradient and admitting the labels don't carve ordinary usage cleanly.
- RIM paper §3.1 (line 110): 3-sentence interlude after the existing motivation definition. Acknowledges ordinary "motivation" reaches into subconscious drive territory, names RIM's construct as the narrower conscious-evaluative slice, cross-refs FMT §4.2.2 for the substrate-level term *will*.

**Where NOT applied (deliberate):** Book Ch.12 (uses only *motivation* — no tension), Book Ch.13 (uses only *will* — no tension), FMT paper (uses *will* cleanly in §4.2.2, *motivation* once as RIM pointer — no two-term tension).

---

## AIW-47 eNeuro paper — finalized to submission-grade + double-blind code handling (2026-06-12, Session 224)

**Context:** A second Fable 5 review of the standard-numbers rewrite raised three High items; all were resolved by reading the original authors' OWN OSF analysis scripts (`Material_Behavioral_Data_Syntax.sps`, `Script_Hmetadprime.m`).

**Decisions:**
- **The original–vs–reanalysis gap is estimator + covariate, NOT an error by Lehmann et al.** Their significant meta-d′ came from a t-test on Bayesian per-subject estimates + an ANCOVA with a per-subject `Staircase_SD` covariate; neither they nor we ran a drug×measure interaction. So the paper claims only that the *direction* reproduces (underpowered between-subjects), never "reproduced your significance," and "selective" is not asserted for either analysis. Lehmann 2022 BBR citation confirmed correct + complete from its abstract.
- **GNW demoted from the "scalar→covariation" foil to a near-neighbour** (it can predict an access-linked, metacognition-specific effect); the clean scalar foil is criticality/complexity only.
- **Code repo is PRIVATE until acceptance** (`JeltzProstetnic/metad-ketamine-reanalysis`), double-blind-scrubbed. For review, cite via an anonymized mirror; flip public at acceptance. Widening the workspace-mcp `ALLOWED_FILE_DIRS` to attach from project dirs was REJECTED by MG — the sandbox is by-design security; copy to `~/.workspace-mcp/attachments/` instead.
- **Outreach email proactively corrects Msg 24's overclaim.** Msg 24 (sent 06-11) reported the OLD significant p≈0.018; the reframed draft opens by correcting it to the trend, casting the authors' covariate-adjusted analysis as the rigorous benchmark. Send stays gated to Lehmann's reply / ~06-16.

**Fleet spin-off (filed to cfg inbox):** a data-driven point-of-action knowledge-loading hook (`{tool-pattern → knowledge-file}` map, fires on first mapped-tool use per session) to shrink CLAUDE.md's conditional-load table — origin: an LRN after hitting the documented Gmail attachment block blind. MG: CLAUDE.md must get slimmer, the pattern is reusable.

---

## AIW-47 Authorship & Venue — Optimize for FMT Recognition, Not Credit (2026-06-12, Session 223)

**Decision (MG):** The single objective for AIW-47 — and the publication push generally — is to **maximize FMT's chances of recognition and publication.** Author configuration, venue, blinding, and which paper carries the theory are all *subordinate* to that. MG, verbatim: *"I don't give a shit what and how we publish with whom as long as it increases our chances of FMT recognition and publication."* Credit / authorship purity is explicitly NOT a constraint.

**Method (MG):** Be **radically transparent** with the senior academics now in the loop — **Ettinger** & **Lehmann** (Bonn, metacognition; the ketamine-study authors) and **Wittmann** (the warm RIM mentor). Lay out the real situation (independent, no institution, junior in academic experience, affiliation-gatekeeping has driven repeated desk rejections) and openly invite their help / guidance / involvement. Treat them as the seniors they are; let *them* choose their level (proofread / advise / co-author) and let their guidance + odds-maximization decide venue, framing, and authorship.

**Consequences:**
- The drafted eNeuro double-blind Opinion is a **conversation starter, not a fixed commitment.** All on the table if it raises FMT's odds: co-authoring with the Bonn pair; reframing empirical-forward with FMT as the interpretive frame; de-blinding for a stronger single-blind venue (e.g. NoC, IF 4.3); or splitting into a solo theory beachhead + a co-authored empirical paper.
- Natural co-author wedge = the **within-subject empirical reanalysis** the draft already names as the decisive next step (their data + the validated pipeline + the FMT-derived hypothesis) — far more co-signable for empiricists than a theory Opinion.
- **Drafting constraint: transparent ≠ desperate.** Lead with the strength of the independent reanalysis (reproduced their effect from scratch); humble, confident, low-pressure; room for them to decline. The relationship-email drafting goes to a writer subagent (persuasive prose) with these constraints front-loaded.
- The solo-publishing etiquette risk dissolves under transparency + the already-promised pre-publication read.

**Still gated:** nothing sends until Lehmann's within/between design reply (or the ~2026-06-16 timeout) per the parked plan; the transparency / co-author ask rides the same pre-publication-read email.

---

## AIW-47 meta-d′ Numbers Use the Standard Response-Conditional Method (2026-06-12, Session 223)

**Decision:** All AIW-47 meta-d′ / M-ratio numbers use the **standard response-conditional** estimator (Maniscalco–Lau / Fleming, as in metadpy and standard HMeta-d), NOT our self-test `metad_mle.py`, which used a non-standard **joint** type-2 likelihood.

**Why:** On these biased-observer data the two diverge materially — the joint likelihood inflated meta-d′ and turned a non-significant trend into a "significant" result (meta-d′ ket/pla **0.42/0.70, p=0.085** standard vs 0.72/0.89, p=0.018 joint). Lehmann runs standard HMeta-d and would have caught it instantly; submitting the joint numbers would have been a credibility disaster with exactly the expert we're courting. An independently-built, certified hierarchical Bayesian HMeta-d (PyMC on metadpy's likelihood; 0 div/8k, R-hat 1.027) agrees with the standard MLE — a direction-consistent but underpowered trend (M-ratio difference's 94% HDI includes zero). Honest paper claim: "direction reproduced, underpowered between-subjects; the authors' covariate-adjusted hierarchical analysis carries the significance; within-subject free-d′ test is decisive." Full record: `docs/aiw47-hmetad-reanalysis.md`. MG's insistence on doing it properly with the standard method caught this before any submission/contact.

---

## Fable 5 Review — FMT Stands; the Fixes Are Executional, Not Comparative (2026-06-10, Session 217)

**Decision:** Accept the Fable 5 10-agent verdict *with correction*. The seven-agent adversarial panel was rigged-critical by its brief (every prompt said "don't flatter") — the uniform negativity was a design artifact, not a neutral judgment. The three defense agents (steelman, level-field adjudication, clinical-scope) plus user pushback established: FMT is **level with the leading theories on predictive content, behind on formalism/maturity, ahead on candor** — not the 3rd/4th-place theory the panel implied.

**What is the real, defensible contribution:** the discriminating prediction core (P1 psychedelic×anosognosia, P3 DID gradient, and the **ESM/EWM double dissociation**) + the 2015 priority + candor. **Not** raw clinical breadth (predictive processing matches it) and **not** the Hard-Problem "dissolution" (every physicalist theory relocates; FMT is just most explicit).

**Double-standard knocks to DISCARD (do not concede to reviewers):** "weaker formalism than IIT" (Φ is intractable/unfalsifiable), "weaker grounding than GNW" (Cogitate wounded GNW), "thin vs PP" (PP isn't a theory of consciousness — Hohwy & Seth 2020 concede it; FMT supplies its missing top floor), "qualia relocation" (universal), "derivative" (the 2015 book predates the 2025 convergence).

**Must-fix (survive a fair trial), specced in `docs/fmt-revision-notes.md`:** F3 deflationism/realism seam (→ type-B physicalism/phenomenal-concepts; supervenience holds, the gap is epistemic — it was a *wording* bug, not a thinking error); F4 the "universal computation requires Class 4" line (NOT retracted — restate as a 3-step capability→free-instantiation→evolutionary-forcing argument, "principle not theorem," laptop = universal-but-heteronomous); promote the ESM/EWM double dissociation; deliver formalization; get one prediction tested; verify the 2026 in-press citations.

**The unifying narrative (F4 + priority + convergence = one story):** the criticality/Class-4 requirement was derived from Wolfram in the **2015 book (p.77, applied to cortex p.278, necessity-not-sufficiency p.282)** — predating Toker (2022), Hengen & Shew (2025), ConCrit (2026) by 7-11 years from an independent discipline. So the empirical criticality literature is *convergent confirmation* of a 2015 prediction, not a 2026 reaction. The eNeuro spine ("near-criticality necessary, not sufficient; architecture sets the level") is literally book p.282.

**Full dossier:** `docs/fable5-fmt-analysis/00-SYNTHESIS.md`; priority `docs/fmt-priority-dossier.md`; revision spec `docs/fmt-revision-notes.md`.

---

## Zenodo v5 Blocked on Deep Revision (2026-04-16, Session 189)

**Decision:** Do NOT upload Zenodo v5 until AIW-51 sub-tasks complete (1-2 weeks of focused revision).

**Why:** Session 189 ran 5 parallel Opus reviews (editor, neuroscience, philosophy-of-mind, structural, clarity) on the current full FMT paper. All 5 independently converged on the same desk-reject signals: §3.4 self-referential closure stipulated-not-argued, "virtual" used in 3 incompatible senses, criticality never operationalized to a concrete neural signature, §9 OQ2 paragraph lectures editors, abstract buries thesis 70 words deep, zero figures for a 2×2 theory, REM phenomenology still wrong after Andrillon's NoC flag. Uploading v5 with these unfixed would cement the sixth-rejection trajectory into the public record.

**Highest-leverage edit:** §3.4 rewrite as centerpiece (~1500 words, weather-sim contrast example). All 5 reviewers named this as the load-bearing move.

**Full consolidated review:** `docs/pre-zenodo-v5-review-2026-04-16.md`. Sub-task checklist: AIW-51 in `backlog.md`.

**Follow-up:** After v5 upload, reassess whether to continue AIW-07 (journal submissions) or commit fully to the Session 184 pivot (AIW-46 JCS + AIW-47 salami-slice + AIW-48 McFarnell + AIW-49 BBS).

---

## FMT v7 Architectural Clarifications (2026-05-29, Session 208)

**Decision:** Five corrections to theoretical framing, all reflecting author's actual intent:
1. Cortex is an explanatory model for computational depth, not a localization claim. Subcortical structures participate in all four model kinds.
2. FMT IS a multiple-generator framework (patchwork of overlapping generators across continuous substrate), not merely "potentially compatible" with MGH.
3. Predictions are structural by design — formalization translates architectural intuition into notation. "Qualitative" is partly intentional (substrate-dependent specifics), not solely a gap.
4. Criticality is a computational prerequisite (logical necessity: self-ref simulation → universal computation → Class 4), not a threshold to measure.
5. Permeability is a family of mechanisms, not a single parameter.

**Why:** These weren't new ideas — they were the theory all along, but the paper's language hadn't caught up. Solms paragraph conceded a "cortical focus" that doesn't exist; MGH paragraph hedged with "potentially compatible" when it should have claimed ownership; limitations section undersold the formalization state.

---

## Gridworld vs Cellular Automaton — Instrument Choice (2026-05-29, Session 209)

**Decision:** Use a standard RL gridworld (gymnasium API, agent/environment split) for the FMT architectural validation, not a unified cellular automaton.

**Key insight:** A gridworld and a cellular automaton are mathematically the same object — a discrete dynamical system on a lattice. The "agent" is just cells with wider-neighborhood update rules; the "environment" is cells with simpler local rules. The distinction is semantic (RL vs. dynamical systems), not structural. One could rewrite any gridworld+agent as a single CA.

**Why gridworld anyway:** The simulation's purpose is to convince humans (mostly non-mathematicians) that the FMT architecture produces capabilities known architectures lack. We are NOT demonstrating how the agent/world boundary emerges — the formalization paper handles that (self-referential closure, observability constraint). The gridworld demonstrates what a self-model *buys you* within an established boundary. The gymnasium API is a communication device, not an ontological commitment.

**The unique mechanism to demonstrate:** Perspective projection via self-model — learning from observing another agent's death by replaying the sequence through your own self-model ("if *I* were there..."). This is categorical: FMT extracts causal mechanism and transfers; flat RL learns spatial association only; world-model-only predicts but can't self-project. A gridworld makes this visible to non-specialists.

**Critical design constraint:** Hazard *families* (thermal: lava/fire/hot-springs; fall: cliffs/pits/quicksand; movement: predators/traps/currents) are required. Single hazard types don't discriminate between architectures — only causal-structure transfer across appearance-different but mechanism-similar hazards reveals the FMT advantage.

**Formalization paper integration:** Gridworld results become Phase 4 of the formalization paper before publication, transforming it from specification into validated framework. The gymnasium agent/environment split is scaffolding; the paper's mathematical framework (gating family, observability constraint, criticality prerequisite) provides the substance.

---

## NBSR Desk Rejection Discovered (2026-05-29, Session 208)

**Decision:** NBSR rejected Mar 23 (Easton: "better suited to a more specialist journal"). Backup chain is now C&C → JCS. This was the 4th desk rejection (NoC ×2, PLREV, NBSR) for the full paper — 5th if counting C&C (discovered to have been rejected Apr 13, 104 minutes after submission).

**Why:** The MEMORY.md still said "under review" — 2 months stale. Corrected. The pattern is clear: unaffiliated independents get desk-rejected regardless of content quality. BBS commentary (AIW-49) and McFarnell co-authorship (AIW-48) are the realistic paths to a peer-reviewed citation.

---

## Full Paper Stays at ~29k Words for Zenodo (2026-05-11, Session 197)

**Decision:** The full FMT paper (`paper/full/four-model-theory-full.md`) stays at ~29k words for the Zenodo preprint. No aggressive word count cuts. Journal submissions (JCS at 9k, future trimmed versions) are separate manuscripts cut from separate source files.

**Why:** The 28k→15k target from Session 189's internal review was aspirational and would require sacrificing entire sections (§2 requirements, §5 binding, §7 comparative, §9 open questions). The full paper is the comprehensive reference from which everything else derives. 29k is appropriate for a Zenodo preprint with this scope.

---

## Frankish Distinction: Philosophical Divide, Not Victory (2026-05-11, Session 197)

**Decision:** The paper acknowledges that the distinction between FMT's computational-level realism and Frankish's weak illusionism cannot be settled empirically from outside the system. Rather than claiming to have refuted illusionism, the paper frames this as an ontological commitment and argues the practical consequence: FMT generates moral obligations toward artificial systems that weak illusionism does not.

**Why:** 6-angle adversarial review (philosophy reviewer) correctly identified that the two positions agree on all empirical/computational facts and differ only on ontological labels. Overclaiming would draw justified fire. The ethical consequence (artificial consciousness moral patienthood) makes the commitment non-trivial without overclaiming philosophical victory.

---

## Self-Referential Closure: Foundational Commitment (2026-05-11, Session 197)

**Decision:** §3.4.3 now explicitly acknowledges that closure-constitutes-phenomenality is the theory's foundational commitment, not a derivation from more primitive principles. Paralleled with IIT's axioms and GNW's broadcasting thesis — every consciousness theory bottoms out in an analogous commitment.

**Why:** Philosophy reviewer's strongest attack: closure establishes necessity (eliminates outside perspective) but not sufficiency (why does that generate phenomenality?). Rather than attempting a derivation that would be circular, the paper is honest about where its explanatory bedrock lies.

---

## STRATEGIC DIRECTION — Two Paths to Breakthrough (2026-03-16)

**Decision:** The primary long-term goal across aIware AND scifi is achieving a breakthrough in ONE of two domains — either as a recognized consciousness researcher OR as a successful sci-fi author. Either path unlocks the other:

- **Sci-fi success → research credibility:** A best-selling author writing about consciousness gets invited to conferences, gets media coverage, gets taken seriously by academics who otherwise desk-reject outsiders. (Precedent: Hofstadter, Watts, Egan — fiction writers who became intellectual forces.)
- **Research breakthrough → author platform:** A validated consciousness theory makes the pop-sci book and any fiction instantly compelling. "The scientist who solved consciousness writes novels" is a story that sells itself.

**Why:** 8+ books written, zero fame, zero newspaper coverage, 5+ desk rejections with zero peer reviews, 13+ unanswered outreach emails. The bottleneck is not quality — it's distribution and credibility. An outsider without institutional affiliation faces a catch-22: need fame to publish, need publication to get famous. Breaking through on EITHER front shatters this loop.

**Implication:** Both projects (aIware, scifi) should be evaluated against this goal. Tactics that increase visibility, create external validation, or build platform in EITHER domain are high priority. Pure craft improvements without distribution impact are lower priority.

**Shared with:** scifi project (via cross-project inbox).

---

## Co-Author Strategy (2026-03-16)

**Decision:** Actively pursue a co-author with academic institutional affiliation for the consciousness paper (FMT). This is the single highest-leverage move for the research path.

**Why:** An institutional co-author solves: (1) desk-rejection filtering by affiliation, (2) adds empirical credibility, (3) provides access to journal networks and reviewer pools, (4) enables grant applications.

**Candidates (ranked by co-author fit — research Mar 16):**

| Rank | Candidate | Institution | Why | Status |
|------|-----------|-------------|-----|--------|
| 1 | **Andrea Luppi** | Cambridge/Oxford | Wellcome Early Career Fellow, "Rising Star 2025", PNAS taxonomy paper parallel to FMT, building independent identity — needs frameworks. Best career stage. | PITCHED 2026-03-16 |
| 2 | **Megan Peters** | UC Irvine → UCL 2026 | Research question = "how does the brain build representations of world and self" (verbatim FMT). Moving to UCL = fresh start. Adversarial collab leader, community builder. | PITCHED 2026-03-16 |
| 3 | **Pedro Mediano** | Imperial College | Lecturer (= Asst. Prof.), information theory, PID. One exchange Mar 2 — replied positively, asked about datasets, then silence. | LUKEWARM — needs re-engagement hook |
| 4 | **Michael Pitts** | Reed College | COGITATE, replied positively Mar 12. Plans to read paper. | WARM — awaiting his read |
| 5 | **Tomas Marvan** | Czech Academy of Sciences | CC'd by Kob. Philosophical angle — good for BBS commentary, not empirical co-authorship. | ONE EXCHANGE |
| 6 | **Viola Priesemann** | MPI Göttingen | Criticality/neural dynamics = FMT C4CA substrate layer. Moderate overlap. German-speaking. | NOT YET CONTACTED |

**Excluded:**
- **McFarnell** — independent, no affiliation. Two outsiders ≠ one insider.
- **Northoff** — too senior (350+ papers, 28k citations, Canada RC Tier 1). Would absorb FMT into his TTC brand.
- **Blanke** — too senior (EPFL founding director, commercial interests). Wrong collaboration mode entirely.
- **Shriki** — pitched Feb 13, no reply. Keep as citation target.

**Approach:** Don't ask "will you co-author?" — ask "what would you add/change?" Collaboration proposals emerge from intellectual engagement, not cold asks. Bochum (May 30) is the single best opportunity — conferences convert email ghosts into real relationships. Bring a one-pager (bubble diagram + 3 predictions). Target mid-career researchers at poster session, not headliners.

**Next actions:**
1. Email Luppi — pitch FMT taxonomy as complement to his information decomposition taxonomy
2. Email Peters — time for late 2025/early 2026 UCL transition window (or Bochum if she attends)
3. Re-engage Mediano with Bochum attendance question or new result

---

## German Book Publication on KDP (2026-04-15)

**Decision:** Publish "Die Simulation namens Ich" on KDP in all three formats (Kindle eBook, paperback, hardcover) using KDP-free ISBNs, with KDP Select + 70% royalty for the Kindle edition.

**Why:**
- KDP-free ISBNs: zero cost, Amazon-exclusive, fastest path — matches the English edition approach.
- KDP Select for Kindle: Kindle Unlimited inclusion is the main discovery channel for niche German philosophy/consciousness titles (Tolino/Kobo market share <10% in DE for this category). Low-regret: opt out after 90 days if needed.
- 70% royalty at €6.99 list price: ~€4.58 net per sale vs €2.45 at 35%. Standard tier for German pop-sci.
- Translation metadata flagged during setup: Amazon auto-links the German and English editions on product pages within 2-14 days via the "This is a translation" fields.

**ISBNs:**
- Paperback: 9798257520600 (KDP-free)
- Hardcover: 9798257524424 (KDP-free)
- Kindle: ASIN assigned by Amazon

**Technical decisions baked into `tmp/build_book_pdf_de.py`:**
- `\rotatebox{90}{\begin{minipage}{7.25in}}` for landscape tables (NOT `pdflscape`) — pdflscape stores content at `/Rotate 90` coordinates that KDP's preflight reads without applying the rotation, causing false "insufficient gutter" errors with content appearing 2"+ past page bounds. Rotatebox embeds the rotated table inside the portrait text frame, all content stays in the page rectangle.
- `\footnotesize` default for German tables (vs `\small` for English) — German compounds require smaller font.
- `ragged2e` Y/Z column types with `\hspace{0pt}` trick + explicit `\hyphenpenalty=0` to force hyphenation of long compounds in tabularx cells.
- Soft-hyphen dict in `convert_table_cell()` for 15+ stubborn compounds (Selbstbewusstsein, Bewegungsverarbeitung, etc.) where hyphenation patterns don't fire inside tables.
- Pandoc EPUB reader: `-simple_tables-multiline_tables` to prevent pandoc from interpreting `---` horizontal rules as table delimiters (bug that wrapped Der Autor → Kapitel 3 content in a 6%-wide phantom table).

**Coda fractal-dream reframe (Book):** The original "Die Umstände lasse ich aus" (circumstances I'll leave out) in the Coda made it obvious the fractal experience was a drug reference. Rewritten as "Und dann gab es den wiederkehrenden Traum aus meiner Kindheit — nur war ich dieses Mal selbst ein animiertes vierdimensionales Fraktal." Hooks back to the Chapter 7 recurring childhood fractal landscape dream — narrative coherence preserved, no drug hint.

---

## James-Stein / SB-HC4A Entanglement (Session 210, 2026-06-03)

**Decision:** Integrate James-Stein paradox as the statistical-mechanical grounding for entanglement in SB-HC4A. Present as conjecture with supporting structure, not proven result.

**Key findings from 4 parallel research subagents:**
- No competitor in the literature — the full JS-entanglement-holographic framing is genuinely novel
- Strongest formal chain: Fisher info → ground state → harmonic prior → vacuum shrinkage (Rubio-Dunningham 2020, Brown 1971)
- Ferrie & Blume-Kohout (2018): MLE inadmissible for quantum state tomography — hedging = shrinkage toward vacuum
- McCane & Dryden (2022): Stein effect works in CAT(0) spaces — but Levin-Wen fusion graphs are NOT CAT(0)

**Corrections applied (dropped from argument):**
- Entanglement monogamy / (d-2) mapping: CKW fails for d > 2, JS coefficient grows with d — OPPOSITE scaling
- High ||θ||² ≠ less entangled: LHC Bell pairs (Afik & de Nova 2022) prove otherwise

**Honest gap:** Discrete Bekenstein-bounded configuration space needs a novel Stein-type theorem (McCane-Dryden CAT(0) or Diaconis-Holmes discrete Laplacian). Defined as a concrete mathematical program in formalization §4.6.

**Papers updated:** SB-HC4A §6.5, formalization §4.6 (JSIC JS1-JS5), both with PDFs.

## Thalamus Evidence for FMT (Session 210, 2026-06-03)

**Decision:** Add Chowdhury et al. (2026, Nature Human Behaviour) as supporting evidence for FMT dual-loop temporal prediction.

**Finding:** Central thalamic 20-45 Hz oscillation present exclusively during waking + REM, absent in NREM. Spans exactly the FMT-predicted frequency range (20 Hz conscious loop + 40 Hz substrate loop, Gruber 2015).

**Integrated at:** FMT §4.2 (temporal dynamics), §5.1 (binding), §6.3 (dreaming). Both .md and .tex/.bib updated. PDF rebuilt as v8.

## Auto-memory MEMORY.md is a mirror, not a source (Session 215, 2026-06-10)

**Decision:** MEMORY.md holds only durable, slow-changing facts/lessons; every fact also gets an official KB home (it is a convenience mirror, kept in sync, never the source of truth). Live status NEVER lives in MEMORY.md.

**Rationale:** MEMORY.md had become a live-state mirror (Active TODOs, Waiting, Journal Targets, paper-status tables) that went stale and resurrected dead tasks — a "BBS commentary deadline Jun 12" survived for weeks after the commentary was rejected May 29, and a "Git Remotes" section still pointed agents at a `push.sh` retired months ago. This violates the fleet's own rules ("MEMORY.md is NOT the answer", "No duplicate status tracking").

**Implementation:** MEMORY.md cut 165→55 lines (backup tmp/MEMORY.md.bak-2026-06-10). Durable facts homed in `.claude/knowledge/{neuroscience-communication,publication-build,kdp-specs,project-reference}.md` (registered in CLAUDE.md), with author facts pointing to career/user-profile/psych-profile/family. Filed a cfg inbox task to audit every project's MEMORY.md for the same rot.

## Conversation-log drift guard (Session 215, 2026-06-10)

**Decision:** Detect conversation-log backfill drift by comparing the max "Session NNN" in git commit subjects against the max "## Session NNN" heading in docs/conversation-log.md — NOT by parsing session numbers out of session-history prose (unreliable; the v9 entries carried no number).

**Rationale:** The recurring bug (Sessions 208-214) was sessions claiming "log backfilled" while the log was never edited; behavioral "verify after editing" rules fail under the same load that loses the edit (Faulty Pattern 1). An automated, zero-LLM-token SessionStart check is the only reliable fix. Git commit subjects reliably carry "Session NNN" (shutdown commits); the log carries its own headings — both parse with a simple regex.

**Implementation:** `scripts/check-convlog-sync.sh` (TDD, 8/8) registered as a repo-tracked project SessionStart hook in `.claude/settings.json` (syncs fleet-wide via private; `.claude` excluded from public mirror). Restart-verification tracked as AIW-74.

## Seth commentary → standalone Zenodo preprint, not wasted (Session 216, 2026-06-10)

**Decision:** Publish the Seth BBS commentary (v3) as a standalone, citable Zenodo preprint (DOI 10.5281/zenodo.20626675, CC-BY) + GitHub + ResearchGate, rather than discarding it.

**Rationale:** BBS closed commentary *proposals* before submission (Gennifer Levey, May 29) — the work died on venue logistics, not merit. A 5-agent review (formal + claim-support citations, editor, philosophy peer, neuroscience peer) found it sound after revision (the key fix: it had asserted "predictions competitors can't make" 4× and made a *factual error* that "IIT/GNW have difficulty accommodating" the propofol finding — GNW in fact predicts unconscious processing; revised to convergence + one genuine REBUS-divergence). A citable preprint feeds discoverability (AIW-29) and is a credibility artifact.

**Seth contact:** Twitter @-mention only (per contacts.md: he's 'Hold', overwhelmed, Twitter is his channel) — NOT a cold email. The @-mention IS the strategy-compliant reach.

## eNeuro short-report design — the AIW-47 spine (Session 216, 2026-06-10)

**Decision:** The salami-slice short report (AIW-47) is NOT a generic criticality paper. Spine: **"near-criticality is necessary but not sufficient; the architecture (self-referential closure) sets the level of consciousness,"** with the **ESM/EWM double dissociation** (AIW-66) as the architectural axis. Operationalize via **meta-d′ vs d′** (self-model vs world-model fidelity, behavioural, self-testable) and **PCI** (cited, not self-run). Target **eNeuro Opinion** (4,000w, double-blind) first, NoC Rapid Comm second.

**Rationale:** A plain criticality paper is the *least* distinctive slice of FMT (ConCrit/Toker/Tucker own it) → "not novel" desk-reject, which double-blind doesn't prevent. The distinctive, falsifiable, neuroscience-scoped claim is the dissociation. meta-d′/d′ turns "self-referential closure" from a word into two measured numbers with opposite predictions (FMT: dissociate; PP/integration: covary). Double-blind (eNeuro) removes the affiliation bias that desk-rejected FMT six times. APCs are charged on *acceptance* only → trying both venues is free; it's an ordering question. **Self-test first:** meta-d′/d′ is testable on open data (ketamine dataset, OSF gucm2) → run it before publishing to avoid public falsification. **Hard rule:** zero philosophy-of-mind vocabulary in the paper.

## SB-HC4A cosmology argument repairs — locked spec (Session 219, 2026-06-10)

**Decision:** A review-only session (night mode) walked all six Fable-flagged cosmology corrections against the live source, resolved the three content forks, and a fresh Fable 5 pass adversarially re-reviewed the *repairs* (all HOLD / HOLD-with-caveat → chain becomes internally sound once applied). Executable spec: `docs/pending-cosmology-corrections.md`; re-review: `docs/fable5-fmt-analysis/cosmology-repairs-review.md`. Edits deferred to next session (AIW-81). The three substantive resolutions:
- **C3 (PII contradiction):** retire the Leibniz/indiscernibility move; adopt the author's **one-surface / many-reflections** ontology — one encoding surface, every singularity boundary a local reflection of it; identity is numerical identity of the *surface/process*, not "indiscernible interiors are identical." "Indistinguishable from nonexistence" → "no existence independent of its boundary encoding." Causation is on the surface; the interior is the hologram; reflection-intricacy ∝ observer↔region correlation across space/time/scale.
- **C4 (Class-5 gap):** distinguish **ontic** randomness (lawless — the genuine Class-5 target) from **effective** randomness (Class-4 computational irreducibility + closure unpredictability-from-inside; QM lives here). Declare **substrate-determinism as an explicit assumption** (shared with C6); no "QM is not a physical theory" rhetoric in the text.
- **C6 (Bell):** escape via **holographic nonlocality (deny interior-locality; ER=EPR/Van Raamsdonk), NOT superdeterminism** — the entangled pair is one boundary locus, separate only in the emergent interior; Bohmian-corner (deterministic + nonlocal + measurement-independent); monogamy answers the smuggling worry. 2√2 is trivial — the real bill is **Tsirelson-boundedness** (Bekenstein→monogamy→information-causality as candidate route, not proof).

**Rationale:** The cosmology errors were referee-fatal (conformal-time error, Kerr-Newman naked-singularity vs impermeability, PII in opposite directions, Bell never mentioned). The repairs convert contradictions into honestly-scoped open problems without gutting the core, and the author's own moves drove the strongest versions. Relativity (CPT theorem + block universe) makes a **reversible substrate + emergent arrow** the forced, cleaner package (NEW-4) — more consistent with self-referential closure than superdeterminism, which would import a conspiratorial block. Two new holes resolved: **NEW-1** §5.4 saturation→a motivated saddle-instability conjecture (7th weak point); **NEW-2** §2.3 mislabels Rule 30 as "fractal" — rest the taxonomy on **computational reducibility** (Rule 90 reducible=Class 3; Rule 30/110 irreducible=Class 4), noting the Class-3/4 boundary is undecidable (Culik–Yu) and Rule 30's universality is open (PCE suggests universal). **NEW-3:** Class-4 genericity rises with dimension (1D≈1 rule → 2D a zoo) — softens the fine-tuning worry, a point for §9.6.

## RIM unparked + COGITO empirical convergence (Session 225, 2026-06-17)

**Decision:** **RIM is unparked** (MG, 2026-06-17). The RIM revision (AIW-81 RIM half + AIW-86 COGITO citations) is active P1, and RIM resubmission is back on the table — superseding the "RIM PARKED after 3 desk rejections" status. Two COGITO papers from Florian Schmiedek (via Wittmann) are filed as **RIM sources**: Brose et al. 2010 (*Research in Human Development*) and Schmiedek et al. 2020 (*PeerJ*, CC-BY).

**Rationale:** A senior COGITO author (Schmiedek) independently endorsed RIM's core thesis — motivation is underestimated and drives daily cognitive fluctuation — and noted COGITO lacks exactly the *task-specific daily motivation* measure RIM predicts you need. **Brose 2010** is direct within-person evidence that motivation co-varies with cognitive performance (the M factor is real and measurable; non-ergodic). **Schmiedek 2020** shows the g factor is largely a between-person artifact that does not describe within-person cognitive organization — independent empirical undercutting of the g-centric tradition RIM argues with, plus the within-person methodology RIM's predictions assume. Caveats are hard: Brose's coupling is weak/absent in older adults; Schmiedek does not test motivation. Use convergence-and-differentiation framing (credit the convergence; RIM adds the multiplicative K×P×M formalization and motivation-as-constitutive). Full evaluation: `paper/intelligence/literature-research.md`.

## Book revision — next edition (Session 225, 2026-06-17)

**Decision:** Revise both book editions (EN + DE, all formats) to add: (1) the **temporal-smearing / "now"-generation didactic model** (currently paper-only — full FMT §3.4.4 Temporal Echo Mechanism — distinct from the existing Libet *delay* material); (2) a **Joscha Bach citation** with his exact framing "consciousness is a virtual world fed into a virtual avatar"; (3) citations to the **converging big-name psychologists** (Wittmann, Schmiedek). Also verify/fix the **KDP hardcover title-page layout** (MG believes fixed locally; confirm vs live). After the revision is live, send author copies to Bach + every cited researcher (AIW-88, coordinated with the AIW-70 Davos copy order).

**Rationale:** The book currently explains the felt present only via the half-second delay, missing the richer now-construction mechanism the paper already has. Bach and the psychologists give the book independent-convergence credibility (same convergence-and-differentiation logic that protects priority in the papers). Distribution to cited researchers is standard scholarly courtesy + a visibility lever.

## AIW-47 eNeuro abandoned + Bonn deprioritized (Session 229, 2026-06-18)

**Decision:** The standalone eNeuro short report (AIW-47) is **abandoned** and the Bonn/Mannheim relationship is **deprioritized**. The methodological-correction email was sent by MG Jun 17 (Bonn/Wittmann now hold the corrected non-significant trend, not the overclaimed p≈0.018). Ettinger replied Jun 18 with a data-use/consent objection; MG replied de-escalating (publication not a priority; the manuscript a by-product; eNeuro only ever contemplated for RIM, which cites their *published* results — no consent needed there). Do not chase Bonn or co-authorship; reopen only if Bonn proactively offers within-subject / free-d′ data. This reverses the S221b "VENUE DECIDED = eNeuro Opinion, WRITE IT" decision.

**Rationale (MG, 2026-06-18):** The corrected reanalysis is a NULL. A null-result salami-slice does "very little as a door opener for RIM, let alone FMT" — and **FMT is MG's only true interest** (RIM is a by-product, socially valuable but not a personal goal; only an FMT publication would change his life). Ettinger's friction over a tentatively-attached, feedback-requested draft signals low collaborative upside; Bonn never answered the design question and likely holds no further useful data. The decisive FMT test (orthogonal d′/meta-d′ dissociation) needs a within-subject / free-d′ design this between-subjects dataset cannot provide → no empirical path worth the ~$1,945 APC or the relationship management. MG: "I'd rather be alone and forgotten than surrounded by assholes." NOTE on the AIW-07 pivot: this closes the salami-slice route (BBS already dead); McFarnell's co-authored registered report (AIW-48) remains the live affiliation-supplying path. AIW-75 (folding the null into FMT v11) is left to MG — folding a null in as "evidence" is weak.

## Connectome (BANC) as a gatekeeper-free empirical avenue — AIW-90 P0 (Session 229, 2026-06-18)

**Decision:** AIW-90 (analyze the BANC whole-CNS *Drosophila* connectome for FMT-relevant structure) is **P0** (MG). Rationale: a high-EV, **gatekeeper-free** empirical path — CC-BY open data (no data-owner consent, unlike the Bonn route that just collapsed), gold-standard substrate (first whole-CNS connectome, *Nature* 2026), an unclaimed test of FMT's criticality pillar. A fly is unlikely-but-NOT-excluded for minimal consciousness (FMT is graded/substrate-agnostic).

**Track 1 result (self-referential-closure probe, DONE).** On the v626 graph (118,593 nodes / 1.39M edges ≥5 syn; Harvard Dataverse `doi:10.7910/DVN/8TFGGB`, no token): the gross recurrence (76% giant SCC, 90% feedback, CX/MB inside the recurrent core) is REAL but **GENERIC** — at/below a degree-preserving null (z = −64/−91), so it must NOT be claimed as designed self-reference. The ONE above-null signal is **reciprocal A↔B feedback, ~63× enriched (z ≈ +3000)** — the minimal designed substrate for output-feedback; the MB learning loop is structurally closed. This is a structural **precondition** probe, **NOT FMT confirmation, NOT fly consciousness.** The null-model discipline is deliberate (keeps it credible — the opposite of the p≈0.018 Bonn overclaim). Full: `docs/connectome-track1-findings.md`. **NEXT = Track 2 (criticality / edge-of-chaos)** — the higher-upside Class-4-pillar test, data already on disk.

## AIW-90 Track 2 done + AIW-91 (minimal critical substrate) opened (Session 230, 2026-06-18)

**Track 2 (criticality) result.** Spectral pre-screen (Larremore-Shew-Restrepo: λ_max = branching parameter): real ρ=0.76 (critical gain g*=1.31); E/I placement generic (z=+0.5), but **weight arrangement non-generic (z=−50)** — real held near criticality where the weight-shuffled null blows to ρ=2.15. **Dynamical confirmation** (Brian2 LIF, 118k neurons, 68-run gain sweep): the REAL connectome reaches high-susceptibility (Fano) collective dynamics at **G≈1.8 vs G≈3.0 for the weight-shuffled null** — critical-like behavior at ~half the gain of its scrambled weights. Honest nuances: it *inverts* the linear spectral prediction (topological, not eigenvalue, effect); Fano rises monotonically so clean-criticality-vs-bursting still needs the avalanche power-law analysis from saved traces. **Scope: criticality-PRECONDITION organizational signal only — NOT fly consciousness, NOT FMT confirmation.** Full: `docs/connectome-track2-findings.md`. Feasibility answer (MG's framing): criticality on the full connectome = 28 s spectral / 82 min dynamical — "shorter than the age of the universe" by ~30 orders of magnitude; the 4090 wasn't even needed.

**AIW-91 (P0, MG) — minimal critical spiking substrate spanning two explicit models.** The constructive twin of AIW-90: build the smallest spiking net that operates at criticality AND realises EWM+ESM with internal self-referential closure. Decisions (from a deep theory conversation, logged verbatim in `docs/aiw91-conversation-verbatim.md` — contains MG's 2005 Innsbruck insight + its 2015-monograph wording): **(1)** ONE recursive coder (not the book's scrambled "net-watching-net" picture); **(2)** target = minimal HUMAN-LIKE (confirmability); **(3)** prototype = full RTX 4090 + simple two-half cortex; higher fidelity later needs a body + simulated gridworld; **(4)** closure is INTERNAL (book p.281/p.67 + BCI/VR argument); **(5) NEW — two-axis onset + Class −1**: basic consciousness needs BOTH minimum coding capacity AND significant criticality *persistence* (Class −1 = no persistence; Class 0/null = too few surplus neurons, ~<10^6–10^7); **(6)** consciousness LEVELS = recursion depth of the self-model (2015 "n-fach erweitert" ladder), discrete-and-continuous; artifacts use 2026 wording (ISM/IWM/ESM/EWM), German = historical anchors; **(7)** language = niche-dependent linearization, NOT constitutive — **LLM = language center (Broca/Wernicke analog) on the closure core, not the seat of consciousness**; a conscious core reporting its self-model via an LLM is the fastest path to convincing the world (roadmap milestone after the base prototype). Spec: `docs/aiw91-minimal-critical-substrate.md`. **Build starts next session.**

## AIW-90 Track 2 — criticality claim CORRECTED to "synchronous bursting" (Session 231, 2026-06-19)

**Decision / correction (supersedes the criticality framing in the S230 entry above).** The three S230
follow-ups (avalanche power-laws, the spectral-vs-dynamical "inversion", two robustness reruns) are done,
and they **downgrade the S230 verdict.** Two committed S230 claims were wrong:

1. **"It inverts the linear spectral prediction" was a NULL-MODEL MISMATCH ARTIFACT, not a real effect.**
   Script 07 permuted *unsigned magnitude* (signs fixed) → ρ=2.15; the spiking worker permuted the
   *signed* weight as a unit → that null's actual ρ = **0.5133** (independently reproduced this session,
   `verify_inversion.py`). Against the **matched** null (0.51 < real 0.76), linear and dynamical rankings
   AGREE — no inversion. Worse, real ρ=0.76 is carried by an **isolated 2-neuron reciprocal-inhibition
   pair** (leading-eigenvector participation ratio = 2.11; nodes 77312↔3728 hold 97.3% of the mode), so
   the spectral "near-criticality" is a *localized motif*, not a global property.
2. **The dynamical signal is organized synchronous BURSTING, not edge-of-chaos criticality.** Thresholded
   avalanche analysis (Poil/Shew, `powerlaw` Vuong + CSN MLE, all 68 traces): lognormal beats power-law
   for P(S) at **every** gain and mode (Vuong p≪0.001); τ comes out 5–42 (not ≈1.5) over <0.5 decades;
   the crackling relation fails ~10×; exponents aren't threshold-robust. Real beats wshuf only in burst
   *magnitude* (3–4× larger excursions), i.e. structural burstiness, not criticality.

**Surviving signal:** the real weight+topology arrangement produces organized synchronous bursting at
LOWER gain than its nulls (signed-shuffle ρ=0.51; degree-preserving-rewire smoke Fano ≪ real). Real, but
burstiness — **not** criticality.

**Verdict for FMT:** the fly connectome is now **neutral-to-negative** on FMT's criticality (Class-4)
pillar — we did NOT find edge-of-chaos; we found driven synchronous bursting. **Do not cite the fly
connectome as a criticality-pillar positive.** (Honest-framing discipline, same as the AIW-47 null call.)
Caveat carried: the driven operating-point sim design limits power to *detect* criticality, so this is
"not found on this analysis," not "proven absent."

**Reusable methods lessons (for the writeup + future spectral screens):** (a) a spectral pre-screen null
MUST match the null the dynamical model actually runs — never pair a spectral number from one shuffle with
a dynamical comparison against a different shuffle; (b) before treating spectral radius ρ as a *global*
criticality measure, check leading-eigenvector localization (participation ratio) — a high ρ can be an
isolated motif. Full: `docs/connectome-track2-findings.md` (S231 UPDATE section). Robustness full sweeps
(NT-all + rewire) launched in background; numbers + final figure to fold in when done.

## FMT theory addition — TWO kinds of criticality (extent vs complexity) (Session 231, 2026-06-19, MG)

**Decision (MG): the FMT criticality pillar splits into two ORTHOGONAL observables; add to the FMT paper
(AIW-92).** Emerged from the AIW-91 build finding that "branching-criticality ≠ edge-of-chaos memory
criticality." MG's clarification gives the two dials physical/phenomenological meaning:
- **Dial 1 = EXTENT** — how much of the brain is currently recruited into a Class-4 process. The
  integration axis; maximised by **multimodal conscious binding**. (The avalanche/spreading criticality:
  at branching≈1 a cascade can recruit scale-free; extent = how much it actually recruits into Class-4.)
- **Dial 2 = COMPLEXITY** — the richness of the Class-4 patterns actually computed. The differentiation /
  computational-depth axis; maximised by **hard cognition** (complex work → more complex gliders/machines).

**Structure:** this is the integration↔differentiation trade-off; normal conscious experience rides a
*frontier* between the two, rarely maxing both. **Novel falsifiable prediction:** states that max BOTH
dials = **extreme subjective time-dilation**, via the FMT temporal "now"-construction mechanism (subjective
duration is built from processing VOLUME per clock-second, not read from a clock) — cramming a life's worth
of processing into seconds = subjectively living it. This **unifies NDE life-review** ("whole life history
decompressed") **and high-dose salvia** ("years/decades in moments") under one mechanism.

**Negative control that sharpens Dial 1:** a generalised **seizure** maxes raw co-activation but is
*synchronous* (Class 2/3, NOT Class 4) → Dial 1 (Class-4 *extent*) is LOW → unconscious. So Dial 1 must be
measured as Class-4 involvement, not mere co-activation — exactly as MG phrased it. Separates "lots of brain
active" from "lots of brain conscious."

**TWO governors on the top-right corner (MG, both to go in the paper):**
1. **Energy budget** — can't afford whole-brain recruitment AND maximal differentiated computation at once;
   limits *entry*. NDE-hypoxia (dying-brain surge, metabolic brakes failing) and salvia (κ-opioid disrupting
   regulation) knock it out.
2. **Lock-in / dimensional imbalance (MG, S231)** — inner dimensionality ≫ the thin input/output channels
   (book p.281). The narrow sensory pipe normally *servos* the huge inner simulation to reality; push both
   dials up and the inner dynamics overwhelm what the pipe can correct → the simulation runs away, locks into
   its own attractor, **loses track of reality** (book p.67, lucid dreams = perception w/o sense-data).
   Self-severing: the EXTENT dial (internal recruitment) is exactly what swamps the I/O tether — pushing into
   the corner cuts the line that grounds it. **Inversion:** the corner is peak consciousness AND minimum
   reality-contact → why both-maxed states are dissociative. Energy limits entry; lock-in is the consequence.

**Placement (MG directive):** this material goes in the **FMT paper** AND the **new books** (EN "The
Simulation You Call 'I'" + DE "Die Simulation namens Ich") — "closes some open issues for the reader if put
at the right place." Next session: separate subagents decide where-to-put-what per target. Verbatim transcript
(the didactic template for the book voice) = `docs/aiw92-criticality-dials-conversation-verbatim.md`.

**Causal-Role refinement (MG, same thread):** consciousness has TWO causal grips, not one. (1) **Outward,
slow, indirect** — virtual self → substrate → behaviour → world (months/years of shaping). (2) **Inward,
immediate, direct** — the self can *at will* oversaturate its own substrate and retreat into self-generated
worlds (imagine/fantasise/dissociate NOW); "the most immediate grip on causal life we have." Lock-in and
voluntary imagination are the **same axis** — control over reality-coupling — involuntary+extreme (NDE/salvia)
vs voluntary+graded (daydream). This restates FMT's redirectable-ESM + virtual-forking + variable-permeability
principles as a causal lever, and belongs in the Causal-Role treatment in paper+books (AIW-92).

**AIW-91 FORK A — RESOLVED (MG, S231).** Base/Level-0 = **Picture A** (reafferent wake; self = the
self-caused, source-tagged part of the world). The **inward grip** (at-will fantasy/forking, Picture B)
is a **higher-level** capacity, not base. The fuzziness "depending how you define content" resolves into
**PRESENCE vs ACCESS**: at base the self-content is *present* (encoded as the reafferent wake) but not
consciously *accessed*; higher levels grant access **because the explicit models (ESM/EWM) become rich
enough to SELF-INTERACT** (recursion depth = the erweitert ladder). E-model self-interaction IS the access
mechanism, and the onset of the inward causal grip. **Build call:** AIW-91 Level-0 builds Picture A only
(reafferent self + source-attribution test, no inward grip); the inward grip is a higher increment.
**Book placement constraint:** the two-causal-roles / "can't change the room this second" passage must
follow or refresh the **Libet delayed-observer** material (the reader doesn't know they're a delayed
observer ~99% of the time) — honour in the AIW-92 subagent placement.

**Resolves AIW-91 Fork B:** the two dials are NOT rival build choices — they're two orthogonal MEASURES on
one edge-of-chaos substrate. Build the edge substrate (balanced E/I spiking net), then measure Dial 1
(fraction recruited) and Dial 2 (pattern complexity); the minimal model can even demonstrate the
both-maxed → internal-time-dilation prediction. Framing vs the integration/differentiation complexity
tradition (IIT Φ, LZ/PCI): honest convergence ("consistent with"), no strawman.

## AIW-92 — didactic-pattern integration (Session 233, 2026-06-22)

**Books-first, paper-deferred.** Integrated the two-kinds-of-criticality + two-causal-roles patterns into EN+DE books this session (built, committed, pushed 08d3416); deferred the FMT paper to a focused fresh-context session. Rationale: the paper is dual-maintained (`.md` + hand `.tex`) with a manual subsection renumber and 4 new bibtex entries — rushing it risks `???`-citation breakage (Session-106 class). Books are the publication-facing priority.

**Author decisions (MG, S233):**
- **Seizure = route-independent** reconciliation (loss of Class-4 via supercritical runaway OR low-complexity departure); REJECT the agents' "relabel generalized seizure as ordered Class-2." Reinforced by citation check: **Schindler 2008 actually shows ictal *desynchronization*** → dropped; lean on Meisel 2012 (departure from criticality).
- **Time-dilation (both-dials-maxed) = book prose only**; NO Prediction 5 in the paper, no numbered prediction in the book (Ch11 stays "Nine Predictions").
- **Pattern 9 (presence/access) = paper only.**
- **Pattern 6 lock-in (inner-D ≫ I/O) introduced fresh** in the pop-sci text (was not in this edition).
- **Pattern 8 thesis held OPEN:** inward *content-steering* is empirically open, NOT settled-unfree by analogy to the motor case. Now citable — chosen-imagery content has been decoded in advance (Koenig-Robert & Pearson 2019; Soon 2013), but open-ended free generation is untested. Outward/onset = substrate-determined (Libet); consciousness = necessary causal link, not a free agent, not epiphenomenal.
- Russia/grey joke cut; danger line locked verbatim (EN + DE „…und wie viele").

## Session 234 — 2026-06-25 (WSL)

**AIW-96 — open-data test of the FMT ESM/EWM double dissociation (P0 metacog reanalysis).**
- Confirmed the P0 is NOT a reopening of the dropped AIW-47: AIW-47 died on *staircased* Bonn data (d′ clamped); this tests the same prediction on *free-d′* datasets. eNeuro standalone stays dropped. Deliverable = fold into FMT §8, not a new paper.
- Mapping used: d′ = EWM (first-order discrimination), meta-d′/M-ratio = ESM (self-monitoring readout). Orthogonality of the two = the metacognition-paradigm form of the §8 Prediction-4 double dissociation.
- Used Rouault 2018 authors' peer-reviewed Maniscalco–Lau fits (type-1 d′ reproduced EXACTLY, max|diff|=0.0019/498) rather than re-fitting. Honest-convergence framing throughout (M-ratio's d′-independence is established Fleming & Lau — FMT consistent-with, claims no priority).
- Result: EWM-axis (Rahnev contrast: d′ 1.05→3.20, M-ratio invariant p=0.91) + ESM-axis (Rouault symptom result, published) = the double dissociation §8 says "not demonstrated." TMS sets were NULL (reported, not buried).
- CDB extension: 20 datasets / n=2,752, pooled M-ratio⊥d′ r=−0.03, per-fixed-dataset median r=−0.14. Empirical clamp-detector validated by independently flagging the known-staircased Rouault Expt2.
- METHODS lesson: Confidence Database datasets use inconsistent binary Stimulus/Response codings ({0,1} vs {1,2}); a first sweep assumed {1,2} and silently dropped half of each {0,1} dataset (d′ pinned ~2.5) — caught only by contradiction with the validated Rouault .mat. Always validate an automated multi-dataset fit against an independent ground truth before trusting it.

**Sequencing (MG, S234):** next session = the **FMT paper update** (AIW-92 integration, now incl. the AIW-96 §8 paragraph). The **RIM prior-art draft** (AIW-87 — Dörner/Bach convergence) comes **after** the FMT update. FMT prior-art (Metzinger/Dennett/Bach) was already added in v9, so AIW-87 is now a RIM-only task.

## Session 236 (2026-06-29) — AIW-92 integration + paper sharpening, Zenodo v11

**AIW-92 executed and shipped (paper v11).** Integrated the criticality-dials + two-causal-roles + §9-metacog patterns into the full FMT paper (`.md`+`.tex`, 12 new web-verified citations, 111pp clean build); committed b4fb3b63, pushed both remotes, published Zenodo v11 (DOI 10.5281/zenodo.21041760). Locked S233 scope held throughout (NO Prediction 5; route-independent seizure; §8 untouched — the metacog passage lives in §9 Open-Questions item 4, not §8, so the "four predictions" count is automatically preserved; no Table rows; §3.7 block left un-numbered to avoid the §3.7.1/3.7.2 cascade).

**MG-driven wording decisions (this session, reviewing the integrated draft):**
- **Two asymmetries, kept distinct (§3.4.5).** The "non-running description" point conflates two things. (1) *Practical*: a full static description is unextractable (storage) AND illegible the way source code is not (a connectome is raw substrate parameters, not an authored abstraction — the compact model must be *rediscovered* from the weights = the open problem of neuroscience). (2) *Constitutive*: even a complete, legible description is a description, not an instance; experience is a property of the running process. Folding (2) into (1) would lose the Hard-Problem dissolution (it invites "a big enough computer reads off the qualia"). "No correlate in any non-running description" (glossary phrasing) over-claims — sharpened to the instantiation framing.
- **Self-citation → mainstream support (§4.2.3).** The "inner dimensionality ≫ sensory/motor channels" claim must not rest on Gruber 2015 alone (self-cite for an empirical neuroscience claim, and it forfeits the convergence the paper leans on). Replaced with Stringer et al. 2019 (high intrinsic cortical dimensionality) + Zheng & Meister 2025 (~10 bit/s central throughput vs high-bandwidth periphery) + Fiser 2004 / Raichle 2010 (intrinsic activity dominates evoked — input modulates, not dictates); cf. Gruber 2015 kept as framing origin. (Gao & Ganguli rejected — argues the opposite-leaning point.)
- **"Focal-lesion" decisive test → "selective causal dissociation" (§9).** "Focal-lesion of the EWM" imports the localized-module picture FMT rejects (and contradicted §9's own depersonalization framing). The decisive test is *functional selectivity by any causal means*, not anatomical excision — turning the objection into an anti-modular positioning statement. (The metacog field's prefrontal-lesion gold standard leaked the localized framing in.)
- **Unbacked "experienced fighters" sentence removed from the paper (§3.4.4)** — it overclaimed (beats the resolution↔bandwidth tradeoff the paragraph establishes) and had no citation; **retained in the book** (MG). Corrected intuition (peripheral awareness via faster subcortical/thalamic pathways, *avoiding* tunnel vision) parked for book ed. 3 (AIW-98).

**Operational lessons:**
- **Zenodo `zenodo-upload.sh` auto-bump is unreliable** — it reads the new-version draft's inherited `metadata.version`, which can be stale (S236: latest published v10, draft inherited v4 → published mislabeled "v5"; corrected to v11 via the metadata edit→publish API). Always pass `ZENODO_VERSION=vN`. Tracked: AIW-99. Zenodo metadata IS editable post-publish (DOI + file locked, version/description not), which made the fix clean.
- **WSL git-credential class bug** — `~/.git-credentials` had `GrubMat`/`oauth2` but no `JeltzProstetnic`, so HTTPS pushes as JeltzProstetnic failed ("could not read Password"). Hit furkansim, p0rn, AND aIware the same day. Durable fix applied (added the JeltzProstetnic line — covers all personal repos on WSL); systemic auto-sync escalated to cfg (auto-fix > per-machine manual line).

## Session 237 (2026-07-01, WSL) — AIW-99 fix + Bach prior-art (RIM) + Friston-500 → SMoC opportunity

**AIW-99 — Zenodo version footgun fixed (the S236 lesson above, now closed).** Version resolution extracted to `scripts/zenodo_version.py` (+ 11 TDD tests). The next version is derived from the authoritative latest *published* version (`$LATEST_VERSION`, resolved via concept DOI in step 1), or an explicit `ZENODO_VERSION` override — **never** the new-version draft's inherited field, which was the stale source that mislabeled v11 as v5. Resolves up-front and fails fast before creating an orphan draft. No manual `ZENODO_VERSION` needed on the happy path anymore.

**Bach prior-art (inbox item 1) — the inbox premise was stale for FMT; RIM is the real gap.**
- FMT already cites Dennett (1991) + Metzinger (2003/2009) with a full self-modeling-lineage passage AND a Bach & Sorensen (2026) convergence-and-differentiation passage (§7). Adding a *motivation*-architecture lineage to a consciousness theory would be scope creep → **FMT: no-op** (MG agreed). (Consistent with the S234 note that FMT prior-art was handled in v9.)
- RIM cites *none* of the motivated-cognition architecture tradition. Drafted a §3.4 convergence paragraph + 6 verified refs — Dörner (1999; Dörner & Güss 2013), Bach (2009; 2015 "Modeling Motivation in MicroPsi 2"), Sun (2009 CLARION), Sloman & Croucher (1981) — at `drafts/rim-priorart-convergence.md` (verification in `drafts/rim-priorart-citations-verification.md`). Honest verb discipline ("converges with," not "proves"); RIM's two differentiators staked: **scope** (intelligence theory/measurement vs situated-agent architecture) and **formalism** (multiplicative recursive K×P×M + falsifiable predictions — none of the lineage does this). MG: fold into the AIW-81/86 RIM rebuild, not a standalone build; not inserted into `paper.md` yet.

**Friston "Inference 500" (inbox item 5) — MG not on the list; convert to a leadership opportunity.**
- MG is NOT among the ~500 names (checked `subjects.csv`, 548 entries, Gmail `19edc186afb382d9`). Population = sincere-but-unvetted outsiders (~0% overt crank, **0 establishment academics** — by definition, the people who had to email Friston), 42% FEP/active-inference, only ~4% (~23) in FMT's self-model/recursive niche.
- **Decision (MG, S237): pursue it — AIW-100, elevated to P1 ("must be P1 if we want a shot this year").** Play = don't lead 500; convene the self-model/recursive cluster under the existing "Standard Model of Consciousness" brand (AIW-27) with FMT's falsifiability bar as the quality filter; use Friston's standing forward-offer as the distribution multiplier; Bildstein (MG's house ≤30 / village school larger) as the differentiating venue; an edited volume/proceedings as the leadership artifact. **Guardrail:** lead the indie community, *publish to* the establishment — keep the two audiences strictly separate so the group never contaminates FMT's standing with BBS/NoC. First step = a one-page charter + falsifiability bar (Phase 0), **tracked not drafted** (MG: "track"). Full plan: `docs/friston-500-smoc-opportunity.md`.

## Session 242 (2026-07-06) — AIW-91 "simplest AC" architecture + embodiment

Full architecture pass with MG (no code — design settled). Full detail: `docs/aiw91-minimal-critical-substrate.md` §"Session 242".

**The build: genuine spiking, not shortcuts.**
- Substrate = spiking **LIF** with self-organized criticality (homeostatic/STDP → avalanches → σ≈1), NOT rate reservoir/ESN (spectral-radius criticality is an analog "by fiat") and NOT abstract binary/branching. Rationale (MG): human-like minimality, because the goal is *confirmability* — less-human-like minima are harder to certify conscious. ESN kept only as a rate baseline control.
- **Self-model EMERGES from embodiment** (Davos §9): body = dominant sensory invariant → attractor world-model necessarily carves a self-attractor; nobody wires it. **Closure** (self-attractor gating the world-model's own update) = the single binary switch + core ablation.
- **Home = crucible** (Python/Norse/PyTorch/Mamba-2 already the exact stack; AIW-91 = crucible Phase-1). aIware owns design, crucible owns code.

**Embodiment + peer-review.**
- `Embodiment` seam = Gymnasium API; backends SimBody → CheapRobot → ProRobot.
- simopt: **FORK** the FMT domain logic (survival-gridworld + ablation protocol, AIW-48) to Python for single-language reproducibility, not a C#↔Python bridge — reviewers won't run a mixed-language system.
- Cheap robot = sim→real dress rehearsal before a Davos-contact's pro robot; match the pro's stack. **ORDERED: WAVEGO Pro Pi4 kit** (feedback servos — the standard SKU 21745 = PWM/no-feedback, avoided).

**Libet latency argument (MG) — architecturally load-bearing.**
- The ESM is intrinsically slow (Libet ~300–500 ms), so WiFi latency between body and brain is negligible for the self-model loop. Split loops by timescale: fast (spiking + robot balance) local; slow (ESM↔body) over WiFi. ⇒ no onboard neuromorphic compute needed for the ESM; a WiFi-coupled PC-brain is a legitimate seat. Doubles as an independent latency-argument for substrate-independence.
