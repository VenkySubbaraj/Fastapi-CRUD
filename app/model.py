from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import base

class User(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=False)
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)