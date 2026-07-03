
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates

from modules.system_info import run as system_info
from modules.scanner import run as scanner

from modules.plugin_manager import load_plugins,run_plugin

from database.db import *

import json



init()



app=FastAPI(
title="WF Security Framework"
)



templates=Jinja2Templates(
directory="dashboard/templates"
)



@app.get("/")
def home(request:Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
        "request":request
        }
    )



@app.get("/api/system")
def system():

    return system_info()



@app.get("/api/plugins")
def plugins():

    return {
    "plugins":load_plugins()
    }



@app.get("/api/plugin/{name}")
def plugin(name:str):

    return run_plugin(name)



@app.get("/api/scan/{target}")
def scan(target:str):

    result=scanner(target)

    add_scan(
    target,
    json.dumps(result)
    )

    return result



@app.get("/api/status")
def status():

    return {

    "status":"online",

    "framework":"WF 3.2"

    }

