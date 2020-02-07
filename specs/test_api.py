import requests
import pytest

def test_get_pizza_orders_for_200_status_code():
    response = requests.get("https://order-pizza-api.herokuapp.com/api/orders")
    assert response.status_code == 200

def test_get_pizza_orders_crusts_no_stuffed_crust():
    response = requests.get("https://order-pizza-api.herokuapp.com/api/orders")
    response_body = response.json()
    for crust in response_body:
        assert crust["Crust"] != 'Stuffed'
