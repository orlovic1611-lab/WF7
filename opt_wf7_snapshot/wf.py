import os

EXT_SUPER = "/opt/wf/ext_super/engine"

def super_cmd():

    print("WF SUPER ENGINE MODULES:")

    for root, dirs, files in os.walk(EXT_SUPER):

        for f in files:

            print(" -", f)




#!/usr/bin/env python3


import sys
import json
import platform
import subprocess


sys.path.insert(
0,
"/opt/wf"
)


from core.engine import plugins,execute

from config.settings import VERSION,NAME




def banner():

 print(f"""

====================================
 {NAME}

 VERSION {VERSION}

====================================

""")



banner()



if len(sys.argv)<2:


 print("""
Commands:

 wf status

 wf doctor

 wf plugins

 wf run <plugin>

""")

 exit()




cmd=sys.argv[1]



if cmd=="status":


 print(json.dumps({

"framework":"online",

"version":VERSION,

"dashboard":"http://localhost:8080",

"service":
subprocess.getoutput(
"systemctl is-active wf-dashboard"
)


},indent=4))





elif cmd=="doctor":


 print(json.dumps({

"python":
platform.python_version(),

"kernel":
platform.release(),

"plugins":
len(plugins()),

"version":
VERSION


},indent=4))




elif cmd=="plugins":


 print(json.dumps(
 plugins(),
 indent=4
 ))




elif cmd=="run":


 print(json.dumps(

execute(
sys.argv[2],
sys.argv[3] if len(sys.argv)>3 else None
),

indent=4

))




# --- WF SUPER MERGE ENGINE COMMANDS ---
import os, sys

EXT_SUPER = "/opt/wf/ext_super/engine"

def super_cmd():
    print("WF SUPER ENGINE MODULES:")
    for root, dirs, files in os.walk(EXT_SUPER):
        for f in files:
            print(" -", f)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "super":
            super_cmd()
            sys.exit(0)
