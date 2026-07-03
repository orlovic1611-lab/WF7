class AIGuard:

    def analyze(self, events):
        result=[]

        for e in events:
            if getattr(e,"severity",None) == "high":
                result.append(
                    {
                    "action":"alert",
                    "reason":"high severity event"
                    }
                )

        return result
