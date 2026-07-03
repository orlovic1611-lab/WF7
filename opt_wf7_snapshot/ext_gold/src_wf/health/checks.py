from __future__ import annotations

from pathlib import Path

from wf.core.events import Event


def healthcheck_paths(root: str | Path) -> list[Event]:
    """
    Verify that the project skeleton is present and readable.

    Health checks should prefer clear, actionable output over broad failure
    messages. Each missing path is emitted as a separate event so the operator
    can see exactly what needs attention.
    """
    root = Path(root)
    required = ["configs", "data", "docs", "logs", "outputs", "scripts", "src", "tests"]
    events: list[Event] = []

    for rel in required:
        if not (root / rel).exists():
            events.append(
                Event(
                    source="health",
                    kind="missing_path",
                    severity="high",
                    details={"path": rel},
                )
            )

    return events
