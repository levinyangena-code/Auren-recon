from __future__ import annotations

import logging


def configure_logger() -> logging.Logger:
    logger = logging.getLogger("auren_recon")
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(handler)
    return logger
