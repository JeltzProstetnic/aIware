<!-- Action: reference -->
<!-- Tracked-by: AIW-174, AIW-254, AIW-100, AIW-03, AIW-10, AIW-63, AIW-156, AIW-166, AIW-167 -->
# S315 — the nine open items the publish gate raised against cosmology v6, and the ruling on each

MG's direction was *"ship now"*, given after being told the two paragraph-sized P2s are not as
cheap as the S315 brief assumed. **All nine are deferred, deliberately.** v6 is a scoped
correctness release — one symbol was carrying two different claims — and none of the nine is a
correctness defect in what v6 ships.

| item | ruling | why |
|---|---|---|
| `AIW-174` (P0, in progress) | **defer** | Its own note records that the derivation reduces to a single premise **the paper already holds** — §5.2's single-surface ontology, adopted to unify singularities for reasons unconnected to Bell. What is owed is the write-up of that reduction, not a repair to anything v6 touches. Open since S293 and deferred at v4 and v5 on the same reasoning. |
| `AIW-166` (P2) | **defer — this is MG's own ruling of today** | Told that `AIW-166` carries its own design document (`drafts/aiw166-cosmos-transfer.md`) and is not a paragraph, MG chose to ship. Recording it here so the deferral is his and not a session's. |
| `AIW-167` (P3) | **defer** | The missing world/self axis is a structural addition to §7, not a defect. It would enlarge the mapping v6 has just made internally consistent, which is the wrong order. |
| `AIW-63` (P1) | **defer** | An empirical programme (Planck SMICA, multifractal analysis), not paper text. Its sibling `AIW-163` is the instrument positive control the same programme needs first. |
| `AIW-03` (P2) | **defer** | An SSRN submission task. Nothing to fold into a PDF. |
| `AIW-10` (P3) | **defer** | Tracks the three formalization roadmaps as a set. The cosmology member is revised in this pass; the item is broader and stays open. |
| `AIW-100` (P1) | **defer** | The Standard-Model-of-Consciousness convening dimension is **parked** by MG until a crucible robot result. Nothing to fold. |
| `AIW-156` (P2) | **defer** | Build-script validation. `scripts/test_build_scripts.py` remains quarantined against a superseded pipeline API; the three build scripts themselves were validated end-to-end at S300 and again today. |
| `AIW-254` (P2) | **defer** | Book publication state across `README.md`, `kdp-specs.md` and the marketing doc. Does not reach the cosmology PDF. ⚠ Noted while checking: `README.md` still describes the formalization as **Eight modules** where the paper has said **Nine** since S300 — folded into `AIW-254`. |

## What shipped in v6

The Φ equivocation, in both cosmology papers. §6.3 had already defined Φ as encoding composed with
decompression and rejected the "whatever the system does" reading; §6.4, §7.1 and §7.2 had not
caught up, and the formalization's §5 was still built on the rejected reading throughout. Detail is
in `docs/zenodo-changelog-cosmology-v6.md`.

## What did NOT ship, and is the one thing to decide next

**The formalization was revised but not separately deposited.** Its canonical PDF is promoted and
current in the repository; whether its own Zenodo record should be bumped is open. The argument for
doing it: its published copy now states a fixed point the parent paper's published copy rejects,
which is the cross-document divergence v6 exists to remove. The argument against: it was not
separately republished at v5 either, and a DOI is not spent lightly. **MG's call.**
