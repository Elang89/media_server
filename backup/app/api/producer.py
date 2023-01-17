from thespian.actors import ActorTypeDispatcher
from loguru import logger

from app.api.watcher import Watcher


class ActorProducer(ActorTypeDispatcher):

    def receiveMessage(self, message, sender: ActorTypeDispatcher):
        if isinstance(message, Watcher):
            self._watcher = message.watcher
            self._watcher.run()