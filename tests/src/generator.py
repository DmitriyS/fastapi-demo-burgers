from faker import Faker

from .models import TestBurger


class TestGenerator:
    def __init__(self, faker: Faker) -> None:
        self.faker = faker

    def burger(self) -> TestBurger:
        return TestBurger(
            name=self.faker.word(),
            price=self.faker.random_digit_not_null(),
        )
