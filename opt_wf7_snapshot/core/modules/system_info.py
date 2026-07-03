import os
import platform
import shutil

def run():

    total, used, free = shutil.disk_usage("/")

    return {
        "system": platform.system(),
        "hostname": platform.node(),
        "python": platform.python_version(),
        "disk_free_gb": round(free / (1024**3),2),
        "cpu": os.cpu_count()
    }
