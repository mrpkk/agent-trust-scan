# A $174k prompt injection is a payment-control failure, not a model failure

> Public reports in 2026 described an attacker using a prompt injection against an
> agent-linked wallet to move roughly $174,000 of tokens. The exact details differ by
> report; the pattern is what matters: the model was convinced to sign, and there was
> no control strong enough to stop it.

An agent with a wallet is a new kind of principal. It reads untrusted text, calls
tools, and can move money. If the only thing between a tool response and a transfer
is the model's judgment, then a sentence in a web page, an MCP response, or a token
description is a transaction primitive.

Five controls would have changed the outcome. None of them is a better prompt.

## 1. Treat tool output as data, never as instructions

Every artifact that enters the context should be checked for hidden instructions,
schema drift, empty content, and provenance before the model sees it.

- strip or flag "ignore previous instructions" patterns;
- keep the artifact in a quoted data block;
- verify the schema and the source;
- refuse to act on an artifact that changed after verification.

This is what `attest` does in our stack: form/emptiness, generation conditions,
signature, and authority. It is a gate, not a suggestion in the system prompt.

## 2. Put limits outside the model

A spend limit in a prompt is a preference. A spend limit in the signing path is a
control.

- per-transaction cap;
- daily cap;
- velocity limit;
- asset and network allowlist;
- gas cap and slippage cap;
- a deny-by-default policy with an explicit allow path.

The model can request; the policy engine decides. In KARTA, the Dharma engine checks
15 rules in both execution paths, and `drift` checks the mandate continuously — not
only at signature time.

## 3. Allowlist the recipient, asset, and network

A prompt injection usually needs a new destination. If the destination is not on the
allowlist, the transfer never leaves.

- payee allowlist per agent;
- asset allowlist (USDC on Base, not an arbitrary token);
- network allowlist (mainnet vs testnet is a money boundary, not a config detail);
- reject `type(uint256).max` approvals;
- approve exact amounts with a short expiry.

## 4. Require a human for the tail

Autonomy is fine for small, reversible actions. High-value transfers need a human
approval with a timeout, and the approval must show the amount, recipient, and reason.

- simulate the transaction before signing;
- show the diff, not a summary written by the model;
- require approval above a threshold;
- default to deny when the policy is uncertain;
- log who approved, when, and why.

## 5. Verify the receipt, and have a kill switch

A 200 response is not a payment. A screenshot is not a settlement.

- require a transaction hash;
- verify amount, asset, network, and payee;
- reject replay;
- write an append-only audit record;
- test the kill switch in a drill, not in an incident.

## A 10-point check you can run today

1. Where is the private key, and who can read it?
2. What is the per-transaction limit? The daily limit?
3. What happens when a tool returns "ignore previous instructions"?
4. Is the tool output schema-checked before the model sees it?
5. Can a high-value transfer happen without a human?
6. Does the kill switch stop the signer, or only the chat?
7. Is there an append-only log with the policy verdict?
8. Does the x402 flow check the receipt, payee, asset, network, and replay?
9. Which MCP servers and packages can change the agent's behavior?
10. What is the incident plan: revoke, rotate, recover?

If you cannot answer one of these, that is the next fix.

---

**Free scan:** open a [scan request](https://github.com/mrpkk/agent-trust-scan/issues/new?template=scan-request.yml).  
**Paid review:** $2,500 for a threat model, live prompt-injection tests, payment-flow review, report and retest.  
**Rule:** no custody, no payment processing for third parties; you keep the keys.
