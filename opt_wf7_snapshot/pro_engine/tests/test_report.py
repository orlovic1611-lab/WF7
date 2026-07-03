from wf.cli.report import build_report

def test_build_report(tmp_path):
    audit = tmp_path / 'audit.json'
    audit.write_text('[{"source":"s","kind":"k","severity":"low","details":{},"timestamp":"2026-05-14T00:00:00"}]')
    out = tmp_path / 'report.txt'
    res = build_report(audit, out)
    assert out.exists()
    assert 'k' in out.read_text()
