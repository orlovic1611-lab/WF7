from __future__ import annotations

import time
from pathlib import Path

from wf.core.events import Event
from wf.detectors.anomaly import detect_anomalies
from wf.sensors.filesystem import scan_filesystem
from wf.sensors.network import scan_network
from wf.sensors.processes import scan_processes
from wf.utils.jsonio import read_json, write_json


def _event_to_obj(e: Event) -> dict:
    if hasattr(e, "model_dump"):
        return e.model_dump()
    if hasattr(e, "dict"):
        return e.dict()
    return {
        "source": e.source,
        "kind": e.kind,
        "severity": e.severity,
        "details": e.details,
        "timestamp": e.timestamp.isoformat(),
    }


def _event_key(e) -> tuple:
    if isinstance(e, dict):
        return (
            e.get("source"),
            e.get("kind"),
            e.get("severity"),
            repr(e.get("details")),
        )
    return (
        getattr(e, "source", None),
        getattr(e, "kind", None),
        getattr(e, "severity", None),
        repr(getattr(e, "details", None)),
    )


def _dedupe_events(items: list[dict]) -> list[dict]:
    seen = set()
    out = []
    for item in items:
        key = _event_key(item)
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def run_cycle(root: str | Path) -> list[Event]:
    root = Path(root)
    events: list[Event] = []
    events.extend(scan_filesystem(root))
    events.extend(scan_network())
    events.extend(scan_processes())
    events.extend(detect_anomalies(events))
    return events


def run_monitor(root: str | Path, audit_path: str | Path, interval: int = 10) -> None:
    root = Path(root)
    audit_path = Path(audit_path)
    audit_path.parent.mkdir(parents=True, exist_ok=True)

    current: list[dict] = []
    if audit_path.exists():
        loaded = read_json(audit_path)
        if isinstance(loaded, list):
            current = loaded

    try:
        while True:
            events = run_cycle(root)
            current.extend(_event_to_obj(e) for e in events)
            current = _dedupe_events(current)
            write_json(audit_path, current)
            time.sleep(interval)
    except KeyboardInterrupt:
        return
