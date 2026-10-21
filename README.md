# EE4435 Sentaurus TCAD Report

This repository contains an Overleaf-compatible LaTeX working report for EE4435. The root document is `main.tex`; compile with **pdfLaTeX**.

## Report status (21 October 2026)

- Part 1: baseline SProcess completed; relevant SOI nMOSFET TDR snapshots were inspected.
- Part 1: SDevice returned a gate-voltage versus drain-current curve at nominal `VDS=0.1 V` in both linear and logarithmic displays. Exact numerical extraction is pending.
- Parts 2--5: parameter sweeps and energy-band comparisons remain pending.
- Baseline simulation raw `.tdr`, `.plx` and `.plt` files remain on the university CADCAM system and have not been committed.

## Figures

The report references six screenshot files in `figures/`. See `figures/README.md` for exact filenames and provenance. **The screenshot images have not yet been pushed to this repository**; until they are, LaTeX displays a missing-image placeholder and still compiles.

The figure macro was corrected on 21 October to protect underscores in missing-image filenames. That fixes the reported cascading `Missing $ inserted` / `Extra }, or forgotten $` errors on lines containing `\\evidence`.

The image files must be copied to the `figures/` directory with their specified filenames and committed. They will then appear automatically in the PDF on the next Overleaf recompilation.

## Submission integrity

Measurements and claims must be supported by Sentaurus outputs. Do not invent electrical metrics or interpret visual estimates as formally extracted results. Insert the second group member's identification, contribution percentages, and the actual AI-assistance disclosure before final submission.

## 21 October data update

The original gate-sweep CSV and a cleaned 34-point drain-current sweep are now in the `data/` directory. `main.tex` uses PGFPlots to render two editable vector Id-Vg graphs directly from this dataset. A linear fit over VGS = -0.35 to 0 V gives SS = 63.61 mV/dec (8 points, R^2 = 0.999999892). Current units require verification. The fabrication snapshot PNGs remain to be uploaded separately.
