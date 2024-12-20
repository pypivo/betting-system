from src.bl.managers.event_bl_manager import EventBlManager
from src.bl.managers.bet_bl_manager import BetBlManager
from src.db.managers.manager import DBManager


class BLManager:
    def __init__(self, db_manager: DBManager) -> None:
        self._event_bl_manager = EventBlManager(db_manager=db_manager)
        self._bet_bl_manager = BetBlManager(db_manager=db_manager)

    @property
    def event_bl_manager(self) -> EventBlManager:
        return self._event_bl_manager

    @property
    def bet_bl_manager(self) -> BetBlManager:
        return self._bet_bl_manager
