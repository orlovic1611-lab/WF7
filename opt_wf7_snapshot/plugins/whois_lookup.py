
import subprocess


NAME="whois_lookup"



def run(target="example.com"):


    try:


        result=subprocess.getoutput(
        f"whois {target}"
        )


        return {

        "target":target,

        "whois":result[:3000]

        }


    except Exception as e:


        return {

        "error":str(e)

        }

