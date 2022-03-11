from typing import Any, TypeVar

from sqlalchemy.orm import Query, Session

from cafe.models import Base, Burger, Order
from cafe.types import BurgerId, OrderId, OrderState, PROCESSING_ORDER_STATES


DbObject = TypeVar('DbObject', bound=Base)


class BaseDao:
    def __init__(self, session: Session) -> None:
        self.session = session

    def q(self, *entities: DbObject, **kwargs: Any) -> Query:
        return self.session.query(*entities, **kwargs)

    def save(self, obj: DbObject) -> DbObject:
        self.session.add(obj)
        self.session.flush()
        return obj


class CafeDao(BaseDao):
    order_states: list[OrderState] = PROCESSING_ORDER_STATES

    def find_burger_by_id(self, burger_id: BurgerId) -> Burger | None:
        return self.q(Burger).filter(Burger.id == burger_id).one_or_none()

    def select_burgers(self, burger_ids: list[BurgerId]) -> list[Burger]:
        return self.q(Burger).filter(Burger.id.in_(burger_ids)).all()

    def get_active_burgers(self) -> list[Burger]:
        return self.q(Burger).filter(Burger.archived_at.is_(None)).all()

    def find_order_by_id(self, order_id: OrderId) -> Order | None:
        return self.q(Order).filter(Order.id == order_id).one_or_none()

    def select_processing_orders(self) -> list[Order]:
        return self.q(Order).filter(Order.state.in_(self.order_states)).all()
