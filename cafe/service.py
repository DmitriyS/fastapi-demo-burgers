from datetime import datetime

from cafe.dao import CafeDao
from cafe.errors import (
    BurgerArchivingError,
    BurgerNotFoundError,
    OrderCompletionError,
    OrderCreationError,
    OrderNotFoundError,
)
from cafe.models import Burger, Order, OrderPosition
from cafe.schemas import BurgerIn
from cafe.types import BurgerId, OrderId


class Cafe:
    def __init__(self, dao: CafeDao) -> None:
        self.dao = dao

    def get_burgers_for_sale(self) -> list[Burger]:
        return self.dao.get_active_burgers()

    def add_burger(self, burger_in: BurgerIn, now: datetime) -> None:
        burger = Burger(burger_in.name, burger_in.price, now)
        self.dao.save(burger)

    def archive_burger(self, burger_id: BurgerId, now: datetime) -> None:
        burger = self.dao.find_burger_by_id(burger_id)
        if burger is None:
            raise BurgerNotFoundError()
        if burger.is_archived():
            raise BurgerArchivingError(burger_id)

        burger.archive(now)

    def get_processing_orders(self) -> list[Order]:
        return self.dao.select_processing_orders()

    def complete_order(self, order_id: OrderId, now: datetime) -> None:
        order = self.dao.find_order_by_id(order_id)
        if order is None:
            raise OrderNotFoundError()
        if order.state.is_completed():
            raise OrderCompletionError(order_id)

        order.complete(now)

    def create_order(self, burger_ids: list[BurgerId], now: datetime) -> Order:
        burgers = self.dao.select_burgers(burger_ids)
        if len(burgers) != len(burger_ids):
            raise OrderCreationError(burger_ids)

        cost = sum(b.price for b in burgers)
        order = self.dao.save(Order(cost, now))
        for b in burgers:
            self.dao.save(OrderPosition(order.id, b.id))
        return order
