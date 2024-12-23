from datetime import datetime
from decimal import Decimal

from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.common.helpers import utcnow


class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = 'event'

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)

    coefficient: Mapped[Decimal] = mapped_column()
    bet_deadline: Mapped[datetime] = mapped_column()
    status: Mapped[str] = mapped_column()

    created_at: Mapped[datetime] = mapped_column(default=utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=utcnow, onupdate=utcnow)
