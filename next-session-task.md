task: true
file: docs/pending-aiw108-it-translation.md
backlog: AIW-108
description: Translate the book to ITALIAN using Opus (MG directive S252 — not waiting for Fable). Everything prepped on WSL: translate script tmp/it-pipeline/aiw108-translate-it.js (Opus, 60 chunks), IT guides, master calque checklist. Steps in the file: translate → assemble (assemble_generic.py → pop-sci/book-manuscript-it.md) → Opus×2 Kalk scan (checklist-primed, the proven ~92%-of-Fable recipe) → auto-apply held B + soften grandeur (conservative) → coherence pass → HOLD for human native Italian gate. RUN ON WSL (pipeline is tmp/-local). JA/ZH stay on hold. Then continue AIW-109 (ES/PT coherence passes + full re-propagation + build scripts + ISBNs for translation publish).
