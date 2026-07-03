
import platform
import socket

def run():
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "kernel": platform.release()
    }

