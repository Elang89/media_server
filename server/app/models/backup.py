from typing import List
from datetime import datetime

from pydantic import BaseModel

class Backup(BaseModel):
    id: str
    stream_id: str 
    file_path: str
    external_filepath: str
    major_brand: str
    compatible_brands: str
    creation_time: str
    duration: str
    start: str
    bitrate: str

class BackupRequest(BaseModel):
    pass

class BackupResponse(BaseModel):
    backup: Backup

class BackupListResponse(BaseModel):
    backups: List[Backup]