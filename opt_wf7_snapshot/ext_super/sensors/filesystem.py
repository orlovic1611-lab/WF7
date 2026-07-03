from __future__ import annotations

from pathlib import Path

from wf.core.events import Event

SKIP_PARTS = {
    ".venv",
    "__pycache__",
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    "site-packages",
    "configs",
}

SKIP_NAMES = {
    "README.md",
    "a",
}

def scan_filesystem(root: str | Path) -> list[Event]:
    root = Path(root)
    events: list[Event] = []

    for path in root.rglob("*"):
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.name in SKIP_NAMES:
            continue
        if not path.exists():
            continue
        if path.is_file() and path.stat().st_size == 0:
            events.append(
                Event(
                    source="filesystem",
                    kind="empty_file",
                    severity="low",
                    details={"path": str(path)},
                )
            )

    return events
