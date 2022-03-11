import secrets
from http import HTTPStatus
from typing import Any

from fastapi import HTTPException, Request
from fastapi.security import HTTPBasic

from cafe.config import get_settings


class AdminHttpBasic(HTTPBasic):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.settings = get_settings()

    async def __call__(self, request: Request) -> None:
        credentials = await super().__call__(request)
        is_username_ok = secrets.compare_digest(credentials.username, self.settings.admin_username)
        is_password_ok = secrets.compare_digest(credentials.password, self.settings.admin_password)

        if not (is_username_ok and is_password_ok):
            raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, headers={'WWW-Authenticate': 'Basic'})
