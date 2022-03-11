from decimal import Decimal

from pydantic import BaseModel

from cafe.types import BurgerId, OrderId, OrderState


class BurgerIn(BaseModel):
    name: str
    price: Decimal


class BurgerOut(BurgerIn):
    id: BurgerId

    class Config:
        orm_mode = True


class OrderIn(BaseModel):
    burger_ids: list[BurgerId]


class OrderOut(BaseModel):
    id: OrderId
    cost: Decimal
    state: OrderState

    class Config:
        orm_mode = True
