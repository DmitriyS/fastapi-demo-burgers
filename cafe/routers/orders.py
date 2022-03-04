from fastapi import APIRouter

from cafe.dao import add_order, complete_order, get_orders
from cafe.schemas import Order, OrderOut
from cafe.types import OrderId


router: APIRouter = APIRouter(prefix='/orders')


@router.post('/')
def create_order(order: Order):
    add_order(order)


@router.get('/', response_model=list[OrderOut])
def show_orders():
    return get_orders()


@router.put('/{order_id}/')
def claim_order(order_id: OrderId):
    complete_order(order_id)
