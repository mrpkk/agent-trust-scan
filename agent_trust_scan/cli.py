"""Command line interface for agent-trust-scan."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .report import render_json, render_markdown
from .scanner import scan_path, threshold_reached


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agent-trust-scan",
        description="Static security scan for AI agents with wallets.",
    )
    parser.add_argument("path", help="file or directory to scan")
    parser.add_argument("--format", choices=("md", "json"), default="md")
    parser.add_argument("--out", help="write report to this file instead of stdout")
    parser.add_argument(
        "--fail-on",
        choices=("none", "low", "medium", "high", "critical"),
        default="high",
        help="exit 1 when a finding at or above this severity exists (default: high)",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="extra directory or file name to skip (repeatable)",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = scan_path(args.path, excludes=set(args.exclude))
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    output = render_json(result) if args.format == "json" else render_markdown(result)
    if args.out:
        Path(args.out).expanduser().write_text(output + "\n", encoding="utf-8")
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        print(output)
    return 1 if threshold_reached(result, args.fail_on) else 0


if __name__ == "__main__":
    raise SystemExit(main())
