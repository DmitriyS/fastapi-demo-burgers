from datetime import datetime

from fastapi import APIRouter, Depends

from cafe.dependencies import get_service
from cafe.models import Burger
from cafe.schemas import BurgerIn, BurgerOut
from cafe.service import Cafe
from cafe.types import BurgerId


router: APIRouter = APIRouter(prefix='/burgers')


@router.post('/')
def add_burger(burger_in: BurgerIn, cafe: Cafe = Depends(get_service)) -> None:
    cafe.add_burger(burger_in, datetime.now())


@router.delete('/{burger_id}/')
def remove_burger(burger_id: BurgerId, cafe: Cafe = Depends(get_service)) -> None:
    cafe.archive_burger(burger_id, datetime.now())


@router.get('/', response_model=list[BurgerOut])
def show_burgers(cafe: Cafe = Depends(get_service)) -> list[Burger]:
    return cafe.get_burgers_for_sale()
