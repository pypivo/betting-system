from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

from src.common.enums import EventStatus


class CreateEventRequest(BaseModel):
    coefficient: Decimal
    bet_deadline: datetime


class CompleteEventRequest(BaseModel):
    event_id: str
    status: EventStatus
