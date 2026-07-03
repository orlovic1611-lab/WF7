from wf.core.events import Event
from wf.detectors.anomaly import detect_anomalies

def test_detect_anomalies():
    events = [Event(source="a", kind="x", severity="low", details={}) for _ in range(3)]
    out = detect_anomalies(events, threshold=3)
    assert len(out) == 1
    assert out[0].kind == "repeated_event"
