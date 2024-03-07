import allure
import pytest
import requests
import random
import string
from urls import Urls

class Courier:

    @allure.title('Генерация данных для регистрации курьера')
    @staticmethod
    def generate_data_courier():
        def generate_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        login = generate_string(10)
        password = generate_string(10)
        first_name = generate_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload


    @allure.title('Регистрация курьера')
    @staticmethod
    def register_new_courier_and_return_login_password():
        payload = Courier.generate_data_courier()
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        return payload


    @allure.title('Удаление курьера')
    @staticmethod
    def delete_courier(data):
        payload = data
        resp = requests.post(Urls.LOGIN_COURIER, data=payload)
        courier_id = resp.json()["id"]
        requests.delete(f'{Urls.CREATE_COURIER}/{courier_id}')