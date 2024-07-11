from django.core.management.base import BaseCommand
from marketapp.models import Item
from datetime import  datetime
from random import randint, uniform

class Command(BaseCommand):
    help = "Add items in DB."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count items')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(1,count+1):
            rand_price = round(uniform(50.50, 500.50), 2)
            rand_count = randint(1_000, 10_000)
            new_item = Item (name=f'item_{i}',
                             description=f'description_{i}',
                             price=f'{rand_price}',
                             count=f'{rand_count}',
                             date_add=datetime.now(),
                             img = None)
            new_item.save()
            self.stdout.write(f'{new_item}')
