# Field notes: three public x402/agent repos

We ran `agent-trust-scan` against three public repositories in the x402/agent-payment
space (tests and vendor directories excluded, no names published). This is a small,
non-random sample; it is not a benchmark.

## What showed up

| Signal | Repos | Notes |
|---|---|---|
| No visible kill switch or human approval in payment files | 2 / 3 | Could live outside the scanned file; needs manual verification |
| x402 testnet / network ambiguity | 1 / 3 | A testnet reference is not a bug by itself; it is a release risk |
| No receipt / tx-hash check in the wallet provider | 1 / 3 | The provider may verify elsewhere; the scan cannot see it |
| Critical secret in tracked code | 0 / 3 | Tests were excluded; a real leak in tests would still matter |
| False positives from `RegExp.exec` | yes | Fixed in v0.1.1: only `child_process` is flagged in JS/TS |

## What this means

- Most projects do not expose a single obvious "drain" in the file names; the risk is
  in the path between tool output, the signer, and the receipt.
- A static scan is good at finding **missing control surfaces**: no approval, no
  kill switch, no receipt check, testnet in production config.
- A paid review has to read the actual call path and test the prompt injection. The
  scanner is the first 30 minutes, not the audit.

## Method

- `agent-trust-scan scan <repo> --exclude tests --exclude node_modules --fail-on none`
- One human read of each finding; no live testing; no exploitation.
- No repository names or customer data are stored in this note.
