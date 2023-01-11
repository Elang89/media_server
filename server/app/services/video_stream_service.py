from pprint import pprint
from typing import Union
from httpx import AsyncClient
from httpx import HTTPStatusError, TimeoutException, HTTPError
from loguru import logger
from starlette import status

from app.models.video_stream import VideoStream


class VideoStreamService: 

    def __init__(self, client: AsyncClient):
        self._client = client

    async def create_stream(self, stream: VideoStream) -> Union[VideoStream, None, HTTPError]:
        try: 
            response = await self._client.post("/broadcasts/create", json=stream.dict())

            if response.status_code == status.HTTP_400_BAD_REQUEST and response.headers["content-type"] == "application/json":
                return None

            return VideoStream(**response.json())

        except HTTPStatusError:
            logger.error(e)
            return e
        except TimeoutException as e:
            logger.error(e)
            return e

    