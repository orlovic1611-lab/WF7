from __future__ import annotations

from pathlib import Path

from wf.core.config import WFConfig
from wf.utils.yamlio import read_yaml


def load_config(root: str | Path) -> WFConfig:
    root = Path(root).resolve()
    if root.suffix in {".yml", ".yaml"} and root.is_file():
        config_path = root
        root = config_path.parent.parent
    else:
        config_path = root / "configs" / "app.yaml"

    data = read_yaml(config_path) if config_path.exists() else {}
    if not isinstance(data, dict):
        data = {}

    return WFConfig(
        root=root,
        data_dir=root / data.get("data_dir", "data"),
        logs_dir=root / data.get("logs_dir", "logs"),
        outputs_dir=root / data.get("outputs_dir", "outputs"),
        interval_seconds=int(data.get("interval_seconds", 10)),
        ai_guard_enabled=bool(data.get("ai_guard_enabled", True)),
        log_level=str(data.get("log_level", "INFO")),
    )
