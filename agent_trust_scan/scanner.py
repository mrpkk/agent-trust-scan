"""Filesystem scanner for agent-trust-scan."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from .rules import RULES, SEVERITY_ORDER, Finding

DEFAULT_EXCLUDES = {
    ".git", "node_modules", ".venv", "venv", "dist", "build",
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    ".next", "coverage", "htmlcov",
}

MAX_FILE_BYTES = 1_000_000
BINARY_SAMPLE = 8192


@dataclass
class ScanResult:
    target: str
    findings: list[Finding] = field(default_factory=list)
    files_scanned: int = 0
    files_skipped: int = 0

    @property
    def counts(self) -> dict[str, int]:
        result = {name: 0 for name in SEVERITY_ORDER}
        for finding in self.findings:
            result[finding.severity] = result.get(finding.severity, 0) + 1
        return result

    @property
    def score(self) -> int:
        weights = {"critical": 25, "high": 15, "medium": 7, "low": 2, "info": 0}
        score = 100
        for finding in self.findings:
            score -= weights.get(finding.severity, 0)
        return max(0, score)

    @property
    def verdict(self) -> str:
        for level in ("critical", "high", "medium", "low"):
            if self.counts.get(level, 0):
                return level
        return "pass"

    def as_dict(self) -> dict:
        return {
            "target": self.target,
            "score": self.score,
            "verdict": self.verdict,
            "counts": self.counts,
            "files_scanned": self.files_scanned,
            "files_skipped": self.files_skipped,
            "findings": [f.as_dict() for f in self.findings],
        }


def _is_binary(data: bytes) -> bool:
    sample = data[:BINARY_SAMPLE]
    return b"\x00" in sample


def _read_text(path: Path) -> str | None:
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            return None
        data = path.read_bytes()
    except OSError:
        return None
    if _is_binary(data):
        return None
    return data.decode("utf-8", errors="replace")


def _iter_files(root: Path, excludes: set[str]):
    if root.is_file():
        yield root
        return
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in excludes]
        for name in filenames:
            if name in excludes:
                continue
            yield Path(dirpath) / name


def _dedupe(findings: list[Finding]) -> list[Finding]:
    seen = set()
    unique = []
    for finding in findings:
        key = (finding.rule_id, finding.path, finding.line, finding.evidence)
        if key in seen:
            continue
        seen.add(key)
        unique.append(finding)
    return unique


def scan_text(text: str, rel: str = "<memory>") -> list[Finding]:
    findings: list[Finding] = []
    for rule in RULES:
        findings.extend(rule(rel, text))
    return _dedupe(findings)


def scan_path(path: str | Path, excludes: set[str] | None = None) -> ScanResult:
    root = Path(path).expanduser().resolve()
    if not root.exists():
        raise FileNotFoundError(f"path does not exist: {root}")
    excluded = set(DEFAULT_EXCLUDES)
    if excludes:
        excluded |= set(excludes)
    result = ScanResult(target=str(root))
    files: list[Path] = []
    findings: list[Finding] = []
    for file_path in _iter_files(root, excluded):
        files.append(file_path)
        text = _read_text(file_path)
        if text is None:
            result.files_skipped += 1
            continue
        try:
            rel = str(file_path.relative_to(root)) if root.is_dir() else file_path.name
        except ValueError:
            rel = file_path.name
        result.files_scanned += 1
        for rule in RULES:
            findings.extend(rule(rel, text))
    result.findings = sorted(
        _dedupe(findings),
        key=lambda f: (-SEVERITY_ORDER.get(f.severity, 0), f.path, f.line, f.rule_id),
    )
    return result


def threshold_reached(result: ScanResult, fail_on: str) -> bool:
    if fail_on == "none":
        return False
    minimum = SEVERITY_ORDER.get(fail_on, 3)
    return any(SEVERITY_ORDER.get(f.severity, 0) >= minimum for f in result.findings)
