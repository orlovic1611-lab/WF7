from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from wf.utils.jsonio import read_json


def build_report(audit: Path, out: Path) -> str:
    data = read_json(audit)
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)

    sources = Counter()
    severities = Counter()
    kinds = Counter()

    for row in data:
        if isinstance(row, dict):
            sources[row.get("source", "unknown")] += 1
            severities[row.get("severity", "unknown")] += 1
            kinds[row.get("kind", "unknown")] += 1

    with out.open("w", newline="", encoding="utf-8") as f:
        f.write(f"total_events: {len(data)}\n")
        f.write("by_source:\n")
        for key, count in sorted(sources.items()):
            f.write(f"  {key}: {count}\n")
        f.write("by_severity:\n")
        for key, count in sorted(severities.items()):
            f.write(f"  {key}: {count}\n")
        f.write("by_kind:\n")
        for key, count in sorted(kinds.items()):
            f.write(f"  {key}: {count}\n")
        f.write("\n")

        w = csv.DictWriter(f, fieldnames=["source", "kind", "severity", "timestamp"])
        w.writeheader()
        for row in data:
            if isinstance(row, dict):
                w.writerow({k: row.get(k) for k in w.fieldnames})

    return str(out)
