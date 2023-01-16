import os

from loguru import logger

from boto3.resources.base import ServiceResource

class S3Service(object):

    def __init__(self, client: ServiceResource):
        self._client = client

    def upload(self, file_name: str) -> None:
        try:
            folder = file_name.split("/")[-2]

            object_file = os.path.basename(file_name)
            self._client.upload_file(file_name, "amsvideo001", f"{folder}/{object_file}")
        except Exception as e: 
            logger.error(e)

