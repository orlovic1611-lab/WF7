import subprocess


def run(target):

    result = {
        "target": target,
        "status":"started"
    }

    try:
        output=subprocess.check_output(
            ["nmap","-sV",target],
            text=True,
            timeout=60
        )

        result["output"]=output

    except Exception as e:
        result["error"]=str(e)

    return result

