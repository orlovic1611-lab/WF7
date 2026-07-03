from __future__ import annotations

from pathlib import Path

from wf.core.events import Event


def cleanup_workspace(root: Path) -> list[Event]:
    root = Path(root)
    events: list[Event] = []

    for p in [root / ".pytest_cache", root / "__pycache__"]:
        if p.exists():
            events.append(Event(source="cleanup", kind="cleanup_found", severity="info", details={"path": str(p)}))

    return events
