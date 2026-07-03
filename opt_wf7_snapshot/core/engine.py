
import os
import importlib
import json


PLUGIN_DIR="/opt/wf/plugins"



def plugins():

    if not os.path.exists(PLUGIN_DIR):
        return []

    return [
        x.replace(".py","")
        for x in os.listdir(PLUGIN_DIR)
        if x.endswith(".py")
        and x != "__init__.py"
    ]




def execute(name, args=None):

    if args is None:
        args=[]


    path = f"plugins.{name}"


    try:

        module = importlib.import_module(path)


        if hasattr(module,"run"):

            result = module.run(*args)

            return result


        return {
            "error":"plugin has no run()"
        }


    except Exception as e:

        return {
            "error":str(e)
        }





def scan(target):

    import subprocess
    import os
    import json
    import datetime


    try:

        result=subprocess.check_output(
            [
            "nmap",
            "-sV",
            target
            ],
            text=True
        )


        os.makedirs(
        "/opt/wf/reports/json",
        exist_ok=True
        )


        data={

        "target":target,
        "time":str(datetime.datetime.now()),
        "result":result

        }


        with open(
        "/opt/wf/reports/json/report.json",
        "w"
        ) as f:

            json.dump(
            data,
            f,
            indent=4
            )


        return {

        "target":target,
        "saved":True,
        "result":result

        }


    except Exception as e:


        return {

        "error":str(e)

        }



def history():

    db="/var/lib/wf/database.db"

    if not os.path.exists(db):
        return []


    import sqlite3

    con=sqlite3.connect(db)

    cur=con.cursor()


    try:

        cur.execute(
        "select * from scans order by id desc"
        )

        return cur.fetchall()


    except:

        return []

