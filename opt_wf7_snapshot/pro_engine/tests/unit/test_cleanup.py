from wf.cleanup import cleanup_workspace

def test_cleanup_finds_pytest_cache(tmp_path):
    (tmp_path / ".pytest_cache").mkdir()
    out = cleanup_workspace(tmp_path)
    assert out
