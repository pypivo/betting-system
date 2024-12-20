from fastapi import APIRouter, Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import ValidationError

from src.bl.managers.manager import BLManager

bet_routers = APIRouter(prefix="/")

@bet_routers.get('/bets')
async def get_bets(bl_manager: BLManager = Depends()):
    return await bl_manager.bet_bl_manager.get_bets()


@bet_routers.post('/bet')
async def make_bet(bl_manager: BLManager = Depends()):
    return await bl_manager.bet_bl_manager.make_bet()
