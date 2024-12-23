from typing import Protocol
from src.bl.managers.event_bl_manager import EventBlManager
from src.db.managers.manager import DBManager
from src.rpc.manager import RpcManager


class BLManager:
    def __init__(self, db_manager: DBManager, rpc_manager: RpcManager) -> None:
        self._event_bl_manager = EventBlManager(db_manager=db_manager, rpc_manager=rpc_manager)

    @property
    def event_bl_manager(self) -> EventBlManager:
        return self._event_bl_manager
