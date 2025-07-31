import os

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


database_url = os.getenv("DATABASE_URL", None)
if database_url is None:
    raise ValueError("`DATABASE_URL` must be provided in .env!")


engine = create_async_engine(database_url)

session_maker = async_sessionmaker(bind=engine)

class Base(DeclarativeBase):
    ...
