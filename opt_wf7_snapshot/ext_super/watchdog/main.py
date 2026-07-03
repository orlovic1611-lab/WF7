from __future__ import annotations

from pathlib import Path

from wf.watchdog.loop import run_cycle, run_monitor


class Watchdog:
    def __init__(self, root: str, audit_path: str, log_level: str = "INFO"):
        self.root = Path(root)
        self.audit_path = Path(audit_path)
        self.log_level = log_level

    def step(self):
        return run_cycle(self.root)

    def monitor(self, interval: int = 10) -> None:
        run_monitor(self.root, self.audit_path, interval=interval)
