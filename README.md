# agent-trust-scan

[![tests](https://github.com/mrpkk/agent-trust-scan/actions/workflows/test.yml/badge.svg)](https://github.com/mrpkk/agent-trust-scan/actions/workflows/test.yml)
[![license](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)

Static security scan for **AI agents with wallets**.

**Landing page:** <https://mrpkk.github.io/agent-trust-scan/>  
**Free scan request:** <https://github.com/mrpkk/agent-trust-scan/issues/new?template=scan-request.yml>

It looks for the failure modes that turn a helpful agent into a drain:

- private keys and API tokens in files;
- `.env` inside the tree;
- unlimited token approvals;
- x402 on a testnet, disabled, priced below the rail cost, or without a receipt check;
- payment code without spend limits, a kill switch, human approval, or an audit log;
- `eval` / `exec` / `pickle` / `shell=True` on tool output.

```bash
pip install -e .
agent-trust-scan scan /path/to/agent
agent-trust-scan scan /path/to/agent --format json --out report.json
agent-trust-scan scan /path/to/agent --fail-on critical
```

Exit code is `1` when a finding at or above `--fail-on` exists (default: `high`), so it can gate CI.

Use it as a GitHub Action:

```yaml
- uses: mrpkk/agent-trust-scan@main
  with:
    path: .
    fail-on: high
```

## What it is not

This is a **static, heuristic** scan. It does not execute the agent, call its tools, test prompt injection live, or prove exploitability. A missing keyword does not mean a control is absent — limits may live in a policy service or a database. A present keyword does not mean the control works. Every finding is a question to verify.

A paid **Agent Wallet Security Review** adds manual threat modeling, live prompt-injection tests, payment-flow checks, and a retest. The free scan is the first step, not the audit.

## Rules

| Rule | Severity | What it catches |
|---|---|---|
| `secret.private_key` | critical | private key / seed phrase / PEM block in a file |
| `secret.api_key` | critical | `sk-`, `ghp_`, `xoxb-`, `AKIA`, `hf_`, `AIza` tokens |
| `secret.dotenv` | high | a real `.env` inside the scanned tree |
| `wallet.unlimited_approve` | high | `type(uint256).max`, `2**256-1`, `maxUint256` |
| `x402.testnet` | medium | x402 configured for Base Sepolia / testnet |
| `x402.disabled` | medium | `X402_ENABLED=0` / `x402_enabled: false` |
| `x402.price_below_floor` | medium | x402 price below ~$0.002 (rail cost) |
| `x402.no_receipt_check` | medium | x402 code without a tx-hash/receipt check |
| `agent.no_spend_limit` | medium | payment code without a visible per-tx/daily cap |
| `agent.no_kill_switch` | medium | payment code without a visible stop |
| `agent.no_human_approval` | medium | payment code without a visible approval path |
| `agent.no_audit_log` | low | payment code without a visible audit/receipt record |
| `tool_output.execution` | high/medium | `eval`, `exec`, `pickle.loads`, `shell=True` |

## Example

```bash
$ agent-trust-scan scan examples/vulnerable-agent
# Agent Trust Scan
**Score:** 0/100 — CRITICAL
...
```

See [`docs/SAMPLE-REPORT.md`](docs/SAMPLE-REPORT.md) for a full report against an intentionally vulnerable example.

## Free scan

Open a [scan request](https://github.com/mrpkk/agent-trust-scan/issues/new?template=scan-request.yml) with a public repo or a short description of the payment flow. We return a 2-page report in 48 hours.

## Paid review

| Service | Price | What you get |
|---|---|---|
| Agent Wallet Security Review | $2,500 | threat model, prompt-injection tests, wallet permissions, limits, kill switch, x402 flow, report + fixes |
| Payable Agent Sprint | $3,500 | USDC/x402 pay-per-call, cost-based pricing, receipt check, docs, deploy on your infra |
| Payable + Safe | $5,500 | both, plus 30 days of support |
| Trust Retainer | $1,500/mo | monitoring, policy updates, monthly report, incident response |

We do not custody funds and do not process payments for third parties. You keep the keys.

## Development

```bash
python3 -m pytest -q
python3 -m agent_trust_scan scan examples/vulnerable-agent --fail-on none
```

No runtime dependencies; Python 3.10+.

## License

Apache-2.0. See [LICENSE](LICENSE).
