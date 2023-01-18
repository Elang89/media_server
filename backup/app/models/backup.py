from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class Backup(BaseModel):
    _id: UUID = Field(default_factory=uuid4)
    stream_id: str
    file_path: str
    external_filepath: str 
    major_brand: str
    minor_version: str
    compatible_brands: str
    creation_time: str
    duration: str
    start: str 
    bitrate: str

    