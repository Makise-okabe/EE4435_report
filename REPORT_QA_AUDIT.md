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
| Part 1: process flow and key physical steps | Original process script; extension, spacer, anneal and final structure PNGs; explanations | **Complete**: authentic SVisual 1D screenshots and traceable region-interface depth reconstructions cover both initial SOI and gate-oxide stages |
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

1. **Early fabrication-stage evidence integrated.** The report now includes three genuine cropped SVisual screenshots (initial stack, gate-oxide full extent and zoom) and two independent dimensionally scaled material-depth diagrams reconstructed from the authentic 1D SProcess TDR exports. The numerical interface positions are preserved in `data/part1_early_1d_region_boundaries.csv`; do not confuse 1D material indicators with spatial Y-coordinates or current curves.
2. **Compile the full current GitHub version in Overleaf**, inspect the compiler log, open every PDF page at readable scale, and resolve any errors, clipped legend labels, unexpected blanks, or missing images. The earlier screenshots of Overleaf are from an older commit and do not certify the present report. **Visual inspection of the existing Sentaurus PNGs identified a specific readability issue:** the NetActive/electrostatic-potential color legends overlap the plotted device region in several exported images, especially the side-by-side Part 2 potential map. Re-exporting these original plots with externally positioned legible color legends would improve presentation without changing the numerical data.
3. **Maintain the metric distinction**: the complete high-current switching-voltage graphs are supplementary; missing reference-current VTH/DIBL results have not become measurable. If the marker expects a numeric DIBL trend at all anneal/doping values, that requires a separately defensible extraction protocol or additional gate-voltage data, not mere relabelling of high-current bias shifts.
4. **Check final submission metadata** against the Canvas group registration and ensure that the submitted artifact is a single final PDF, as the course requires.

The numerical audit does **not** imply a guaranteed assessment mark. Successful compilation and final layout review remain important for a fully defensible submission.

## Final follow-up audit after authentic screenshots

- Official rubric: Compared Chapter 4 against Parts 1-5, group delta=2, original process screenshots, five electrical metrics, output families, potential/band cutlines, 50/50 contributions and AI-use disclosure.
- Source integrity: 14 LaTeX files; 38 balanced figure environments; 7 balanced table environments. All literal LaTeX input, image and CSV paths resolve to files in GitHub. No stale missing-screenshot or Pending notes remain in LaTeX.
- Genuine image evidence: Initial SOI, gate-oxide full stack and zoom original SVisual cropped PNGs are embedded separately from the dimensionally accurate 1D depth-region reconstructions.
- Part 2 plotting: Both scaled output CSVs now label their columns as scaled_x1000, rather than mA_assuming_A. Every one of the 28 affected PGFPlots column references is verified against its updated CSV header. Numeric data remain unchanged.
- Numerical data: Inspected Part 2/3/4 metric and output archives, the complete 35-point Part 4 transfer sweeps and 37-point depth profile, and Part 5 lateral/vertical band samples.
- Text corrections: Removed an obsolete statement that Part 1 screenshots are still missing, harmonized AreaFactor and exported-current language, and explicitly identified DIBL as the first electrostatic relative departure at the tested gate lengths.
- PDF visual smoke test: Newly inserted two-panel SVisual figure compiled successfully with pdfLaTeX, zero errors. The initial image labels wrapped awkwardly; explicit paragraph breaks fixed the layout and the updated test was rerendered.
- Limit: This is NOT a successful full current-report PDF compilation. The full Overleaf PDF is not available here, so a complete page-by-page final document review is still needed.
- Scientific limit: Part 3 strict-current DIBL is unavailable and Part 4 strict-current DIBL exists for only one doping with the chosen 1e-7 current criterion. High-current switching-voltage markers cannot be relabelled as threshold/DIBL.

## Uploaded 33-page PDF review and subsequent source fixes

- Source PDF reviewed: `EE4435_report.pdf` (33 A4 pages, compiled 25 October 2026). Checked original 1D layer-depth figures, raw SVisual screenshots, transfer/output plots, channel profiles and band diagrams against official Chapter 4 requirements.
- Page 4 initial-SOI plot: 30.000 nm top silicon and 150.000 nm BOX; original SVisual colors blue/top silicon, green/BOX, red/substrate. Figure 1 is a genuine numeric reconstruction while Figure 2 is a real 1D screenshot.
- Pages 5-6 gate oxidation: gate oxide 1.53231 nm, remaining silicon 29.98571 nm, BOX 150.000 nm. In the uploaded PDF Figure 4 displayed a wrong manually authored color legend (green labelled top silicon, red labelled oxide), while the caption correctly identified green Oxide_2 and red Silicon_2. GitHub source `sections/part1_gateoxide_svisual_screenshots.tex` was verified already corrected to red/top silicon and green/gate oxide; re-pull before exporting final PDF.
- PDF right-margin audit identified overflow on pages 3, 10, 12, 15 and 18 caused by unbreakable path/filename strings. Their wording has been shortened in GitHub source. The Part 2 archived TDR names now refer to verified n53 and n57 archived node files.
- Part 3 Figure 23 appeared visually before Figure 22 in the uploaded PDF because the first plot was floating and the second forced `[H]`. The first figure has been changed to `[H]` in GitHub to preserve numerical figure order on recompilation.
- Part 4 discussion originally claimed the entire 3e15-3e17 interval met the >=50% leakage reduction criterion, although only the 3e17 tested point meets it. This source interpretation has been corrected to a tested-discrete-point conclusion.
- Core numerical evidence: Part 1 two-drain-bias transfer and seven-curve output; Part 2 12 gate-length/film combinations with five metrics and four extreme output families; Part 3 five anneal runs with 14 extreme output curves and source-side arsenic comparison; Part 4 four dopings with semilog transfer, electron-density comparison and quantitative trade-off; Part 5 four band profiles. The report carefully distinguishes unavailable 1e-7-based threshold/DIBL values from high-current switching voltage proxies.
- Remaining marks risk: official rubric explicitly demands VTH, SS, ION, IOFF and DIBL plots in Parts 3 and 4; missing numerical DIBL results are scientifically explained but still may receive fewer marks. The original 2D SVisual screenshots on pages 7-8 also have scale bars over the silicon regions and would benefit from clearer re-exports.
- The uploaded PDF is **not** the fully corrected PDF. Pull the new GitHub commits, recompile in Overleaf, and inspect pages corresponding to the updated Part 1 legend, formerly clipped paragraphs, Part 3 figure order, and Part 4 trade-off text.
