from fastapi import APIRouter, Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import ValidationError

from src.bl.managers.manager import BLManager

event_routers = APIRouter(prefix="/events")

@event_routers.get('')
async def get_events(bl_manager: BLManager = Depends()):
    return await bl_manager.event_bl_manager.get_events()
