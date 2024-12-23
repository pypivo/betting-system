from typing import Any

from src.bl.managers.manager import BLManager
from src.rpc.schemas import CreateEventRequest, UpdateEventStatusRequest
from src.common.helpers import rpc_wrapper

class RpcRouters:
    notification_event_status_updated = 'notification.event.status.updated'
    notification_event_created= 'notification.event.created'


class BaseRoutes:
    def __init__(self, bl_manager: BLManager) -> None:
        self._bl_manager = bl_manager


class EventRpcRouter(BaseRoutes):
    @rpc_wrapper(CreateEventRequest)
    async def create_event(self, message: CreateEventRequest) -> None:
        await self._bl_manager.event_bl_manager.create_event(
            event_id=message.event_id,
            status=message.status,
            coefficient=message.coefficient,
            bet_deadline=message.bet_deadline
        )

    @rpc_wrapper(UpdateEventStatusRequest)
    async def update_event_status(self, message: UpdateEventStatusRequest) -> None:
        await self._bl_manager.event_bl_manager.update_event_status(
            event_id=message.event_id,
            status=message.status
        )
