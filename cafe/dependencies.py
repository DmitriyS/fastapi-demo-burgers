from fastapi import Request

from cafe.background.scheduler import KitchenScheduler, create_scheduler
from cafe.service import Cafe, create_service


def get_service(request: Request) -> Cafe:
    return create_service(request.state.db_session)


def get_scheduler(request: Request) -> KitchenScheduler:
    return create_scheduler(request.state.db_session)
