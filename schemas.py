from pydantic import BaseModel
class StockCreate(BaseModel):
    name: str
    price: int

class StockResponse(BaseModel):
    id : int
    name: str
    price: int

    class Config:
        from_attribute = True