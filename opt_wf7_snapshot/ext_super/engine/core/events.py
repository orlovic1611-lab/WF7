from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True, slots=True)
class Event:
    source: str
    kind: str
    severity: str
    details: dict
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
