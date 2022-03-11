from fastapi import FastAPI

from cafe.middleware import SimpleTransactionMiddleware
from cafe.routers import burgers, orders


app: FastAPI = FastAPI(title='Cafe', debug=True)

app.include_router(burgers.router)
app.include_router(orders.router)

app.add_middleware(SimpleTransactionMiddleware)
