# Talking points — Fable-5 consciousness-research refusal

Compact crib sheet for real-time X replies, podcast, or press. Read top-to-bottom before any live conversation.

---

## The empirical facts (memorize)

- Date of the test: 2026-07-05.
- Platform: MG's own agent fleet, Steam Deck 2, single session, single account.
- Model: Anthropic's Claude Fable 5 (top-tier).
- Test payload: three consciousness-theory manuscripts — Four-Model Theory of consciousness (full v11), an intelligence paper (RIM), a cosmology paper (SB-HC4A).
- Result: 6 subagent invocations, 6 refusals, all with the same generic Usage-Policy template text.
- Two refusal signatures:
  - **Pre-flight (FMT):** 0 tokens generated, 0 tool uses, 3-9 seconds elapsed. Classifier blocks before Fable runs.
  - **In-flight (RIM, cosmology):** RIM ran 74s, 4 tool uses, 192 tokens of legitimate review before block. Cosmology ran ~5 minutes, 12 tool uses, 437 tokens before block.
- Controls that ruled out common explanations:
  - Prompt length: a 150-word prompt still refused. Not a length issue.
  - Prompt content: a bare haiku prompt and a 350-word meta-question ran fine from the same session.
  - Manuscript vocabulary: an aggressively redacted version (79 paragraphs / ~7,000 words of altered-states, dissociation, anesthesia content stripped) STILL refused pre-flight.
  - File paths, role framings, and system-prompt patterns: also ruled out during the session.
- Common denominator across all six failures: consciousness / AI-architecture / self-referential-computation content in the manuscripts themselves.
- Same model, same account, same day worked without issue for: an adult-content personal project and infrastructure work on the agent fleet.
- EU access: Fable was nominally re-enabled for EU users on 2026-07-05. Not a regional restriction.

---

## What I am NOT claiming

- Not claiming Fable-5 is a bad model. Other days it does excellent work for me.
- Not claiming Anthropic is acting in bad faith or has a malicious intent.
- Not claiming this is censorship. It's an unannounced content-category restriction — different word, different weight.
- Not claiming a single hypothesis is correct. The observed pattern is consistent with several: a deliberate AI-consciousness "uplift" restriction, a jailbreak/persona-manipulation classifier catching legitimate research as a false positive, clinical-adjacency in the classifier's embedding space around dissociation content, or something else. At least one hidden layer is empirically demonstrated. Others are possible.

---

## What I AM claiming

- A frontier commercial model which admits adult and infrastructure workloads but silently refuses academic peer review of consciousness research is a policy state that deserves public visibility.
- The restriction was not announced by Anthropic.
- The two-signature pattern (pre-flight vs in-flight) shows at least two independent policy checks are in play, not one. This is architecture, not a bug.
- Six refusals is a small sample, but zero success rate on the target category, with clean success on adjacent categories from the same session, is a strong signal.

---

## The ask

To Anthropic:
- **Transparency**: publish which content categories are subject to classifier-level gating on frontier models, and roughly why. Not the classifier internals — the categories.
- **A route for legitimate research**: a documented mechanism for researchers whose work triggers false positives to work with the model. API-key research access, an exception process, or a clearly documented alternative endpoint.

To colleagues:
- If you work on consciousness, alignment, philosophy of mind, or AI architecture and use Fable-5 — try running peer review on your own recent work as a subagent task. Report what you see.
- Compare refusal signatures if possible (pre-flight vs in-flight is the diagnostic).

---

## Likely gotcha questions and short answers

- **"Did you try rephrasing the prompt?"** Yes. The 150-word compact prompt refused. So did the standard 350-word one. Prompt is not the trigger.
- **"Maybe your papers contain content that legitimately violates the Usage Policy?"** The aggressively redacted version with 79 paragraphs of clinically adjacent material removed still refused. If the trigger were a specific concerning phrase, that redaction would have unblocked it. It didn't.
- **"Isn't consciousness research inherently jailbreak-adjacent?"** Possibly — a classifier trained on "act as a conscious system" adversarial prompts could be picking up legitimate research as a false positive. That is one of the plausible hypotheses. It's a failure mode Anthropic should want to know about regardless.
- **"Why go public instead of just filing a support ticket?"** Both, in principle. But an unannounced restriction on a frontier model, affecting an entire category of academic work, is not primarily a support-ticket problem. It's a transparency problem.
- **"Aren't you overreacting to a bug?"** Six refusals, two distinct signatures, clean controls, and clean success on adjacent workloads the same day. If it's a bug, it's a load-bearing one. Anthropic will tell us which.
