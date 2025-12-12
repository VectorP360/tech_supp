import asyncio

from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import settings

async_engine = create_async_engine(settings.DATABASE_URL_asyncpg)

async_session_factory = async_sessionmaker(async_engine)

class Base(DeclarativeBase):...
