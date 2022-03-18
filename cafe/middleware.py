from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.types import ASGIApp

from cafe.database import get_session_factory, transaction


class SimpleTransactionalMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)
        self.session_factory = get_session_factory()

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request.state.db_session = session = self.session_factory()
        with transaction(session):
            return await call_next(request)
