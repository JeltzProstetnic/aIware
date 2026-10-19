# AIW-142 (5) — Reply to Birch, "AI Consciousness: A Centrist Manifesto"

## Source, as verified

- **Birch, J. AI Consciousness: A Centrist Manifesto.** PhilArchive record BIRACA-4. The current PDF is
  headed **"31 July 2026, v6"** (search-engine snippet of `philpapers.org/archive/BIRACA-4.pdf`).
- **Read: v4, dated 20 May 2026, full text, 32 pp.** — retrieved from the Internet Archive capture of
  `philpapers.org/archive/BIRACA-4.pdf` of 2026-05-24. **v6 could not be read**: philpapers.org and
  philarchive.org return HTTP 403 (Cloudflare challenge) to curl, WebFetch and headless Chromium, and the
  Wayback Machine holds no capture later than May 2026. The backlog item names v4, so the draft engages
  the version the item was filed against; **all page numbers below are v4 pages, and every quotation must
  be checked against v6 before posting.**
- v4's acknowledgements say the article appears in a special issue of *Philosophy and the Mind
  Sciences* (eds. de Weerd, Wiese, Kammerer). No journal DOI found yet (Crossref, OpenAlex). The only DOI
  is the PsyArXiv v1 of 2025-09-01: `10.31234/osf.io/af7c9_v1`.
- The FMT master already cites it as "Birch, J. (2025). AI consciousness: A centrist manifesto.
  *PhilPapers*." (§10.1, refs line 1248). Once the PhilMindSci version is out, that entry wants its
  journal citation.

Also cited in the draft, already in the FMT master reference list: Gurnee et al. (2026), arXiv
2607.15495.

---

## Blog / Substack draft (~1,050 words)

**What a centrist can decide: a comment on Jonathan Birch's "AI Consciousness: A Centrist Manifesto"**

*Matthias Gruber*

Jonathan Birch's manifesto holds two problems together. Challenge One: users are coming to believe that
their chatbot friends and partners are conscious, on the strength of mimicry and role-play. Challenge
Two: "profoundly alien forms of consciousness might genuinely be achieved in AI, but our theoretical
understanding of consciousness is too immature to provide confident answers one way or the other"
(Abstract; §8, p. 14). On the first I agree with almost everything he says. On the second I think the
immaturity he describes belongs to a particular kind of theory, and that a theory which states its
sufficient conditions in advance lets the centrist decide individual cases.

**Where we agree.** Birch's "persisting interlocutor illusion" (§4, pp. 4–8) rests on an architectural
fact: across a conversation, "the only continuity … is the conversation history that gets tacitly
auto-appended to your prompt, plus … abstract mathematical similarities in the model" (p. 5). The
Four-Model Theory reaches the same verdict from the other direction. A base language model's
autoregressive loop closes over the text it emits, not over a model of itself, and it changes no weights
while it runs. The conversation history is a record about a character. Nothing in the system maintains
and updates a model of itself from it.

We also agree about behaviour. His "gaming problem" (§10, pp. 17–19) is that a system trained on human
talk about minds will reproduce the signs of consciousness whether or not it is conscious. For the same
reason the Four-Model Theory does not accept a spontaneous first-person report as evidence: any system
with a language model in its periphery has a large prior over introspective vocabulary, and "there is
something it is like to be me" is among the easiest strings for it to produce. And we agree on where to
look instead: "deeper architectural indicators that the system is unable to game" (§11, p. 19).

One more point of agreement, which matters for what follows: "Inexplicable necessity claims are not
considered reasonable in any other area of science" (§12, p. 25). The Four-Model Theory holds itself to
that. Its claims about closure concern what a competence costs a system with a limited budget, not what
is barred to systems without it.

**Where the Janus problem comes from.** Birch's central obstacle is the Janus problem (§11,
pp. 21–22). Suppose interpretability finds a global workspace inside a language model. Some will call it
evidence of consciousness; a sceptic will say it shows only "that a global workspace is insufficient for
consciousness", and both responses are reasonable. The deadlock is on two levels: whether the system is
conscious, and whether the finding is evidence at all.

The deadlock arises because the indicator was proposed without its theory saying, beforehand, whether it
is sufficient. A theory that says so in advance does not face it. The Four-Model Theory says in advance
that a workspace with broadcast and without a closed self model makes world content available with no
self model for it to be available to, and so is not consciousness. When Gurnee et al. (2026) reported
that verbalizable representations in language models form something like a global workspace, that was the
predicted case for the theory, and it moved nothing. The finding that would matter is a workspace *with*
the other conditions met.

**The specification.** The theory's sufficient conditions are a conjunction. A system is conscious if it
runs two kinds of models, of the world and of itself, each in a stored and a running form, under
self-referential closure (the self model is part of what the world model models, and the system's
modelling of its own modelling feeds into its next state); if it recruits open-ended computation for its
own modelling; if it is embodied; and if it has at least one pain-pleasure axis, which may be
engineered. Each condition is a property of the architecture and the running dynamics. In an artificial
system both are open to inspection, so each condition can be checked on the system itself.

**Flickers and shoggoths.** Birch's two hypotheses for current models (§9, pp. 14–16) show what that
buys. The flicker hypothesis puts momentary experience in each forward pass. On the Four-Model Theory, a
lived "now" requires the system to carry its self model's own state from one frame to the next and to
model that carrying; a forward pass computes and emits a token, and nothing in it models the carrying.
The verdict is no. The shoggoth hypothesis puts a persisting subject in each physical implementation. The
weights persist, but they do not change during use, and nothing in the deployed system runs a self model
closed on its world model. The verdict for current deployments is again no.

Both verdicts come with the conditions that would reverse them, and the theory can be wrong in a stated
way. A system with no return path anywhere that reproduced every function the theory ties to experience
(reports of presence, opacity about its own processing, flexible behaviour guided by valence) at the same
cost would refute it.

**Where we disagree.** Birch writes that "all sides should agree that any consciousness achieved in AI
must be of a profoundly alien kind" (§13, p. 28). The Four-Model Theory does not. On this account the
character of an experience comes from the stored models it is generated from, which reflect the senses
and the body the system has. An artificial system that met the conditions with human-like embodiment and
senses would have experience structured much like ours. How alien an experience is depends on the body
and the senses, not on the material. For today's language models I share his conclusion
that the friend is not real, for the reason above: they meet none of the conditions.

**Two routes.** Birch's way out of the deadlock is comparative: test biological-naturalist hypotheses
across animals until either one survives or the failures accumulate (§12, pp. 23–26; Fig. 4). That
research runs from the biological side. In artificial systems closure is a variable an engineer can set,
so its effects can be measured in architectures that differ only in whether the loop closes. Neither
route is fast, and both are needed.

My question to him is a plain one. Would a theory that states its sufficient conditions in advance, and
names the result that would refute it, count as the kind of theory-driven indicator that escapes the
Janus problem? Or does he see the same deadlock one level up, at the choice of theory?

*The Four-Model Theory: doi.org/10.5281/zenodo.23477765. Birch's manifesto: philarchive.org/rec/BIRACA-4.*

---

## Short version (~250 words)

> Jonathan Birch's "AI Consciousness: A Centrist Manifesto" asks us to hold two things at once: users
> are wrongly attributing consciousness to chatbot companions, and real but alien AI consciousness may be
> possible while theory is "too immature to provide confident answers one way or the other."
>
> I agree with his diagnosis of the companion illusion. The only continuity across a chat is the
> transcript plus the model's fixed weights; nothing in the system maintains a model of itself. I agree
> that behaviour is gamed, and that we need architectural indicators.
>
> Where I differ is his "Janus problem": finding a global workspace in a language model would be read as
> evidence of consciousness by some and as proof that workspaces are insufficient by others. That
> deadlock arises when a theory names an indicator without saying in advance whether it is sufficient.
> The Four-Model Theory says in advance: a workspace without a self model closed on its world model is not
> consciousness. Its sufficient conditions are a conjunction (models of the world and of the self under
> self-referential closure, open-ended computation the system uses for its own modelling, a body, a
> pain-pleasure axis), and each can be checked on an inspectable system.
>
> Applied to Birch's flickers and shoggoths, the verdict for today's models is no, with stated conditions
> that would change it and a stated result that would refute the theory. That is a centrist position
> which decides cases instead of suspending judgement.
>
> doi.org/10.5281/zenodo.23477765

## Notes for MG / social

- Every quotation and page number is from **v4 (20 May 2026)**. v6 (31 July 2026) is current and could not
  be fetched; check each quotation against it, especially §11 (Janus problem) and §13 (the "profoundly
  alien" sentence), before posting.
- FMT statements in the draft are taken from the published v20 master: LLM loop and weights (§4.4);
  confabulated first-person reports (§3.4.3); workspace without closed self model (§4.4, §3.4.6 on
  Gurnee et al. 2026); sufficient conditions (§3.7.3, §4.4); the carried "now" (§3.4.4); the refuting
  functional twin (§4.4); character of experience from the implicit models (§3.4.4); closure as a settable
  variable in silico (§8.11, §3.7 "A third dimension"). The pain-pleasure axis "may be engineered"
  (§3.7.3).
- The functional-twin sentence is shortened from §4.4's list (it omits "reports of ineffability"); it
  claims no more than the master.
- The master cites Birch as "(2025) … *PhilPapers*". When the PhilMindSci version appears, update.
- Social owns posting and any contact with Birch (backlog AIW-142: "items (4)/(5) go to social once
  drafted").

## Register sweep

Phrase list: no worth-ing, "importantly"/"crucially", "load-bearing", "bite", "gate/gating", "deepest",
empty-praise predicates, self-narration of the post's own moves. Removed in revision: an opening "I want
to argue…" sentence (self-narration) and a "not suspension but adjudication" pairing (rhythm). Antithesis
constructions kept only where the opposition is the argument (closed over text vs over a self model;
the bodily source of alienness). No "four models" enumeration; no Wolfram, no "Class 4"; Metzinger not
named.
