from typing import List, Optional
from fastapi import APIRouter, Depends, Body, Query, HTTPException
from fastapi.responses import JSONResponse

from app.models.backup import BackupResponse, BackupListResponse
from app.resources.backup_constants import (
    TAG_BACKUP, 
    QUERY_BACKUP_SORT_REGEX, 
    QUERY_BACKUP_FILTER_REGEX,
    QUERY_BACKUP_DEFAULT_LIMIT,
    QUERY_BACKUP_DEFAULT_OFFSET,
)


router = APIRouter()

@router.get(
    "",
    name="backup:get-backups",
    tags=[TAG_BACKUP],
    response_class=JSONResponse,
    response_model=BackupListResponse
)
async def get_backups(
    limit: int = Query(
        QUERY_BACKUP_DEFAULT_LIMIT,
        alias="limit",
        description="Backups per page"
    ),
    offset: int = Query(
        QUERY_BACKUP_DEFAULT_OFFSET,
        alias="offset",
        description="Pagination offset"
    ),
    sort: Optional[List[str]] = Query(
        None,
        alias="sort",
        description="Sorting for collection",
        regex=QUERY_BACKUP_SORT_REGEX
    ),
    filters: Optional[List[str]]  = Query(
        None,
        alias="filters",
        description="Filters for collection",
        regex=QUERY_BACKUP_FILTER_REGEX
    )
) -> BackupListResponse:
    raise NotImplementedError

@router.get(
    "\{id}",
    name="backup:get-one-backup",
    tags=[TAG_BACKUP],
    response_class=JSONResponse,
    response_model=BackupResponse
)
async def get_one_backup(id: str) -> BackupResponse:
    raise NotImplementedError