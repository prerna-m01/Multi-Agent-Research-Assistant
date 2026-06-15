import logging
from logging.handlers import RotatingFileHandler
import os

os.makedirs(
    "logs",
    exist_ok=True
)

log_file = "logs/app.log"

handler = RotatingFileHandler(
    log_file,
    maxBytes=5 * 1024 * 1024,
    backupCount=5
)

logging.basicConfig(
    handlers=[handler],
    level=logging.INFO,
    format=(
        "%(asctime)s - "
        "%(levelname)s - "
        "%(name)s - "
        "%(message)s"
    )
)

logger = logging.getLogger(
    "research_assistant"
)