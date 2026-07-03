from __future__ import annotations

try:
    import psutil
except ModuleNotFoundError:
    psutil = None

from wf.core.events import Event


def scan_processes() -> list[Event]:
    events: list[Event] = []
    if psutil is None:
        return events

    for proc in psutil.process_iter(["pid", "name", "status"]):
        try:
            info = proc.info
            if info.get("status") in {"zombie", "dead"}:
                events.append(
                    Event(
                        source="process",
                        kind="suspicious_process",
                        severity="medium",
                        details={"pid": info.get("pid"), "name": info.get("name"), "status": info.get("status")},
                    )
                )
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return events
