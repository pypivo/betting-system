from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

from src.common.enums import EventStatus


class CreateEventRequest(BaseModel):
    event_id: str
    status: EventStatus
    coefficient: Decimal
    bet_deadline: datetime


class UpdateEventStatusRequest(BaseModel):
    event_id: str
    status: EventStatus
