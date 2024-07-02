from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from datetime import timedelta, date
from .models import Order, User, Item
from .forms import ItemForm


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

def show_users(request):                    # показать всех пользователей
    list_users = User.objects.all()
    return render(request, 'marketapp/users.html', {'users':list_users})

def show_user_orders(request, user_id):     # показать все заказы пользователя
    user = get_object_or_404(User, pk=user_id)
    list_orders = Order.objects.filter(user_id=user).order_by('-date_add')
    return render(request, 'marketapp/orders.html', {'user': user, 'orders': list_orders})

def last_days_orders(request, days):        # выборка всех заказов за Х дней
    filter_dt = date.today() - timedelta(days=days)
    list_orders = Order.objects.filter(date_add__gt=filter_dt).order_by('-date_add')
    return render(request, 'marketapp/orders.html', {'orders':list_orders})

def week_orders(request):                   # выборка за неделю
    filter_dt = date.today() - timedelta(days=7)
    list_orders = Order.objects.filter(date_add__gt=filter_dt).order_by('-date_add')
    return render(request, 'marketapp/orders.html', {'orders':list_orders})

def month_orders(request):                   # выборка за месяц
    filter_dt = date.today() - timedelta(days=30)
    list_orders = Order.objects.filter(date_add__gt=filter_dt).order_by('-date_add')
    return render(request, 'marketapp/orders.html', {'orders':list_orders})

def year_orders(request):                   # выборка за год
    filter_dt = date.today() - timedelta(days=365)
    list_orders = Order.objects.filter(date_add__gt=filter_dt).order_by('-date_add')
    return render(request, 'marketapp/orders.html', {'orders':list_orders})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            date_add = form.cleaned_data['date_add']
            img = form.cleaned_data['img']
            
            fs = FileSystemStorage()
            fs.save(img.name, img)
            item = Item(name=name, 
                        description=description,
                        price=price,
                        count=count,
                        date_add=date_add)
            item.save()
            message = 'Товар сохранен'
    else:
        form = ItemForm()
        message = 'Заполните форму'        
    return render(request, 'marketapp/add_item.html', {'form': form, 'message': message})