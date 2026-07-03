

def explain(event):

    kind=event.get("kind")


    if kind=="interface_down":

        return """
NETWORK CHANGE

Probability:
normal event

Reason:
Interface state changed.

Recommendation:
Check connection.
"""


    if kind=="suspicious_process":

        return """
PROCESS WARNING

Possible abnormal process.

Recommendation:
Inspect PID.
"""


    return """
No strong anomaly detected.
"""

