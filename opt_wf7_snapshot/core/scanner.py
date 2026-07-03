import subprocess
import os
import json
import datetime

DB="/var/lib/wf/database.db"
REPORT="/opt/wf/reports/json/report.json"


def scan(target):

    try:
        result=subprocess.check_output(
            ["nmap","-sV",target],
            stderr=subprocess.STDOUT,
            text=True
        )

    except Exception as e:
        result=str(e)


    data={
        "target":target,
        "time":str(datetime.datetime.now()),
        "result":result
    }


    os.makedirs(
        "/opt/wf/reports/json",
        exist_ok=True
    )

    with open(REPORT,"w") as f:
        json.dump(data,f,indent=2)


    return {
        "target":target,
        "saved":True,
        "report":REPORT,
        "result":result
    }
