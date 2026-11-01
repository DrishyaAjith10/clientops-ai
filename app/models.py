from sqlalchemy import Column, BigInteger, String, Text
from app.database import Base
from sqlalchemy import  Boolean, DateTime
from sqlalchemy.sql import func

class Document(Base):
    __tablename__ = "documents"

    id = Column(BigInteger, primary_key=True, index=True)
    flags = Column(Text)
    instruction = Column(Text, nullable=False)
    category = Column(String, nullable=False)
    intent = Column(String, nullable=False)
    response = Column(Text, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())