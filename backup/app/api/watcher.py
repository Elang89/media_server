import os
import time

from loguru import logger
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileCreatedEvent
from ffprobe import FFProbe
from app.aws.services.s3_service import S3Service
from app.db.repositories.backup_repository import BackupRepository

from app.models.backup import Backup

class Watcher(object):

    def __init__(
        self, path: str, 
        backup_repo: BackupRepository, 
        s3_service: S3Service, 
        actor_wait_time: float
    ) -> None:
        
        self._observer: Observer = Observer()
        self._path = path
        self._backup_repo = backup_repo
        self._s3_service = s3_service
        self._actor_wait_time = actor_wait_time

    @property
    def path(self) -> str:
        return self._path


    def run(self):
        event_handler: Handler = Handler(self._backup_repo, self._s3_service)
        self._observer.schedule(event_handler, self._path, recursive=True)
        self._observer.start()

        try:
            while True:
                time.sleep(self._actor_wait_time)
                logger.info(f"Watcher will sleep for {self._actor_wait_time}s")
        finally:
            self._observer.stop()
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
        folder = file_path.split("/")[-2]

        object_file = os.path.basename(file_path)

        backup = Backup(
            stream_id="stream", 
            file_path=file_path,
            external_filepath=f"s3://amsvideo001/{folder}/{object_file}",
            major_brand=metadata["major_brand"],
            minor_version=metadata["minor_version"],
            compatible_brands=metadata["compatible_brands"],
            creation_time=metadata["creation_time"],
            duration=metadata["Duration"],
            start=metadata["start"],
            bitrate=metadata["bitrate"]
        )
        
        logger.info(f"Watcher-{self.__hash__} backing up data into S3...")
        self._s3_service.upload(file_path, folder, object_file)
        
        logger.info("{object_file} backed up into S3 bucket")
        
        logger.info(f"Watcher-{self.__hash__} inserting reference data to mongo db...")
        self._backup_repo.insert_one(backup)

        logger.info(f"Watcher-{self.__hash__} inserted data into mongo db")


