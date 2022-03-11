# Описание

Демо-приложение: FastAPI + Celery + PyTest + Docker

# Задача

Реализовать API бургерного кафе:

Этап 1: Базовый функционал
 - административные методы добавления бургера на витрину и снятия с нее
 - метод получение клиентом витрины с бургерами
 - метод создания клиентом заказа с выбранными бургерами
 - метод получения инфорационного табло с закзами клиентов
 - метод получения клиентом заказа

Этап 2: (TODO)
Создать сессии клиентов и коризну заказов

Важный момент: созданный заказ уходит в очередь выполнения и только через некоторое время появляется на информационном табло выполненных

# Установка

- python 3.10+
- pip install -r requirements.txt

# Запуск

- docker-compose up --build

# Использование

- http -v POST localhost:8000/admin/burgers/ name=bigmac price:=10.0
- http -v DELETE localhost:8000/admin/burgers/{burger_id}/
- http -v GET localhost:8000/burgers/
- http -v POST localhost:8000/orders/ burger_ids:=[1,2,3]
- http -v GET localhost:8000/orders/
- http -v PUT localhost:8000/orders/{order_id}/

# Тесты

- pytest -v tests

# Документация

- http://localhost:8000/docs

# Миграции

- alembic revision --autogenerate -m "init" --rev-id 0.0.1
- alembic upgrade head
