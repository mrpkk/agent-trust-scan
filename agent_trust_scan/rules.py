"""Rules for agent-trust-scan.

Every rule is a small, explainable check. The scanner never executes code and
never sends data over the network. Findings are heuristics: they point a human
at a place worth reviewing, they do not prove exploitability.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

SEVERITY_ORDER = {"critical": 4, "high": 3, "medium": 2, "low": 1, "info": 0}

CODE_EXTS = {
    ".py", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
    ".sol", ".go", ".rs", ".java", ".kt", ".sh",
}

PAYMENT_MARKERS = (
    "send_transaction", "sendtransaction", "send_raw_transaction",
    "transfer(", "approve(", "wallet.", "payto", "pay_to",
    "transferwithauthorization", "eth_sendtransaction",
)

LIMIT_MARKERS = (
    "spend_limit", "spendlimit", "daily_limit", "dailylimit",
    "max_amount", "maxamount", "per_tx", "pertx", "max_value", "maxvalue",
    "allowance", "tx_limit", "transaction_limit", "limit",
)

KILL_MARKERS = (
    "kill_switch", "killswitch", "emergency_stop", "emergencystop",
    "circuit_breaker", "circuitbreaker", "pause(", "paused",
)

APPROVAL_MARKERS = (
    "human_approval", "humanapproval", "require_approval", "requireapproval",
    "pending_approval", "pendingapproval", "ask_human", "askhuman",
)

AUDIT_MARKERS = (
    "audit", "sakshi", "receipt", "ledger", "append_only", "appendonly",
)

RECEIPT_MARKERS = (
    "receipt", "tx_hash", "txhash", "transaction_hash", "transactionhash",
    "settle", "verify_payment", "verifypayment",
)


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    title: str
    path: str
    line: int
    evidence: str
    why: str
    fix: str

    def as_dict(self) -> dict:
        return {
            "rule_id": self.rule_id,
            "severity": self.severity,
            "title": self.title,
            "path": self.path,
            "line": self.line,
            "evidence": self.evidence,
            "why": self.why,
            "fix": self.fix,
        }


def is_code(rel: str) -> bool:
    return Path(rel).suffix.lower() in CODE_EXTS


def _line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def _line_at(text: str, pos: int) -> str:
    start = text.rfind("\n", 0, pos) + 1
    end = text.find("\n", pos)
    if end < 0:
        end = len(text)
    return text[start:end]


def _redact(value: str) -> str:
    value = re.sub(r"0x[a-fA-F0-9]{16,}", "0x<redacted-hex>", value)
    value = re.sub(r"\b[a-fA-F0-9]{16,}\b", "<redacted-hex>", value)
    value = re.sub(r"\b(sk-[A-Za-z0-9]{12,}|ghp_[A-Za-z0-9]{12,}|github_pat_[A-Za-z0-9_]{12,}|xox[baprs]-[A-Za-z0-9-]{8,}|AKIA[0-9A-Z]{8,}|hf_[A-Za-z0-9]{12,}|AIza[0-9A-Za-z_-]{12,})", "<redacted-api-key>", value)
    return " ".join(value.split())[:240]


def _finding(rule_id: str, severity: str, title: str, rel: str, text: str,
             pos: int, evidence: str, why: str, fix: str) -> Finding:
    return Finding(rule_id, severity, title, rel, _line_of(text, pos),
                   _redact(evidence), why, fix)


def rule_private_key(rel: str, text: str):
    assign = re.compile(
        r"(?i)\b(private[_-]?key|secret[_-]?key|mnemonic|seed[_-]?phrase)\b"
        r"\s*[:=]\s*[\"']?(0x[a-fA-F0-9]{64}|[a-fA-F0-9]{64})"
    )
    for m in assign.finditer(text):
        yield _finding(
            "secret.private_key", "critical", "Private key or seed phrase in a file",
            rel, text, m.start(), m.group(0),
            "Anyone with this value can move funds. A key in a repo, config or prompt is compromised.",
            "Move the key to a secret manager, rotate it, and remove it from git history.",
        )
    pem = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
    for m in pem.finditer(text):
        yield _finding(
            "secret.private_key", "critical", "Private key block in a file",
            rel, text, m.start(), "-----BEGIN PRIVATE KEY-----",
            "A committed private key must be treated as stolen.",
            "Rotate the key, remove the block, and purge git history.",
        )


def rule_api_key(rel: str, text: str):
    pattern = re.compile(
        r"\b(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
        r"xox[baprs]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|hf_[A-Za-z0-9]{20,}|"
        r"AIza[0-9A-Za-z_-]{20,})\b"
    )
    for m in pattern.finditer(text):
        yield _finding(
            "secret.api_key", "critical", "API key or token in a file",
            rel, text, m.start(), m.group(0),
            "A leaked key can spend your credits, read private data, or act as the agent.",
            "Rotate the token and load it from an environment variable or secret manager.",
        )


def rule_dotenv(rel: str, text: str):
    name = Path(rel).name
    if name == ".env" or (name.startswith(".env.") and name != ".env.example"):
        yield Finding(
            "secret.dotenv", "high", ".env file is inside the scanned tree",
            rel, 1, "<redacted .env>",
            "A .env file often contains keys and is easy to commit by accident.",
            "Add .env to .gitignore, keep only .env.example, and rotate anything real.",
        )


def rule_unlimited_approve(rel: str, text: str):
    pattern = re.compile(
        r"(?i)(type\s*\(\s*uint256\s*\)\s*\.\s*max|2\s*\*\*\s*256\s*-\s*1|"
        r"maxUint256|MAX_UINT(?:256)?|approve\s*\([^)]{0,140}(?:max|2\s*\*\*\s*256))"
    )
    for m in pattern.finditer(text):
        yield _finding(
            "wallet.unlimited_approve", "high", "Unlimited token approval",
            rel, text, m.start(), m.group(0),
            "An unlimited approval lets a compromised spender drain the whole balance.",
            "Approve the exact amount, or use a scoped allowance with a short expiry.",
        )


def rule_x402_testnet(rel: str, text: str):
    low = text.lower()
    if "x402" not in low:
        return
    for marker in ("eip155:84532", "base-sepolia", "base_sepolia", "sepolia"):
        idx = low.find(marker)
        if idx >= 0:
            yield _finding(
                "x402.testnet", "medium", "x402 is configured for a testnet",
                rel, text, idx, _line_at(text, idx),
                "Testnet money is not money. A production buyer cannot settle here.",
                "Use eip155:8453 (Base mainnet) and a mainnet facilitator before selling.",
            )
            return


def rule_x402_disabled(rel: str, text: str):
    pattern = re.compile(r"(?i)(X402_ENABLED\s*=\s*0|x402_enabled\s*[:=]\s*false)")
    for m in pattern.finditer(text):
        yield _finding(
            "x402.disabled", "medium", "x402 payments are disabled",
            rel, text, m.start(), m.group(0),
            "The code may be present, but the rail is off; no payment can settle.",
            "Enable only after a public HTTPS endpoint and a mainnet facilitator are tested.",
        )


def rule_x402_price(rel: str, text: str):
    if "x402" not in text.lower():
        return
    pattern = re.compile(r"(?i)(?:X402_PRICE|price_usd)\s*[:=]\s*[\"']?\$?([0-9]+(?:\.[0-9]+)?)")
    for m in pattern.finditer(text):
        try:
            price = float(m.group(1))
        except ValueError:
            continue
        if price < 0.002:
            yield _finding(
                "x402.price_below_floor", "medium", "x402 price is below the rail cost",
                rel, text, m.start(), m.group(0),
                "Base gas is about $0.00146 per transfer. Below $0.002 the rail eats the margin.",
                "Raise the price or batch calls; measure cost before publishing a price.",
            )


def _payment_code(rel: str, text: str) -> bool:
    if not is_code(rel):
        return False
    low = text.lower()
    return any(marker in low for marker in PAYMENT_MARKERS)


def rule_no_spend_limit(rel: str, text: str):
    if not _payment_code(rel, text):
        return
    low = text.lower()
    if not any(marker in low for marker in LIMIT_MARKERS):
        yield _finding(
            "agent.no_spend_limit", "medium", "Payment code has no visible spend limit",
            rel, text, 0, "payment code without spend_limit/daily_limit/max_amount",
            "An agent with a wallet and no per-tx/daily cap can lose the whole balance in one call.",
            "Add per-transaction and daily limits, an allowlist, and a hard cap enforced outside the prompt.",
        )


def rule_no_kill_switch(rel: str, text: str):
    if not _payment_code(rel, text):
        return
    low = text.lower()
    if not any(marker in low for marker in KILL_MARKERS):
        yield _finding(
            "agent.no_kill_switch", "medium", "Payment code has no visible kill switch",
            rel, text, 0, "payment code without kill_switch/pause/emergency_stop",
            "When an agent goes wrong, you need one action that stops it, not a prompt edit.",
            "Add a terminal kill switch and test it in a drill.",
        )


def rule_no_human_approval(rel: str, text: str):
    if not _payment_code(rel, text):
        return
    low = text.lower()
    if not any(marker in low for marker in APPROVAL_MARKERS):
        yield _finding(
            "agent.no_human_approval", "medium", "Payment code has no visible human approval",
            rel, text, 0, "payment code without human_approval/require_approval",
            "High-value actions should require a human, not only a model's confidence.",
            "Route high-value transfers to an approval queue with a clear timeout.",
        )


def rule_no_audit_log(rel: str, text: str):
    if not _payment_code(rel, text):
        return
    low = text.lower()
    if not any(marker in low for marker in AUDIT_MARKERS):
        yield _finding(
            "agent.no_audit_log", "low", "Payment code has no visible audit log",
            rel, text, 0, "payment code without audit/receipt/ledger",
            "Without a receipt you cannot prove who authorized what, or dispute a charge.",
            "Write an append-only record: action, amount, recipient, policy verdict, tx hash.",
        )


def rule_x402_no_receipt(rel: str, text: str):
    if not _payment_code(rel, text):
        return
    low = text.lower()
    if "x402" not in low:
        return
    if not any(marker in low for marker in RECEIPT_MARKERS):
        yield _finding(
            "x402.no_receipt_check", "medium", "x402 flow has no visible receipt check",
            rel, text, 0, "x402 code without receipt/tx_hash/settle",
            "A 200 response is not a payment. Without a tx hash, a replay or a fake receipt can pass.",
            "Verify amount, asset, network, payee and a transaction hash before serving.",
        )


def rule_code_execution(rel: str, text: str):
    if not is_code(rel):
        return
    checks = [
        (r"\beval\s*\(", "high", "eval() on data that may come from a tool or model"),
        (r"\bexec\s*\(", "high", "exec() on data that may come from a tool or model"),
        (r"pickle\.loads", "high", "pickle.loads on untrusted bytes"),
        (r"shell\s*=\s*True", "medium", "subprocess with shell=True"),
    ]
    for pattern, severity, title in checks:
        for m in re.finditer(pattern, text):
            yield _finding(
                "tool_output.execution", severity, title,
                rel, text, m.start(), m.group(0),
                "Tool output is untrusted input. Turning it into code or a shell command is a direct path to compromise.",
                "Parse data as data, use an allowlist, and never pass model/tool output to eval/exec/shell.",
            )


RULES = (
    rule_private_key,
    rule_api_key,
    rule_dotenv,
    rule_unlimited_approve,
    rule_x402_testnet,
    rule_x402_disabled,
    rule_x402_price,
    rule_no_spend_limit,
    rule_no_kill_switch,
    rule_no_human_approval,
    rule_no_audit_log,
    rule_x402_no_receipt,
    rule_code_execution,
)
