from wf.health.main import healthcheck


def test_healthcheck():
    assert isinstance(healthcheck("."), list)
