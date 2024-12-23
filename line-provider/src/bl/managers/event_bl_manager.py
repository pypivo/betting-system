from datetime import datetime
from decimal import Decimal

from src.bl.managers.base_bl_manager import BaseBLManager
from src.common.enums import EventStatus
from src.bl.schemas.event_schemas import CreateEvent
from src.rpc.routes import RpcRouters


class EventBlManager(BaseBLManager):
    async def create_event(
        self,
        coefficient: Decimal,
        bet_deadline: datetime, 
    ) -> CreateEvent:
        event = await self._db_manager.event_manager.create_event(
            coefficient=coefficient,
            bet_deadline=bet_deadline
        )
        await self._rpc_manager.publish(
            message_body={
                'event_id': event.id,
                'status': event.status,
                'coefficient': event.coefficient,
                'bet_deadline': event.bet_deadline,
            },
            routing_key=RpcRouters.notification_event_created
        )

        return CreateEvent(id=event.id)

    async def update_event_status(
        self,
        event_id: str,
        status: EventStatus
    ) -> None:
        event = await self._db_manager.event_manager.update_event_status(
            event_id=event_id,
            status=status
        )
        await self._rpc_manager.publish(
            message_body={
                'event_id': event.id,
                'status': event.status,
            },
            routing_key=RpcRouters.notification_event_status_updated
        )
