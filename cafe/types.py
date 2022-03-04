from enum import Enum
from typing import NewType


BurgerId = NewType('BurgerId', int)
OrderId = NewType('OrderId', int)


class OrderState(str, Enum):
    new = 'new'
    prepared = 'prepared'
    completed = 'completed'
