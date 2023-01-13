import uuid
from pydantic import BaseModel, Field

class Backup(BaseModel):
    id: uuid = Field(default_factoru=uuid.uuid4)
    stream_id: str
    file_path: str
    size: int
    