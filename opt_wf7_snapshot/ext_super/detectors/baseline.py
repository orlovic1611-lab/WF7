from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING

from wf.core.events import Event

if TYPE_CHECKING:
    from wf.core.runtime import RuntimeState


def detect_baseline(events: list[Event], state: "RuntimeState") -> list[Event]:
    """Learn baseline and detect deviations."""
    events_out = []

    # Count events by kind
    counts = defaultdict(int)
    for e in events:
        counts[e.kind] += 1

    # Baseline learning
    baseline = state.get("baseline", {})
    for kind, count in counts.items():
        prev_count = baseline.get(kind, 0)
        if prev_count > 0 and count > prev_count * 2:
            events_out.append(Event(
                source="baseline",
                kind="anomaly_spike",
                severity="high",
                details={"kind": kind, "count": count, "baseline": prev_count},
                timestamp=datetime.now(datetime.timezone.utc)
            ))
        baseline[kind] = max(baseline.get(kind, 0), count)

    state.set("baseline", dict(baseline))
    return events_out
