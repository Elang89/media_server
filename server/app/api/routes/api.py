from fastapi import APIRouter

from app.api.routes import video
from app.resources.video_constants import TAG_VIDEO

router = APIRouter()

router.include_router(video.router, tags=[TAG_VIDEO], prefix="/stream")