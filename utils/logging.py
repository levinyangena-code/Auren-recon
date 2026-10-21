from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


def validate_authorization(target: Dict[str, Any]) -> bool:
    if not isinstance(target, dict):
        return False

    if target.get("authorized") is False:
        return False

    if not target.get("identifier"):
        return False

    auth_file = target.get("authorization_file")
    if auth_file:
        path = Path(auth_file)
        if not path.exists():
            return False

    return True
