from __future__ import annotations

import json
from pathlib import Path

from wf.core.events import Event


class AuditLog:
    """Append-only audit store."""
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _load(self) -> list[dict]:
        if not self.path.exists():
            return []
        return json.loads(self.path.read_text(encoding="utf-8"))

    def write(self, event: Event) -> None:
        payload = {
            "source": event.source,
            "kind": event.kind,
            "severity": event.severity,
            "details": event.details,
            "timestamp": event.timestamp.isoformat(),
        }
        data = self._load()
        data.append(payload)
        self.path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
