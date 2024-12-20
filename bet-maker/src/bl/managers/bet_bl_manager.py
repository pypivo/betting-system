from typing import Any

from src.bl.managers.base_bl_manager import BaseBLManager


class BetBlManager(BaseBLManager):
    async def get_bets(self):
        await self._db_manager.bet_manager.get_bets()

    async def make_bet(self):
        pass