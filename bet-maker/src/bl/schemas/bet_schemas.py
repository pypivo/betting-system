from decimal import Decimal
from pydantic import BaseModel

from src.common.enums import BetStatus


class MakeBet(BaseModel):
    id: str


class GetBets(BaseModel):
    id: str
    event_id: str
    status: BetStatus
