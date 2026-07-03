import subprocess
import sys

def run_cmd(*args):
    return subprocess.run([sys.executable, "-m", "wf.cli.main", *args], capture_output=True, text=True)

def test_cli_healthcheck():
    r = run_cmd("healthcheck", "--root", ".")
    assert r.returncode == 0
    assert r.stdout.strip() == "[]"
