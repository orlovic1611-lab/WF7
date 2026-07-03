from __future__ import annotations

try:
    import psutil
except ModuleNotFoundError:
    psutil = None

from wf.core.events import Event


def scan_network() -> list[Event]:
    events: list[Event] = []
    if psutil is None:
        return events

    stats = psutil.net_if_stats()
    for device, st in stats.items():
        if not st.isup:
            events.append(
                Event(
                    source="network",
                    kind="interface_down",
                    severity="medium",
                    details={"device": device, "type": "network", "state": "down"},
                )
            )
    return events
