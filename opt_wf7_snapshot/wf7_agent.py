#!/usr/bin/env python3
import time, os, requests

LOG = "/opt/wf7/wf7_agent.log"

def log(msg):
    with open(LOG, "a") as f:
        f.write(msg + "\n")
    print(msg)

def check_super_engine():
    return os.path.exists("/opt/wf7/pro_engine")

def ping_cloud_api():
    try:
        r = requests.get("http://127.0.0.1:7070/api/status", timeout=2)
        return r.status_code == 200
    except:
        return False

def main():
    log("WF7 Agent started.")
    while True:
        time.sleep(5)
        log("Heartbeat: agent alive")

        if check_super_engine():
            log("Super engine OK")
        else:
            log("Super engine MISSING!")

        if ping_cloud_api():
            log("Cloud API OK")
        else:
            log("Cloud API DOWN")

if __name__ == "__main__":
    main()
