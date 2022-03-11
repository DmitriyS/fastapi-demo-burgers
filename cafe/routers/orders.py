from datetime import datetime
from http import HTTPStatus

from fastapi import APIRouter, Depends

from cafe.background.scheduler import KitchenScheduler
from cafe.dependencies import get_scheduler, get_service
from cafe.models import Order
from cafe.schemas import OrderIn, OrderOut
from cafe.service import Cafe
from cafe.types import OrderId


router: APIRouter = APIRouter()


@router.post('/', response_model=OrderOut, status_code=HTTPStatus.ACCEPTED)
def make_order(
    order_in: OrderIn,
    cafe: Cafe = Depends(get_service),
    kitchen_scheduler: KitchenScheduler = Depends(get_scheduler),
) -> Order:
    order = cafe.create_order(order_in.burger_ids, datetime.now())
    kitchen_scheduler.schedule_cook_burger(order.id)
    return order


@router.get('/', response_model=list[OrderOut])
def show_orders(cafe: Cafe = Depends(get_service)) -> list[Order]:
    return cafe.get_processing_orders()


@router.put('/{order_id}/')
def claim_order(order_id: OrderId, cafe: Cafe = Depends(get_service)) -> None:
    cafe.complete_order(order_id, datetime.now())
