from __future__ import annotations

import shutil
from typing import Iterable, List


def check_tools(required_tools: Iterable[str], allow_missing: bool = False) -> List[str]:
    missing: List[str] = []
    for tool in required_tools:
        if shutil.which(tool) is None:
            missing.append(tool)
    if allow_missing and missing:
        return []
    return missing
