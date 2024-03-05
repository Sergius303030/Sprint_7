import allure
from urls import Urls
from helpers import Courier
import pytest
import requests

class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    @allure.description('Проверяем, что регистрация нового курьера доступна.')
    def test_create_courier_success(self):
        payload = Courier.generate_data_courier()
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 201 and response.json().get('ok') == True

    @allure.title('Повторное создание курьера')
    @allure.description('Проверяем, что повторное создание курьера с теми же данными недоступно')
    def test_create_courier_twice(self):
        payload = Courier.generate_data_courier()
        requests.post(Urls.CREATE_COURIER, data=payload)
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 409 and response.json().get('message') == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Создание курьера без обязательных полей')
    @allure.description('Проверяем, что создание курьера без обязательных полей недоступно')
    @pytest.mark.parametrize('field', ['login', 'password', 'first_name'])
    def test_create_courier_missing_field(self, field):
        payload = Courier.generate_data_courier()
        del payload[field]
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 400 and response.json().get('message') == 'Недостаточно данных для создания учетной записи'

