from __future__ import annotations

from pathlib import Path

from wf.core.events import Event


def cleanup_workspace(root: str | Path) -> list[Event]:
    root = Path(root)
    events: list[Event] = []

    for path in root.rglob("__pycache__"):
        if path.is_dir():
            events.append(
                Event(
                    source="cleanup",
                    kind="remove_pycache",
                    severity="low",
                    details={"path": str(path)},
                )
            )

    for path in root.rglob(".pytest_cache"):
        if path.is_dir():
            events.append(
                Event(
                    source="cleanup",
                    kind="remove_pytest_cache",
                    severity="low",
                    details={"path": str(path)},
                )
            )

    for path in root.rglob("*.pyc"):
        events.append(
            Event(
                source="cleanup",
                kind="remove_pyc",
                severity="low",
                details={"path": str(path)},
            )
        )

    return events
