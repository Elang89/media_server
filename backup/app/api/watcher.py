import time

from loguru import logger
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher(object):

    def __init__(self, path: str):
        self._observer: Observer = Observer()
        self._path = path

    @property
    def path(self) -> str:
        return self._path


    def run(self):
        event_handler: Handler = Handler()
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

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        
        elif event.event_type == "created":
            logger.info("Something was created")
