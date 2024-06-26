from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint

# Create your views here.
# Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.
# Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.
# Сохраняйте в логи данные о посещении страниц.

def index(request):
    html = '''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Django</title>
        </head>
        <body>
        <h1>Главная страница</h1>
        <h3>Что такое Django?</h3>
        <p>Django - это высокоуровневый фреймворк для веб-приложений на языке
        Python. Он был создан в 2005 году и с тех пор активно развивается и
        обновляется сообществом разработчиков по всему миру</p>
        <hr>
        <a href="http://127.0.0.1:8000/info/about/">Обо мне</a>.
        </body>
        </html>'''
    return HttpResponse(html)

def about(request):
    html = '''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>About</title>
        </head>
        <body>
        <h1>О Себе</h1>
        <h3>Расскажу немного о себе</h3>
        <p>Меня зовут Влад. Живу в Самаре. Изучаю Django</p>
        <hr>
        <a href="http://127.0.0.1:8000/info/">На главную страницу</a>.
        </body>
        </html>'''
    return HttpResponse(html)