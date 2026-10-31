# AIW-108 — ZH Kalk-scan findings (native-Simplified-Chinese calque/naturalness sweep)

Session 254, 2026-07-10/11. Method: parallel **Opus 4.8** native-Simplified-Chinese editors over `pop-sci/book-manuscript-zh.md` (36 general @70ln + 54 aggressive checklist-primed @46ln = 90 agents). **354 findings: A=235, B=114, C=1, D=4.** (Translation: Fable, EN+DE dual-source.)

Per MG policy: **A + B applied, D softened (warm-middle), C kept.** **288 applied** via verified match-once (`tmp/kalk_apply.py`). Plus systematic mechanical fixes: **16 half-width commas between CJK → full-width （，）**, and earlier **160→2 straight→curly quote normalization** (CJK content) + **3 dropped chapter separators** restored (now 45, matches EN).

**Not applied (44):** overlap-duplicates (the 70ln & 46ln passes cover the same text; twin fix already applied — spot-verified: English-word leak 'signature', 十亿倍 grandeur, 社交本领, half-colon all confirmed fixed by twins). Listed by category below for the reviewer.

## D — grandeur softenings (warm middle) — APPLIED (4) — reviewer tone-check
- **[seg 14·grandeur]** 「那感觉比自由潜水或水肺潜水，乃至侧挂式潜水，都要好上十亿倍」 → 「那种感觉，比自由潜水、水肺潜水乃至侧挂式潜水都要好上千百倍」 — 「好上十亿倍」is US-style hyperbolic boasting; soften to warm-middle wonder while keeping the awe.
- **[seg 25·grandeur]** 「而如果这一切还没有让你想坐下来定一定神，那你就还没有真正读懂它。」 → 「如果读到这里，你还没有一点想坐下来缓一缓的冲动，那也许你还没真正读进去。」 — EN "if this doesn't make you want to sit down... you haven't really understood it" is a mild you-don't-get-it flourish; soften the accusatory second clause toward the warm middle while keeping the wonder.
- **[seg 22·grandeur]** 「都要好上十亿倍」 → 「简直好过太多」 — “a billion times better” is US-style boasting; keep the wonder but soften the salesmanship.
- **[seg 26·grandeur]** 「整台宏伟的机器慢慢垮掉」 → 「整台精密的机器慢慢垮掉」 — "宏伟" (grand/magnificent) over-inflates "the whole magnificent machine"; warm-middle prefers 精密 (intricate) for the body-as-machine without the boast.

## C — deliberate motifs KEPT as-is (1)
- **[seg 10·motif]** 「那半秒钟的“无人在家”」 — “无人在家”虽是 nobody home 的直译,但此处加引号回指前文已确立的固定说法,属跨段一致的既定母题,保留。

## Ambiguous — quote appears >1×, skipped (0)

## Whole-book coherence pass (S254, 1 Opus read) — 18 findings

**10 zh-only single-fixes APPLIED** (verified match-once): TOC↔heading mismatches — 心智→心灵 (第9/12章), 那个并不存在的点→圆点, 虚拟的一面→那一面, 感觉-quotes removed (第4章), 灯光熄灭→灯熄灭 (第7章), 动物问题→动物的问题 (第10章), 神经学基础→基础神经学 (附录A), 四个模型→"四"个 (附录E), 《Dr. Strangelove》→《奇爱博士》(Dr. Strangelove).

**Chapter-numbering unified (systematic, APPLIED):** 38 references normalized to `第N章` (Arabic, no-space, matching TOC) — 10 Chinese-numeral (第一章…第十一章) + 28 spaced (第 N 章) + 附录 H→附录H.

**5 structural → AIW-109** (NOT patched — THIRD independent confirmation of IT+JA): neuron contradiction (一百万 vs 85,000), Ch.10 off-by-one (上一章→第8章), Coda re-narration, Ch.15 Per Bak re-intro, German-original authorial ref (德语原著).

**DEFERRED to native reviewer (diffuse, judgment):**
- **预言 vs 预测:** the "nine predictions" concept wobbles between 预言 (esp. 附录H: 九个预言, 预言1…9) and 预测 (第11章 mainline: 九个预测). 预言 also appears ~24× in main text. Recommend unifying to 预测, but 预言 may be intended as "prophecy" in some spots — reviewer to judge per-occurrence.
- **real/virtual side term:** 真实的一侧／虚拟的一侧 (dominant) vs 虚拟的那一面 / 真实侧-虚拟侧 (scattered). Reviewer to standardize (literary chapter titles may keep 那一面).

**Status:** ZH = **publish-candidate** (288 Kalk + comma/quote normalization + 3 separators + 10 coherence fixes + chapter-numbering unification). Gate: human native Chinese reviewer before any KDP upload. NOTE: glossary-zh used 「难问题」 (JP/Traditional brackets) but the manuscript correctly uses “” (Mainland) per the culture guide.