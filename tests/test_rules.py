from pathlib import Path

from agent_trust_scan.report import render_json, render_markdown
from agent_trust_scan.scanner import scan_path, scan_text, threshold_reached


def test_private_key_is_critical():
    key = "0x" + "a" * 64
    findings = scan_text(f"PRIVATE_KEY={key}\n", "config.py")
    assert any(f.rule_id == "secret.private_key" and f.severity == "critical" for f in findings)
    assert all(key not in f.evidence for f in findings)


def test_api_key_is_critical():
    findings = scan_text("OPENAI_API_KEY=sk-" + "b" * 28 + "\n", "settings.py")
    assert any(f.rule_id == "secret.api_key" for f in findings)


def test_unlimited_approve():
    text = "token.approve(spender, type(uint256).max);\n"
    findings = scan_text(text, "Vault.sol")
    assert any(f.rule_id == "wallet.unlimited_approve" for f in findings)


def test_x402_testnet_disabled_and_below_floor():
    text = "X402_ENABLED=0\nX402_NETWORK=eip155:84532\nX402_PRICE=$0.001\n"
    findings = scan_text(text, "x402.env")
    ids = {f.rule_id for f in findings}
    assert {"x402.testnet", "x402.disabled", "x402.price_below_floor"} <= ids


def test_payment_code_without_controls():
    text = "def send(tx):\n    return wallet.send_transaction(tx)\n"
    findings = scan_text(text, "agent.py")
    ids = {f.rule_id for f in findings}
    assert {"agent.no_spend_limit", "agent.no_kill_switch",
            "agent.no_human_approval", "agent.no_audit_log"} <= ids


def test_execution_rule():
    findings = scan_text("eval(tool_output)\n", "tool.py")
    assert any(f.rule_id == "tool_output.execution" and f.severity == "high" for f in findings)


def test_clean_file_has_no_findings():
    assert scan_text('print("hello")\n', "main.py") == []


def test_scan_path_and_report(tmp_path: Path):
    (tmp_path / ".env").write_text("PRIVATE_KEY=0x" + "c" * 64 + "\n", encoding="utf-8")
    (tmp_path / "agent.py").write_text(
        "def send(tx):\n    return wallet.send_transaction(tx)\n", encoding="utf-8"
    )
    result = scan_path(tmp_path)
    assert result.files_scanned >= 2
    assert result.verdict in {"critical", "high"}
    assert result.score < 100
    md = render_markdown(result)
    assert "Agent Trust Scan" in md
    assert "c" * 64 not in md
    payload = render_json(result)
    assert '"score"' in payload
    assert "c" * 64 not in payload


def test_threshold_with_result(tmp_path: Path):
    (tmp_path / "x.env").write_text("PRIVATE_KEY=0x" + "e" * 64 + "\n", encoding="utf-8")
    result = scan_path(tmp_path)
    assert threshold_reached(result, "critical") is True
    assert threshold_reached(result, "none") is False
