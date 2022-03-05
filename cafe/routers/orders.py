from fastapi import APIRouter

from cafe.background.tasks import CookBurgerTask
from cafe.dao import create_order, complete_order, get_orders
from cafe.schemas import OrderIn, OrderOut
from cafe.types import OrderId


router: APIRouter = APIRouter(prefix='/orders')


@router.post('/', response_model=OrderOut)
def make_order(order: OrderIn):
    o = create_order(order)
    CookBurgerTask().apply_async(args=(o.id,))
    return o


@router.get('/', response_model=list[OrderOut])
def show_orders():
    return get_orders()


@router.put('/{order_id}/')
def claim_order(order_id: OrderId):
    complete_order(order_id)
