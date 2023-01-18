from pymongo.collection import Collection


class BaseRepository:
    def __init__(self, collection: Collection) -> None:
        self._collection = collection

    def _add_sorting(self) -> None:
        raise NotImplemented

    def _add_filters(self) -> None: 
        raise NotImplemented