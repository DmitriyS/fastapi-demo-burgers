from decimal import Decimal

from pydantic import BaseModel

from cafe.types import BurgerId, OrderId


class Burger(BaseModel):
    name: str
    price: Decimal

    class Config:
        orm_mode = True


class Order(BaseModel):
    burger_ids: list[BurgerId]
    cost: Decimal

    class Config:
        orm_mode = True


class OrderOut(BaseModel):
    id: OrderId
    cost: Decimal

    class Config:
        orm_mode = True
