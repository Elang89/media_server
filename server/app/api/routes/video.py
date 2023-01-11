from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models.video_stream import VideoStreamRequest, VideoStreamResponse
from app.resources.video_constants import TAG_VIDEO


router = APIRouter()

@router.post(
    "",
    name="stream:create-stream",
    tags=[TAG_VIDEO],
    response_class=JSONResponse,
    response_model=VideoStreamResponse
)
async def create_stream(stream_request: VideoStreamRequest) -> VideoStreamResponse:
    # response = VideoStreamResponse(video_stream=stream_request.video_stream)

    return stream_request