from http import HTTPStatus

from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse

from cafe.config import Settings, get_settings
from cafe.errors import ApiError
from cafe.middleware import SimpleTransactionalMiddleware
from cafe.routers import admin, burgers, orders
from cafe.security import AdminHttpBasic


settings: Settings = get_settings()

app: FastAPI = FastAPI(title=settings.project_name, debug=True)

app.include_router(admin.router, prefix='/admin/burgers', dependencies=[Depends(AdminHttpBasic())], tags=['admin'])
app.include_router(burgers.router, prefix='/burgers', tags=['burgers'])
app.include_router(orders.router, prefix='/orders', tags=['orders'])

app.add_middleware(SimpleTransactionalMiddleware)


@app.exception_handler(ApiError)
async def api_error_exception_handler(request: Request, error: ApiError):
    return JSONResponse(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, content={'code': error.code})
