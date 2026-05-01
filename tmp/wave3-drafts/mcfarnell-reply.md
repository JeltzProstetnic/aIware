To: scott.mcfarnell.research@gmail.com
From: matthias@matthiasgruber.com
Subject: Re: ACU and self-model architecture — complementary frameworks?
References: <CAAAXBjOGz_vJxd5o-7uU6yphoM4htUWqbGzeghRA-bng5vObkA@mail.gmail.com> <CAAAXBjO7k8JDWHQSTFzGAa7tMGidis9mArV_L25jdVH0MFpTUA@mail.gmail.com>
In-Reply-To: <CAAAXBjO7k8JDWHQSTFzGAa7tMGidis9mArV_L25jdVH0MFpTUA@mail.gmail.com>
Status: SENT 2026-05-01 (Message ID: 19de3b85aa54f358, Thread: 19c919733ddfa66d)
Sent-via: matthias@matthiasgruber.com (Gmail send-as)
Edits-before-send: §4 third-collaborator paragraph rewritten — corrected ACU/Australian-Catholic conflation; UK candidates (Haggard/UCL, Tsakiris/Royal Holloway, Mediano/Imperial) replaced wrong Sydney candidates.

---

Dear Scott,

Apologies for the gap — three weeks of journal-rejection housekeeping ate the calendar. Back on this now.

Your design is essentially the experiment. Same task throughout, vary affective variance and time pressure orthogonally, dissociate accuracy / vividness / agentive commitment as three separate measures. That's the right shape and I don't want to over-engineer it. A few sharpening points so the registered report locks the predictions cleanly:

**1. The FMT-vs-ACU fork, written as preregisterable contrasts.**

- Fork A (vividness × affective variance). FMT predicts a null or near-null effect of affective variance on vividness ratings, and a substantial effect on agentive commitment ratings. Specifically: vividness should track perceptual difficulty (signal-to-noise of the stimulus), not stakes. ACU predicts vividness scales with affective variance, with or without an additional agency effect. Operationally this is the interaction term in a vividness ~ difficulty × affective_variance model: FMT = main effect of difficulty only; ACU = main effect of affective_variance (or interaction).
- Fork B (agency × time pressure). FMT predicts a piecewise function — agentive commitment flat across loose deadlines, then a step-up once the deadline crosses the implicit-resolution threshold. ACU predicts a smooth monotonic increase. Three deadline levels (long / medium / short) is the minimum to detect this; four would be safer. Test: model comparison between a piecewise (changepoint) fit and a linear/sigmoid fit.

If we preregister those two contrasts as the primary analyses, the predictions are locked and the design is doing real work regardless of which way the data go.

**2. One addition to your trial structure.**

Worth interleaving, on a subset of trials, an "ownership probe" that asks "did the choice feel like *yours*, or did it feel automatic?" alongside the confidence rating. Confidence and ownership are correlated but separable, and ACU and FMT predict them slightly differently — ACU collapses them via the affective signal, FMT keeps them dissociable because confidence is a perceptual metacognitive readout while ownership is an ESM signature. If they dissociate, that's a third independent contrast.

**3. Cortex as venue.**

Stage-1 in-principle acceptance is the whole point — it neutralises the desk-reject pattern that has been the structural problem for the FMT papers so far. We submit hypotheses, design, and analysis plan; reviewers evaluate the design on its merits; data come second. Their adversarial-collaboration framing fits this exactly.

**4. Third collaborator.**

Both of us are independent, so the third author is the institutional anchor. Online platforms (Prolific, Pavlovia) shrink the participant-pool ask substantially — what we mainly need is institutional affiliation, ethics approval, and a co-PI who has run this kind of paradigm before. A postdoc-level collaborator is plenty; we don't need a senior name. UK candidates worth considering, given you're closer to that side: Patrick Haggard's group at UCL (sense of agency is their core territory, near-perfect topical fit), Manos Tsakiris at Royal Holloway (perception × affect × agency intersection), or Pedro Mediano at Imperial (computational signatures, currently co-authored with Seth on the IIT critique — relevant ecosystem). Happy to do the outreach myself once the protocol stabilises; if any are in your network already, ping them yourself.

Concrete next step: shared Google Doc for the protocol, with sections for hypotheses, design, measures, analysis plan, and power calculation. I'll set one up this week and send the link. Once the protocol stabilises we approach candidate third authors with a near-complete Stage-1 draft rather than a vague pitch — much higher hit rate.

Best,
Matthias

---

## Notes for Matthias

**Word count:** ~485 words (target 350-500). On budget.

**Decision points / fact-checks:**

1. **Third-collaborator candidates.** I named Joel Pearson (UNSW), Anina Rich and Alex Holcombe (Macquarie), and Micah Allen (USyd, but I'm uncertain whether he's still there — check before sending; he may have moved to Aarhus or elsewhere). Pearson is the most direct fit for vividness measurement. **Verify these names are still at those institutions and not in conflict with anyone you'd rather not collaborate with.** If any of them is on your "no-go" list, swap the name.

2. **Three-week delay framing.** I went with "journal-rejection housekeeping ate the calendar" — true (C&C rejection Apr 13, JCS prep) and dry. If you'd rather not flag the rejections, swap for something neutral like "other deadlines ate the calendar." Per AIW-59 instructions, no grovelling.

3. **Ownership probe addition.** This is my own extension, not in Scott's draft or your Apr 7 mail. It's defensible (separating confidence from felt-ownership is standard in agency research, e.g. Haggard's work) and adds a third independent contrast. If you'd rather keep the design tighter — only Scott's two forks — delete the entire "(2) One addition" section. The reply still works.

4. **Sydney-candidate framing.** I assumed ACU's small infrastructure → look to bigger Sydney universities. If Scott is on the ACU Melbourne campus rather than Sydney, swap for Melbourne Uni / Monash / La Trobe. **Check Scott's institutional address before sending.**

5. **"Postdoc-level collaborator is plenty" line.** This is a real signal — we don't need a famous co-author, we need someone with ethics + pool + paradigm experience. But it could read as condescending toward Scott's seniority concerns. Consider softening if it lands wrong.

6. **Shared doc commitment ("I'll set one up this week").** This is a real promise that needs to be kept within ~7 days of sending. If you can't commit to that turnaround, downgrade to "happy to set one up — let me know if you'd prefer that or staying on email."

7. **Greeting/sign-off.** "Dear Scott" / "Best, Matthias" matches your established register in the thread. No changes needed.

8. **Subject line.** Preserved exactly: "Re: ACU and self-model architecture — complementary frameworks?". Don't let your mail client mangle it.

9. **Sending alias.** matthias@matthiasgruber.com (Gmail send-as) per AIW-59 — same alias the rest of the thread uses.

10. **Not verified independently:** ACU's actual research infrastructure (whether they have a participant pool / EEG lab). I assumed not based on AIW-59's "ACU is small, no scanner" framing. If they do have something, the third-author paragraph needs softening to "to widen the participant pool" rather than implying ACU has nothing.
