from datetime import datetime
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.managers.base_db_manager import DBManagerBase
from src.db.models import Event
from src.common.helpers import str_uuid
from src.common.enums import EventStatus


class EventManager(DBManagerBase):
    async def get_locked_event(
        self,
        event_id: str,
        current_session: AsyncSession | None = None,
    ) -> Event | None:
        async with self.use_or_create_session(current_session) as session:
            return await session.scalar(
                select(Event)
                .with_for_update()
                .where(Event.id == event_id)
            )
    
    async def create_event(
        self,
        coefficient: Decimal,
        bet_deadline: datetime,
        current_session: AsyncSession | None = None,
    ) -> Event:
        async with self.use_or_create_session(current_session) as session:
            event = Event(
                id=str_uuid(),
                coefficient=coefficient,
                bet_deadline=bet_deadline,
                status=EventStatus.UNCOMPLETED,
            )
            session.add(event)
            return event

    async def update_event_status(
        self,
        event_id: str,
        status: EventStatus,
        current_session: AsyncSession | None = None,
    ) -> Event | None:
        async with self.use_or_create_session(current_session) as session:
            event = await self.get_locked_event(event_id=event_id, current_session=session)
            if event is None:
                raise Exception('event not found')

            event.status = status
            return event
