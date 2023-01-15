from pymongo.database import Collection
from loguru import logger

from app.models.backup import Backup
from app.utils.sync import run_in_thread

class BackupRepository(): 

    def __init__(self, collection: Collection):
        self._collection = collection

    async def insert_one(self, backup: Backup) -> Backup:
        try:
            await run_in_thread(self._collection.insert_one, backup.dict())
            return Backup
        except:
            logger.error("Error")
