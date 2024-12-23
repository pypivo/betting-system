from typing import Annotated
from fastapi import APIRouter, Depends, status

from src.bl.managers.manager import BLManager
from src.api.schemas.bet_schemas import MakeBetRequest
from src.bl.schemas.bet_schemas import GetBets, MakeBet
from src.common.helpers import Stub

bet_routers = APIRouter(prefix="")


@bet_routers.get('/bets', response_model=list[GetBets], status_code=status.HTTP_200_OK)
async def get_bets(bl_manager: Annotated[BLManager, Depends(Stub(BLManager))]) -> list[GetBets]:
    return await bl_manager.bet_bl_manager.get_bets()


@bet_routers.post('/bet', response_model=MakeBet, status_code=status.HTTP_200_OK)
async def make_bet(bet: MakeBetRequest, bl_manager: Annotated[BLManager, Depends(Stub(BLManager))]) -> MakeBet:
    return await bl_manager.bet_bl_manager.make_bet(
        event_id=bet.event_id,
        amount=bet.amount,
    )
