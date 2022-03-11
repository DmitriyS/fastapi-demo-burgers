from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.types import ASGIApp

from cafe.config import get_settings
from cafe.database import SessionFactory


class SimpleTransactionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)
        self.session_factory = SessionFactory(get_settings())

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request.state.db_session = session = self.session_factory()
        try:
            response = await call_next(request)
            session.commit()
            return response
        except Exception:
            if session.is_active:
                session.rollback()
            raise
        finally:
            session.close()
