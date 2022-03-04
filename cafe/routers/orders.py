from fastapi import APIRouter

from cafe.schemas import Order
from cafe.types import BurgerId, OrderId


router: APIRouter = APIRouter(prefix='/orders')


@router.post('/')
def create_order(burger_ids: list[BurgerId]):
    return {'message': f'create_order {burger_ids}'}


@router.get('/', response_model=list[Order])
def show_orders():
    return {'message': 'show_orders'}


@router.put('/{order_id}/')
def claim_order(order_id: OrderId):
    return {'message': f'claim_order {order_id}'}
