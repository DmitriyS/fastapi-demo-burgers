from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, DECIMAL, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import MetaData

from cafe.types import BurgerId, OrderId, OrderState


Base = declarative_base(metadata=MetaData())


class Burger(Base):
    __tablename__ = 'burgers'

    id: BurgerId = Column(Integer, primary_key=True)
    name: str = Column(String(32), nullable=False)
    price: Decimal = Column(DECIMAL(precision=2), nullable=False)
    created_at: datetime = Column(DateTime(timezone=True), nullable=False)
    archived_at: datetime | None = Column(DateTime(timezone=True), nullable=True)

    def __init__(self, name: str, price: Decimal, created_at: datetime) -> None:
        self.name = name
        self.price = price
        self.created_at = created_at

    def archive(self, now: datetime) -> None:
        self.archived_at = now


class Order(Base):
    __tablename__ = 'orders'

    id: OrderId = Column(Integer, primary_key=True)
    cost: Decimal = Column(DECIMAL(precision=2), nullable=False)
    state: OrderState = Column(Enum(OrderState), nullable=False)
    created_at: datetime = Column(DateTime(timezone=True), nullable=False)
    prepared_at: datetime | None = Column(DateTime(timezone=True), nullable=True)
    completed_at: datetime | None = Column(DateTime(timezone=True), nullable=True)

    positions = relationship('OrderPosition', back_populates='order')

    def __init__(self, cost: Decimal, created_at: datetime) -> None:
        self.cost = cost
        self.state = OrderState.new
        self.created_at = created_at

    def prepare(self, now: datetime) -> None:
        self.state = OrderState.prepared
        self.prepared_at = now

    def complete(self, now: datetime) -> None:
        self.state = OrderState.completed
        self.completed_at = now


class OrderPosition(Base):
    __tablename__ = 'orders_positions'

    id: int = Column(Integer, primary_key=True)
    order_id: OrderId = Column(ForeignKey(Order.id), nullable=False)
    burger_id: BurgerId = Column(ForeignKey(Burger.id), nullable=False)

    order = relationship('Order', back_populates='positions')

    def __init__(self, order_id: OrderId, burger_id: BurgerId) -> None:
        self.order_id = order_id
        self.burger_id = burger_id
