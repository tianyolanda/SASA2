#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


CLASSES = ["Car", "Pedestrian", "Cyclist", "Van"]
STRICT = {
    "Car": "0.70, 0.70, 0.70",
    "Pedestrian": "0.50, 0.50, 0.50",
    "Cyclist": "0.50, 0.50, 0.50",
    "Van": "0.70, 0.70, 0.70",
}
LOOSE = {
    "Car": "0.70, 0.50, 0.50",
    "Pedestrian": "0.50, 0.25, 0.25",
    "Cyclist": "0.50, 0.25, 0.25",
    "Van": "0.70, 0.50, 0.50",
}


def clean_model_name(path: Path) -> str:
    name = path.name
    name = name.replace("_test_snow_console.log", "")
    name = name.replace("_", " ")
    name = name.replace("plus", "+")
    return name


def parse_epoch(text: str, fallback_name: str) -> str:
    m = re.search(r"\*+ EPOCH\s+([0-9]+)\s+EVALUATION", text)
    if m:
        return m.group(1)
    m = re.search(r"\be([0-9]+)\b", fallback_name)
    return m.group(1) if m else "-"


def parse_sample_count(text: str) -> str:
    m = re.search(r"Average predicted number of objects\(([0-9]+) samples\)", text)
    return m.group(1) if m else "-"


def parse_triplet(text: str, cls: str, threshold: str):
    marker = f"{cls} AP_R40@{threshold}:"
    idx = text.find(marker)
    if idx < 0:
        return None
    block = text[idx : idx + 500]
    m = re.search(r"3d\s+AP:([0-9.]+),\s*([0-9.]+),\s*([0-9.]+)", block)
    if not m:
        return None
    return tuple(float(x) for x in m.groups())


def collect(log_dir: Path):
    rows = []
    for log_path in sorted(log_dir.glob("*_test_snow_console.log")):
        text = log_path.read_text(errors="ignore")
        if "Evaluation done" not in text:
            continue

        model = clean_model_name(log_path)
        row = {
            "model": model,
            "epoch": parse_epoch(text, model),
            "samples": parse_sample_count(text),
            "log": log_path.name,
            "strict": {},
            "loose": {},
        }
        for cls in CLASSES:
            row["strict"][cls] = parse_triplet(text, cls, STRICT[cls])
            row["loose"][cls] = parse_triplet(text, cls, LOOSE[cls])
        rows.append(row)
    return rows


def mean_mod(row, mode: str):
    values = []
    for cls in CLASSES:
        triplet = row[mode].get(cls)
        if triplet is None:
            return None
        values.append(triplet[1])
    return sum(values) / len(values)


def fmt(value):
    if value is None:
        return "-"
    return f"{value:.4f}"


def mode_table(rows, mode: str):
    ordered = sorted(
        rows,
        key=lambda r: mean_mod(r, mode) if mean_mod(r, mode) is not None else -1,
        reverse=True,
    )
    lines = [
        f"## {mode.title()}",
        "",
        "| Model | Epoch | Samples | Mean mod | Car easy | Car mod | Car hard | Ped easy | Ped mod | Ped hard | Cyc easy | Cyc mod | Cyc hard | Van easy | Van mod | Van hard | Log |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in ordered:
        vals = []
        for cls in CLASSES:
            triplet = row[mode].get(cls)
            vals.extend([None, None, None] if triplet is None else triplet)
        lines.append(
            "| "
            + " | ".join(
                [
                    row["model"],
                    row["epoch"],
                    row["samples"],
                    fmt(mean_mod(row, mode)),
                    *[fmt(v) for v in vals],
                    row["log"],
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("log_dir", type=Path)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    rows = collect(args.log_dir)
    skipped = sorted(p.name for p in args.log_dir.glob("*.status") if p.read_text(errors="ignore").startswith("SKIP"))

    doc = [
        "# DENSE Snow Test Results With Van",
        "",
        "Evaluation split: `test_snow` from `dense_infos_test_snow.pkl`.",
        "",
        "Metrics are 3D AP_R40 over four classes: Car, Pedestrian, Cyclist, and Van.",
        "",
        "- Strict thresholds: Car/Van `0.70`, Pedestrian/Cyclist `0.50`",
        "- Loose thresholds: Car/Van `0.50`, Pedestrian/Cyclist `0.25`",
        "- Mean mod is the average of moderate AP_R40 over Car, Pedestrian, Cyclist, and Van.",
        "",
        mode_table(rows, "strict"),
        "",
        mode_table(rows, "loose"),
    ]
    if skipped:
        doc.extend(["", "## Skipped", ""])
        doc.extend(f"- `{name}`" for name in skipped)

    output = "\n".join(doc) + "\n"
    if args.output:
        args.output.write_text(output)
    print(output)


if __name__ == "__main__":
    main()
