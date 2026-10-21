from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


def validate_authorization(target: Dict[str, Any]) -> bool:
    if not isinstance(target, dict):
        return False

    if target.get("authorized") is False:
        return False

    identifier = str(target.get("identifier", "")).strip()
    owner = str(target.get("owner", "")).strip()
    if not identifier or not owner:
        return False

    auth_file = target.get("authorization_file")
    if auth_file:
        path = Path(auth_file)
        if not path.exists():
            return False

    return True


def ensure_authorized_target(target: Dict[str, Any]) -> Dict[str, Any]:
    if not validate_authorization(target):
        raise ValueError("Authorization validation failed. Target must be explicitly authorized.")
    return target
