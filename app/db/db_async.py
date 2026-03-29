# db.py
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession,async_sessionmaker,create_async_engine

from app.config import get_settings_singleton
settings = get_settings_singleton()

AIN_SUPA_URL = settings.AIN_SUPA

ain_db_async_engine = create_async_engine(AIN_SUPA_URL,    pool_pre_ping=True,    echo=False, )
AinDbSession = async_sessionmaker(ain_db_async_engine,    expire_on_commit=False,)


async def get_session():
    async with AinDbSession() as t4_session:
        async with t4_session.begin():
            yield t4_session
