
import subprocess


NAME="nmap_scan"


def run(target="127.0.0.1"):


    try:

        output=subprocess.getoutput(
        f"nmap -sV {target}"
        )


        return {

        "target":target,

        "result":output

        }


    except Exception as e:


        return {

        "error":str(e)

        }

