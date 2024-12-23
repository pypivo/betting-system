from src.bl.managers.manager import BLManager
from src.db.managers.manager import init_db_manager
from src.rpc.manager import init_rpc_manager
from settings import settings


class AppManagerContainer:
    def __init__(self):
        self._bl_manager = None
        self._db_manager = None
        self._rpc_manager = None

    @property
    def bl_manager(self):
        return self._bl_manager

    @property
    def rpc_manager(self):
        return self._rpc_manager

    @property
    def db_manager(self):
        return self._db_manager 

    async def init_managers(self):
        self._db_manager = await init_db_manager(str_for_connect=settings.DATABASE_URL)
        self._rpc_manager = await init_rpc_manager(
            rabbitmq_url=settings.RABBITMQ_CONNECTION_URL,
            exchange_name=settings.RABBITMQ_EXCHANGE_NAME
        )
        self._bl_manager = BLManager(db_manager=self.db_manager, rpc_manager=self.rpc_manager)
