from __future__ import annotations

from enum import Enum
from typing import NewType


BurgerId = NewType('BurgerId', int)
OrderId = NewType('OrderId', int)


class OrderState(str, Enum):
    new = 'new'
    prepared = 'prepared'
    completed = 'completed'

    def is_new(self) -> bool:
        return self is self.new

    def is_prepared(self) -> bool:
        return self is self.prepared


PROCESSING_ORDER_STATES: list[OrderState] = [OrderState.new, OrderState.prepared]
