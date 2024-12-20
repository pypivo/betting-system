from src.db.managers.manager import DBManager


class BaseBLManager:
    def __init__(self, db_manager: DBManager) -> None:
        self._db_manager = db_manager
