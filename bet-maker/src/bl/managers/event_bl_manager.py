from typing import Any

from src.bl.managers.base_bl_manager import BaseBLManager


class EventBlManager(BaseBLManager):
    async def get_events(self):
        await self._db_manager.event_manager.get_events()
