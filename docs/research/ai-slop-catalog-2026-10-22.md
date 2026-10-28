# AI-slop pattern catalog — web research, 2026-10-22 (S354)

Research subagent (Opus), 22 sources, for MG's request: "after a good research (i cant be the only one
doing this worldwide) known ai slop patterns that i missed." Use with `.claude/knowledge/prose-register.md`.
**Principle (MG):** nothing is banned on one use; accumulation and overuse are the problem. The sources agree.

Tags: [RX] regex finds it · [RX+R] regex candidates, reader decides · [R] reading only.

## Top 15 new patterns (not in prose-register before S354), most likely in a twice-scrubbed LLM-assisted book

1. **Aphoristic ender** [RX+R] — paragraph ends on a short quotable epigram ("A theory that explains everything has stopped explaining."). Audit paragraph-final sentences < 12 words. (Velitchkov #1)
2. **Mirrored-clause symmetry** [RX+R] — two clauses, same frame, slots swapped ("Physics fixes the stage; biology writes the script."). Where not-X-but-Y goes once "not" is scrubbed.
3. **Colon reveal / suspense hook** [RX] — "The answer is simple: …"; "This problem has a name."; "comes down to this".
4. **Significance signalling** [RX] — "This matters because…"; "matters" is a mid-2026 tell (Wikipedia).
5. **Clean-consequence connectors** [RX] — "falls out of", "follows directly/naturally", "drops out", "is no accident".
6. **Confidence by litotes** [RX] — "is not optional", "it is not hard to see", "not without". Mid-sentence relative of denial openers.
7. **Restatement gloss** [RX] — "in other words", "put differently", "that is to say". Flag > ~1 per 2k words.
8. **Reflexive calibration hedges** [RX] — "largely", "roughly", "tends to", "almost always"; the tell is uniform rate.
9. **Participial tails** [RX] — ", highlighting/underscoring/making/leaving/ensuring …". Best-measured structural tell: 5.3× human in GPT-4o (Reinhart et al., PNAS 2025).
10. **Nominalization and doublet density** [RX] — -tion/-ment/-ness/-ity nouns 2.1× human (GPT-4o); "X and Y" doublets 1.9×.
11. **Uniform sentence/paragraph rhythm** [RX] — sentence-length CV human ≈ 0.45 vs AI rewrite ≈ 0.38 (TextPulse, 60,779 pairs); rewrites flatten rhythm.
12. **Corrective pivot / anticipate-and-rebut / reframe** [RX+R] — "It would be wrong, though, to…"; "…as though it carried no stance. It carries one."; "The real question is".
13. **Invented concept labels + self-echo** [RX+R] — coined labels re-used as stamps; distinctive 3–5-grams recurring ≥ 3 times across chapters.
14. **Magic adverbs** [RX] — genuinely, precisely, exactly, quietly, fundamentally, structurally; plus validate-then-precision ("is right, and it can be made precise").
15. **Synonym cycling and recurring metaphor families** [R + lemma counts] — theory/account/framework/model rotating; one image family (price/cost/pay/ledger, shape/texture/sits) across chapters. The economic-metaphor cluster has no published source: MG's own observation.

Runners-up: fractal summaries (preview → content → recap at every level), staccato fragments, balanced-take seesaw ("While X has merits, Y…"), candor flags ("the honest answer"), contribution framing ("supplies the missing half"), stacked rhetorical questions, rhetorical question answered at once, "Not X. Not Y. Just Z.", deflating tail ("…and no more."), copula avoidance ("serves as"), vague attribution ("critics argue"), connector-addicted paragraph openers (> ~30 %), em-dash density (historical ≈ 2.5 per 1k words; flag sustained > 5), content duplication (8-gram overlap between distant paragraphs).

## Lexical lists (they drift by model generation; a twice-scrubbed text has usually lost the old ones)

- Kobak et al. 2025 (Sci. Adv.): delves (r = 28), underscores (13.8), showcasing (10.7); potential, findings, crucial, comprehensive, notably, particularly.
- Juzek & Ward 2025 (COLING): delve(s/d), showcasing, boasts, underscores, intricacies, intricate, realm, groundbreaking, garnered, aligns.
- Liang et al. 2024 (ICML): commendable, meticulous, intricate, notable, versatile; meticulously, lucidly, aptly, undoubtedly, profoundly.
- Reinhart et al. 2025: tapestry, camaraderie, palpable, amidst (100–170× human).
- Wikipedia mid-2026 list: challenge, clearer, dependable, echoed, foster, leverage, matters, multifaceted, practical, prioritize, quietly, steady, universally.
- Claude-ish (Mollick, HN, Velitchkov): load-bearing, key insight, push back, lands, "I keep coming back to", "the honest answer", earned, sits, "the shape of", texture.

## Sources

- Wikipedia: Signs of AI writing — https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Kobak et al., Sci. Adv. 2025 — https://pmc.ncbi.nlm.nih.gov/articles/PMC12219543/
- Liang et al., ICML 2024 — https://arxiv.org/abs/2403.07183 ; https://arxiv.org/pdf/2404.01268
- Juzek & Ward, COLING 2025 — https://aclanthology.org/2025.coling-main.426.pdf
- Reinhart et al., PNAS 2025 — https://arxiv.org/html/2410.16107 ; notebook https://www.refsmmat.com/notebooks/llm-style.html
- Herbold et al. 2023 — https://arxiv.org/abs/2304.14276
- Paech et al., Antislop (ICLR 2026) — https://arxiv.org/pdf/2510.15061
- Pangram — https://www.pangram.com/blog/walking-through-ai-phrases
- GPTZero — https://gptzero.me/news/most-common-ai-vocabulary/
- Washington Post via Boston Globe — https://www.bostonglobe.com/2025/11/13/business/chatgpt-writing-style-clues/
- Goedecke, em-dashes — https://www.seangoedecke.com/em-dashes/
- Kriss (NYT) summary — https://atsixtyseven.com/why-does-ai-write-like-that/
- Velitchkov, 22 Claude Clichés — https://www.linkandth.ink/p/catalog-of-claude-cliches
- LessWrong, Problems with AI prose — https://www.lesswrong.com/posts/nTuKjJBwMtMuuLonA/hot-take-problems-with-ai-prose
- tropes.fyi — https://tropes.fyi/directory
- Vollmer, Field Guide to AI Tells — https://matthewvollmer.substack.com/p/i-asked-the-machine-to-tell-on-itself
- sneak, LLM_PROSE_TELLS — https://git.eeqj.de/sneak/prompts/src/branch/main/prompts/LLM_PROSE_TELLS.md
- unslop — https://github.com/crypdick/unslop/blob/main/skills/unslop/references/ai-writing-patterns.md
- autonovel ANTI-SLOP — https://github.com/NousResearch/autonovel/blob/master/ANTI-SLOP.md
- Stockton, Don't Write Like AI — https://www.blakestockton.com/p/sentence-stacking
- Algorithmic Bridge — https://www.thealgorithmicbridge.com/p/10-signs-of-ai-writing-that-99-of
- Robots Ate My Homework (defence) — https://robotsatemyhomework.substack.com/p/ai-writing-patterns
- TextPulse burstiness — https://textpulse.ai/research/ai-burstiness-sentence-length
