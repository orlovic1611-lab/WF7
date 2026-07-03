from .main import Watchdog

def run_scan(root, state=None):
    audit_path = getattr(state, "audit_path", None)
    if audit_path is None:
        raise TypeError("state must contain audit_path")
    w = Watchdog(root, audit_path)
    return w.run()

__all__ = ["Watchdog", "run_scan"]
