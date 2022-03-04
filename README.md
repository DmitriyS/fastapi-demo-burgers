# Описание

Демо-приложение: FastAPI + Celery + PyTest + Docker

# Задача

Реализовать API бургерного кафе:
 - административные методы добавления бургера на витрину и снятия с нее
 - метод получение клиентом витрины с бургерами
 - метод создания клиентом заказа с выбранными бургерами
 - метод получения инфорационного табло с закзами клиентов
 - метод получения клиентом заказа

Важный момент: созданный заказ уходит в очередь выполнения и только через некоторое время появляется на информационном табло выполненных

# Установка

- python 3.10+
- pip install -r requirements_dev.txt

# Запуск

- docker-compose up --build

# Использование

- http -v POST localhost:8000/burgers/ title=бургер cost=50.0
- http -v DELETE localhost:8000/burgers/{burger_id}/
- http -v GET localhost:8000/burgers/
- http -v POST localhost:8000/orders/ burger_ids:=[1,2,3]
- http -v GET localhost:8000/orders/
- http -v PUT localhost:8000/orders/{order_id}/

# Тесты

- pytest -v tests
