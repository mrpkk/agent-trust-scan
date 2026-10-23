import json
from pathlib import Path

from agent_trust_scan.cli import main


def test_cli_exit_code_for_critical(tmp_path: Path):
    (tmp_path / "leak.py").write_text(
        'PRIVATE_KEY = "0x' + "a" * 64 + '"\n', encoding="utf-8"
    )
    assert main([str(tmp_path), "--fail-on", "critical"]) == 1


def test_cli_exit_code_clean(tmp_path: Path):
    (tmp_path / "main.py").write_text('print("ok")\n', encoding="utf-8")
    assert main([str(tmp_path), "--fail-on", "high"]) == 0


def test_cli_json_out(tmp_path: Path):
    (tmp_path / "main.py").write_text('print("ok")\n', encoding="utf-8")
    out = tmp_path / "report.json"
    assert main([str(tmp_path), "--format", "json", "--out", str(out), "--fail-on", "none"]) == 0
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["score"] == 100
    assert payload["findings"] == []
