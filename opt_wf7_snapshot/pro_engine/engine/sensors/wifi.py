from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from wf.core.events import Event

if TYPE_CHECKING:
    from pathlib import Path


def scan_wifi(root: "Path") -> list[Event]:
    """Scan WiFi interfaces and signal strength."""
    import subprocess
    from pathlib import Path

    events = []
    root = Path(root)

    try:
        result = subprocess.run(
            ["nmcli", "-t", "-f", "DEVICE,TYPE,STATE,NAME", "dev"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        
        for line in result.stdout.strip().split("\n"):
            if ":" in line:
                device, dev_type, state, name = line.split(":", 3)
                if dev_type == "wifi":
                    if state != "connected":
                        events.append(Event(
                            source="wifi",
                            kind="interface_down",
                            severity="medium",
                            details={"device": device, "state": state},
                            timestamp=datetime.now(datetime.timezone.utc)
                        ))
                    else:
                        events.append(Event(
                            source="wifi",
                            kind="wifi_scan",
                            severity="info",
                            details={"device": device, "network": name},
                            timestamp=datetime.now(datetime.timezone.utc)
                        ))
    except Exception:
        pass

    return events
