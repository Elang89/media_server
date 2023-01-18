from typing import Union
from pymongo.database import Database
from loguru import logger
from uuid import UUID

from app.db.repositories.base import BaseRepository
from app.models.backup import Backup
from app.utils.sync import run_in_thread

class BackupRepository(BaseRepository):

    def __init__(self, db: Database) -> None:
         self._db = db

    async def find_one_backup(self, id: str) -> Union[Backup, None]:
        import pdb

        pdb.set_trace()

        query = {"id": UUID(id)}
        backup = await run_in_thread(self._db.backups.find_one, query)

        if backup:
            return Backup(**backup.dict())

        return backup
        

    async def find_all(self) -> None: 
        pass