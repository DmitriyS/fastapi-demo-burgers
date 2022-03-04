from sqlalchemy import Column, DECIMAL, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Burger(Base):
    __tablename__ = 'burgers'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    price = Column(DECIMAL(precision=2), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    archived_at = Column(DateTime(timezone=True), nullable=True)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    cost = Column(DECIMAL(precision=2), nullable=False)

    positions = relationship('OrderPosition')


class OrderPosition(Base):
    __tablename__ = 'orders_positions'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey(Order.id), nullable=False)
    burger_id = Column(ForeignKey(Burger.id), nullable=False)
