from __future__ import annotations

from pathlib import Path

from wf.core.events import Event


def healthcheck_paths(root: Path) -> list[Event]:
    root = Path(root)
    events: list[Event] = []

    if not root.exists():
        events.append(Event(source="health", kind="missing_root", severity="high", details={"path": str(root)}))
        return events

    for p in [root / "logs", root / "outputs", root / "configs"]:
        if not p.exists():
            events.append(Event(source="health", kind="missing_path", severity="medium", details={"path": str(p)}))

    return events
