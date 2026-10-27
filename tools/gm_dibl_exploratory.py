#!/usr/bin/env python3
"""Exploratory ELR/ESR threshold shifts from archived Sentaurus Id-Vg CSVs.

This is a supplementary *model-dependent* diagnostic, not a replacement for
a missing constant-current threshold measurement. No voltage points are
invented, and no extrapolated value is called a measured threshold crossing.

Expected columns: VGS_V, Id_<CASE>_0p1, Id_<CASE>_1p2.
Works on Part 4's archived CSV and a Part 3 CSV with the same convention.
"""
import argparse
import csv
import math
import re
from pathlib import Path

WINDOWS = (3, 5, 7, 9)


def straight_line(x, y):
    n = len(x)
    xm, ym = sum(x) / n, sum(y) / n
    sxx = sum((v - xm) ** 2 for v in x)
    slope = sum((v - xm) * (w - ym) for v, w in zip(x, y)) / sxx
    intercept = ym - slope * xm
    total = sum((w - ym) ** 2 for w in y)
    residual = sum((w - slope * v - intercept) ** 2 for v, w in zip(x, y))
    r2 = 1 - residual / total if total else 1.0
    return slope, intercept, r2


def extrapolate(vg, currents, high_drain, width):
    if len(vg) != len(currents) or len(vg) < width:
        raise ValueError("Unequal traces or insufficient points")
    if any(not math.isfinite(y) or y <= 0 for y in currents):
        raise ValueError("Need positive, finite |Id| samples")
    if any(b <= a for a, b in zip(vg, vg[1:])):
        raise ValueError("VGS must be strictly increasing")
    y = [math.sqrt(i) if high_drain else i for i in currents]
    half = width // 2
    candidates = []
    for center in range(half, len(vg) - half):
        xs = vg[center-half:center+half+1]
        ys = y[center-half:center+half+1]
        slope, intercept, r2 = straight_line(xs, ys)
        candidates.append((slope, intercept, r2, center))
    slope, intercept, r2, center = max(candidates, key=lambda z: z[0])
    if slope <= 0:
        raise ValueError("Nonpositive maximal transconductance slope")
    intercept_v = -intercept / slope
    # Linear-region correction at VDS=0.1 V; high bias sqrt(Id)
    # method is an *assumed* saturation-region extrapolation.
    apparent_vth = intercept_v if high_drain else intercept_v - 0.1 / 2
    return apparent_vth, r2, vg[center], center in (half, len(vg)-half-1)


def analyze(source):
    with source.open(newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        records = list(reader)
    vg = [float(row["VGS_V"]) for row in records]
    cases = {}
    for name in fieldnames:
        m = re.fullmatch(r"Id_(.+)_(0p1|1p2)", name)
        if m:
            cases.setdefault(m[1], {})[m[2]] = [abs(float(r[name])) for r in records]
    if not cases or any(set(q) != {"0p1", "1p2"} for q in cases.values()):
        raise ValueError("CSV must contain matched low/high columns for every case")
    data = []
    for case, q in sorted(cases.items(), key=lambda kv: float(re.sub("^T", "", kv[0]))):
        result = {"case": case}
        trial = []
        for width in WINDOWS:
            lo, lo_r2, lo_v, lo_edge = extrapolate(vg, q["0p1"], False, width)
            hi, hi_r2, hi_v, hi_edge = extrapolate(vg, q["1p2"], True, width)
            shift = 1000 * (lo - hi) / 1.1
            trial.append(shift)
            result[f"DIBL_apparent_w{width}_mV_per_V"] = f"{shift:.6f}"
            if width == 5:
                result.update({
                    "ELR_low_VTH_V": f"{lo:.9f}",
                    "ESR_high_VTH_V": f"{hi:.9f}",
                    "low_fit_R2": f"{lo_r2:.7f}",
                    "high_fit_R2": f"{hi_r2:.7f}",
                    "low_tangent_VGS_V": f"{lo_v:.3f}",
                    "high_tangent_VGS_V": f"{hi_v:.3f}",
                    "fit_peak_at_search_boundary": str(lo_edge or hi_edge),
                })
        result["DIBL_window_min_mV_per_V"] = f"{min(trial):.6f}"
        result["DIBL_window_max_mV_per_V"] = f"{max(trial):.6f}"
        data.append(result)
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("data/part4_idvg_all.csv"))
    parser.add_argument("--output", type=Path, default=Path("data/part4_elr_esr_sensitivity.csv"))
    args = parser.parse_args()
    data = analyze(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0]))
        writer.writeheader()
        writer.writerows(data)
    for row in data:
        print(f'{row["case"]}: apparent ELR/ESR DIBL (5-point) '
              f'{float(row["DIBL_apparent_w5_mV_per_V"]):.2f} mV/V; '
              f'3-9 point sensitivity '
              f'{float(row["DIBL_window_min_mV_per_V"]):.2f}–'
              f'{float(row["DIBL_window_max_mV_per_V"]):.2f} mV/V')
    print("MODEL DEPENDENT: low-bias linear versus high-bias sqrt(Id) "
          "fit. Do not relabel original constant-current N/A values.")


if __name__ == "__main__":
    main()
