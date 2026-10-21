from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


class BlueToolkit:
    """Minimal BlueToolkit integration wrapper."""

    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def check(self) -> bool:
        return True

    def run(self, target: str, capture_path: Path) -> str:
        return f"BlueToolkit would run against {target} and save capture to {capture_path}"
