from loguru import logger
from multiprocessing import Process
from uuid import uuid4
from loguru import logger

from app.api.watcher import Watcher


class Producer(Process):

    def __init__(self, watcher: Watcher) -> None:
        self.id = uuid4()
        self._watcher = watcher
        super().__init__()

    @property
    def watcher(self) -> Watcher:
        return self._watcher

    def run(self) -> None:
        try: 
            self._watcher.run()
        except OSError as e: 
            logger.error(f"Producer-{self.id} error: {e}")