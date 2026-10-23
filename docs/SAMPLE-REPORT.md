> Demo report against `examples/vulnerable-agent`. All values are fake. The scanner redacts secrets; the target path is local.

# Agent Trust Scan

**Target:** `/media/Sruti/iamthat/work/sales/agent-trust/examples/vulnerable-agent`  
**Score:** **3/100** — **CRITICAL**  
**Files scanned:** 3 (skipped: 0)  
**Findings:** 1 critical · 2 high · 6 medium · 0 low

## Findings

| Severity | Rule | Location | Evidence |
|---|---|---|---|
| CRITICAL | `secret.private_key` | `config.py:2` | PRIVATE_KEY = "0x<redacted-hex> |
| HIGH | `wallet.unlimited_approve` | `agent.py:8` | type(uint256).max |
| HIGH | `tool_output.execution` | `agent.py:10` | eval( |
| MEDIUM | `agent.no_human_approval` | `agent.py:1` | payment code without human_approval/require_approval |
| MEDIUM | `agent.no_kill_switch` | `agent.py:1` | payment code without kill_switch/pause/emergency_stop |
| MEDIUM | `agent.no_spend_limit` | `agent.py:1` | payment code without spend_limit/daily_limit/max_amount |
| MEDIUM | `x402.disabled` | `config.py:3` | X402_ENABLED = 0 |
| MEDIUM | `x402.testnet` | `config.py:4` | X402_NETWORK = "eip155:84532" |
| MEDIUM | `x402.price_below_floor` | `config.py:5` | X402_PRICE = 0.001 |

## Details

### [CRITICAL] Private key or seed phrase in a file

- **Rule:** `secret.private_key`
- **Location:** `config.py:2`
- **Evidence:** `PRIVATE_KEY = "0x<redacted-hex>`
- **Why it matters:** Anyone with this value can move funds. A key in a repo, config or prompt is compromised.
- **Fix:** Move the key to a secret manager, rotate it, and remove it from git history.

### [HIGH] Unlimited token approval

- **Rule:** `wallet.unlimited_approve`
- **Location:** `agent.py:8`
- **Evidence:** `type(uint256).max`
- **Why it matters:** An unlimited approval lets a compromised spender drain the whole balance.
- **Fix:** Approve the exact amount, or use a scoped allowance with a short expiry.

### [HIGH] eval() on data that may come from a tool or model

- **Rule:** `tool_output.execution`
- **Location:** `agent.py:10`
- **Evidence:** `eval(`
- **Why it matters:** Tool output is untrusted input. Turning it into code or a shell command is a direct path to compromise.
- **Fix:** Parse data as data, use an allowlist, and never pass model/tool output to eval/exec/shell.

### [MEDIUM] Payment code has no visible human approval

- **Rule:** `agent.no_human_approval`
- **Location:** `agent.py:1`
- **Evidence:** `payment code without human_approval/require_approval`
- **Why it matters:** High-value actions should require a human, not only a model's confidence.
- **Fix:** Route high-value transfers to an approval queue with a clear timeout.

### [MEDIUM] Payment code has no visible kill switch

- **Rule:** `agent.no_kill_switch`
- **Location:** `agent.py:1`
- **Evidence:** `payment code without kill_switch/pause/emergency_stop`
- **Why it matters:** When an agent goes wrong, you need one action that stops it, not a prompt edit.
- **Fix:** Add a terminal kill switch and test it in a drill.

### [MEDIUM] Payment code has no visible spend limit

- **Rule:** `agent.no_spend_limit`
- **Location:** `agent.py:1`
- **Evidence:** `payment code without spend_limit/daily_limit/max_amount`
- **Why it matters:** An agent with a wallet and no per-tx/daily cap can lose the whole balance in one call.
- **Fix:** Add per-transaction and daily limits, an allowlist, and a hard cap enforced outside the prompt.

### [MEDIUM] x402 payments are disabled

- **Rule:** `x402.disabled`
- **Location:** `config.py:3`
- **Evidence:** `X402_ENABLED = 0`
- **Why it matters:** The code may be present, but the rail is off; no payment can settle.
- **Fix:** Enable only after a public HTTPS endpoint and a mainnet facilitator are tested.

### [MEDIUM] x402 is configured for a testnet

- **Rule:** `x402.testnet`
- **Location:** `config.py:4`
- **Evidence:** `X402_NETWORK = "eip155:84532"`
- **Why it matters:** Testnet money is not money. A production buyer cannot settle here.
- **Fix:** Use eip155:8453 (Base mainnet) and a mainnet facilitator before selling.

### [MEDIUM] x402 price is below the rail cost

- **Rule:** `x402.price_below_floor`
- **Location:** `config.py:5`
- **Evidence:** `X402_PRICE = 0.001`
- **Why it matters:** Base gas is about $0.00146 per transfer. Below $0.002 the rail eats the margin.
- **Fix:** Raise the price or batch calls; measure cost before publishing a price.

## What this scan does not do

- It does not execute the agent, call its tools, or test prompt injection live.
- It does not prove exploitability; it points a human at places worth reviewing.
- It does not replace a smart-contract audit or a full threat model.
- It does not read secrets out of a vault; it only flags values in files.

## Limits of static evidence

A missing keyword does not mean a control is absent: limits may live in a policy service, an environment variable, or a database. A present keyword does not mean the control works. Treat every finding as a question to verify.

