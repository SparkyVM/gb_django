from django.core.management.base import BaseCommand
from marketapp.models import User, Item, Order
from datetime import  datetime, timedelta
from random import randint, uniform, choice

class Command(BaseCommand):
    help = "Add orders in DB."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count items')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        list_users = User.objects.all()
        list_items = Item.objects.all()
        for i in range(1,count+1):
            rand_price = round(uniform(50.50, 500.50), 2)            
            rand_dt = datetime.now() - timedelta(days=randint(0,600))
            new_order = Order (user_id=choice(list_users),
                             item_id=choice(list_items),
                             price=f'{rand_price}',
                             date_add=rand_dt )
            new_order.save()
            self.stdout.write(f'{new_order}')