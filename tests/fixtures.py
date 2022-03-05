import pytest
from faker import Faker
from fastapi.testclient import TestClient

from cafe.app import app
from tests.api import Api
from tests.generator import TestGenerator


__all__ = ('api', 'faker', 'generator')


@pytest.fixture(scope='session', autouse=True)
def overrides() -> None:
    app.dependency_overrides[lambda: {'celery_always_eager': False}] = lambda: {'celery_always_eager': True}


@pytest.fixture(scope='session')
def api() -> Api:
    return Api(TestClient(app))


@pytest.fixture(scope='session')
def faker() -> Faker:
    return Faker()


@pytest.fixture(scope='session')
def generator(faker: Faker) -> TestGenerator:
    return TestGenerator(faker)