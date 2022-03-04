from fastapi import APIRouter

from cafe.dao import add_burger, archive_burger, get_burgers
from cafe.schemas import Burger
from cafe.types import BurgerId


router: APIRouter = APIRouter(prefix='/burgers')


@router.post('/')
def add_burger(burger: Burger):
    return add_burger(burger)


@router.delete('/{burger_id}/')
def remove_burger(burger_id: BurgerId):
    return archive_burger(burger_id)


@router.get('/', response_model=list[Burger])
def show_burgers():
    return get_burgers()
