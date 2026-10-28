<!-- Action: reference -->
<!-- Tracked-by: AIW-328, AIW-320, AIW-322, AIW-312 -->
# S354 → S355 handover

## What S354 did (all committed + pushed)
- No Outside v1.0.3 PUBLISHED 10.5281/zenodo.23577460 (md5 verified; source e42e13ae), from MG's review mails of 2026-10-22 plus a full read-through (`docs/research/no-outside-v1.0.3-fullread.md`) and web research (`docs/research/ai-slop-catalog-2026-10-22.md`). simbook built the KDP set from e42e13ae: `C:\temp\no-outside-kdp`; uploading it to KDP is MG's click.
- FMT v27 PUBLISHED 10.5281/zenodo.23576866 (§3.4.5 no-stance paragraph citing No Outside).
- MG: density, not bans — prose-register.md, simbook checker and `scripts/register_gate.py` all updated.
- Build fix: the Preface and References carry their own running head.

## Next session — first thing (MG S354: "reply next session")
1. **Reply to Dr. Fabian Unterhofer** (Gmail thread 1a15e269512425cf, his mail of 2026-10-22 16:30 UTC). He is interested in principle, says the design needs medical review, and offers a short call — **asks for dates within the next two weeks**. No money mentioned. MG S354: a funded study is "unaffordable for me forever". Draft in Gmail (research@ thread) once MG signals ready: thank him; propose 2–3 call slots (query the fleet calendar first, `knowledge/fleet-calendar.md`); state plainly that there is no budget; ask whether his centre takes part in funded studies and which academic groups he works with. Before drafting: check contacts.md row 73 and update it after MG sends (AIW-328).
2. Then the S353 carry-over: AIW-320, AIW-322 (decisions below), then the RG window (AIW-312: also refresh the No Outside file to v1.0.3 and the FMT file to v27).

## Open decisions for MG — ALL ANSWERED S355 2026-10-23 (see docs/decisions.md S355)
- **Call slots for Unterhofer** (premise: his mail asks for dates in the next two weeks): (a) propose three evening slots via Zoom (recommended — after office hours); (b) let him propose; (c) phone only.
- **AIW-320 baseline choice** (premise: backlog AIW-320 — beating a lookup fitted to past behaviour shows generalisation, not free modelling): (a) a feedforward model of matched capacity trained on the same history (recommended); (b) a recurrent model without self-model closure; (c) both, reported separately.
- **AIW-322 placement** (premise: backlog AIW-322, FMT master §7 / §3.4.3): (a) §7 comparative section, a short reply to the 'dynamical relevance' premise (recommended); (b) a dedicated subsection; (c) a footnote only.
- **Optional: colon density in No Outside** (2.7 per 1k words; a sample of 25 showed ordinary explanatory colons): (a) leave it (recommended); (b) thin the colons in a later version.

## Known issues
- FMT master fails the structural gate on denial openers (1.57/1k vs ceiling 1.2) and callbacks (4.82 vs 2.5) — known since SIM-80; not tackled.
- Prose sources for RIM, SB-HC4A and the three formalizations carry the 'buys' rewording, unpublished; it rides their next versions.
