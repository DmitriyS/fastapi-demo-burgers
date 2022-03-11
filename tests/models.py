from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from cafe.types import OrderState


@dataclass
class TestBurger:
    name: str
    price: Decimal
    id: int | None = None

    @classmethod
    def deserialize(cls, data: dict) -> TestBurger:
        return cls(
            id=data['id'],
            name=data['name'],
            price=Decimal(data['price']),
        )

    def serialize(self) -> dict:
        return {
            'name': self.name,
            'price': str(self.price),
        }


@dataclass
class TestOrder:
    id: int
    state: OrderState

    @classmethod
    def deserialize(cls, data: dict) -> TestOrder:
        return cls(
            id=data['id'],
            state=OrderState(data['state']),
        )
