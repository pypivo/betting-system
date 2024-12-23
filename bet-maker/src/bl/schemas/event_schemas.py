from pydantic import BaseModel

from src.common.enums import EventStatus

class GetEvent(BaseModel):
    id: str
    status: EventStatus