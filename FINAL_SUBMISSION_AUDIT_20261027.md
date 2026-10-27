# EE4435 full pre-submission audit — 27 October 2026

This is a **source and PDF quality-control record**, not an additional submitted assignment section.
The audit basis is Chapter 4 (pp. 34–36) of the supplied `EE4435_Sentaurus_Simulation_manual`, the GitHub `main` report source as of commit `c3fb20f40ff2168efb985bcdae6db973ee1eea73`, and the corresponding successful GitHub Actions pdfLaTeX build `40440990196`. Source-level formatting corrections were made on branch `audit/final-submission-20261027`, and require a new successful build before final release.

## Coverage against the actual Chapter 4 assignment

| Official requirement | Audit | Location / limitation |
| --- | --- | --- |
| Cover: full names, student IDs, contribution percentage; final single PDF; AI use declared | **PASS** | Page 1 cover, page 37 disclosure; final submission itself remains the students' action |
| Parameter delta = (A + B)/2 and same non-swept parameters | **PASS in reported setup** | Both rightmost IDs are 2, so delta = 2; source claims nominal settings held fixed; only original process decks can independently prove every hidden parameter |
| Part 1: all major fabrication snapshots and physical/process explanations | **PASS; visual improvement desirable** | Figures 1–8. Authentic early one-dimensional SVisual screenshots are accompanied by genuinely source-derived dimensioned reconstructions. The early gate-oxide screenshots are thin single-line traces and remain intrinsically hard to read, even at full-page scale |
| Part 1: two Id-Vg drain biases, seven-curve Id-Vd, VTH, SS, ION, IOFF, DIBL | **PASS** | Figures 9–13, baseline table; 0.1/1.2-V DIBL = 16.45 mV/V |
| Part 2: six gate lengths for each 10/30 nm Tsi; five metrics vs LG, extreme Id-Vd overlays; 2D potential maps; SCE/depletion discussion | **PASS with one unavailable extraction and image issue** | 12 cases, Figures 14–21. The 30-nm/52-nm high-VDS current never crosses 1e-7, so strict-current DIBL N/A, not zero. In Figure 21, original SVisual potential legends overlap the plotted silicon on both panels; re-export clearer originals with a colorbar outside the device if possible |
| Part 3: five anneal temperatures, VTH/SS/ION/IOFF/DIBL vs temperature, As extreme profiles and Id-Vd curves, drive/leakage discussion | **PASS for runs/comparisons; conditional for threshold DIBL** | Figures 22–31 and Tables 6–8. All original strict 1e-7 high-VDS thresholds remain N/A; matched-current shifts and alternative ELR/ESR extrapolations are separate quantities. The As comparison is a genuine **source-side vertical** profile, not a lateral junction-penetration study |
| Part 4: four dopings, five electrical metrics on log concentration axis, extreme log Id-Vg and channel-centre vertical electron density, quantitative trade-off | **PASS for runs/comparisons; conditional for DIBL** | Figures 32–39; Tables 9–10. Original strict current DIBL available for only the 3e18 cm^-3 case. Supplementary high-current and ELR/ESR apparent shifts cannot be labelled interchangeable physical DIBL |
| Part 5: two longitudinal and vertical Ec/Ev band comparisons at VGS=0 and VDS=1.2, barrier, bending and depletion discussion | **PASS for specified operating point, with correct scope limits** | Figures 40–43. Single-drain-bias profiles cannot quantify drain-induced barrier lowering from a VDS comparison, and the report explicitly notes this |
| Readable figures, axes and legends | **PASS for overall PDF; conditional on original screenshots** | All 43 figures and 10 tables present, no clipped PDF text found. Figure 21 legends encroach on contours; Figure 4 original one-dimensional screenshots are visually sparse. The figure source artwork, rather than the LaTeX typesetting, limits their readability |

## Independent numerical and technical checks in this audit

- Independently recomputed all available Part 2 matched-threshold DIBL entries from both geometry CSVs, no discrepancies beyond rounding.
- Independently checked Part 3 and Part 4 ON/OFF current ratios from their archived metrics, no discrepancies beyond rounding.
- Independently reconstructed the **original 1e-7 constant-current crossings** for all four Part 4 dopings from the archived 35-point Id-Vg curves: both thresholds N/A at 3e15 and 3e16; only low-VDS available at 3e17 (about -0.1858183 V); both available at 3e18 (about 0.4838252 and 0.3808958 V). These agree with the report.
- Checked all five user's Part 3 ELR/ESR terminal-summary voltage differences against the rounded DIBL entries, within rounding tolerance. Their ON/OFF currents independently match the earlier Part 3 metric table within reported precision. **This is not a reconstruction of the absent raw Part 3 ten PLT curves.**
- Verified all 16 LaTeX source files and 15 section imports; all 108 referenced CSV file paths and existing original image paths resolve after accounting for LaTeX escaped underscores and the `\evidence` macro. Structural `figure`, `table`, `tikzpicture` and relevant axis environments are balanced. The completed 37-page PDF contains Figures 1–43 and Tables 1–10 consecutively.
- Checked every page using PDF contact sheets, including close views of original process screenshots, Part 2 electrostatic fields, Part 3 alternative DIBL, Part 4 comparisons and Part 5 bands. No obvious clipped page-edge text, missing figures, blank pages or unrendered formula placeholders; some whitespace is a legitimate consequence of fixed placement.
- Cross-checked the paper cited in the ELR/ESR section: Ortiz-Conde et al., *Microelectronics Reliability* 42 (2002) 583–596, DOI 10.1016/S0026-2714(02)00027-6. Its topic legitimately covers CC, ELR and ESR threshold methods. The report correctly warns that model-dependent values can differ.

## Report edits made in this audit

- Changed blue clickable TOC/DOI/internal-reference text to **black text with invisible hyperlink borders**, consistent with the requested professional black-and-white wording.
- Set only the major-process-snapshot figure captions to ragged-right to avoid exaggerated word spacing in Figures 5–8. Numerical data, graphs and original image assets are not modified.
- Added this separate final audit record. The full current branch must still compile successfully and be merged into `main`.

## Remaining actions and non-guarantees

1. **Recommended high-impact visual improvement:** Re-export the *original* Part 2 SVisual 2D potential maps with the same shared legend scale and a readable colorbar positioned outside the mapped silicon, and supply high-resolution early SVisual gate-oxide snapshots if time permits. Do not redraw physically unverified contours.
2. **Scientific limitation:** No editorial change can convert strict-current N/A values into measured 1e-7 crossings. Part 3/4 ELR/ESR shifts and high-current switching shifts are relevant *apparent* sensitivities but are not interchangeable with a uniquely measured physical DIBL. Especially the 1000 C ESR threshold -0.9417 V is an extrapolation beyond the original -0.5-V gate sweep.
3. **Reproducibility:** The NUS Part 3 raw PLT files and consolidated `part3_alt_dibl/part3_idvg_all.csv` are not currently archived in GitHub. For a complete third-party numeric rerun, retain/export those source files or at least the consolidated raw CSV.
4. **Delivery:** Verify the final merged GitHub `main` build and then inspect the PDF at full size in Overleaf/PDF reader; check that submission details match course group registration and upload **one PDF** to the designated course portal.

**Assessment:** All required study parts are substantially documented and the audited numerical claims agree with the data available here. The result is not a guaranteed 100/100; missing physical constant-current crossings and the legibility of a few original figures are the principal residual marking risks.
