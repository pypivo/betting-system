from decimal import Decimal
from pydantic import BaseModel, validator


class MakeBetRequest(BaseModel):
    event_id: str
    amount: Decimal

    @validator('amount', allow_reuse=True)
    def validate_status(cls, amount: Decimal) -> Decimal:
        if amount <= 0:
            raise ValueError('amount must greater than 0')
        return amount
