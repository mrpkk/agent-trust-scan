# Payment proxy checklist — 10 checks before an agent moves money

For a gateway, proxy, or wallet that enforces agent payments. The order is deliberate:
identity first, then authorization, then settlement, then evidence.

1. **Mandate per action, not per session.** A valid agent identity is not a payment
   authorization. Re-check the mandate for every charge: payee, amount, asset, network,
   purpose, expiry.
2. **Payee allowlist and cap at the proxy.** The agent may hold intent; the proxy holds
   the limit. A cap that exists only in a prompt is advisory once the context is
   attacker-controlled.
3. **Expiry, audience, and nonce.** Validate that the authorization was issued for this
   API/merchant, has not expired, and has not been used before. A token for one service
   must not settle at another.
4. **Idempotency key per purchase intent.** A network timeout must not become a second
   charge. Store the key and return the original result on retry.
5. **Failed and partial calls.** A failed call that was billed is a finding, not a
   rounding error. So is a charge above the quoted amount with no refund row.
6. **Receipt bound to the action.** The receipt should name the mandate, amount, asset,
   network, payee, tx hash, usage, and the artifact/action hash it paid for. A transfer
   log alone does not say what was bought.
7. **Human approval for the exceptions.** New payee, amount above cap, or a category
   outside the policy should pause for a human. Routine repeat calls inside policy can
   proceed with a notification and a kill switch.
8. **Kill switch that propagates.** One switch should stop new authorizations, cancel
   pending ones where possible, and leave the audit log intact.
9. **Evidence, not just logs.** Store the policy hash, the package/tools hash the agent
   saw, the mandate hash, and the settlement receipt. That is what lets someone
   reconstruct the decision after an incident.
10. **Reconciliation.** Match the proxy records to the provider invoice or on-chain
    settlement. Name what is closed, what nobody paid, and what arrived without an
    invoice. Duplicates count once.

## Where to enforce

Enforce at the **proxy or gateway** for anything that moves money. Agent-side checks are
useful for intent and explanation, but they are advisory once the model's context is
attacker-controlled. Defense in depth: the agent explains, the proxy enforces, the
receipt proves.

## What this is not

Not a statutory audit, not legal advice, not a guarantee that a payment is safe. It is a
control checklist and an evidence format. If a check cannot be answered from the records,
the honest answer is "not verified", not "probably fine".

Source: Nidhipati / Agent Trust. Free spend scan:
https://mrpkk.github.io/nidhipati/free-spend-audit.html
