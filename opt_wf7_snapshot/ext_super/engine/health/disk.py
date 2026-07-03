from __future__ import annotations

from pathlib import Path

from wf.core.events import Event


def check_disk_usage(root: str | Path, warning_bytes: int = 500_000_000) -> list[Event]:
    """
    Rough disk footprint check.

    This is a guardrail, not a replacement for a real storage monitor. The
    objective is to surface obvious growth patterns before they become an
    operational incident.
    """
    root = Path(root)
    total = 0
    for path in root.rglob("*"):
        if path.is_file():
            try:
                total += path.stat().st_size
            except OSError:
                continue

    events: list[Event] = []
    if total >= warning_bytes:
        events.append(
            Event(
                source="health",
                kind="disk_usage_high",
                severity="medium",
                details={"bytes": total, "warning_bytes": warning_bytes},
            )
        )

    return events
