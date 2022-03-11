from faker import Faker
from fastapi.testclient import TestClient
from pytest import fixture

from cafe.app import app
from cafe.config import Settings, get_settings
from tests.api import Api
from tests.generator import TestGenerator


__all__ = ('overrides', 'api', 'faker', 'generator')


def get_settings_override() -> Settings:
    return Settings(celery_task_always_eager=True)


@fixture(scope='session', autouse=True)
def overrides() -> None:
    app.dependency_overrides[get_settings] = get_settings_override


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
