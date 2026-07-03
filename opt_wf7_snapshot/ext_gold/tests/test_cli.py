import subprocess
import sys

def test_show_help():
    r = subprocess.run([sys.executable, "-m", "wf.cli.main", "--help"], capture_output=True, text=True)
    assert r.returncode == 0
    assert "usage:" in r.stdout
