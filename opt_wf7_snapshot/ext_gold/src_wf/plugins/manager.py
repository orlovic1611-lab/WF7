
from pathlib import Path


def list_plugins():

    p=Path("src/wf/plugins")

    return [
        x.stem
        for x in p.glob("*.py")
        if x.name!="manager.py"
    ]

