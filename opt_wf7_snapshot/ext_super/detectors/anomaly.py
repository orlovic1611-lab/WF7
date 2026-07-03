from __future__ import annotations

from collections import Counter

from wf.core.events import Event


def detect_anomalies(events: list[Event], threshold: int = 3) -> list[Event]:
    counts = Counter(e.kind for e in events)
    anomalies: list[Event] = []

    for kind, count in counts.items():
        if count >= threshold:
            anomalies.append(
                Event(
                    source="anomaly",
                    kind="repeated_event",
                    severity="medium",
                    details={"kind": kind, "count": count, "threshold": threshold},
                )
            )
    return anomalies
