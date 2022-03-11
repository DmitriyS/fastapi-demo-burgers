from http import HTTPStatus
from datetime import datetime

from fastapi import APIRouter, Depends

from cafe.dependencies import get_service
from cafe.schemas import BurgerIn
from cafe.service import Cafe
from cafe.types import BurgerId


router: APIRouter = APIRouter()


@router.post('/', status_code=HTTPStatus.CREATED)
def add_burger(burger_in: BurgerIn, cafe: Cafe = Depends(get_service)) -> None:
    cafe.add_burger(burger_in, datetime.now())


@router.delete('/{burger_id}/', status_code=HTTPStatus.NO_CONTENT)
def remove_burger(burger_id: BurgerId, cafe: Cafe = Depends(get_service)) -> None:
    cafe.archive_burger(burger_id, datetime.now())
