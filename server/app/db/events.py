
from loguru import logger

from app.core.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

async def connect_to_db(app: FastAPI) -> None:
    logger.info(
        """
        Establishing connection to database {0} with user {1} on host and port {2}:{3}
        """,
        repr(DB_NAME),

    )