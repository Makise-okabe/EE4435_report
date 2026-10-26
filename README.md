# EE4435 Sentaurus TCAD Report

This repository contains the LaTeX report for EE4435. Compile `main.tex` using **pdfLaTeX** or import/sync the repository into Overleaf.

## Completed simulations and report sections

- **Part 1:** SProcess fabrication stages, matched dual-drain-bias transfer curves, extracted electrical metrics and seven-curve output characteristics.
- **Part 2:** twelve SOI geometries, transfer sweeps and electrical metrics; output curves for the gate-length extremes at both top-silicon thicknesses; a matched high-drain-bias two-dimensional electrostatic potential comparison.
- **Part 3:** anneal-temperature sweep, metrics, seven output curves at each extreme anneal and arsenic-profile comparison. Strict-current DIBL thresholds outside the sweep remain N/A; the five-temperature high-current switching-voltage and drain-shift markers are plotted **separately** as non-DIBL metrics using `data/part3_common_current_switching.csv`.
- **Part 4:** channel doping sweep, all metrics, low/high doping transfer and electron-density comparisons, and a quantitative current trade-off. The original strict-current threshold/DIBL metrics remain N/A when their crossings are outside the gate sweep. To show a *complete comparison without inventing missing VTH values*, the new charts also show clearly labelled **high-current switching-voltage markers** and the corresponding drain-bias shifts; these are **not** physical VTH or DIBL substitutes. Source: `data/part4_common_current_switching.csv`.
- **Part 5:** conduction and valence bands along source-to-drain and through channel depth for both 10-nm and 30-nm films using the archived Part 2 SDevice TDR snapshots. Source data and plots are stored under `data/` and `sections/`.

**New Part 3 diagnostic (1000 °C anneal, high drain).** One isolated SDevice test reused the existing annealed structure and swept the gate from -1.2 to +1.2 V at VDS = 1.2 V. The successful 49-point sweep reached a minimum |ID| of 2.11370e-4 at VGS = -1.2 V, still 2,113.7 times above the predeclared 1e-7 constant-current threshold. It therefore **does not** recover a threshold or DIBL value. See `data/part3_1000c_extended_gate_diagnostic.csv` and the new Part 3 subsection. The original Part 3 and 4 results were not overwritten; the full diagnostic PLT/deck/log remain in the university server's isolated `EE4435_DIBL_PILOT_1000C` workspace and have **not** been committed to this repository. The CSV holds summary values only. The temperature denotes process annealing, not electrical measurement temperature.

## Available figure assets

The repository already contains actual Sentaurus images:
`figures/02_extension.png`, `03_spacer.png`, `04_annealed.png`, `05_final.png`, and `part2_potential_comparison.png`. They are included directly by LaTeX. The original 1D TDR exports for the initial SOI stack and gate oxidation were converted to authentic, scale-accurate vector material-depth diagrams included in the report: `sections/part1_initial_soi_profile.tex` and `sections/part1_gateoxide_profile.tex`. Their measured boundaries are archived in `data/part1_early_1d_region_boundaries.csv`. The original SVisual evidence is additionally included as three cropped screenshots `figures/00_initial_soi_svisual.png`, `figures/01_gateoxide_full_svisual.png`, and `figures/01_gateoxide_zoom_svisual.png`, with correct 1D-axis captions. The reconstructed material-depth diagrams are distinct from the screenshots.

## Report presentation and verification

The title has no date. Both team members, Du Yanzhang (A0277012M) and Fang Tianchi (A0272402R), are listed without a first/second-member distinction. The table of contents has a separate page. The old report-status banner and `Data integrity and pending work` section have been removed. The factual methods and limitations remain alongside the relevant results.

**Before submission:** compile and review the complete report in Overleaf. The original SVisual screenshots and the source-derived 1D material-depth diagrams are now both included. Terminal-current values are intentionally retained in simulator-exported units because their two-dimensional normalization has not been independently established. The report's AI-assistance disclosure reflects the drafting and data-processing assistance.

## Data integrity

Numerical results must be traceable to the Sentaurus CSV/TDR exports. No unavailable threshold, DIBL or additional bias-point measurement is extrapolated to make figures appear complete.
