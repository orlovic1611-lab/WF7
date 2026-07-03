from __future__ import annotations

from wf.core.events import Event


def detect_policy_violations(events: list[Event]) -> list[Event]:
    """
    Translate raw sensor events into policy violations.

    This is where the system begins to behave like a real security product:
    sensors observe, detectors interpret, and policy decides what matters.
    """
    alerts: list[Event] = []

    for event in events:
        if event.kind == "suspicious_process":
            alerts.append(
                Event(
                    source="detector",
                    kind="policy_violation",
                    severity="high",
                    details={"reason": "suspicious process", **event.details},
                )
            )

    return alerts
