from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models.backup import BackupResponse, BackupListResponse
from app.resources.backup_constants import TAG_BACKUPS


router = APIRouter()

@router.get(
    "/{id}",
    name="backup:get-backup",
    tags=[TAG_BACKUPS],
    response_class=JSONResponse,
    response_model=BackupResponse
)
async def get_backup(id: str) -> BackupResponse:
    pass

@router.get(
    "",
    name="backup:get-backups",
    tags=[TAG_BACKUPS],
    response_class=JSONResponse,
    response_model=BackupListResponse
)
async def get_backups() -> BackupListResponse:
    pass