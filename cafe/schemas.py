from decimal import Decimal

from pydantic import BaseModel


class Burger(BaseModel):
    name: str
    price: Decimal


class Order(BaseModel):
    pass
