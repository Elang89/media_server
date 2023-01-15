import os

from loguru import logger
from app.utils.sync import run_in_thread


class S3Service(object):

    def __init__(self, client, bucket):
        self._client = client
        self._bucket = bucket

    async def upload(self, file_name: str) -> None:
        try:
            object_file = os.path.basename(file_name)
            await run_in_thread(self._client.upload_file , file_name, self._bucket, object_file)
 
        except: 
            logger.error("S3 Error")

