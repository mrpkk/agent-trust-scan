# x402 `upto` settlement: seven checks before you trust the refund

`exact` is simple: the buyer signs for a known amount, the seller settles that amount.
`upto` is more useful for AI calls because output length is unknown — the buyer signs a
ceiling, the seller settles by actual usage and refunds the difference. That is also
where the trust moves.

These are the checks we run on an `upto` flow.

## 1. The ceiling is a real ceiling

- Is the maximum enforced on-chain or only in the server's database?
- Can a bug settle above the signed ceiling?
- Does the client show the ceiling before signing, in the same units as the final charge?

## 2. The meter is not the seller's private opinion

- Who counts tokens/units — the seller, the model provider, or an independent meter?
- Is the meter output signed and timestamped?
- Can the buyer request the raw usage record?
- What happens when the provider reports usage late or twice?

## 3. The refund path exists and is testable

- Is the unused amount refunded automatically, or only on request?
- Who pays the gas for the refund?
- What is the timeout? What if the refund transaction fails?
- Can the buyer see the refund tx hash?

## 4. A receipt is not a 200

- Does the response include the actual amount, asset, network, payee, and tx hash?
- Is the receipt signed by the seller?
- Can the buyer verify it independently against the chain?
- Is the receipt bound to the request (nonce/resource), or replayable?

## 5. Authorization is single-use

- Is the EIP-3009/EIP-712 authorization bound to a nonce and a validity window?
- Can a spent authorization be replayed with a different resource?
- Is the domain separator checked against the token contract, not a string in config?

## 6. The asset/network allowlist is enforced

- USDC on Base and USDC on another chain are not the same asset.
- A testnet USDC is not money.
- A fake token with the same symbol is not USDC.
- Is the payee address allowlisted per engagement?

## 7. Failure is a state, not a silence

- What does the buyer see when settlement times out?
- Is there an idempotency key?
- Can the seller retry without double-charging?
- Is there an append-only record of authorization → usage → settlement → refund?

---

If you run an `upto` endpoint and cannot answer one of these, that is the next fix.

**Free 10-point scan:** https://github.com/mrpkk/agent-trust-scan/issues/new?template=scan-request.yml  
**Paid review:** $2,500 — threat model, live tests, payment flow, report, retest.  
**Rule:** no custody; you keep the keys.
