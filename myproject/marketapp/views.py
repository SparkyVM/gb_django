from django.shortcuts import render
from django.http import HttpResponse
from models import User, Item, Order

# 2
"""
Создайте три модели Django: клиент, товар и заказ.
Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа

Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой ба
"""

def index(request):
    html = '''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Market</title>
        </head>
        <body>
        <h1>Главная страница</h1>
        <p>Приветствуем в Django Маркет</p>
        <hr>
        <a href="http://127.0.0.1:8000/info/about/">Обо мне</a>.
        </body>
        </html>'''
    return HttpResponse(html)

def show_users(request):
    html = 'users'
    return HttpResponse(html)