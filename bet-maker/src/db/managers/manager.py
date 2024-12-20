import logging

from sqlalchemy import Connection, text
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

# import settings
from alembic.command import upgrade
from alembic.config import Config
from src.db.managers.base_db_manager import DBManagerBase
from src.db.managers.event_db_manager import EventManager
from src.db.managers.bet_db_manager import BetManager

logger = logging.getLogger(__name__)


class DBManager(DBManagerBase):
    def __init__(self, async_engine: AsyncEngine):
        super().__init__(async_engine)
        self._event_manager = EventManager(async_engine)
        self._bet_manager = BetManager(async_engine)

    @property
    def event_manager(self) -> EventManager:
        return self._event_manager
    
    @property
    def bet_manager(self) -> BetManager:
        return self._bet_manager

    async def healthcheck(self) -> bool:
        try:
            async with self.session() as session:
                result = await session.execute(text('CREATE TEMPORARY TABLE amogus (abobus INTEGER) ON COMMIT DROP;'))
                return result.connection.connection.is_valid  # type: ignore
        except Exception:
            logger.exception('db healthcheck failed')
            return False


async def init_db_manager(
    str_for_connect: str,
    run_migrations: bool = True,
) -> DBManager:
    engine = create_async_engine(
        str_for_connect,
        pool_pre_ping=True,
        # pool_size=settings.POSTGRESQL_MAX_CONNECTIONS,
        # json_serializer=json_dumps,
        # json_deserializer=json_loads,
    )

    if run_migrations:
        def run_upgrade(connection: Connection, alembic_config: Config) -> None:
            alembic_config.attributes['connection'] = connection
            alembic_config.attributes['skip_logging_configuration'] = 'True'
            upgrade(alembic_config, 'head')

        async with engine.begin() as conn:
            await conn.run_sync(run_upgrade, Config('alembic.ini'))

    return DBManager(engine)
