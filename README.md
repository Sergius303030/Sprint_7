﻿
Sprint_7 Автотесты API сервиса qa-scooter

Выполняемые проверки:
1. Создание учетной записи курьера
2. Авторизация курьера
3. Создание заказа
4. Получение списка заказов

* Запуск тестов: pytest -v ./tests
* Генерация отчета Allure: pytest -v ./tests --alluredir=allure_results
* Формирование отчета Allure: allure serve allure_results
