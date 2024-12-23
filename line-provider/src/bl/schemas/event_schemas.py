from pydantic import BaseModel


class CreateEvent(BaseModel):
    id: str
