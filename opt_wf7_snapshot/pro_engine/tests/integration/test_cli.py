import subprocess
import sys

def run_cmd(*args):
    return subprocess.run([sys.executable, "-m", "wf.cli.main", *args], capture_output=True, text=True)

def test_show_config():
    r = run_cmd("show-config")
    assert r.returncode == 0
    assert '"root"' in r.stdout
