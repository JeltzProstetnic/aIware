# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-05-26T15:15Z — the office
**Goal:** Prepare Wittmann reply (3 May 21 emails), store in docs, shutdown
**Completed:**
- Git sync check (origin + private up to date)
- Cross-project inbox read (1 aIware item: Wittmann emails)
- Pending files processed (CMB→reference, 4 already reference)
- Backlog read
- Wittmann reply drafted — consolidated reply to 3 messages (BIS-Daten, Tallinn/recursive self-improvement, Berkeley/CIMC)
- Reply stored at docs/wittmann-reply-2026-05-26.md
- Gmail draft created (from matthias@matthiasgruber.com, Draft ID: r5586823964453339452)
**Key Decisions:**
- Wittmann reply does NOT reveal Bach DM channel (Apr 26) — acknowledges Bach's work and CIMC convergence only
- BIS data strategy adjusted: ask if Tracon data (with motivation vars) available via Ackerman, offer fallback with BIS reasoning factors alone
**Pending at shutdown:** User to review and send Wittmann reply from Gmail drafts
**Recovery/Next session:**
Reply is in Gmail drafts AND docs/wittmann-reply-2026-05-26.md. After sending, update correspondence/wittmann-werner.md with Messages 17-19 (Wittmann May 21) + reply. Delete docs/wittmann-reply-2026-05-26.md after send.

### 2026-05-20T05:00Z — WSL
**Goal:** Relaunch CMB MFDFA after WSL crash fix, analyze results, write paper, publish
**Completed:**
- Verify 48GB RAM available (47Gi confirmed)
- Launch MFDFA via tmux-launch.sh — 500 sims completed in 114 min
- Confirm data phase completes (7 bands, values match previous)
- Confirm parallel workers survive without OOM (peak 34Gi/47Gi)
- Analyze results: null at large scales (Bands 0-5), 9.6σ Band 6 (instrumental noise)
- Write full paper: abstract, §4.4 results, §5 discussion reframed, §6 conclusions
- Fix LaTeX formulas for weasyprint PDF rendering
- Run parallel review subagents (citations: clean, content: Z-score precision fixed)
- Push to both GitHub remotes (public + private)
- Publish CMB-MFDFA on Zenodo: DOI 10.5281/zenodo.20306785 (8 files)
- Update cosmology paper .md + .tex with MFDFA reference (Gruber 2026c)
- Create infrastructure inbox item for webpage update
- Update MEMORY.md (seven papers, intelligence unparked, all DOIs current)
**Key Decisions:**
- CMB null result at large scales is consistent with SB-HC4A — the CMB is a recombination-era observable, not a direct picture of the singularity surface. Criticality signatures would be erased by inflationary processing.
- Band 6 (ℓ=1500-2500) 9.6σ detection attributed to instrumental noise / unresolved point sources, not primordial physics. Needs FFP10 sims to confirm.
- Paper framed as methods contribution + honest negative result. Publishable venue: Entropy (MDPI) or Phys. Rev. D.
**Recovery/Next session:**
- All work committed and pushed. No dangling state.
- Zenodo deposit is live: https://zenodo.org/record/20306785
- Cosmology paper references CMB-MFDFA with live DOI

### 2026-05-20T02:00Z — WSL
**Goal:** Diagnose and fix WSL2 crash caused by MFDFA parallel compute; harden WSL config.
**Completed:**
- Diagnosed crash: 8 workers × 3.5GB = 32GB peak on 32GB WSL = zero headroom OOM
- Fixed MFDFA script: added memory cleanup (del/gc.collect), checkpointing every 50 sims
- Created .wslconfig: 48GB RAM, 24 processors, 16GB swap (was: only networkingMode=mirrored)
- Restored 8 workers (safe on 48GB WSL, ~32GB peak with 16GB headroom)
- Committed script fix + Phase 1-3 surviving figures
**Key Decisions:**
- WSL memory set to 48GB (of 64GB host) — leaves 16GB for Windows/browser/Claude Code
- GPU (RTX 4090) not usable for this workload — healpy SHT is CPU-only
- Native Windows Python rejected — healpy doesn't build on Windows
**Pending at shutdown:** User needs to `wsl --shutdown` from PowerShell to apply .wslconfig, then relaunch MFDFA

