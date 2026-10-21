#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Dict

import yaml

from modules.capture import run_capture
from modules.report import write_report
from utils.deps import check_tools
from utils.legal import validate_authorization
from utils.logging import configure_logger


def load_config(path: str) -> Dict[str, Any]:
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    with config_path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    return data


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Auren Recon")
    parser.add_argument("--config", default="config.yaml", help="Path to config.yaml")
    parser.add_argument("--target", help="Optional target identifier override")
    parser.add_argument("--demo", action="store_true", help="Run a demonstration capture without external tooling")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    logger = configure_logger()

    try:
        config = load_config(args.config)
    except FileNotFoundError as exc:
        logger.error(str(exc))
        return 1
    except yaml.YAMLError as exc:
        logger.error(f"Invalid YAML in configuration: {exc}")
        return 1

    target = config.get("authorized_target", {})
    if args.target:
        target["identifier"] = args.target

    if not validate_authorization(target):
        logger.error("Authorization validation failed. This workflow must only run against explicitly authorized targets.")
        return 2

    required_tools = config.get("tools", {}).get("required", [])
    missing_tools = check_tools(required_tools, allow_missing=args.demo)
    if missing_tools:
        logger.error("Missing required tools: %s", ", ".join(missing_tools))
        if not args.demo:
            return 3

    capture_config = config.get("capture", {})
    output_dir = Path(capture_config.get("output_dir", "./sessions"))
    output_dir.mkdir(parents=True, exist_ok=True)

    capture_path = run_capture(capture_config, demo=args.demo)
    report_path = write_report(config, capture_path)

    logger.info("Capture saved to: %s", capture_path)
    logger.info("Report saved to: %s", report_path)
    print(f"\nAuren Recon completed successfully.")
    print(f"Capture: {capture_path}")
    print(f"Report: {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
