from wf.cli.config import load_config

def test_load_config():
    cfg = load_config(".")
    assert cfg.root.exists()
    assert cfg.data_dir.name == "data"
    assert cfg.logs_dir.name == "logs"
    assert cfg.outputs_dir.name == "outputs"
    assert cfg.interval_seconds == 10
    assert cfg.ai_guard_enabled is True
    assert cfg.log_level == "INFO"
