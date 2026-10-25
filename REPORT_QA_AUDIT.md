# EE4435 report: final technical and rubric audit

This file is a quality-control record **outside** the submitted LaTeX report. Its purpose is to distinguish verified evidence from genuine remaining submission risks. It is not an additional assignment section.

## Verified numerical and source checks

- **Part 2:** independently re-extracted threshold crossings, apparent SS, ON/OFF currents and DIBL for 12 geometry pairs (24 transfer curves). All **72** metric comparisons match the archived metrics within numeric tolerance, including intentionally undefined reference-current thresholds.
- **Part 3:** independently re-extracted the same 6 metrics/availability checks for 5 anneal temperatures. All **30** comparisons match. The separate arsenic source-side profiles reproduce the reported 800/1000 C numerical values.
- **Part 4:** independently re-extracted the 6 metrics/availability checks for 4 dopings. All **24** comparisons match. The (2\times10^{-4}) common-current switching marker crosses each of the eight measured sweeps within the simulated range. Relative ION/IOFF trade-off results agree with the archived data.
- **Part 5:** independently inspected source TDR-derived exports. The channel-centre silicon intervals measure approximately **29.99 nm** and **9.99 nm**. Vertical EC bending is **65.1 meV** and **10.1 meV**, and the reported small minority-carrier/acceptor ratios agree with the original exports.
- **Figures and code:** all identified plotted CSV columns were checked against their actual GitHub CSV headers across the report. Figure, table, PGFPlots axis and TikZ begin/end structures were balanced in the inspected LaTeX sources. The PNG files referenced in the report exist in the repository. These are static checks and do **not** replace a full LaTeX compilation and visual proofread.

## Chapter 4 requirement matrix

| Requirement | Evidence | Audit outcome |
| --- | --- | --- |
| Part 1: process flow and key physical steps | Original process script; extension, spacer, anneal and final structure PNGs; explanations | **Partial visual evidence**: separate initial-SOI and gate-oxide process-stage screenshots are absent |
| Part 1: VDS=0.1/1.2 V Id-Vg, Id-Vd family, VTH, SS, ION, IOFF and DIBL | Verified 2 transfer sweeps, 7 output curves and table | Verified |
| Part 2: 6 lengths by 2 film thicknesses, five trends, extreme Id-Vd overlays | 12 structures, 24 transfer curves, 28 output curves and metric plots | Verified, with the 30-nm 52-nm high-drain threshold/DIBL correctly marked unavailable |
| Part 2: short-device 2D electrostatic potential at VGS=0,VDS=1.2 | Two archived Part 2 bias-point structures and comparison PNG | Verified presence; visual color-scale parity described in text |
| Part 2: performance tradeoff and depletion discussion | Source-derived current ratios, SS/DIBL trends and Part 5 depletion evidence | Verified |
| Part 3: anneal 800 to 1000 C, five metrics, extreme As and Id-Vd | 5 structures, 10 transfers, 14 output traces and As profiles | Verified, **except strict-current DIBL is not numerically available** with selected threshold-current criterion |
| Part 4: four dopings, five metrics, extreme log transfer and vertical electron profiles | 4 structures, 8 transfers, two final-state silicon profiles | Verified, **except 3/4 strict-current DIBL values are not numerically available** with selected threshold-current criterion |
| Part 5: two silicon thicknesses, lateral and vertical EC/EV, barrier and depletion | Four cutline comparisons from archived Part 2 TDR operating points | Verified for the required single VGS=0,VDS=1.2 bias; quantitative drain-induced barrier lowering is not inferable from one drain bias |
| Cover, group membership and declaration | Both names and student IDs, 50/50 contributions, concise abstract, AI-use statement | Verified in LaTeX source |
| Submission presentation | No date, contents on separate page, labelled plots and explanations | Source-level check passed; **full final PDF compilation/proofreading remains to be done in Overleaf** |

## What has been improved in this audit

- Removed a misleading assumption of absolute **mA** in Part 2: output ordinates are correctly described as (10^3) times simulator-exported 2D current units.
- Documented the actual **AreaFactor=1.0** supplied to SDevice and its default 1-micrometre effective width in the 2D Sentaurus convention, without applying any new numerical scaling to the archived data.
- Rechecked all Part 2–4 output-current extraction results from the raw input CSVs rather than trusting the tables alone.
- Added **five-temperature measured switching-voltage and drain-shift trends** for Part 3, using a common 3.5e-4 exported-current crossing. These supplementary curves are explicitly **not** labelled as physical VTH/DIBL.
- Preserved honest N/A values for the original (10^{-7}) threshold and DIBL metrics in Parts 2–4, rather than inventing extrapolated values.

## Remaining high-impact actions before final submission

1. **Capture genuine Sentaurus Visual snapshots** from `soi_00_start_fps.tdr` and `soi_01_gateoxide_fps.tdr` for the initial SOI and gate-oxide stages. Save the original images as **`figures/00_initial_soi.png`** and **`figures/01_gateoxide.png`**. `main.tex` now includes conditional, accurately labelled figure blocks that appear automatically when those images are committed, without displaying any missing-image placeholders beforehand. Do not substitute inferred illustrations for simulation screenshots.
2. **Compile the full current GitHub version in Overleaf**, inspect the compiler log, open every PDF page at readable scale, and resolve any errors, clipped legend labels, unexpected blanks, or missing images. The earlier screenshots of Overleaf are from an older commit and do not certify the present report. **Visual inspection of the existing Sentaurus PNGs identified a specific readability issue:** the NetActive/electrostatic-potential color legends overlap the plotted device region in several exported images, especially the side-by-side Part 2 potential map. Re-exporting these original plots with externally positioned legible color legends would improve presentation without changing the numerical data.
3. **Maintain the metric distinction**: the complete high-current switching-voltage graphs are supplementary; missing reference-current VTH/DIBL results have not become measurable. If the marker expects a numeric DIBL trend at all anneal/doping values, that requires a separately defensible extraction protocol or additional gate-voltage data, not mere relabelling of high-current bias shifts.
4. **Check final submission metadata** against the Canvas group registration and ensure that the submitted artifact is a single final PDF, as the course requires.

The numerical audit does **not** imply a guaranteed assessment mark. Authentic process-stage screenshots and successful compilation remain important for a fully defensible submission.
