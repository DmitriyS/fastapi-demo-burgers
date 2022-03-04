from fastapi import APIRouter

from cafe.schemas import Burger
from cafe.types import BurgerId


router: APIRouter = APIRouter(prefix='/burgers')


@router.post('/')
def add_burger(burger: Burger):
    return {'message': f'add_burger: {burger}'}


@router.delete('/{burger_id}/')
def remove_burger(burger_id: BurgerId):
    return {'message': f'remove_burger {burger_id}'}


@router.get('/', response_model=list[Burger])
def show_burgers():
    return {'message': 'list_burgers'}
