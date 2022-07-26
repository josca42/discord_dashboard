from src.db.db.base_class import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Link(Base):

    message_id = Column(Integer, ForeignKey("message.id"), primary_key=True, index=True)
    url = Column(String, primary_key=True)

    message = relationship("Message")
