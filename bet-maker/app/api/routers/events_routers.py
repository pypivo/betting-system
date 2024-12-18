from fastapi import APIRouter, Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession


events_routers = APIRouter(prefix="/events")

@events_routers.get('')
async def get_events(message):
    return message