from datetime import datetime
from decimal import Decimal
from typing import Any

from src.bl.managers.base_bl_manager import BaseBLManager
from src.bl.helpers import map_event_status_to_bet_status
from src.common.helpers import utcnow
from src.bl.schemas.bet_schemas import MakeBet, GetBets


class BetBlManager(BaseBLManager):
    async def get_bets(self) -> list[GetBets]:
        bets = await self._db_manager.bet_manager.get_bets()
        bets_with_statuses = []

        for bet in bets:
            bet_status = map_event_status_to_bet_status(bet.event.status)
            bets_with_statuses.append(GetBets(id=bet.id, status=bet_status, event_id=bet.event_id))

        return bets_with_statuses

    async def make_bet(
        self,
        event_id: str,
        amount: Decimal,
    ) -> MakeBet:
        event = await self._db_manager.event_manager.get_event(event_id=event_id)
        if event is None:
            raise Exception('event not found')
        if event.bet_deadline < utcnow():
            raise Exception('bet deadline passed')

        bet = await self._db_manager.bet_manager.make_bet(
            event_id=event_id,
            amount=amount,
        )
        return MakeBet(id=bet.id)
