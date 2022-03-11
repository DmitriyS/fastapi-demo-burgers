from faker import Faker

from tests.api import Api
from tests.generator import TestGenerator


def test_create_and_get_burger(api: Api, generator: TestGenerator) -> None:
    burger = generator.burger()

    api.add_burger(burger)
    burgers = api.get_burgers()

    assert burger.name in [b.name for b in burgers]


def test_create_and_remove_and_get_burger(api: Api, faker: Faker, generator: TestGenerator) -> None:
    api.add_burger(generator.burger())

    burgers = api.get_burgers()
    burger_to_remove = faker.random_element(burgers)
    api.remove_burger(burger_to_remove)

    burgers = api.get_burgers()
    assert burger_to_remove not in burgers


def test_order_several_burgers(api: Api, faker: Faker, generator: TestGenerator) -> None:
    for _ in range(faker.random_int(2, 5)):
        api.add_burger(generator.burger())

    burgers = api.get_burgers()
    order = api.make_order(burgers)

    orders = api.get_orders()
    assert order in orders
    assert order.state.is_new()


def test_claim_ordered_burger(api: Api, faker: Faker, generator: TestGenerator) -> None:
    api.add_burger(generator.burger())

    burgers = api.get_burgers()
    order = api.make_order([faker.random_element(burgers)])
    api.claim_order(order)

    orders = api.get_orders()
    assert order not in orders
