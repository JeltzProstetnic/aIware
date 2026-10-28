# Local AI-text detector selection (AIW-339) — Fable 5.1 research, S356 2026-10-23

Requested by MG after JCS #8090 was flagged by Imprint's detector (*"we need such an ai detection software so we can edit accordingly"*). The research was read-only; Fable verified its sources. The orchestrator verified the Imprint policy quote against the PDF (copy: `imprint-ai-policy-2025-07-30.pdf`).

## Verdict
A local **Binoculars + Fast-DetectGPT** pair (Llama-3-8B base + Instruct, int8 or sequential bf16 on the 4090, windowed, calibrated) is usable as a **register diagnostic**. It is **not a proxy** for what journals run: independent head-to-heads show open zero-shot detectors agree poorly with Pangram/GPTZero/Turnitin on 2025–26 frontier-model prose (GPTZero 2026 vendor study: Binoculars AUC 40, Fast-DetectGPT 52.6 on frontier abstracts; UMD/Russell 2025: Pangram 98 % TPR / 2 % FPR, Fast-DetectGPT 80/7.2, Binoculars 66.7/1.3). "Clean locally" never means "will pass".

## What journals run
- **Imprint Academic AI policy (PDF dated 2025-07-30, verified verbatim):** AI "should only be used to improve readability and language of the work and not to create content, produce scientific (or other) insights, draw scientific or philosophical conclusions…"; "Authors should not over-rely on AI technology in the writing process or use generative AI to create content based on an author's initial ideas or hypotheses." Editors "may use specialist AI detector software … in the initial preview stages … to determine which papers should be permitted to move forward." **No vendor named.**
- Default publisher screen: Turnitin/iThenticate (AI-writing indicator add-on). Rising: **Pangram** (AACR, ICLR 2026, literary prizes; self-reported FPR 1/10,000; independent 2 %). GPTZero (arXiv 2602.13042). Imprint's vendor UNVERIFIED.

## Candidates (repo/paper facts per Fable)
| Detector | Fit | Notes |
|---|---|---|
| **Binoculars** (arXiv 2401.12070) | primary | best non-native FPR (0 → 0.1 % after editing, Style-as-Confound 2026); weak on frontier prose; code truncates at 512 tokens; BSD-3; frozen since 2024-05 |
| **Fast-DetectGPT** (arXiv 2310.05130) | primary (same pair) | README 2026-01: Llama-3-8B pair best for LRM text; high naive FPR (25–32 % on non-native manuscripts) → must calibrate; MIT; active |
| **ImBD** (arXiv 2412.10432) | secondary | built for machine-*revised* text (polish/rewrite); gpt-neo-2.7B + LoRA, ~11 GB; Apache-2.0 |
| AdaDetectGPT repo | integration base | unified scripts for Binoculars, Fast-DetectGPT, ImBD, RADAR, GLTR |
| RADAR, RoBERTa classifiers, Ghostbuster, DetectGPT | reject | high FPR / non-commercial / dead backend / superseded |

## Build plan
- Models: `meta-llama/Meta-Llama-3-8B` + `-Instruct` (gated; HF token available), int8 via bitsandbytes (~17 GB) or bf16 sequentially. Fallback pair: Falcon-7B/-instruct.
- Outputs per 400-word window (step 100) and per document: Binoculars score, Fast-DetectGPT criterion (ImBD later), each as a **percentile against human-control windows**. Exclude quotes and references; strip citations/LaTeX; ≥200 tokens per window.
- Calibration: human controls = JCS open-access articles 2016–2022 (pre-ChatGPT, ~24 titles, imprint.co.uk OA page); machine positives = our raw LLM renders before human edits. Window AUROC human vs raw render; **if AUROC < ~0.85 the tool is no diagnostic for our material, and we say so.** Threshold = 99th percentile of human windows.
- Throughput (estimate, unmeasured): a 9k-word paper ~2–3 min cold.

## Risks
Non-native bias differs by detector; polished hybrid text is where every detector is least reliable (APT-Eval: Pangram flags 42.6 % of minimally polished human text); rewriting until green is Goodharting (Binoculars −36 points under synonym swap); **policy risk dominates the score**: the Imprint text forbids generating content from an author's ideas, so the disclosure wording and the actual workflow decide the outcome more than any detector.

## Run 1 result (S356, Falcon-7B pair, 8-bit) — the tool FAILS as a diagnostic for our material
- Human controls: 20 JCS open-access papers 2015–2022 (1,701 windows). Machine positives: Fable's raw replacement drafts, the original eNeuro opinion draft, the July NoC draft.
- **AUROC 0.247 (Binoculars) and 0.235 (Fast-DetectGPT)** — inverted: Claude-written prose reads LESS machine-like than the human JCS papers. Far from the 0.85 bar.
- Silent Suffering: machine-percentile 10.0 / 6.8, 0/41 windows past the human 99th percentile. Cortex Viewpoint: 12.2 / 10.5, 0/19. **Not interpretable**, given the inverted AUROC.
- Likely causes: (1) 2023-era open models do not recognise frontier-model prose (consistent with GPTZero 2026: Binoculars AUC 40 on frontier abstracts); (2) published pre-2023 papers are probably in Falcon's training data, and memorised text scores "AI", biasing the human baseline toward machine.
- Report: `ai-detector-run1-falcon-s356.md`. Raw scores: `tmp/detector/out/` (not tracked).
- Next options: a Llama-3-8B pair (newer; still memorisation-confounded) with human controls the model cannot have seen; or a commercial detector on texts that are already public (Silent Suffering is on Zenodo, 10.5281/zenodo.23479963), which is MG's call.

## Commercial check (S356, MG D15): GPTZero free web scan of the PUBLIC Zenodo text
Silent Suffering v2 (Zenodo 10.5281/zenodo.23483537, already public), cleaned text 4,862 words, scanned in 10k-char chunks on gptzero.me (basic scan, not logged in), 2026-10-23 ~17:00 CEST:
- chunk 1 (title, abstract, §1–§3 start): "We are highly confident this text was AI generated" — **AI 100 %, Mixed 0 %, Human 0 %**
- chunk 2 (§3 end – §7 start): **AI 100 %**
- chunk 3 (§7 – §10 start): **AI 100 %**
- chunk 4 (tables, ~3k chars) not scanned.
⇒ Consistent with the JCS flag; the local Falcon pair (10th machine-percentile) was blind to it. A commercial frontier-trained detector classifies the text as fully AI-generated at maximum confidence; rewording passages to move such a score is not a realistic edit target for this paper.

## Run 2 (S356, Gemma-4 E4B base + it, 8-bit, transformers 5, `.venv-detector`) — also unusable
- Human control: MG's own pre-2022 English (3 books + 2016 dissertation, 723 windows at step 200); machine positives as in run 1.
- AUROC 0.746 (Binoculars) / 0.778 (Fast-DetectGPT): right direction, below the 0.85 bar.
- **Decisive check failed:** a human JCS paper (2022) scores machine-percentile 61.8 / 62.5, ABOVE Silent Suffering (53.7 / 59.1), which GPTZero calls 100 % AI. The AUROC came from genre (narrative/martial-arts books vs academic prose), not AI-ness.
- Conclusion: local zero-shot detectors with open 2023–2026 small models do not reproduce a commercial frontier-trained classifier on this material. A rewrite loop needs the commercial detector (GPTZero or Pangram API) as its measuring stick.
- Per MG: the unusable model weights were deleted (Falcon pair after run 1, Gemma E4B pair after run 2). `scripts/ai_detector.py` stays (model-agnostic; `gemma4e4b` and `llama3` pairs defined).
