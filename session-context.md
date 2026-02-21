# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-21 (Session 95)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: NIdP submission prep + first press pitch

## CURRENT STATE — IN PROGRESS

### Session 95 Completed:
1. **Session 94 commit + push** — All press materials committed, pushed to both remotes
2. **NIdP submission research** — Confirmed requirements via search-specialist agent:
   - 7,500 word limit (body only, abstract/refs don't count)
   - Body is actually 7,400 words — NO TRIMMING NEEDED (earlier 7,858 count included abstract)
   - Abstract: 230 words (under 250 limit)
   - Double-blind review: manuscript must be anonymized
   - Highlights: 3-5 bullets, max 85 chars each
   - Format: .docx, double-spaced, APA 7th, single-column
   - Submit via Editorial Manager on ScienceDirect
3. **Article highlights written** (5 bullets, all under 85 chars)
4. **.docx files created** (two files for double-blind):
   - `paper/intelligence/title-page.docx` — author info, highlights, author note
   - `paper/intelligence/manuscript-anonymous.docx` — full paper, self-citations anonymized ([Author] replaces Gruber)
   - Both copied to Windows Desktop for easy access
   - Build script: `tmp/build_intelligence_docx.js`
5. **First press pitch drafted** — `tmp/pitch-scinexx-podbregar.md` ready to send to scinexx.de

### Key Findings:
- NIdP word limit is body-only (7,500). Paper body is 7,400 words — under limit.
- Double-blind review requires anonymized manuscript (9 self-citations masked)
- Review timeline: ~78 days to first decision, ~178 days to acceptance
- Subscription model = no publication fee

## NEXT STEPS:
1. **Matthias**: Submit to NIdP via Editorial Manager (upload title-page.docx + manuscript-anonymous.docx + highlights)
2. **Matthias**: Review and send pitch email to Nadja Podbregar (scinexx.de) — `tmp/pitch-scinexx-podbregar.md`
3. **Update press release** — change to "Zwei wissenschaftliche Arbeiten befinden sich im Begutachtungsprozess" after NIdP submission
4. **German book review** — author reviewing German manuscript PDF (ongoing)
5. **Quick-reference card** — translate to German for interview prep

## Recovery:
1. NIdP submission files: `paper/intelligence/title-page.docx`, `paper/intelligence/manuscript-anonymous.docx` (also on Windows Desktop)
2. Build script: `tmp/build_intelligence_docx.js` (run with `NODE_PATH=/home/jeltz/.npm-global/lib/node_modules node tmp/build_intelligence_docx.js`)
3. Press pitch: `tmp/pitch-scinexx-podbregar.md`
4. Press materials: `tmp/pressemitteilung-de.md`, `tmp/pitch-email-templates.md`, `tmp/press-release-strategy.md`
5. Source paper: `paper/intelligence/paper.md` (7,400 body words, 230-word abstract)

## Conversation Summary
Continued from Session 94. Committed and pushed Session 94 press materials. Researched NIdP submission requirements (double-blind, 7,500 word body limit). Discovered paper body is only 7,400 words — no trimming needed. Created 5 article highlights (all under 85-char limit). Built two .docx files via docx-js: anonymized manuscript (9 self-citations masked with [Author]) and title page with author info/highlights. Drafted customized press pitch for scinexx.de with psychedelic mechanism hook. User asked about anonymization — explained double-blind review process.
