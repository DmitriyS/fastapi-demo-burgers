from fastapi.testclient import TestClient
from requests import Response

from .models import TestBurger, TestOrder


class Api:
    def __init__(self, client: TestClient) -> None:
        self.client = client

    def add_burger(self, burger: TestBurger) -> None:
        r = self.client.post('/burgers/', json=burger.serialize())
        self.assert_response_code(r, 200)

    def get_burgers(self) -> list[TestBurger]:
        r = self.client.get('/burgers/')
        self.assert_response_code(r, 200)
        return [TestBurger.deserialize(data) for data in r.json()]

    def remove_burger(self, burger: TestBurger) -> None:
        r = self.client.delete(f'/burgers/{burger.id}')
        self.assert_response_code(r, 200)

    def make_order(self, burgers: list[TestBurger]) -> TestOrder:
        r = self.client.post('/orders/', json={'burger_ids': [b.id for b in burgers]})
        self.assert_response_code(r, 200)
        return TestOrder.deserialize(r.json())

    def get_orders(self) -> list[TestOrder]:
        r = self.client.post('/orders/')
        self.assert_response_code(r, 200)
        return [TestOrder.deserialize(data) for data in r.json()]

    def claim_order(self, order: TestOrder) -> None:
        r = self.client.put(f'/orders/{order.id}/')
        self.assert_response_code(r, 200)

    def assert_response_code(self, response: Response, expected_code: int) -> None:
        assert response.status_code, expected_code
