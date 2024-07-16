from modelo.database import Base
from sqlalchemy import Column, Integer, String, Unicode, DateTime


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    dateOfCreation = Column(DateTime, nullable=False)
    category = Column(String)
