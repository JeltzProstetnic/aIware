# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-20 (Session 89)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Fix hardcover cover dimensions per KDP rejection feedback

## What Session 89 Did
1. **KDP hardcover cover rejection**: Expected 14.329"×10.417", we submitted 14.141"×10.382"
2. **Root cause**: Missing board overhang in case laminate formula (boards extend 0.094" per side, 0.1175" top/bottom beyond page block)
3. **Fixed `build_book_cover.py`**:
   - Replaced ad-hoc constants with proper physical parameters (wrap, joint, overhang)
   - Corrected total dimension formula
   - Split margin into margin_x / margin_y for asymmetric hardcover geometry
   - Fixed image crop (was using wrong height, causing aspect ratio distortion)
4. **Rebuilt cover**: `pop-sci/cover-wrap-hc.pdf` now exactly 14.329"×10.417"

## KDP Case Laminate Geometry (for reference)
- Layout L→R: [wrap 0.591][board(trim+0.094)][joint 0.197][spine][joint 0.197][board(trim+0.094)][wrap 0.591]
- Height: [wrap 0.591][trim+2×0.1175][wrap 0.591]
- Width = 2×0.591 + 2×(6+0.094) + 2×0.197 + spine = 14.329" (251pp)
- Height = 2×0.591 + 9 + 2×0.1175 = 10.417"

## KDP-Ready Files
| File | Purpose | Status |
|------|---------|--------|
| `pop-sci/book-manuscript.pdf` | US paperback interior | READY |
| `pop-sci/book-manuscript-hc.pdf` | US hardcover interior | READY |
| `pop-sci/book-manuscript.epub` | Kindle eBook | READY |
| `pop-sci/cover-wrap.pdf` | US paperback full cover | READY |
| `pop-sci/cover-wrap-hc.pdf` | US hardcover case laminate | FIXED — resubmit |
| `pop-sci/cover-kindle.jpg` | Kindle eBook cover | READY |

## Recovery
1. Read this file + MEMORY.md
2. Book: `pop-sci/book-manuscript.md` — content source of truth
3. Build: `tmp/build_book_{pdf,epub,cover}.py`
4. Next: Resubmit hardcover cover to KDP
