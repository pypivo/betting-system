from src.db.managers.manager import DBManager
from src.rpc.manager import RpcManager


class BaseBLManager:
    def __init__(self, db_manager: DBManager, rpc_manager: RpcManager) -> None:
        self._db_manager = db_manager
        self._rpc_manager = rpc_manager
