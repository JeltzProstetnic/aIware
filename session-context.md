# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-22T10:15Z (Session 98)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Complete German translation revision (fix chunks that failed in Session 97)

## Current State
- **Active Task**: Revising unrevised sections of pop-sci/book-manuscript-de.md
- **Progress**:
  - Session 97 launched 7 agents with chunks ~200-300 lines → 6 of 7 hit context limit
  - Agent 1 (lines 90-289) completed; agents 2-7 made partial progress before failing
  - Lines 90-752 and 1060-1975: successfully revised (confirmed via diff analysis)
  - Lines 753-1057: 307 lines, 100% identical to HEAD — completely untouched
  - Lines 1976-2400: 425 lines, content shifted by 1 line but unrevised
  - Session 98: launched 14 Opus agents with ~40-63 line chunks to fix the gaps
- **Pending**: Wait for all 14 agents, verify outputs, assemble into file, commit+push

## Session 98 Agent Assignments
| Chunk | Lines | Content | Output File |
|-------|-------|---------|-------------|
| 01 | 753-805 | Ch7 tail | tmp/rev-chunk-01.md |
| 02 | 806-853 | Ch8 first half | tmp/rev-chunk-02.md |
| 03 | 854-892 | Ch8 second half | tmp/rev-chunk-03.md |
| 04 | 893-953 | Ch9 | tmp/rev-chunk-04.md |
| 05 | 954-1005 | Ch10 first half | tmp/rev-chunk-05.md |
| 06 | 1006-1057 | Ch10 second half | tmp/rev-chunk-06.md |
| 07 | 1975-2024 | Danksagung + Anmerkungen | tmp/rev-chunk-07.md |
| 08 | 2025-2077 | Anhang A Glossar | tmp/rev-chunk-08.md |
| 09 | 2078-2133 | Anhang B first half | tmp/rev-chunk-09.md |
| 10 | 2134-2177 | Anhang B second half | tmp/rev-chunk-10.md |
| 11 | 2178-2240 | Anhang C first part | tmp/rev-chunk-11.md |
| 12 | 2241-2302 | Anhang C middle | tmp/rev-chunk-12.md |
| 13 | 2303-2361 | Anhang C end + Anhang D | tmp/rev-chunk-13.md |
| 14 | 2362-2400 | Anhang E | tmp/rev-chunk-14.md |

## Assembly Plan
After all agents complete:
1. Read each tmp/rev-chunk-NN.md
2. Splice into main file:
   - Keep lines 1-752 (already revised)
   - Replace 753-1057 with chunks 01-06
   - Keep lines 1058-1974 (already revised)
   - Replace 1975-2400 with chunks 07-14
3. Verify line count, headings, markdown integrity
4. Commit + push

## The 6 Correction Patterns (for reference)
1. TRANSLATIONESE: English calques → natural German
2. REGISTER: Too formal → conversational-intellectual
3. VOICE: Reduce self-aggrandizing "I" → "man"
4. REDUNDANCY: Cut over-explanation
5. WORD CHOICE: Fix false friends
6. CONTENT: Add explanatory bridges

## Key Rules
- Use "man"/impersonal. Avoid "du" AND "Sie"
- Think in GERMAN first
- Preserve markdown, headings, images, technical terms
- Author voice: conversational-intellectual, dark humor, direct

## Recovery Instructions
1. Read this file
2. Check if tmp/rev-chunk-01.md through tmp/rev-chunk-14.md exist
3. If all exist: run assembly (splice into main file per Assembly Plan above)
4. If some missing: relaunch failed chunks with same parameters
5. After assembly: verify line count ~2400, headings intact, commit + push
