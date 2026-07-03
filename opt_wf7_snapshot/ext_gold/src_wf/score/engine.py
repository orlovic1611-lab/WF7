

def calculate(events):

    score=100


    for e in events:

        if e.get("severity")=="medium":
            score-=5

        if e.get("severity")=="high":
            score-=15

        if e.get("kind")=="suspicious_process":
            score-=20


    if score<0:
        score=0


    return score



def label(score):

    if score>80:
        return "SAFE"

    if score>50:
        return "WARNING"

    return "DANGER"

