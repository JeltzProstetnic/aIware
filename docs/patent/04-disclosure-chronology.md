# Annex A — Public-Disclosure Chronology (FMT / Crucible Spiking Substrate)

**Compiled 2026-08-11 (evening), WSL.** Companion to `docs/patent/01-patentability-strategy.md`
(§1.3 called for this audit; §6 open point 2). **Not legal advice.** Every date below carries its
evidence; nothing is guessed — items that could not be pinned are marked `UNDETERMINED` with the
exact step that would settle them.

**Dating conventions and caveats**

- *Public-git dates* are commit dates on `origin/main` (github.com/JeltzProstetnic/aIware — the
  filtered public mirror, `filtered-push.sh` rewrites history but preserves commit timestamps).
  Pushes happen at session end, normally the same evening as the commit; the GitHub `pushed_at`
  for today (2026-08-11T18:58Z) matches today's tip commit (17:59Z), confirming the same-day
  pattern. Treat commit date = disclosure date with a possible lag of hours, not days. If a date
  is ever load-bearing to the day, counsel can request GitHub's push-event log for the repo.
- The public repo has existed and been public since **2026-02-12T22:10Z** (GitHub API
  `created_at`; visibility currently `private: false`). No evidence was found of a later
  private→public flip; treat all mirror content as public from its commit date.
- *Zenodo dates* are from the Zenodo REST API on 2026-08-11: record `created` timestamps (the
  moment the version actually went live) and the author-entered `publication_date`. Where they
  differ, the `created` timestamp governs disclosure.
- `~/crucible` (github.com/JeltzProstetnic/crucible) returns **404 to unauthenticated GitHub API**
  → the repo is private. It has exactly one remote. **Crucible has no public mirror.** Its content
  becomes public only via the aIware paper/backlog channels documented below.
- US grace expiry = first-public date + 12 months (35 U.S.C. §102(b)(1)); the strategy doc's
  caveats about §102(b)(1)(B) sharp edges apply. EP: everything public is dead (Art. 54).
  **Austrian/German utility-model note:** everything first disclosed on or after ~2026-02/03 is
  inside the 6-month AT-GM grace *only if a GM is filed promptly* — that covers every 2026
  disclosure from v1 onward if filed within 6 months of that disclosure; the Jul–Aug items have
  the most runway. Counsel to confirm (§1.1 of the strategy doc).

---

## 1. LEAD FINDING — what is still NOT public (the patentable surface)

These are the items on which no enabling public disclosure was found anywhere (public git history
searched with `git log -S` over all of `origin/main`, all Zenodo records, wiki source, monograph,
trade-book repos, blog inventory):

| Still-private element | Where it lives (private) | Erosion status |
|---|---|---|
| **Non-foldable closure-loop designs** — the tier-A fold identity `x' = tanh((W + W_fb·W_out)x + W_in·u)` (verified to 3.2×10⁻¹⁵, 2026-08-10) and the repair designs (loop carrying its own differential time constant / delay / nonlinearity) | crucible `docs/pending-next-session-2026-08-12.md` §0b/§2; design docs | ⚠ **The phrase "non-foldable closure loop (differential-τ second filter state)" leaked to the public backlog TODAY, 2026-08-11 19:59 CEST** (see §2). The mechanism is *named* publicly; the algebra, the verification, and the concrete designs are not. |
| **Local three-factor credit-routing rule, CRU-83 Gate A result** — 92.4% of hand-wired ceiling, 8 seeds, pre-registered (crucible result doc dated **2026-08-09**) | crucible `docs/results/cru83-gate-a-local-rule.md` | Name leaked today ("local three-factor credit-routing rule (CRU-83)"); the rule's content, numbers, and protocol are private. Related but distinct: CRU-57 G1 Stage-0 credit-path *design* partially leaked 2026-08-04 (see §4, row 11). |
| **M1s3 emergence/sufficiency protocol** — the staged regime under which the loop *builds* the self-model; pre-registration exists, experiment **not yet run** (crucible milestones: "the only open M1 target") | crucible `docs/design/cru83-m1s3-sufficiency-prereg.md` | Name + "and its control arms" leaked today. Control-arm identities (delay-line, nonlinear-feedforward, detuned) never public; "scrambled" and "foreign-body" arm names appeared in the 2026-08-04 backlog leak in a different context. |
| **Self-model-survival three-DV control scheme** (task performance / retained fidelity on pre-redeployment body / frame approximation) | crucible design docs | No public trace found (`three-DV`, `fidelity retained` absent from `origin/main`). |
| **CRU-72 decompilation pipeline** (locating explicit models in a running spiking substrate) | crucible | Name leaked today. The master paper has carried a *theory-level, in-principle* "decompiler" passage since Feb 2026 (§4, explicitly stating extraction is doubly intractable) — that passage arguably teaches *away* from a concrete pipeline; the concrete method is private. |
| **Regional substrate engineering** — ~22k-neuron region taxonomy, hand-written inter-region connectivity table, per-region τ heterogeneity, homeostatic regulation, **"delivered drive" instrumentation** | crucible codebase + docs | Fragments leaked: "1-SCC-over-22,000" (2026-08-08 backlog), "regional substrate with its connectivity table and τ heterogeneity" (named today), CRU-86 modularity finding summarized 2026-08-09/10 (see §4 row 17). "Delivered drive" instrumentation: no public trace. **However**: the *small* two-pool spiking substrate methods (LifPool E/I LIF, n_world = 256, gain 2.0, re-entry scaling 3.0, delayed-parity task, branching-σ 0.44–1.03) were published in the companion paper v1 methods, 2026-07-26. |
| **CRU-70 fidelity decomposition** — the 60%-state-dimension / 40%-return-length split behind the λ crossover | crucible `docs/results/cru70-return-latency.md` | The λ ≈ 1732 vs 210 cost crossover itself IS public (2026-08-08, §8.9); only the fidelity half is private. |
| **Embodiment seam + staged body plan (B1→B2→B3) + non-biasing LLM coupling (M3)** | crucible milestones | "Embodiment seam" named today; "WAVEGO Pro Pi4 ordered (feedback servos)" + "WiFi-coupled PC-brain a legitimate ESM seat" public since **2026-07-06** (backlog); B1/B2/B3 staging and M3 coupling design not public. |
| **CRU-57 G1 Stage-1+ implementation** (Jstab, L2/L3 spiking numbers — noted "genuinely absent" even from the private paper placeholders) | crucible results | Not public; Stage-0 design partially leaked 2026-08-04 (§4 row 11). |

**Bottom line for counsel:** the §1.4 clusters of the strategy doc survive as filable subject
matter, but their *names and headline framings* are now public (mostly since 2026-08-04, worst
today), and several implementation fragments have leaked through the public `backlog.md`. The
enabling level — algebra, protocols, code, numbers — remains private for everything in the table
above. Whether the name-level leaks anticipate or merely signpost is a legal judgment; the
factual record is below.

---

## 2. URGENT — disclosure event of TODAY, 2026-08-11 19:59 CEST

Public commit `46e6f193` ("S301 … patent lane opened") pushed `backlog.md` to the public mirror
containing the new AIW-206 disclosure-freeze item, whose text **enumerates the entire
still-patentable surface by name**:

> "…the regional substrate with its connectivity table and τ heterogeneity, the **non-foldable
> closure loop** (differential-τ second filter state), the **local three-factor credit-routing
> rule** (CRU-83), the M1s3 emergence protocol and its control arms, the CRU-72 decompilation
> pipeline, the embodiment seam."

The freeze notice itself leaked the freeze list. First public appearance of the strings
"non-foldable", "three-factor", "M1s3", "CRU-72", "CRU-83", "connectivity table",
"differential-τ", "embodiment seam" on `origin/main` is this commit (verified by
`git log -S … --reverse origin/main`). As of compilation the leak is hours old.

Options (decision belongs to MG + counsel, not this document): (a) immediately rewrite
`origin/main` to remove the AIW-206 text and force-push, then ask counsel whether hours of
availability on a low-traffic repo was "made available to the public" (EPC case law on
transient availability; GitHub forks/caches are the risk); (b) treat 2026-08-11 as the
disclosure date of the *names* and file before further detail moves. Either way:
**`backlog.md` must be added to `.push-filter.conf` excludes** — it is the leak channel for
every crucible-detail disclosure in §4, and it is not currently excluded (verified: the exclude
list covers tmp/drafts/scripts/docs/.claude/paper/aiw47 + session files only).

---

## 3. Master artifact chronology (what carries the disclosures)

### 3.1 The 2015 monograph — *Die Emergenz des Bewusstseins* (D1)

- Publication date per project records: **2015-01-20** (conversation-log, Session ~130 correction:
  "book was published January 20, 2015"). ⚠ **Known discrepancy (AIW-178, S292):** Lulu's
  catalogue lists ISBN 9781326652074 as **2016-07-15**. Either date is >12 months ago — dead in
  EP and US alike — but the discrepancy should be resolved for the evidence pack (order Lulu's
  publication record). The full PDF is also tracked in the *public* aIware repo root
  (re-added 2026-03-16, commit `a5aef2fd`), so the text itself is on the public mirror.
- Verified contents (read via PyMuPDF from the canonical PDF, printed page = PDF page):
  - **p. 59–61**: the definitional ladder; p. 61 defines *doppelt erweitertes Bewusstsein* — "das
    Metamodell die eigene Beobachtung des Selbstmodells mit abbildet" — the 2015-vocabulary form
    of the self-model-embedded-in-world-model closure criterion (O_ESM ⊆ S_EWM).
  - **p. 260**: self/world boundary via direct-vs-indirect feedback; confabulation examples.
  - **p. 263**: qualia as experience-sequences in the simulation (virtual qualia).
  - **p. 281**: model instances used "wie kleine Lego-Figuren" — the reuse/redeployment germ; the
    electrochemical substrate hosting all cognitive operations.
  - **pp. 77, 274–282**: **Wolfram Class 4 / edge-of-chaos material is IN the 2015 book** —
    p. 77 introduces Wolfram classes; p. 274 ties Class-4 cellular automata to the brain's
    dynamics; p. 276 tabulates emergent/holographic vs Wolfram classes. ⇒ the
    criticality/Class-4 operating condition is 2015 prior art at concept level, not merely
    Feb-2026 prior art.

### 3.2 Zenodo — exact per-version dates (API-verified 2026-08-11)

**FMT master paper**, concept DOI 10.5281/zenodo.18669891 — 13 live versions (v8 absent):

| Version | Version DOI | Record created (UTC) | Stated pub. date |
|---|---|---|---|
| v1 | 10.5281/zenodo.18669892 | **2026-02-17 11:52** | 2026-02-17 |
| v2 | 10.5281/zenodo.18758315 | 2026-02-24 13:38 | 2026-02-16 ⚠ (backdated field; disclosure = Feb 24) |
| v3 | 10.5281/zenodo.18861613 | 2026-03-04 11:32 | 2026-03-04 |
| v4 | 10.5281/zenodo.19064950 | 2026-03-17 10:58 | 2026-03-17 |
| v5 | 10.5281/zenodo.20124948 | 2026-05-11 15:56 | 2026-05-11 |
| v6 | 10.5281/zenodo.20415804 | 2026-05-27 16:55 | 2026-05-27 |
| v7 | 10.5281/zenodo.20448177 | 2026-05-29 15:41 | 2026-05-29 |
| v9 | 10.5281/zenodo.20594617 | 2026-06-08 13:06 | 2026-06-08 |
| v10 | 10.5281/zenodo.20631497 | 2026-06-10 17:38 | 2026-06-10 |
| v11 | 10.5281/zenodo.21041760 | 2026-06-29 17:18 | 2026-06-29 |
| v12 | 10.5281/zenodo.21226262 | 2026-07-06 19:13 | 2026-07-06 |
| v13 | 10.5281/zenodo.21611849 | 2026-07-26 21:08 | 2026-07-26 |
| v14 | 10.5281/zenodo.21822872 | **2026-08-06 11:20** | 2026-08-06 |

Key consequence: **v14 (Aug 6) predates the closure-cost / argmin / λ-crossover push to the
paper (Aug 7–8)** — no Zenodo version yet carries the three cost-family results; the public
GitHub mirror is their only carrier until v15.

**Companion computational paper** (*Closure and Criticality as Enabling Conditions for
World-Modelling*), concept 10.5281/zenodo.21610993 → v1 10.5281/zenodo.21610994, created
**2026-07-26 19:47 UTC**. Contents verified from the draft as frozen at publication (commit
`e514e4ed`, 2026-07-26 22:00): two-closure taxonomy (§3.1), capability-first criticality (§3.2),
banked results §4.1–§4.5 (planner depth-scaling; survival advantage; self/other transfer 0.98 vs
0.78, d = 2.44; criticality-computes demand/scale-gated; **the spiking maintenance partial
result WITH methods** — two-pool `WorldSelfLoop`, torch `LifPool` E/I LIF, n_world = 256,
gain 2.0, branching-σ 0.44–1.03, delayed-parity with re-entry scaling 3.0, decode 0.63–0.77
through D = 45, scrambled-drive control at chance, delay-line downstream gate G9 FAILS,
implementation tag `cru40-partB0-atom`), CRU-36 null (§5). MG ruled 2026-08-04 (AIW-140): defer
retitle/v2 — v1 stands as published.

**Formalization roadmap**, concept 10.5281/zenodo.21843693 → v1 created **2026-08-07 20:49 UTC**.

**RIM (intelligence paper)**, concept 10.5281/zenodo.20125095: v2 created **2026-05-11 16:01**,
v3 created **2026-08-07 16:18**. (No v1 under this concept; earliest RIM Zenodo presence =
2026-05-11, "cross-posted alongside PsyArXiv" per Session 198 log.)

**Seth (2025) commentary**, 10.5281/zenodo.20626675, published **2026-06-10** (also ResearchGate
406829656; blog version same day). Theory-level.

### 3.3 Public GitHub mirror (D5) — repo-level events

| Date | Event | Evidence |
|---|---|---|
| 2026-02-12 22:10 UTC | Repo created, public; initial commit includes theory/challenges (edge-of-chaos vocabulary present from commit 1) | GitHub API; `git log --reverse origin/main` |
| 2026-02-13 | "Ich-Modell as redirectable virtual process" (redeployment germ, modern form) | commit `f7e29597` |
| 2026-03-16 | 2015 monograph PDF tracked at repo root (public) | `a5aef2fd` |
| 2026-03-19 | **Full FMT wiki source added to public repo** (99+ articles, incl. `wiki/ai-consciousness/engineering-specification.md`) | `575abec8`/`a1104583` |
| 2026-05-29 | O_ESM ⊆ S_EWM notation lands (v7 work, S207/S208) | `dd87d137` |
| 2026-06-22 | `aiw91/` public: **minimal critical recursive coder roadmap** — smallest spiking net at criticality realizing EWM+ESM with internal closure; architecture (3-layer coder, critical middle σ≈1, output folded back internally), onset axes (coding capacity ~10⁶–10⁷ neurons; criticality persistence), O_ESM ⊆ S_EWM, increment plan | `a132aeaf`; `aiw91/ROADMAP.md` |
| 2026-07-06 | Backlog discloses: WAVEGO Pro Pi4 robot ordered (feedback servos), "WiFi-coupled PC-brain a legitimate ESM seat" (AIW-91). Same commit added the full EN book manuscript to the public history (later extracted; blob purge deferred = CFG-479) | `6c3b5fe3` |
| 2026-07-24 | §8.9 first lands in master (v13 work): three banked results (depth-scaling, survival, self/other transfer) | `ed95ce84` |
| 2026-07-28 | Wiki refresh pt1: free-compute reframe; "redeploy" vocabulary enters public wiki/engineering-spec pages | `1d3a1771` |
| 2026-08-04 | **The big backlog leak** (see §4 rows 5, 11) — AIW-140's full crucible claim-state digest pushed public | `770a047a` |
| 2026-08-07 18:38 | Backlog AIW-177 carries closure-cost numbers (14.0%/12.0%, 74.0%/71.5%, 5.3×/6.0×) — first public appearance, one day before the paper | `217b30b8` |
| 2026-08-08 20:36 | **CRU-81 package into §8.9**: R² −0.001→0.640 (+0.403, t = 14.6), 72-architecture argmin with all four conditions, self-inclusion-from-wiring-cost derivation, closure-cost paragraph, spiking-maintenance paragraph in master | `15fa92fd` |
| 2026-08-08 23:11 | λ exchange-rate crossover numbers (≈1732 one-stage vs ≈210 eight-stage) + "22,000" (1-SCC-over-22,000) into public text | `f203809b` |
| 2026-08-09 23:08 | Backlog summarizes CRU-86 kill-first: "rest modularity does NOT unblock necessity; separates the span cut…" | `ddd20612` |
| 2026-08-11 19:59 | **AIW-206 freeze-list leak** (§2) | `46e6f193` |

Session/state files (`session-history.md`, `next-session-task.md`, `private/`) leaked to public
before 2026-07-31 (red-team finding recorded in `.push-filter.conf`); now excluded, history purge
pending. Counsel should know pre-Jul-31 session state is in the public history.

### 3.4 Wiki — fmt.matthiasgruber.com (D6)

Built and deployed **2026-03-19** (Session 167: "74 articles, 25 images" → same-day completion to
99 articles; conversation-log S167 records the live domain). Source publicly mirrored in the repo
from the same day (see above), so wiki content is public via two channels. Contains, since
2026-03-19: the **Engineering Specification for Artificial Consciousness** page ("implement the
four-model architecture on a substrate with free compute", spec derived from the two thresholds),
criticality/Wolfram-classes pages, four-model architecture, glossary. Refreshed 2026-07-28
(free-compute reframe, redeployment vocabulary). Continuously updated — rolling disclosure.

### 3.5 Trade books (D7)

| Edition | First public | Evidence |
|---|---|---|
| EN *The Simulation You Call "I"* (Kindle + paperback + hardcover) | live and verified on Amazon by **2026-03-06** (Session 146 "all 3 formats confirmed LIVE"; S144 = 2026-03-06, S148 = 2026-03-06 bracket it). Exact KDP publish timestamp: get from the KDP dashboard | conversation-log L6032–6038 |
| DE *Die Simulation namens Ich* (3 KDP editions) | **2026-04-14/15** (S186, 2026-04-15: "Three editions published … live", amazon.de/dp/B0GX2WJYB1; S187 next day confirms) | conversation-log L381–393 |
| 6 translation eBooks (ES/FR/IT/PT/JA + …) | **2026-07-12/13** (S258: "MG published EN/DE/ES/FR/IT/PT/JA eBooks (ed2)"; ZH blocked) | conversation-log S258 |
| 11-edition / 3-tier wave (incl. Greek, PublishDrive) | **NOT yet public** — built and publish-ready 2026-08-11, upload is MG's, not done | `~/simbook` git log 2026-08-11 |
| Consolidation-channel material (strategy doc open point 7) | **NOT in any shipped edition** — settled two ways: (i) chronology: the consolidation-channel formulation dates to 2026-07-31 (MG theory note), after the last shipped edition content freeze (Jul 12/13 eBooks built from earlier manuscript); (ii) text search of the full `~/simbook` manuscript tree for "consolidation channel"/"Konsolidierungskanal" = zero hits | grep + dates |

### 3.6 Blog, OSF, conferences

- Blog (matthiasgruber.com/blog): 2026-03-19 ×3 (FMT intro; GWT critique; Can AI Be Conscious),
  2026-05-19 (AI interviews), 2026-05-27 (One Theory All the Phenomena), 2026-06-10 (Seth
  commentary). All theory-level (per web-presence inventory, verified live 2026-07-17).
- OSF/PsyArXiv `kctvg`: a stale RIM preprint deposit (AIW-200 opened S299 for republish; retired
  as citation target 2026-08-10). Original deposit date `UNDETERMINED` — settle by opening
  https://osf.io/kctvg and reading the record's date fields (RIM PsyArXiv link was already being
  shared by 2026-03-20, Session ~171). Intelligence-paper content; not spiking-substrate-relevant.
- MoC7 (Copenhagen, Oct 12–16 2026): poster accepted; **wording not yet submitted** (AIW-198
  "WAIT", hard deadline Thu 2026-08-27). The submitted abstract's content = what was disclosed to
  the committee; conference-committee submission is normally confidential until presented
  **[verify with MoC7 policy]**. The poster itself becomes a public disclosure Oct 12–16.
- eNeuro AIW-47 submission: double-blind, excluded from public mirror — confidential, not a
  disclosure. NoC journal submissions: confidential (per strategy §1.5.5).
- AICE anonymized extended abstract + draft public in repo since **2026-03-16** (`cd275147`);
  theory-level, same bucket as D2.

---

## 4. Element-by-element ledger

Status vocabulary: **EP-dead + US-dead** (first public >12 mo ago) · **EP-dead + US-filable
until \<date\>** · **not yet public** (with erosion notes). "First public" = earliest date on any
channel.

| # | Technical element | First public disclosure | Artifact + evidence | Status |
|---|---|---|---|---|
| 1 | **Four-model architecture** (implicit/explicit × world/self; modern 2×2) | 2015-01-20 (concept: Selbstmodell/Metamodell ladder, monograph pp. 59–61); modern form 2026-02-12/17 (repo v1 / Zenodo v1) | Monograph (fitz-verified); `d0468c03`; Zenodo 18669892 | **EP-dead + US-dead** |
| 2 | **Self-referential closure criterion** (O_ESM ⊆ S_EWM) | 2015-01-20 (p. 61, verbatim: Metamodell "die eigene Beobachtung des Selbstmodells mit abbildet"); formal notation 2026-05-29 (v7 + repo `dd87d137`); also public in `aiw91/ROADMAP.md` since 2026-06-22 | Monograph p. 61; git; Zenodo v7 (20448177) | **EP-dead + US-dead** (concept level; the notation adds no separately claimable matter) |
| 3 | **Criticality / edge-of-chaos operating condition** | 2015-01-20 (Wolfram Class 4 tied to brain dynamics, monograph pp. 77, 274–282 — fitz-verified); modern statement 2026-02-12 (repo) / 2026-02-17 (Zenodo v1) | Monograph pp. 274–276; `d0468c03`/`bc84a954` | **EP-dead + US-dead** |
| 4 | **Redeployment of a rich self-model onto non-self targets** | Concept: 2015 p. 281 (model instances as "Lego-Figuren") + 2026-02-13 ("redirectable Ich-Modell", `f7e29597`); in-silico transfer result (0.98 vs 0.78, d = 2.44): 2026-07-24 repo / 2026-07-26 Zenodo v13 + companion §4.3; richness-axis correction + kill-first GO (8 seeds) + foreign-body-control naming: 2026-08-04 backlog | git; Zenodo; `770a047a` | Concept **EP+US-dead**; quantitative results **EP-dead + US-filable until 2027-07-24/26**; richness-axis framing until **2027-08-04** |
| 5 | **Closure-as-consolidation-channel claim** (closure writes the transient explicit model into the implicit substrate; two-tier awareness) | **2026-08-04** (public backlog, AIW-140(B) — MG's 2026-07-31 theory note pushed verbatim) | `770a047a` `backlog.md` | **EP-dead + US-filable until 2027-08-04.** Not in any Zenodo version or book (verified §3.5). |
| 6 | **Closure-removal cost results** (open global loop = 14.0%/12.0% of connectome, 2–3 closed systems survive; return-freedom = 74.0%/71.5%; 5.3×/6.0×) | **2026-08-07 18:38** (backlog AIW-177); paper §8.9 2026-08-08 | `217b30b8`; `15fa92fd` | **EP-dead + US-filable until 2027-08-07.** Not yet in any Zenodo version (v14 predates). |
| 7 | **72-architecture bottleneck argmin** (four selection conditions; per-condition numbers 241→6288, −2428…−7324, 195/2159/6048, double crossing) + **"self-inclusion falls out of wiring cost" derivation** | **2026-08-08 20:36** (§8.9, CRU-81/75 package) | `15fa92fd` | **EP-dead + US-filable until 2027-08-08.** GitHub-only until v15. |
| 8 | **λ return-latency crossover** (exchange rate ≈1732 at one-stage return vs ≈210 at eight; short-return selection condition) | **2026-08-08 23:11** (S297 push) | `f203809b` | **EP-dead + US-filable until 2027-08-08.** The CRU-70 fidelity decomposition (60% state-dimension / 40% return-length) is **not public**. |
| 9 | **Conditional value of the return** (R² −0.001→0.640, +0.403 ± 0.027, t = 14.6; 0.398/0.209/0.089 gradation; rival-readout tie at 4 decimals) | **2026-08-08 20:36** (§8.9) | `15fa92fd` | **EP-dead + US-filable until 2027-08-08** |
| 10 | **Spiking maintenance result** (re-entrant loop holds decodable operands 0.63–0.77 through D = 45; scrambled control at chance; delay-line downstream gate fails) **including methods** (n = 256 E/I LIF pool, gain, re-entry scaling, task spec) | **2026-07-26** (companion Zenodo v1 §4.5 with full methods); §8.9 prose 2026-08-08 | Zenodo 21610994; `e514e4ed`; `15fa92fd` | **EP-dead + US-filable until 2027-07-26** |
| 11 | **CRU-57 sparse plastic spiking thread / G1 credit routing** | Partial: **2026-08-04** backlog leaked the Stage-0 design state — "credit path is option C, rehearsal-derived (`g.forward` only, never a derivative), not weight transport, not Levenberg-Marquardt", held-out numbers 0.074/0.070, Akrout-citation directive, **and the method placeholders: OBS 48 / FRAME 24 / SELF 256, frame_w 0.22, p = 0.5/0.1, syn_scale 0.45, τ = 0.1, ρ = 0.269**; "CRU-57" as a label public since 2026-07-30 (`correspondence/frey-alen.md`) | `770a047a`; `12933654` | **Mixed.** The leaked Stage-0 design + hyperparameters: EP-dead, US-filable until **2027-08-04**. Stage-1+ (Jstab, L2/L3 spiking numbers, the sparse p_out = 0.02 coupling condition): **not yet public**. |
| 12 | **Local three-factor credit-routing rule** (CRU-83 Gate A: 92.4% of hand-wired ceiling, 8 seeds, pre-registered, result dated 2026-08-09) | Name only, **2026-08-11** (§2 leak) | `46e6f193`; crucible `cru83-gate-a-local-rule.md` | **Not yet public at enabling level** — rule content, protocol, numbers all private. Name+class ("local three-factor credit routing through a learning self-model region") public as of today; counsel to judge whether that is a disclosure of anything claimable. |
| 13 | **M1s3 emergence protocol** (staged sufficiency regime + control arms) | Name only, **2026-08-11**; experiment not yet run | `46e6f193`; crucible prereg | **Not yet public** (and not yet reduced to practice — prophetic-example territory if filed now) |
| 14 | **Non-foldable closure loop** (fold algebra M = W + W_fb·W_out, verified 2026-08-10; differential-τ / delay / nonlinearity repair designs) | Mechanism name + one-phrase repair hint ("differential-τ second filter state"), **2026-08-11** | `46e6f193`; crucible pending-2026-08-12 doc | **Not yet public at enabling level** — the algebra, verification, and designs are private; the spiking-transposition question is still open even privately. ⚠ The leaked parenthetical names the key structural feature; scrub decision urgent (§2). |
| 15 | **Closure-loop credit / decompilation pipeline (CRU-72, L7)** | Name only, **2026-08-11**; a theory-level in-principle "decompiler" passage (teaching intractability, not a method) public since 2026-02 in the master | `46e6f193`; paper §4 | **Not yet public** (concrete method). Early-stage — enablement risk noted in strategy §1.4 Cluster C. |
| 16 | **Regional substrate build** (22k neurons, region taxonomy, connectivity table, τ heterogeneity, homeostatic regulation, delivered-drive instrumentation) | Fragments only: "1-SCC-over-22,000" 2026-08-08; taxonomy/connectivity-table/τ-heterogeneity *named* 2026-08-11; small-substrate methods (row 10) 2026-07-26 | `f203809b`; `46e6f193`; Zenodo 21610994 | **Not yet public at enabling level**; delivered-drive instrumentation has zero public trace |
| 17 | **CRU-86 modular substrate result** ("rest modularity does not unblock necessity; separates the span cut…") | **2026-08-09/10** (backlog summaries) | `ddd20612`; `799b5915` | Headline **EP-dead + US-filable until 2027-08-09**; build details private |
| 18 | **Self-model-survival three-DV control scheme** | — | absence verified across `origin/main` | **Not yet public** |
| 19 | **Embodiment: staged body plan + WAVEGO + LLM coupling (M3)** | WAVEGO Pro Pi4 + PC-brain-as-ESM-seat: **2026-07-06** (backlog); "embodiment seam" named 2026-08-11; B1→B3 staging and M3 design not public | `6c3b5fe3`; `46e6f193` | Robot identity + coupling *idea* EP-dead (US until 2027-07-06); the seam/staging/non-biasing-coupling **designs not yet public** |
| 20 | **Minimal critical recursive coder design (AIW-91)** — spiking net at criticality with EWM+ESM and internal closure, onset axes, increment plan | **2026-06-22** (public `aiw91/ROADMAP.md` + findings + code `minimal_coder.py`) | `a132aeaf` | **EP-dead + US-filable until 2027-06-22.** Note: this is a *public* spiking-implementation design from the same inventor — counsel must treat it as prior art against the crucible claims and distinguish the claimed mechanisms from it. |
| 21 | **Ablation-control self-recognition criterion (§3.4.3)** — the test-method | ≤2026-07 (v13 §3.4.3; per strategy D3, and today's public edit renamed it "disconnection control") | Zenodo v13 | **EP-dead**; strategy doc already writes this off (§2.3 "already given away") |
| 22 | **Two-closure taxonomy + capability-first criticality reading** | **2026-07-26** (companion v1 §3) | Zenodo 21610994 | EP-dead + US-filable until 2027-07-26 |
| 23 | **No-Free-Lunch unroll passage** (the published design-around) | **2026-08-04** (backlog verbatim; §8.9 wording 2026-08-08) | `770a047a`; `15fa92fd` | Public — relevant as the self-supplied design-around (strategy §3.5), not as filable matter |

---

## 5. UNDETERMINED items and exactly what settles each

1. **2015 vs 2016 monograph publication date** — order the Lulu sales/publication record for ISBN
   9781326652074; both candidate dates are >12 months, so only the evidence pack cares.
2. **Exact KDP publish timestamps** (EN early-Mar 2026; DE mid-Apr 2026) — KDP dashboard
   "Publishing history"; bracketed here to ±2 days from session logs.
3. **OSF/PsyArXiv `kctvg` deposit date** — open https://osf.io/kctvg; the record shows
   date-created/date-published. RIM content; low stakes for the substrate filing.
4. **Whether any push lagged its commit by more than a day** — only relevant if a specific
   Jul/Aug date becomes legally decisive; settle via GitHub push-event API for the repo
   (events expire, so do it soon if needed).
5. **Wiki go-live to the day** — S167 (2026-03-19) is the build-and-deploy session; if the
   DNS/webserver went live a day later it changes nothing (the same content entered the public
   git mirror the same day). Hostinger deployment logs would give the hour.
6. **MoC7 abstract confidentiality** — ask the MoC7 organizers whether submitted abstracts are
   published before the conference; the poster wording is not yet submitted (deadline
   2026-08-27), so this is controllable.

---

## 6. Immediate consequences (for the main session / MG, not legal advice)

1. **The freeze list itself leaked today (§2).** Decide scrub-vs-accept within hours, not days;
   add `backlog.md` (and `correspondence/`) to `.push-filter.conf` excludes regardless.
2. **The public `backlog.md` has been the dominant leak channel** — every crucial Aug-2026
   disclosure (rows 5, 6, 11, 17, and today's) went public through it, not through the papers.
   The strategy doc's §1.5(4) push-workflow patent gate is not hypothetical; it is already
   needed retroactively.
3. **The US clock is now running on the entire cost-economics family** (rows 6–9: expiries
   2027-08-07/08) and on the consolidation-channel claim (2027-08-04). These are the youngest,
   most valuable disclosed items; a priority filing before MoC7 keeps everything in §1 filable
   in the US and (per counsel) AT-GM.
4. **Nothing in the enabling layer of Clusters A–C has been found public** — the strategy doc's
   central premise survives this audit, with the caveat that the *names* of every mechanism are
   now public as of today, and implementation *fragments* (hyperparameters in row 11, methods in
   row 10) are public with dates as listed.
