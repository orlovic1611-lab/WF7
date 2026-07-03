from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class WFConfig:
    """
    Immutable runtime configuration.

    Keeping configuration immutable helps avoid accidental side effects in
    long-running monitoring loops where one module should not silently mutate
    the global runtime behavior of another module.
    """
    root: Path = Path(".").resolve()
    data_dir: Path = Path("data")
    logs_dir: Path = Path("logs")
    outputs_dir: Path = Path("outputs")
    interval_seconds: int = 10
    ai_guard_enabled: bool = True
    log_level: str = "INFO"
