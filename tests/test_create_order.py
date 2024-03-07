import allure
import json
from urls import Urls
from data import Order
import pytest
import requests


class TestCreateOrder:

    @allure.title('Создание заказа')
    @allure.description('Проверяем, что заказ успешно создается при любом значении цвета')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order(self, color):
        payload = Order.order_data
        payload['color'] = color
        payload = json.dumps(payload)
        response = requests.post(Urls.ORDER, payload)
        assert response.status_code == 201 and len(str(response.json()['track'])) > 0