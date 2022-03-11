from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from cafe.errors import ApiError
from cafe.middleware import SimpleTransactionMiddleware
from cafe.routers import admin, burgers, orders


app: FastAPI = FastAPI(title='Cafe', debug=True)

app.include_router(admin.router)
app.include_router(burgers.router)
app.include_router(orders.router)

app.add_middleware(SimpleTransactionMiddleware)


@app.exception_handler(ApiError)
async def api_error_exception_handler(request: Request, error: ApiError):
    return JSONResponse(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, content={'code': error.code})
