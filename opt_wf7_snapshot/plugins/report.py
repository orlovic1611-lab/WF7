
import json
import os
from datetime import datetime



NAME="report"



def run(data=None):


    os.makedirs(
    "reports",
    exist_ok=True
    )


    file="reports/report_"+datetime.now().strftime("%Y%m%d_%H%M%S")+".json"


    with open(file,"w") as f:

        json.dump(
        data or {},
        f,
        indent=4
        )


    return {

    "saved":file

    }

