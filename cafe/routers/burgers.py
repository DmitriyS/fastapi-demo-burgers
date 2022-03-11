from fastapi import APIRouter, Depends

from cafe.dependencies import get_service
from cafe.models import Burger
from cafe.schemas import BurgerOut
from cafe.service import Cafe


router: APIRouter = APIRouter()


@router.get('/', response_model=list[BurgerOut])
def show_burgers(cafe: Cafe = Depends(get_service)) -> list[Burger]:
    return cafe.get_burgers_for_sale()
