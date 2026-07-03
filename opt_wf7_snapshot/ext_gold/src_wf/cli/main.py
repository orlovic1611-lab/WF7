from __future__ import annotations

import argparse
import json
from dataclasses import asdict, is_dataclass
from pathlib import Path

from wf.cli.cleanup import cleanup_workspace
from wf.cli.config import load_config
from wf.cli.health import healthcheck_paths
from wf.cli.report import build_report
from wf.watchdog.main import Watchdog


def _event_to_obj(e):
    if hasattr(e, "model_dump"):
        return e.model_dump()
    if hasattr(e, "dict"):
        return e.dict()
    if is_dataclass(e):
        return asdict(e)
    if isinstance(e, dict):
        return e
    return {"value": str(e)}


def _cfg_to_obj(cfg):
    if hasattr(cfg, "model_dump"):
        return cfg.model_dump()
    if hasattr(cfg, "dict"):
        return cfg.dict()
    if is_dataclass(cfg):
        return asdict(cfg)
    if isinstance(cfg, dict):
        return cfg
    return {"value": str(cfg)}


def main() -> int:
    parser = argparse.ArgumentParser(prog="wf")
    sub = parser.add_subparsers(dest="command", required=True)

    p_show = sub.add_parser("show-config")
    p_show.add_argument("--config", default="configs/app.yaml")

    p_health = sub.add_parser("healthcheck")
    p_health.add_argument("--root", default=".")

    p_cleanup = sub.add_parser("cleanup")
    p_cleanup.add_argument("--root", default=".")

    p_run = sub.add_parser("run")
    p_run.add_argument("--audit", required=True)
    p_run.add_argument("--log-level", default="INFO")
    p_run.add_argument("--root", default=".")

    p_monitor = sub.add_parser("monitor")
    p_monitor.add_argument("--audit", required=True)
    p_monitor.add_argument("--root", default=".")
    p_monitor.add_argument("--interval", type=int, default=10)
    p_monitor.add_argument("--log-level", default="INFO")

    p_report = sub.add_parser("report")
    p_report.add_argument("--out", required=True)
    p_report.add_argument("--audit", default="logs/audit/main.json")

    args = parser.parse_args()

    if args.command == "show-config":
        cfg = load_config(Path(args.config))
        print(json.dumps(_cfg_to_obj(cfg), indent=2, default=str))
        return 0

    if args.command == "healthcheck":
        events = healthcheck_paths(Path(args.root))
        print(json.dumps([_event_to_obj(e) for e in events], indent=2, default=str))
        return 0

    if args.command == "cleanup":
        events = cleanup_workspace(Path(args.root))
        print(json.dumps([_event_to_obj(e) for e in events], indent=2, default=str))
        return 0

    if args.command == "run":
        w = Watchdog(str(Path(args.root)), str(Path(args.audit)), args.log_level)
        events = w.step()
        print(json.dumps([_event_to_obj(e) for e in events], indent=2, default=str))
        return 0

    if args.command == "monitor":
        w = Watchdog(str(Path(args.root)), str(Path(args.audit)), args.log_level)
        w.monitor(interval=args.interval)
        return 0

    if args.command == "report":
        out = build_report(Path(args.audit), Path(args.out))
        print(out)
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
