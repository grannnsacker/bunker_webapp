from sqlalchemy import Column, BigInteger, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

from store.postgres import sa


class Setting(sa.Model):
    __tablename__ = "settings"
    id = Column(Integer, primary_key=True)
    # user_id = Column(Integer, ForeignKey('users.id'), index=True)
    exchange_add = Column(Boolean, default=True)
    user = relationship("User", back_populates="settings")

