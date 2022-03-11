from fastapi import Depends, Request

from cafe.background.scheduler import KitchenScheduler, TaskSender
from cafe.dao import CafeDao
from cafe.service import Cafe


def get_dao(request: Request) -> CafeDao:
    return CafeDao(request.state.db_session)


def get_service(dao: CafeDao = Depends(get_dao)) -> Cafe:
    return Cafe(dao)


def get_scheduler(request: Request) -> KitchenScheduler:
    return KitchenScheduler(TaskSender(request.state.db_session))
