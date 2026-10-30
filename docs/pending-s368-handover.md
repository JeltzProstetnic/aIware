<!-- Action: await-user-decision -->
<!-- Tracked-by: AIW-367, AIW-363, AIW-361, AIW-130, AIW-321, AIW-243, AIW-142, AIW-263, AIW-201, AIW-366, AIW-351 -->
# S367 → S368 handover (written 2026-10-30 ~21:30, WSL)

Full record: `docs/conversation-log.md` § Session 367; decisions D-S367-A…U in `docs/decisions.md`.

## 1. Order of work, in MG's words
1. **S367-L discussion first** — MG: *"1. lets discuss now"*, then *"we'll postpone the theory discussion to next session since you obviously suffer from context rot already"*. Ask S368-A below.
2. **Then, in parallel:** MG: *"2. 3. 4. 5. 6. first thing next session, in parallel with the second JAIC paper work"* — i.e. AIW-321 (PP paragraph: active inference now has a consciousness theory, Whyte et al. 2024 + Robinson et al. 2025, not yet in the master), AIW-243 (v15 leftovers), AIW-142 (five external works to place; Pattee already in the master, check the other four), AIW-263 (free-will part (ii), awaits MG confirmation), AIW-201 (capability-null inversion) — alongside the detector, AIW-130 (the second JAIC paper). See S368-B on how the detector proceeds.
3. **Then the formalization review** — MG: *"1. after the work is done"*. AIW-367: v7 source ready (47 pp, gates green; build `tmp/build-fmt-formal/fmt-formalization-v7.pdf`); changes PDF vs v6 only when MG asks; deposit AFTER the master (v7 cites definitions that exist only at master HEAD); then ABOUT.md row 5 (still "v5") + canonical PDF.
4. **Waiting on crucible ("a few more days", MG):** companion v7 (AIW-361, D-S367-H: add D10 + CRU-234/238), detector status re-check (AIW-130, D-S367-C), master T5 Principle 2 "survive their own inputs" (AIW-363, CRU-238).
5. **Monday 2026-11-02:** MG sends the van der Vlag reply (Gmail draft r-8105962394251957582, research@; fleet calendar 09:30 @crucible). Package waits for crucible (CRU-239).
6. **AIW-366 lrn bundle is with cfg** (P0: CFG-609 restore, auto-memory off fleet-wide + 7 orphans, pre-push secret scan + masked settings read, restored rules re-checked before commit + rule-removal guard + lrn self-integrity; P1: recipient Comms hook CFG-887, reply-length rule, CFG-24 retired / delete-locally clause). Verify when cfg reports; detail `docs/pending-lrn-audit-2026-10-30.md`.

## 2. State
- FMT master at HEAD carries undeposited MG-ruled edits: S366 framework rulings, S367 §8 rewrite (D-S367-I), rank clause (S367-K), E15. AIW-363 = MG reviews, then a new FMT version; wiki redeploy only after that (D-S367-A).
- simbook inbox carries two book lessons moved out of aIware memory (German book tone, translation chunking).
- aIware auto-memory holds only a one-line "nothing lives here" note; never write memory files (D-S367-O).

## 3. Decisions for MG (re-verify each premise, then ask with AskUserQuestion, stable IDs)
- **S368-A — the "two sorts of explicit model" sentence (S367-L).** Premise: MG's 2026-10-27 crucible spec (`~/crucible/docs/decisions.md`, block around "Never a region, population, slice or module") distinguishes robust sustained patterns (what the body does and senses) from flexible dynamical patterns (prospective planning, simulation); the formalization's §2.1 sentence ("whether a pattern outlives its input is a question about its kind…", visible in `git show cadeba91:paper/fmt_formal/fmt-formalization.md`) was removed on MG's S367-L ruling; master Principle 2 still says explicit patterns "survive their own inputs" (T5 waits for CRU-238). Options: (a) wait for CRU-238, then state the two sorts in master + formalization together with T5 (recommended); (b) state them now in both papers as MG's spec, hedged; (c) keep them as crucible instrument design only, not a paper claim.
- **S368-B — how the detector (AIW-130) proceeds now that crucible's results take a few more days.** Premise: D-S367-C ties the status re-check to those results; MG wants detector work next session in parallel with AIW-321…201. Options: (a) work on the detector now on the current record and run the D-S366-C/E status re-check when the results land (recommended); (b) hold all detector work until the results land.

No credentials needed.
