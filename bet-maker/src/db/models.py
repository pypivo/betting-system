from datetime import datetime
from decimal import Decimal
from typing import Any, Optional

from sqlalchemy import ForeignKey, String, UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from src.common.helpers import utcnow, str_uuid


class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = 'event'

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)

    coefficient: Mapped[Decimal] = mapped_column()
    bet_deadline: Mapped[datetime] = mapped_column(index=True)
    status: Mapped[str] = mapped_column()

    created_at: Mapped[datetime] = mapped_column(default=utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=utcnow, onupdate=utcnow)

    bets: Mapped[list['Bet']] = relationship(back_populates='event')


class Bet(Base):
    __tablename__ = 'bet'

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True, default=str_uuid)

    amount: Mapped[Decimal] = mapped_column()
    event_id: Mapped[str] = mapped_column(UUID(as_uuid=False), ForeignKey('event.id'))

    created_at: Mapped[datetime] = mapped_column(default=utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=utcnow, onupdate=utcnow)

    event: Mapped[Event] = relationship(back_populates='bets')
