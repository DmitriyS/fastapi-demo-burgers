from typing import NewType

from fastapi.testclient import TestClient
from requests import Response

from .models import TestBurger, TestOrder


Auth = NewType('Auth', tuple[str, str])


class Api:
    admin_auth: Auth = 'admin', 'password'

    def __init__(self, client: TestClient) -> None:
        self.client = client

    def add_burger(self, burger: TestBurger, auth: Auth | None = None) -> None:
        r = self.client.post('/admin/burgers/', json=burger.serialize(), auth=auth or self.admin_auth)
        self.assert_response_code(r, 201)

    def remove_burger(self, burger: TestBurger, auth: Auth | None = None) -> None:
        r = self.client.delete(f'/admin/burgers/{burger.id}/', auth=auth or self.admin_auth)
        self.assert_response_code(r, 204)

    def get_burgers(self) -> list[TestBurger]:
        r = self.client.get('/burgers/')
        self.assert_response_code(r, 200)
        return [TestBurger.deserialize(data) for data in r.json()]

    def make_order(self, burgers: list[TestBurger]) -> TestOrder:
        r = self.client.post('/orders/', json={'burger_ids': [b.id for b in burgers]})
        self.assert_response_code(r, 202)
        return TestOrder.deserialize(r.json())

    def get_orders(self) -> list[TestOrder]:
        r = self.client.get('/orders/')
        self.assert_response_code(r, 200)
        return [TestOrder.deserialize(data) for data in r.json()]

    def claim_order(self, order: TestOrder) -> None:
        r = self.client.put(f'/orders/{order.id}/')
        self.assert_response_code(r, 200)

    def assert_response_code(self, response: Response, expected_code: int) -> None:
        assert response.status_code == expected_code, response
