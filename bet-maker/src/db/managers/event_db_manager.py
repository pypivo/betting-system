from typing import Any
from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from src.db.managers.base_db_manager import DBManagerBase


class EventManager(DBManagerBase):
    async def get_events(
        self,
        current_session: AsyncSession | None = None,
    ) -> None:
        async with self.use_or_create_session(current_session) as session:
            return {}
