from httpx import AsyncClient

from app.models.video_stream import VideoStream


class VideoStreamService: 

    def __init__(self, client: AsyncClient):
        self.client = client

    def create_stream(stream: VideoStream):
        pass

    