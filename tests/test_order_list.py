import allure
from urls import Urls
import pytest
import requests


class TestOrderList:

    @allure.title('Получение списка заказов')
    @allure.description('Проверяем, что список заказов возвращается')
    def test_order_list_success(self):
        response = requests.get(Urls.ORDER)
        assert response.status_code == 200 and len(response.json()['orders']) > 0