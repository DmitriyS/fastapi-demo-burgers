from datetime import datetime

from cafe.database import session
from cafe.models import Burger, Order, OrderPosition


def get_burgers():
    return session.query(Burger).all()


def create_burger(burger):
    burger = Burger(**burger.dict(), created_at=datetime.now())
    session.add(burger)
    session.flush()
    session.commit()


def archive_burger(burger_id):
    burger = session.query(Burger).filter(Burger.id == burger_id).one_or_none()
    if burger:
        burger.archive(datetime.now())
        session.commit()


def create_order(order):
    o = Order(cost=order.cost, created_at=datetime.now())
    session.add(o)
    session.flush()
    for burger_id in order.burger_ids:
        position = OrderPosition(o.id, burger_id)
        session.add(position)
        session.flush()
    session.commit()
    return o


def get_orders():
    return session.query(Order).all()


def complete_order(order_id):
    order = session.query(Order).filter(Order.id == order_id).one_or_none()
    if order:
        order.complete(datetime.now())
        session.commit()
