from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import contains_eager
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.managers.base_db_manager import DBManagerBase
from src.db.models import Bet, Event
from src.common.helpers import str_uuid


class BetManager(DBManagerBase):
    async def get_bets(
        self,
        current_session: AsyncSession | None = None,
    ) -> list[Bet]:
        async with self.use_or_create_session(current_session) as session:
            return await session.scalars(
                select(Bet)
                .join(Event)
                .options(contains_eager(Bet.event))
            )     

    async def make_bet(
        self,
        event_id: str,
        amount: Decimal,
        current_session: AsyncSession | None = None,
    ) -> Bet:
        async with self.use_or_create_session(current_session) as session:
            bet = Bet(
                id=str_uuid(),
                amount=amount,
                event_id=event_id,
            )
            session.add(bet)
            return bet
