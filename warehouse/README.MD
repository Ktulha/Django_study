# API WAREHOUSE

API реализует логику поставки и потребления товаров. 

Поставка и потребление товаров со складов осуществляются в зависимости от типа пользователя (`SUPPLIER`/`CONSUMER`):
- `SUPPLIER`: поставляет товары на склады.
- `CONSUMER`: потребляет товары с складов.

Поставка и потребление сотваров со складов происходит в транзакциях

## Установка
``` bash
python -m venv venv
source venv/bin/activate  # Для Linux/MacOS
# или
venv\Scripts\activate  # Для Windows

pip install -r requirements.txt
```
## Настройка и запуск

``` bash
python manage.py migrate
python manage.py runserver
```
### Основной интерфейс
http://127.0.0.1:8000/


###  Создание первого юзера

http://127.0.0.1:8000/register/
###  Авторизация
http://127.0.0.1:8000/api-authlogin/

## Эндпойнты

### Пользователи
- `POST /users/`: создание пользователя
- `GET /users/`: получение списка пользователей
- `GET /users/{id}/`: получение пользователя по id

### Склады
- `POST /warehouses/`: создание склада
- `GET /warehouses/`: получение списка складов
- `GET /warehouses/{id}/`: получение склада по id
- `PUT /warehouses/{id}/`: обновление склада по id
- `DELETE /warehouses/{id}/`: удаление склада по id

### Товары
- `POST /products/`: создание товара
- `GET /products/`: получение списка товаров
- `GET /products/{id}/`: получение товара по id
- `PUT /products/{id}/`: обновление товара по id
- `DELETE /products/{id}/`: удаление товара по id

### Транзакции
- `POST /transactions/`: создание транзакции
- `GET /transactions/`: получение списка транзакций

### Остатки товаров
- `GET /stock/`: получение остатков товаров на складах
