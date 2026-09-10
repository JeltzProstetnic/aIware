<!-- Action: reference -->
<!-- Tracked-by: AIW-137, AIW-144, AIW-206, AIW-130 -->
<!-- Demoted present -> reference S306 2026-08-23. AIW-208/209/203 are closed and the travel item
     was discharged 2026-08-14; presenting this file at startup re-raises answered questions.
     The live items are tracked in backlog.md, which is the only place status lives. -->
# S303 handover — what shipped, what is waiting, and the one trap to avoid

> **S303 was a long session with a lot of MG interaction.** Everything below is committed and pushed
> to both remotes. Nothing is half-finished in the working tree.

---

## 0. ▸▸ PRESENT AT STARTUP — the items actually waiting on MG

### 0a. ✅ CLOSED 2026-08-14 — travel booking is DONE. Stop reminding.

**MG confirmed "booked" on 2026-08-14 (S304).** The standing instruction to lead with this in every
exchange is **discharged** — do not raise it again. Everything below is kept for the record only.

- **Registration + payment: ✅ done 4 August.**
- **Accommodation Oct 11–17: ✅ BOOKED 2026-08-14.** (Recommendation was Charlottehaven; MG confirmed
  the booking without naming the property, so do not assert which one in any artifact.)
- **Exact requirement, established S303:** arrive **Sun 11 Oct** (Carlsberg Museum event), conference
  **Mon 12 – Fri 16 Oct**, check out **Sat 17 Oct = 6 nights** (5 nights if he flies out Friday
  evening — both were priced).
- **Venue anchor: HC Ørsted Institute, Universitetsparken 5, DK-2100 København Ø.** This is
  **Østerbro, not the city centre** — city-centre hotels are the wrong search and a previous pass
  wasted effort there.
- **MG's preferences:** walking distance to the venue, and **a sauna** if possible.
- ⚠ **Greece is 28 Aug – 8 Sep.** MG wanted to book after Greece; the advice given was that flights
  can wait but **accommodation cannot**, because conference demand plus (probably) Danish
  *efterårsferie* week 42 tightens Copenhagen supply. He did not dispute it.
- ✅ **The accommodation question is ANSWERED — do not re-run the research.** MG changed the brief at
  the end of S303 (taxis fine; the requirement is a **heated pool he can swim in, a sauna and a steam
  bath, usable every morning or evening**, in-hotel or nearby), and the search finished after
  shutdown. **CHARLOTTEHAVEN wins decisively** — 20 m indoor heated pool, 70 °C sauna, tylarium,
  **Mon–Fri 05:30–23:00**, included in the rate, **6 min by taxi**, free cancellation,
  **€1,408 / 5 nights or €1,696 / 6**. Full reasoning, the losers and the caveats:
  **`drafts/moc7-accommodation-shortlist.md`**.
- ⚠ **Two things to put to MG before he books:** (i) Charlottehaven's *tylarium* is a warm humid room,
  **not a true 45 °C steam room** — if that is not enough, the backup is **Kurhotel Skodsborg**
  (21 m pool, real *dampbade*, but 18 km / 20 min each way, ~€47–67 per taxi); (ii) the
  "spa included in the rate" claim is confirmed from booking research and a third-party directory but
  **not from charlottehaven.com itself** — worth one phone call.

### 0b. `AIW-137` — the MoC7 poster is the real critical path and it needs MG

**MG deferred the organiser nudge on 2026-08-12** ("3 defer to next session or later"), so do **not**
re-raise the four logistics questions with the organisers without asking him first.

- ✅ **Figure settled:** MG chose **Variant A (2×2 grid)** and approved the repaired closure symbol.
- ⚠ **Still open and needs MG in the room:** the **trim + re-layout pass**. It has not happened.
- ⚠ **Still blocked:** board dimensions, orientation, session length, whether posters stay up all
  week — unanswered by the organisers since **3 August**. A0 portrait remains the working assumption.
- ⚠ **Do not re-propose** telling the organisers that the booklet will print "five formal principles".
  MG ruled on 2026-08-12 not to raise it; he wants a spoken answer instead.
- **Print options:** fabric poster (hand luggage) or print in Copenhagen (~€40–70).

### 0c. `AIW-144` — booklets are in the mail

MG confirmed 2026-08-12: the 500 SJÄLV booklets are **shipped and will arrive in time**. **Do not
chase Bereuter.** Mark `[x]` and delete `docs/pending-sjalv-print-order.md` on physical arrival.
⚠ The upload question is **settled** and was wrongly put to MG twice — never a third time.

---

## 1. What shipped in S303 (no action needed, context only)

- **`AIW-208` CLOSED.** All 8 formalization fixes applied; **Zenodo v2 published** —
  version DOI `10.5281/zenodo.21907258`, concept `10.5281/zenodo.21843693` auto-resolves to it.
- **⚠ The S302 brief was wrong on a material point:** the roadmap had **already been published on
  2026-08-07** (v1.0, record 21843694). The handover described it as an unpublished manuscript
  needing a first deposit. What was actually broken was the master's stale reference-list entry.
  ✅ **The disclosure question is clean** — the CRU-58 / dominant-loop-mode text entered in commit
  `9c84be9e` on **2026-08-08**, the day *after* the deposit, so it was never public.
- **`AIW-209` CLOSED** (MG raised it to P0: *"wrong references can damage reputation"*). The three
  formalization roadmaps joined the gate corpus, 129 previously-unchecked references came with them,
  34 flagged, **all 34 adjudicated the same day**. **Gate is 603/603 verified, exit 0.**
- **`AIW-203` chapter written and MG-approved**, routed to simbook. See §3.
- **Closure symbol generalised** into `scripts/closure_symbol.py` + 12 geometry tests; MG approved it
  across eight rendered variants and asked for it to be shared. Filed to crucible and simbook.
- **Five→three principles** swept through every live deliverable (README, `wiki/llms-full.txt`, NoC
  `.md` **and** `.tex`, cc, full-tracked). The submitted MoC7 abstract stays at five, banner-marked,
  per MG.
- **FMT v15 canonical promoted:** 130pp → **138pp**, bibtex clean, 0 undefined citations.

---

## 2. ⚠⚠ THE TRAP — `zenodo-upload.sh` will do this again

**It silently appends whatever sits at `tmp/zenodo-changelog.md`.** In S303 a **stale RIM v3
changelog** was sitting there, and it went live on the FMT roadmap's public record — the published
formalization paper briefly carried release notes about the Flynn effect and von Stumm & Ackerman.
It was caught after publishing, the record's metadata was reopened, corrected and republished, and
the RIM text is verified gone.

**Before any future Zenodo deposit: open `tmp/zenodo-changelog.md` and confirm it describes the paper
you are actually publishing.** The file said "v3" while the script published "v2" — a version-string
match check would have caught it, and building that guard is a worthwhile small task nobody has
picked up yet.

Other operational notes:
- `ZENODO_VERSION` must match `vN`. `2.0` is rejected.
- `publish_gate.py` blocks on open backlog items naming the artifact and **will flag the very item
  doing the publishing** — ack it explicitly, e.g. `PUBLISH_GATE_ACK=AIW-10,AIW-208`.
- ⚠ Never a bare `verify_references.py --update --paper <x>` — use `--only-flagged`, and read the
  **real** exit code (`${PIPESTATUS[0]}`); a trailing `echo` masked three silent crashes at S302.
- `bibtex` needs `dangerouslyDisableSandbox`. Roadmap PDFs need `-H paper/fmt_formal/unicode-header.tex`.

---

## 3. `AIW-203` — the chapter is with simbook now

**Draft: `drafts/aiw203-chapter-en.md`.** *"The One Thing Missing from Your World"*, ~2,100 words,
new **Chapter 14**, inserting after the `---` at **L1334** of `~/simbook/pop-sci/book-manuscript.md`.
Plus four labelled patches (Ch13 L1290 · Ch14 L1364 · Ch7 L712 · a **seam repair** at L1338, whose
*"this chapter"* and *"That same capacity"* both break on insertion).

- **MG overrode the NOT-ATOMIC finding**: eleven editions need re-publishing anyway, and *his* time
  is the bottleneck, not agent time. So the renumbering/covers/translations objections were correctly
  discounted as effort; only the content objections were real, and they were solved.
- ⚠ **A P1 hold is on simbook's wave upload** (`docs/pending-wave-upload.md` on their side). If the
  wave ships before the chapter lands, it ships twice.
- **Open questions for MG are listed at the end of the draft:** renumbering sweep scope across
  editions, an optional L1362 micro-edit, keep/cut on the AC-prediction paragraph, and
  "amusement park" vs "funpark" diction.
- **aIware owns the theory; the integration and all editions are simbook's.** Do not integrate from here.

---

## 4. The Copenhagen accommodation research — ✅ COMPLETE

**Full shortlist with prices, walk times and the booking argument: `drafts/moc7-accommodation-shortlist.md`.
Read it out to MG; it is written for him.** Headlines:

- ⚠ **His two requirements do not intersect.** Nothing with a sauna is within a 20-minute walk of
  Universitetsparken 5, and nothing within 20 minutes has a sauna. It is proximity or sauna.
- **First choice: Bob W Cph Østerbro** — 10 min walk, no sauna, **€854 / 5 nights, €1,040 / 6**.
  €554 cheaper than the sauna option; Øbro-Hallen public sauna is 15 min away at €8–20 a visit.
  ⚠ No reception at all (contactless check-in) and the cheap tiers are non-refundable.
- **Backup: Charlottehaven** — free sauna + tylarium + pool + gym, **free cancellation on every rate**,
  28 min on foot / 10 by bike, **€1,408 / 5 nights, €1,696 / 6**.
- **Efterårsferie: YES**, Københavns Kommune gives 12–16 Oct 2026 exactly — but the effect is **mild**,
  a domestic leisure bump on a cheap shoulder-season base, not a squeeze.
- **The organisers publish a ~22-hotel list but negotiated NO block booking and no discount code**, and
  it is chosen for metro access, not walking — its nearest entry is 27 min on foot.
- **⇒ The recommendation is to book a free-cancellation 6-night rate now and drop to 5 later at no
  cost.** The market is soft overall (264 properties) but the good rooms are not: Hotel Nora 1 left,
  A&O 2 left, Bob W's refundable tier 2 left, Rye115 already gone on the 11th.

Supporting detail also established:

- **The ≤20-minute walk set is only four properties:** Bob W Østerbro (10 min), A&O Hostel Nørrebro
  (18), Rye115 (20), Hotel Nora (20). **Rye115 is sold out on 11 Oct and has no private bathroom in
  any room type**, so the real field is three.
- **Bob W Østerbro — first choice, but NO sauna** (confirmed three ways; Bob W's saunas are all
  Helsinki/Tallinn properties).
- **Charlottehaven — backup, and the sauna option**: 70 °C sauna, tylarium, saunagus several times
  weekly, lap pool and squash, all listed under *"Included in the price"*. Minimum stay 2 nights.
- **A&O Nørrebro — no sauna.** Correct address **Tagensvej 135-137, 2200 København N**. Private rooms
  do have private shower/WC.
- **Scandic Nørreport — no sauna** (Scandic's own sauna page names Sluseholmen, Spectrum,
  CPH Strandpark and Scandic Copenhagen; Nørreport is absent). **Scandic Copenhagen does have one.**
- **Hotel 9 små hjem**, Classensgade 38, Østerbro — hotel-apartment, private bath + kitchen, published
  DKK 920–975/night. UCPH's own directions page says ~20 min on foot; routing said 26.6. ⚠ **Reception
  is closed at weekends**, which collides with the **Sunday 11 Oct** arrival — key pickup would need
  arranging in advance.
- **Public sauna fallback: Øbro-Hallen**, near the venue. Cost **58–150 DKK (€8–20), unconfirmed** —
  two sources disagree and the Øbro Kurbad spa is closed for building work with no reopening date.
- **Ruled out, with reasons:** Globalhagen Hostel (**permanently closed** — OTAs still list it with
  2026 prices, they are stale), 1 Hotel Copenhagen (its Bamford spa opens **2027**), STAY Nordhavn
  (10-day minimum), Livjæger (one-month minimum), Urban Camper (indoor tents, no ensuite).

**Still unverified, and flagged as such in the shortlist:** sauna at Go Hotel Østerport (the cheapest
option); free-cancellation terms and live pricing at 9 små hjem (whose **reception is closed at
weekends**, colliding with the Sunday arrival); whether Øbro-Hallen's drop-in is 58 or 110/150 DKK.
⚠ **Direct-with-hotel rates were never compared** — every hotel's own booking engine blocked automated
access, so better rates may exist by booking direct.

---

## 5. Carried forward

- **`AIW-206`** — the public-git-history rewrite is still MG's call, and lower-stakes now that there
  is no patent to protect. Tidiness/CFG-479, not legal.
- **`AIW-130`** — Alen Frey is out of the JAIC slice; the §6 in-silico grounding he was to co-build is
  unowned. **Send him nothing** — MG owns the next contact and it happens in person.
- **The 15 AC engineering design docs** still carry the five-principle spec basis. **MG ruled
  2026-08-12: "history"** — leave them as historical design rationale. Do not sweep them.
- ~~**`references.bib` is still outside the gate corpus.**~~ ✅ **DONE S305 2026-08-21** — the `.bib` arm was built and the FMT master is green (234 printed bibtex citations matched). It found six real defects across two papers and put the NoC cut under the gate. Full write-up: `docs/pending-s305-bib-gate.md`; residue is `AIW-213`. Original text kept for the reasoning: The gate parses the `.md`; the canonical PDF
  builds from `.tex` + `.bib`; S302 proved they drift into *different works under the same citation
  key*. **The artifact that actually ships has still never been checked.** S303 hit this live — a
  safety assertion caught `Rubio` surviving in `sb-hc4a-formalization.tex` after it had been removed
  from the `.md`. This is the most valuable remaining reference-integrity job.
- **`tmp/moc7-poster/` holds durable build assets** (`build.sh`, the figure SVGs) in a throwaway
  directory — an `AIW-145` violation. The poster build overwrites `drafts/moc7-poster-fig-2x2.svg`
  from there, which silently reverted a fix mid-session until it was traced. Worth moving to tracked
  `scripts/` + an assets dir.
