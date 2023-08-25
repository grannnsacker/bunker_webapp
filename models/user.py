from sqlalchemy import Column, BigInteger, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

from store.postgres import sa


class User(sa.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    user_id = Column(String)  # Telegram user id
    settings_id = Column(Integer, ForeignKey('settings.id'), index=True)

    diamonds = Column(Integer)
    ''''''

    ''''''
    settings = relationship("Setting", back_populates="user")
