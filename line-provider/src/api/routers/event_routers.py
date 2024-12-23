from typing import Annotated
from fastapi import APIRouter, Depends, status

from src.bl.managers.manager import BLManager
from src.bl.schemas.event_schemas import CreateEvent
from src.api.schemas.event_schemas import CreateEventRequest, CompleteEventRequest
from src.common.helpers import Stub

event_routers = APIRouter(prefix="/events")


@event_routers.post('/create', response_model=CreateEvent, status_code=status.HTTP_200_OK)
async def create_event(
    create_event_request: CreateEventRequest,
    bl_manager: Annotated[BLManager, Depends(Stub(BLManager))]
) -> CreateEvent:
    return await bl_manager.event_bl_manager.create_event(
        coefficient=create_event_request.coefficient,
        bet_deadline=create_event_request.bet_deadline
    )


@event_routers.post('/complete', response_model=None, status_code=status.HTTP_200_OK)
async def complete_event(
    complete_event_request: CompleteEventRequest,
    bl_manager: Annotated[BLManager, Depends(Stub(BLManager))]
) -> None:
    return await bl_manager.event_bl_manager.update_event_status(
        event_id=complete_event_request.event_id,
        status=complete_event_request.status
    )
