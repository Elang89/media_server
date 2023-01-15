import uuid
from pydantic import BaseModel, Field

class Backup(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
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

    