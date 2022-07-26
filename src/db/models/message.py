from operator import index
from sqlalchemy.sql.sqltypes import Boolean
from src.db.db.base_class import Base
from sqlalchemy import (
    Column,
    Float,
    BigInteger,
    Integer,
    String,

    DateTime,
)
from sqlalchemy.sql import func


class Message(Base):
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=False), index=True)
    content = Column(String)
    author = Column(Integer)
    reactions = Column(Integer, default=0)
    channel_id = Column(Integer, index=True)
    guild_id = Column(Integer)

