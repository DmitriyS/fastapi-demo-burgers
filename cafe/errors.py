from http import HTTPStatus

from fastapi import HTTPException


class ApiError(Exception):
    code: str


class NotFoundError(HTTPException):
    def __init__(self) -> None:
        super().__init__(HTTPStatus.NOT_FOUND)


class BurgerError(ApiError):
    pass


class BurgerNotFoundError(NotFoundError):
    pass


class BurgerArchivingError(BurgerError):
    code: str = 'burger_archive_error'


class OrderError(ApiError):
    pass


class OrderNotFoundError(NotFoundError):
    pass


class OrderPrepareError(OrderError):
    pass


class OrderCompletionError(OrderError):
    code: str = 'order_complete_error'


class OrderCreationError(OrderError):
    code: str = 'order_create_error'
