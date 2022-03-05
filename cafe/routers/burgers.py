from fastapi import APIRouter

from cafe.dao import create_burger, archive_burger, get_burgers
from cafe.schemas import BurgerIn, BurgerOut
from cafe.types import BurgerId


router: APIRouter = APIRouter(prefix='/burgers')


@router.post('/')
def add_burger(burger: BurgerIn):
    return create_burger(burger)


@router.delete('/{burger_id}/')
def remove_burger(burger_id: BurgerId):
    return archive_burger(burger_id)


@router.get('/', response_model=list[BurgerOut])
def show_burgers():
    return get_burgers()
