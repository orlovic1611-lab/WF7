from __future__ import annotations

from pathlib import Path

from wf.core.events import Event


def healthcheck(root: str | Path) -> list[Event]:
    root = Path(root)
    events: list[Event] = []
    for rel in ["configs", "data", "docs", "logs", "outputs", "scripts", "src", "tests"]:
        if not (root / rel).exists():
            events.append(Event(source="health", kind="missing_path", severity="high", details={"path": rel}))
    return events
