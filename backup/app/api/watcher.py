import time

from loguru import logger
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileCreatedEvent
from pymongo.database import Database
from ffprobe import FFProbe
from app.aws.services.s3_service import S3Service
from app.db.repositories.backup_repository import BackupRepository

from app.models.backup import Backup
from app.utils.sync import run_in_thread

class Watcher(object):

    def __init__(self, path: str, backup_repo: BackupRepository, s3_service: S3Service):
        self._observer: Observer = Observer()
        self._path = path
        self._backup_repo = backup_repo
        self._s3_service = s3_service

    @property
    def path(self) -> str:
        return self._path


    def run(self):
        event_handler: Handler = Handler(self._backup_repo, self._s3_service)
        self._observer.schedule(event_handler, self._path, recursive=True)
        self._observer.start()

        try:
            while True:
                time.sleep(2.5)
        except:
            self._observer.stop()
            logger.error("Error")
        
        self._observer.join()

class Handler(FileSystemEventHandler):

    def __init__(self, backup_repo: BackupRepository, s3_service: S3Service) -> None:
        super().__init__()
        self._backup_repo = backup_repo
        self._s3_service = s3_service

    def on_created(self, event: FileCreatedEvent):
        if event.is_directory:
            return None
        
        file_path = event.src_path
        logger.info(f"File created at {file_path}")

        metadata = FFProbe(file_path)
        metadata = metadata.metadata

        backup = Backup(
            stream_id="stream", 
            file_path=file_path,
            external_filepath=f"s3://amsvideo001/{file_path}",
            major_brand=metadata["major_brand"],
            minor_version=metadata["minor_version"],
            compatible_brands=metadata["compatible_brands"],
            creation_time=metadata["creation_time"],
            duration=metadata["Duration"],
            start=metadata["start"],
            bitrate=metadata["bitrate"]
        )
        
        self._s3_service.upload(file_path)
        self._backup_repo.insert_one(backup)
        # await run_in_thread(collection.insert_one, backup.dict())

