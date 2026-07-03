from __future__ import annotations

import csv
from pathlib import Path

from wf.core.events import Event


def write_event_summary_csv(path: str | Path, events: list[Event]) -> Path:
    """
    Write a CSV file that is easy to plot later.

    CSV is used here because it is simple, portable, and can feed directly into
    charts, dashboards, or further offline analysis without forcing the system
    into a database dependency too early.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    counts: dict[str, int] = {}
    for event in events:
        counts[event.kind] = counts.get(event.kind, 0) + 1

    with p.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["kind", "count"])
        for kind, count in sorted(counts.items()):
            writer.writerow([kind, count])

    return p
