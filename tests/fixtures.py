from faker import Faker
from fastapi.testclient import TestClient
from pytest import fixture

from cafe.app import app
from tests.api import Api
from tests.generator import TestGenerator


__all__ = ('api', 'faker', 'generator')


@fixture(scope='session', autouse=True)
def overrides() -> None:
    app.dependency_overrides[lambda: {'celery_always_eager': False}] = lambda: {'celery_always_eager': True}


@fixture(scope='session')
def api() -> Api:
    with TestClient(app) as client:
        return Api(client)


@fixture(scope='session')
def faker() -> Faker:
    return Faker()


@fixture(scope='session')
def generator(faker: Faker) -> TestGenerator:
    return TestGenerator(faker)
