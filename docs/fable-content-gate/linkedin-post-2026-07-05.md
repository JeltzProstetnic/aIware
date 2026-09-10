# LinkedIn post — Fable-5 refusal pattern

Target: 300-450 words. Cold-open hook (no thread context). Reference Anthropic by name, do not tag.

---

Anthropic's top-tier model, Claude Fable 5, spent today helping me with security and infrastructuire work I'd have expected it to refuse. 

Then I asked the same model, on the same account, on the same day, to peer-review three of my consciousness-theory manuscripts — the Four-Model Theory of consciousness paper (full v11), an intelligence paper, and a cosmology paper. Six subagent invocations across the three. Every single one refused with the same generic Usage-Policy template.

Two distinct refusal signatures showed up. Some refusals were pre-flight: zero tokens generated, zero tool actions taken, three to nine seconds elapsed — a classifier scanning the manuscript before Fable ever ran. Others were in-flight: the model started reading, took several tool actions, produced a few hundred tokens of legitimate review, then hit a mid-process policy check and stopped.

I ruled out the usual candidates. Prompt length wasn't the trigger — a 150-word prompt refused. Prompt framing wasn't it — a bare haiku and a 350-word meta-question ran without issue from the same session. I even prepared an aggressively redacted version of the main manuscript, stripping 79 paragraphs — roughly 7,000 words — of altered-states, dissociation, and anesthesia material. The redacted version still triggered a pre-flight refusal. The common factor across all six failures was consciousness / AI-architecture / self-referential-computation content in the manuscripts themselves.

Why this matters: Fable was nominally re-enabled for EU users today, so this isn't a regional restriction. It's a content-category gate that was not announced. At least one hidden policy layer is empirically demonstrated on a model many researchers rely on for serious work. A classifier trained on jailbreak-adjacent clusters — where "act as a conscious system" adversarial prompts live — catching legitimate consciousness research as a false positive is one plausible explanation. It is not the only one.

I'm not claiming Fable is a bad model, and I'm not claiming Anthropic is acting in bad faith. I am claiming that a frontier model which admits adult and infrastructure workloads but silently refuses academic peer review of consciousness papers deserves a public explanation.

To Anthropic: which content categories are gated, and why? Is there a documented route for legitimate research to bypass false positives?

To colleagues working on consciousness, alignment, or philosophy of mind who use Fable: are you seeing the same pattern? I'd be interested in the comparison.

— Matthias Gruber
