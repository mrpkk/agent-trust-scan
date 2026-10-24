# Agent Spend Audit — find the money your agent wastes

AI agents now pay for models, tools, APIs, x402 calls and stablecoin services. The bill arrives, but the control doesn't. This audit looks at the payment path, not the dashboard.

## Why now

- Gartner: **$2.59 trillion** in AI spending in 2026.
- **98%** of FinOps teams track AI spend, but **73%** still blow the budget.
- Only **26%** see AI costs fully and in real time.
- Agentic commerce already has a named failure class: **overcharge, duplicate billing, structuring, warm-up fraud** (arXiv, 2026).

## Not another dashboard

AI FinOps and LLM observability tools show what you spent. They do not prove the charge was correct, and they do not recover the difference. This audit is independent of the router, the model vendor, and the payment processor. We get paid only when the finding is verified.

## Eight checks

1. **Duplicate calls** — retries without idempotency; the same request billed twice.
2. **Price escalation** — the quote says $0.01, the settlement says $0.04.
3. **Wrong asset / network / payee** — USDC on the wrong chain, a wrong recipient, a testnet in production.
4. **Failed calls still billed** — timeout or 500, but the charge settles.
5. **Runaway loops** — the agent retries itself into a budget hole.
6. **Refund / receipt mismatch** — the receipt says one amount, the wallet says another.
7. **Model routing overpay** — a frontier model used for a task a small model handles.
8. **Budget bypass** — a limit exists in the prompt, not in the signing path.

## What we need

- A read-only export: API usage CSV, invoice lines, x402 settlement log, or a public transaction list.
- No private keys, no seed phrases, no customer data.
- One written point of contact.

## What you get

- A written report: finding, evidence, estimated recoverable amount, fix.
- A before/after measurement plan so “savings” are proven, not claimed.
- Optional control retainer: budgets, alerts, receipt checks, monthly report.

## Pricing

| Service | Price |
|---|---|
| Free Agent Spend Scan (one flow, one week) | **0** |
| Audit | **$2,500** fixed, or **20% of verified savings** for 6 months |
| Control retainer | **$1,500/mo** |
| Security add-on (wallet/payment review) | **$2,500** |

No calls. Written scope and written report.

## Illustrative example (synthetic, not a client)

| Finding | Calls | Overpay |
|---|---|---|
| Duplicate retries | 4.2% | $1,260 |
| Price escalation | 1.8% | $840 |
| Failed-but-billed | 0.9% | $310 |
| Frontier model on simple tasks | 11% | $2,100 |
| **Total** | | **$4,510** |

This table is an example of the report format, not a claim about any real client.

## Honest limits

- We do not guarantee savings. If the data shows none, the report says so.
- “Recovered” means verified against the provider’s invoice/transaction, not a estimate.
- We do not custody funds, move money, or act as a payment processor.
- The report is technical, not legal, tax, or investment advice.

## Request

Open a spend scan request: https://github.com/mrpkk/agent-trust-scan/issues/new?template=spend-scan.yml

Do not paste keys or customer data.
