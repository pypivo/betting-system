from typing import Annotated
from fastapi import APIRouter, Depends, status

from src.bl.managers.manager import BLManager
from src.bl.schemas.event_schemas import GetEvent
from src.common.helpers import Stub

event_routers = APIRouter(prefix="/events")


@event_routers.get('', response_model=list[GetEvent], status_code=status.HTTP_200_OK)
async def get_events(bl_manager: Annotated[BLManager, Depends(Stub(BLManager))]) -> list[GetEvent]:
    return await bl_manager.event_bl_manager.get_events()
