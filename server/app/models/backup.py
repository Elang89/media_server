from typing import List
from datetime import datetime

from pydantic import BaseModel

class Backup(BaseModel):
    id: str
    filepath: str
    created_at: datetime

class BackupRequest(BaseModel):
    pass

class BackupResponse(BaseModel):
    backup: Backup

class BackupListResponse(BaseModel):
    backups: List[Backup]