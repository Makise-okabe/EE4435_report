# EE4435 Sentaurus TCAD Report

This repository contains an Overleaf-compatible LaTeX working report for EE4435. The root document is `main.tex`; compile with **pdfLaTeX**.

## Report status (24 October 2026)

- Part 1: baseline fabrication, matched 0.1/1.2-V transfer sweeps, electrical metrics and seven-curve output characteristic completed.
- Part 2: all 12 geometry structures and 24 transfer sweeps completed; five metric comparisons, required output-characteristic and electrostatic-potential comparisons included in LaTeX.
- Part 3: all five anneal-temperature structures, ten transfer sweeps, 14 output-curve traces at 800/1000 C and source-side vertical arsenic profiles completed. The numerical threshold-based DIBL values are unavailable because the selected 1e-7 current criterion is not crossed within the high-drain-bias gate sweep. Missing values are disclosed, not extrapolated.
- Part 4: all four channel-doping structures and eight transfer sweeps completed for 3e15, 3e16, 3e17 and 3e18 cm^-3 at both drain voltages. Metrics, five logarithmic-doping graphs (unextractable thresholds/DIBL marked N/A), extreme-doping semilog transfer overlay, and channel-center 30-nm vertical electron-density profiles are included in `sections/part4_doping_analysis.tex` using `data/part4_doping_metrics.csv`, `data/part4_idvg_all.csv`, and `data/part4_electron_vertical.csv`. At the four tested values, 3e17 cm^-3 meets the declared >=50% OFF-current reduction and <30% ON-current reduction criterion.
- Part 5: completed using the previously saved Part 2 off-gate/high-drain snapshots of the 52-nm-gate 10-nm and 30-nm SOI devices. Longitudinal conduction/valence bands are compared at 1.5 nm below the gate oxide; vertical conduction/valence bands are compared at channel centre through the full top silicon. The four figures, source-channel barrier estimates, vertical band bending, and depletion qualification appear in `sections/part5_band_analysis.tex` (which inputs `sections/part5_longitudinal.tex` and `sections/part5_vertical.tex`). Display data: `data/part5_longitudinal_tsi10.csv`, `data/part5_longitudinal_tsi30.csv`, `data/part5_vertical_tsi10.csv`, `data/part5_vertical_tsi30.csv`.
- Remaining final-report work: review pending fabrication screenshot placeholders, team member details/contribution percentages, and PDF compilation.
- Verification still needed for two-dimensional terminal-current normalization and final submission metadata/AI disclosure.

Part 3 plotted source CSVs are archived as `data/part3_idvd_T800.csv`, `data/part3_idvd_T1000.csv`, and `data/part3_arsenic_vertical_source_800_1000.csv`. The analysis is in `sections/part3_transfer_analysis.tex` and included by `main.tex`.

## Figures

The report references six screenshot files in `figures/`. See `figures/README.md` for exact filenames and provenance. **The screenshot images have not yet been pushed to this repository**; until they are, LaTeX displays a missing-image placeholder and still compiles.

The figure macro was corrected on 21 October to protect underscores in missing-image filenames. That fixes the reported cascading `Missing $ inserted` / `Extra }, or forgotten $` errors on lines containing `\\evidence`.

The image files must be copied to the `figures/` directory with their specified filenames and committed. They will then appear automatically in the PDF on the next Overleaf recompilation.

## Submission integrity

Measurements and claims must be supported by Sentaurus outputs. Do not invent electrical metrics or interpret visual estimates as formally extracted results. Insert the second group member's identification, contribution percentages, and the actual AI-assistance disclosure before final submission.

## 21 October data update

The original gate-sweep CSV and a cleaned 34-point drain-current sweep are now in the `data/` directory. `main.tex` uses PGFPlots to render two editable vector Id-Vg graphs directly from this dataset. A linear fit over VGS = -0.35 to 0 V gives SS = 63.61 mV/dec (8 points, R^2 = 0.999999892). Current units require verification. The fabrication snapshot PNGs remain to be uploaded separately.
