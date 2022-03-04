from fastapi import FastAPI

from cafe.routers import burgers_router, orders_router


class Cafe(FastAPI):
    title: str = 'Burgers'


app: FastAPI = FastAPI()
app.include_router(burgers_router)
app.include_router(orders_router)
