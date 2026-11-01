from sqlalchemy import Column, BigInteger, String, Text
from app.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(BigInteger, primary_key=True, index=True)
    flags = Column(Text)
    instruction = Column(Text, nullable=False)
    category = Column(String, nullable=False)
    intent = Column(String, nullable=False)
    response = Column(Text, nullable=False)