from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)

class Credits(Base):
    __tablename__ = 'credits'
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'), primary_key=True)
    credits = Column(Integer, default=0)
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())
