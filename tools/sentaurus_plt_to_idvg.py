#!/usr/bin/env python3
"""Convert *existing* Sentaurus Device DF-ISE text PLT transfer sweeps to CSV.

Example (replace each PLT path with its actual archived path):
  python3 tools/sentaurus_plt_to_idvg.py \
    --pair T800 /path/low_vds.plt /path/high_vds.plt \
    --pair T850 /path/low_vds.plt /path/high_vds.plt \
    --output data/part3_idvg_all.csv

Does not rerun SProcess/SDevice or modify the original PLT files.
Confirm each file's node, process temperature and drain bias independently.
"""
import argparse
import csv
import math
import re
from pathlib import Path

NUMBER = re.compile(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][+-]?\d+)?")


def load_dfise_xy(path):
    content = Path(path).read_text()
    ds = re.search(r"\bdatasets\s*=\s*\[(.*?)\]", content, re.S)
    data = re.search(r"(?m)^\s*Data\s*\{(.*?)(?=^\s*\})", content, re.S)
    if not ds or not data:
        raise ValueError(f"{path}: expected DF-ISE text datasets/Data blocks")
    names = re.findall(r'"([^"]+)"', ds.group(1))
    required = ("gate OuterVoltage", "drain OuterVoltage", "drain TotalCurrent")
    if any(k not in names for k in required):
        raise ValueError(f"{path}: missing contact field; got {names!r}")
    raw = re.sub(r"(?m)#.*$", "", data.group(1))
    values = [float(t) for t in NUMBER.findall(raw)]
    if not names or len(values) % len(names):
        raise ValueError(
            f"{path}: {len(values)} values cannot form {len(names)}-field rows")
    result = []
    indexes = [names.index(k) for k in required]
    for pos in range(0, len(values), len(names)):
        line = values[pos:pos+len(names)]
        result.append(tuple(line[i] for i in indexes))
    return result


def gate_sweep(path, vds):
    samples = load_dfise_xy(path)
    samples = [(vgs, abs(idrain)) for vgs, vd, idrain in samples
               if abs(vd-vds) < 5e-4 and math.isfinite(idrain)]
    if len(samples) < 15:
        raise ValueError(f"{path}: too few matched VDS={vds} samples")
    # If an identical gate value appears during the initial drain ramp,
    # retain its final (post-ramp) current measurement.
    unique = {round(vgs, 6): idrain for vgs, idrain in samples}
    v = sorted(unique)
    if len(v) < 15:
        raise ValueError(f"{path}: fewer than 15 unique VGS values")
    print(f"{path}: {len(v)} unique VGS points at VDS={vds:.1f} V; "
          f"range {v[0]:.3f} to {v[-1]:.3f} V")
    return unique


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--pair", action="append", nargs=3, metavar=("CASE", "LOW_PLT", "HIGH_PLT"),
                   required=True, help="Case name, low-drain and high-drain paths")
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    fields = {}
    common_vgs = None
    for case, low_path, high_path in args.pair:
        if not re.fullmatch(r"[A-Za-z0-9]+", case):
            p.error("Case label must contain letters/digits only")
        for label, path, vd in (("0p1", low_path, 0.1), ("1p2", high_path, 1.2)):
            values = gate_sweep(path, vd)
            if common_vgs is None:
                common_vgs = sorted(values)
            if sorted(values) != common_vgs:
                raise ValueError(
                    f"{path}: VGS sampling differs; do not silently interpolate")
            fields[f"Id_{case}_{label}"] = values
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["VGS_V", *fields])
        for v in common_vgs:
            writer.writerow([f"{v:.6f}", *(f"{trace[v]:.14g}" for trace in fields.values())])
    print(f"Wrote {args.output}; no Sentaurus raw files changed")


if __name__ == "__main__":
    main()
