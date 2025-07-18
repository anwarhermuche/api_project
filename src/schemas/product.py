from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    description: str

    class Config:
        from_attributes = True


class ProductRead(Product):
    id: int
