from pydantic import BaseModel
from datetime import datetime

class ItemBase(BaseModel):
    name: str
    price: int
    quantity: int
    category: str | None = None

class ItemCreateOrUpdate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    dateOfCreation: datetime
    
    class Config:
        orm_mode = True

class SuccessMessage(BaseModel):
    message: str