
#!/usr/bin/env python3

import sys
import os
import json
import subprocess
import platform
import time


sys.path.insert(
0,
os.path.dirname(
os.path.dirname(
os.path.abspath(__file__)
))
)


from modules.plugin_manager import load_plugins,run_plugin


VERSION="4.1"



def banner():

 print(f"""

====================================
 WF SECURITY FRAMEWORK

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
 wf scan <ip>

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
 len(load_plugins()),

 "dashboard":
 subprocess.getoutput(
 "systemctl is-active wf-dashboard"
 ),

 "version":
 VERSION

 },indent=4))





elif cmd=="plugins":


 print(json.dumps(
 load_plugins(),
 indent=4
 ))




elif cmd=="run":


 if len(sys.argv)<3:

  print("missing plugin")

  exit()


 print(json.dumps(

 run_plugin(
 sys.argv[2],
 sys.argv[3] if len(sys.argv)>3 else None
 ),

 indent=4

 ))




elif cmd=="scan":


 print(json.dumps(

 run_plugin(
 "nmap_scan",
 sys.argv[2]

 ),

 indent=4

 ))



else:

 print("Unknown command")

