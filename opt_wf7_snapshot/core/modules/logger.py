
import datetime
import os


LOG="logs/wf.log"


def write(message):

    os.makedirs(
        "logs",
        exist_ok=True
    )

    with open(LOG,"a") as f:

        f.write(
        f"[{datetime.datetime.now()}] {message}\n"
        )


