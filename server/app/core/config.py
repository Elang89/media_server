import logging
import sys
from typing import Tuple

from loguru import logger
from starlette.config import Config

from app.core.logging import InterceptHandler

config = Config(".env")

# API Prefix
API_PREFIX: str  = config("API_PREFIX", default="/api/v1")

# API Version
VERSION: str = config("VERSION", default="1.0.0") 

# Application Settings
DEBUG: bool = config("DEBUG", cast=bool, default=False)
PROJECT_NAME: str = config("PROJECT_NAME", default="Media Server API")

# Database

DB_USER: str = config("DB_USER", default="root")
DB_PASSWORD: str = config("DB_PASSWORD", default="password")
DB_HOST: str = config("DB_HOST", default="localhost")
DB_PORT: str = config("DB_HOST", default="27017")
DB_NAME: str = config("DB_NAME", default="video_db")

# Logging Settings 

LOGGING_LEVEL: int = logging.DEBUG if DEBUG else logging.INFO
LOGGERS: Tuple[str, str] =  ("uvicorn.asgi", "uvicorn.acces")

logging.getLogger().handlers = [InterceptHandler()]

for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])