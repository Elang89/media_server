import pytest

from fastapi import FastAPI
from starlette import status
from httpx import AsyncClient

from app.models.video_stream import VideoStreamRequest, VideoStreamResponse

pytestmark = pytest.mark.asyncio

POST_STREAM_ROUTE = "stream:create-stream"

async def test_create_stream(
    app: FastAPI,
    client: AsyncClient,
    stream_request: VideoStreamRequest
) -> None:

    response = await client.post(
        app.url_path_for(POST_STREAM_ROUTE),
        json=stream_request.dict() 
    )

    assert response.status_code == status.HTTP_201_CREATED

    stream_response = VideoStreamResponse(**response.json())

    assert stream_response.video_stream.streamId == stream_request.video_stream.streamId
    assert stream_response.video_stream.name == stream_request.video_stream.name
    