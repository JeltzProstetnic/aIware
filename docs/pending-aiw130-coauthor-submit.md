<!-- Action: reference — S277 handover. AIW-130 co-author round → submission. Tracked-by: AIW-130, AIW-103, AIW-62. -->
# AIW-130 — co-author round → submission (S277 → next)

Both papers are first-draft-**APPROVED by MG** and built with figures. Co-author invites **SENT 2026-07-30**.

## State
- **NoC (Lane A, AIW-103):** `drafts/aiw130-noc-draft.md` + `drafts/aiw130-noc-cover-letter.md`. Reframed (necessity + constitutive; over-claim killed; strictly one-directional). Title: "More Than Computation, Made of Computation: … a Self-Model That Takes Itself for Its Bearer." Provisional co-author **Georgia Sousouri**. PDF `tmp/aiw130-build/aiw130-noc.pdf`. NoC-SI deadline **2026-12-31**; single-blind; ≤9k words.
- **JAIC (Lane B, AIW-62):** `drafts/aiw130-jaic-draft.md` + `drafts/aiw130-jaic-cover-letter.md`. Math verified (Box 1 B1 contradiction fixed; σ→m; B2–M8) + register swept clean. Provisional co-author **Alen Frey**. PDF `tmp/aiw130-build/aiw130-jaic.pdf`. Section "Assessing AI Consciousness"; EiC = Kanai; no word cap.
- Figures: `figures/aiw130/*.{svg,pdf,png}` (tracked); generator `scripts/gen-aiw130-figures.py`. Build: `bash scripts/build-md-pdf.sh <in.md> <out.pdf> -H tmp/aiw130-extra-preamble.tex`.

## Next actions (in order)
1. **Await Georgia + Alen replies** (Gmail invites sent from matthias@, cross-cc'd). Per-person: `correspondence/{sousouri-georgia,frey-alen}.md`.
2. **Resolve affiliations (MG decision):** Alen = Ivoclar vs independent/ETH (IP + symmetry with MG's "Independent researcher" line); Georgia = confirm ETH/Children's-Hosp; both ORCIDs. Update author blocks + CRediT (currently marked *provisional — pending consent*).
3. **Fold contributions into v2** — Georgia: §5 interventional-necessity EEG protocol (closed-loop auditory stim) + vet sleep/anaesthesia claims. Alen: Box 1 review + §6 in-silico grounding (= crucible Target A / CRU-57).
4. **On MG go:** finalize + submit. Update AIW-103 / AIW-62 / AIW-130 on submission.

## Crucible ↔ JAIC detector (MG asked S277)
Checks 1 & 3 pass at toy scale; check-2's decisive scaled form (capability dies when the loop is cut, graded/novelty-relative) is OPEN = the paper's own "open scaled test." Movers: Target A / AIW-124 (port the d=2.44 ESM-ablation to the large spiking brain) + CRU-57 (plastic closure engine that must beat a linear delay-line, gate G9). If it lands → "detector passed on our own substrate" = a strong revision/follow-up result. Alen's §6 contribution IS this work.

## Also carried
- `docs/pending-claude-md-build-scripts-location.md` (follower S277) — CLAUDE.md convention fix (build scripts tmp→scripts), deferred per CFG-384 → apply on next SOLO session with MG consent.
- `docs/pending-lrn-audit-2026-07-30.md` (follower S277) — lrn audit; triage next session.
- Pipeline hardened → `scripts/fmt-pipeline/` (register-ai-tell + theory-fidelity reviewer lenses + RE-REVIEW hard gate). Reuse for future FMT slices.
- numpy 2.5.1 installed on WSL (`--break-system-packages`) → matplotlib works; note in `~/.claude/machines/wsl.md` (inbox item filed for cfg-agent-fleet).
