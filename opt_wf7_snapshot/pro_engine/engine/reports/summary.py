from __future__ import annotations

from collections import Counter

from wf.core.events import Event


def build_summary(events: list[Event]) -> dict:
    """
    Convert a scan result into a compact operational summary.
    """
    return {
        "total": len(events),
        "by_kind": dict(Counter(e.kind for e in events)),
        "by_severity": dict(Counter(e.severity for e in events)),
    }
