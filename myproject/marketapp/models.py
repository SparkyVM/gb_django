from django.db import models

# Create your models here.
'''
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
'''

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    adr = models.CharField(max_length=100)
    date_add = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Name: {self.name}, email: {self.email}, phone:{self.phone}'

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField(default=0)
    date_add = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='products/')

    def __str__(self) -> str:
        return f'Name: {self.name}, description: {self.description}, price: {self.price}'

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_add = models.DateField()