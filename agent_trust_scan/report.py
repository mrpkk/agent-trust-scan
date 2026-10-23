"""Report rendering for agent-trust-scan."""

from __future__ import annotations

import json

from .scanner import ScanResult


def _cell(value: str) -> str:
    return " ".join(str(value).split()).replace("|", "\\|")[:160]


def render_markdown(result: ScanResult) -> str:
    counts = result.counts
    lines = [
        "# Agent Trust Scan",
        "",
        f"**Target:** `{result.target}`  ",
        f"**Score:** **{result.score}/100** — **{result.verdict.upper()}**  ",
        f"**Files scanned:** {result.files_scanned} (skipped: {result.files_skipped})  ",
        f"**Findings:** {counts.get('critical', 0)} critical · {counts.get('high', 0)} high · "
        f"{counts.get('medium', 0)} medium · {counts.get('low', 0)} low",
        "",
    ]
    if not result.findings:
        lines += [
            "No findings from the static rules. This is not a clean bill of health: "
            "the scan does not execute code, test prompts, or review business logic.",
            "",
        ]
    else:
        lines += [
            "## Findings",
            "",
            "| Severity | Rule | Location | Evidence |",
            "|---|---|---|---|",
        ]
        for finding in result.findings:
            lines.append(
                f"| {finding.severity.upper()} | `{finding.rule_id}` | "
                f"`{finding.path}:{finding.line}` | {_cell(finding.evidence)} |"
            )
        lines += ["", "## Details", ""]
        for finding in result.findings:
            lines += [
                f"### [{finding.severity.upper()}] {finding.title}",
                "",
                f"- **Rule:** `{finding.rule_id}`",
                f"- **Location:** `{finding.path}:{finding.line}`",
                f"- **Evidence:** `{finding.evidence}`",
                f"- **Why it matters:** {finding.why}",
                f"- **Fix:** {finding.fix}",
                "",
            ]
    lines += [
        "## What this scan does not do",
        "",
        "- It does not execute the agent, call its tools, or test prompt injection live.",
        "- It does not prove exploitability; it points a human at places worth reviewing.",
        "- It does not replace a smart-contract audit or a full threat model.",
        "- It does not read secrets out of a vault; it only flags values in files.",
        "",
        "## Limits of static evidence",
        "",
        "A missing keyword does not mean a control is absent: limits may live in a "
        "policy service, an environment variable, or a database. A present keyword "
        "does not mean the control works. Treat every finding as a question to verify.",
        "",
    ]
    return "\n".join(lines)


def render_json(result: ScanResult) -> str:
    return json.dumps(result.as_dict(), indent=2, ensure_ascii=False)
