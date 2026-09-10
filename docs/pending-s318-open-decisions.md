<!-- Action: await-user-decision -->
<!-- Tracked-by: AIW-256, AIW-257, AIW-258, AIW-260, AIW-10, AIW-246, AIW-249 -->
# S318 — what MG has to answer, and the one thing that is merely blocked

S318 was a Gmail session that turned into a correction session. Everything below is either a
decision only MG can make, or a push waiting on someone else's server.

---

## ⏳ NOT A DECISION — just blocked, retry it first thing

**`AIW-257`'s live Zenodo edit.** The corrected abstract is generated, verified and committed at
`docs/zenodo-pending/fmt-abstract-v15.html`; the push instructions are in
`docs/zenodo-pending/README.md`. **Zenodo went down mid-session — 504 on its own unauthenticated
front page**, twenty minutes after the records API had answered normally. **Retry, do not
re-diagnose, and do not conclude the token is wrong.**

⚠ And fix the builder in the same pass, or the next version re-inherits the correct abstract by
luck: `scripts/zenodo_metadata.py::apply_version_metadata` inherits the description and only
appends a changelog, which is why a v8-era abstract has been carrying v15 changelogs.

---

## THE DECISIONS

### 1. `AIW-256` — Eric Platon, and a promise that came due on 8 September
He offered to contribute as *"sounding board, coder, experimenter"*, is explicitly **not** looking for
a job, and brings *"a couple GPUs, one similar to the 4090, but up to about 110GB memory"* — roughly
4.5× the usable VRAM of the WSL machine, free. MG accepted in principle on 6 Sep: *"I cannot possibly
pass on a good GPU! :D I'll contact you with details right after my vacation!"*

**What MG must decide:** what Platon is actually pointed at. The natural fit is crucible's two stuck
results, and that is exactly the lane `AIW-206` still freezes. **Cheaper first move that needs no
disclosure ruling: give him something to *run* rather than access to something to *see*.**
Contact is LinkedIn only — no email address held (`contacts.md` #48).

### 2. `AIW-246` — the OSF letter, drafted and unsent
The PsyArXiv tombstone reads *"Withdrawn due to duplication"*, not the statement OSF negotiated. A
formal **Article 16 rectification** demand sits in Gmail Drafts, Cc `contact@osf.io`. It leads on
rectification rather than re-arguing Article 17 (already lost), names the misconduct imputation
plainly, and gives them the one-month Art. 12(3) window before escalation.
**Send, edit, or drop.** ⚠ Also unread: the moderators' feedback on the request they **declined** at
11:06 UTC on 28 Aug, eight minutes before approving a second one. It sits behind an OSF login.

### 3. `AIW-249` — Wittmann is owed a reply, and the first draft was bad
He answered all three questions and sent two files. **MG cut most of the draft** — it ran ~3× its
needed length and staged its reasoning at him. `prose-register.md` step 0 now exists to stop that
recurring. **The substance that still has to go back is one question:** Fig. 11's MOTSKIL coefficient
is **positive** (std. coef. .203, *p* = .024, N = 93) — more motivation, *more* performance
variability — where Prediction 8 naively wants the opposite sign. Ask him which reading is his; do
not set out the alternatives for him.

### 4. `AIW-10` — three citable roadmaps, nobody approached
Explained to MG this session; he did not rule. Two questions, unchanged: **does it go out now or wait
for MoC7 (12–16 Oct)** where the poster is already accepted and face-to-face beats cold email; and
**which roadmap leads**, since they want different people — RIM → psychometrics/SDE (Wittmann is
already live), SB-HC4A → mathematical physics (Wetterich is cited heavily), FMT → information
geometry and dynamical systems. **No drafting until MG names targets.**

### 5. `AIW-258` — authorise the wiki long tail, or leave it
The headline fix landed. The remaining ~30 files are **`AIW-27` Part 2**, whose re-runnable workflow
script has sat unrun since a burst rate limit killed it on **2026-07-28**. **Running it needs MG's
explicit say-so** — workflows are opt-in in this fleet. Also unapplied: the `criticality.md` article
is titled *"The Criticality Requirement"* while its body says the opposite, and every cross-link uses
that phrase as anchor text.

### 6. `AIW-260` — Rosario Tomasello, still unread
MG asked for a read this session and it did not happen; the P0s took the time. Nothing is assessed —
the LinkedIn post is unread, the convergence uncharacterised, and he is not in `contacts.md`.

---

## Two things MG asked about that are answered, so they need no decision

- **The Seth/BBS history he could not remember:** the ScholarOne portal never carried the target
  article (`docs/conversation-log.md:124`), and the proposal was **rejected the same day it was
  submitted** because the window had already closed (`AIW-01`/`AIW-49`). The commentary was not
  wasted — it published standalone at `10.5281/zenodo.20626675`.
- **The Anthropic complaint:** sent 2026-08-24 22:38, auto-escalated to a human Privacy Team the same
  evening, **silent since**. The cfg pending file claiming it was never sent is wrong and has been
  filed for correction. Open question is only whether to chase them.
