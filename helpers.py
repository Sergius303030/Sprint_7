
import pytest
import requests
import random
import string
from urls import Urls

class Courier:

    @staticmethod
    def register_new_courier_and_return_login_password():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
        "login": login,
        "password": password,
        "firstName": first_name
        }

        response = requests.post(Urls.CREATE_COURIER, data=payload)

        return payload

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

