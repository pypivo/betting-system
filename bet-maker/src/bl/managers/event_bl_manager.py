from datetime import datetime
from decimal import Decimal

from src.bl.managers.base_bl_manager import BaseBLManager
from src.bl.schemas.event_schemas import GetEvent
from src.common.enums import EventStatus


class EventBlManager(BaseBLManager):
    async def get_events(self):
        events = await self._db_manager.event_manager.get_events_for_bet()
        return [GetEvent(id=event.id, status=event.status) for event in events]

    async def create_event(
        self,
        event_id: str,
        status: EventStatus,
        coefficient: Decimal,
        bet_deadline: datetime, 
    ) -> None:
        await self._db_manager.event_manager.create_event(
            event_id=event_id,
            status=status,
            coefficient=coefficient,
            bet_deadline=bet_deadline
        )

    async def update_event_status(
        self,
        event_id: str,
        status: EventStatus
    ) -> None:
        await self._db_manager.event_manager.update_event_status(
            event_id=event_id,
            status=status
        )
