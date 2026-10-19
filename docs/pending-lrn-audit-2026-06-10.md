<!-- Action: reference -->
# lrn self-audit — Session 218 (2026-06-10)

Deferred execution (wrap-up + context >50%). Findings captured; rule changes need user consent before applying. Tracked-by: AIW-83, AIW-80.

## FINDING 1 — durable build scripts created in throwaway tmp/ ✅ **FIXED S289 2026-08-06**
**The rule change landed with MG's explicit sign-off on the wording** (`AIW-145`, which superseded `AIW-80`/`AIW-83`/`AIW-114`): `CLAUDE.md` now reads *"Build scripts in `scripts/build_*.py` — tracked; never `tmp/`"*, the Project Structure table and the Build Infrastructure table were rewritten to match, and 9 durable scripts physically moved. **This finding's own prediction was correct and understated** — four scripts named in `CLAUDE.md` turned out to be gone for good, not two (`AIW-156`), and moving one recovered test into `scripts/` immediately surfaced 9 real citation defects in the published RIM paper (`AIW-157`). The diagnosis below stands as written; it is kept for the root-cause reasoning, not as an open task.

ROOT CAUSE: the aIware project CLAUDE.md actively *directs* build scripts into tmp/ — "Publication Pipeline: Build scripts in `tmp/build_*.py`" and the Build Infrastructure table lists `tmp/build_*.py`. This competing project rule (Known Faulty Pattern 5e) overrides the global "tmp/ = throwaway, durable files don't belong here" rule. It is also the root cause of the lost content-integrity tests (they lived in tmp/, vanished on rotation). Not a "follow it better" — the rule structurally points the wrong way.
FIX: change the project CLAUDE.md Publication Pipeline + Build Infrastructure references from `tmp/build_*.py` → `scripts/`.
TARGET: /home/jeltz/aIware/CLAUDE.md (Publication Pipeline section; Build Infrastructure table)
TIER: project-rule (+ AIW-80 migrates the 13 existing tmp/build_*.py and the missing tests)

## FINDING 2 — claimed a capability was unavailable without checking
ROOT CAUSE: told the user "no Zenodo token configured, I can't auto-deposit" from a shallow grep (.mcp.json/vault only), ignoring the obvious contradicting evidence — the cosmology paper and prior FMT v7/v9 were ALREADY on Zenodo. Did not grep `scripts/` (where `zenodo-upload.sh` lives) nor ask "how did the existing artifact get there?".
FIX (executed S218, knowledge capture — discovery→ingest, not a behavioral-rule change): documented the Zenodo + bot-blocked-PDF tooling in `.claude/knowledge/publication-build.md`, incl. an explicit "Zenodo deposit IS available — never tell the user it can't be done."
OPTIONAL general guard (user decides): a project rule — "Before telling the user a task is impossible or a tool/credential is missing, grep `scripts/` and check whether the capability already produced an artifact." Risk: borderline Pattern-2 (general principle). Lean: the knowledge capture already prevents the concrete recurrence; add the general rule only if the user wants it.

## DISCOVERIES persisted (publication-build.md)
- Zenodo upload mechanism (scripts/zenodo-upload.sh, .env.zenodo, concept DOI, ZENODO_VERSION).
- Playwright PMC-redirect + same-origin-fetch method for bot-blocked OA PDFs (14/15 recovered S218).
