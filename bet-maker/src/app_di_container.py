from src.bl.manager import BLManager
from src.db.manager import init_db_manager


class AppDiContainer:
    async def __init__(self):
        self._bl_manager = None
        self._db_manager = None

    @property
    def bl_manager(self):
        return self._bl_manager

    async def init_managers(self):
        self._db_manager = await init_db_manager(str_for_connect='')  # TODO: settings
        self._bl_manager = BLManager(db_manager=self._db_manager)