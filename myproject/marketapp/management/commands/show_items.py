from django.core.management.base import BaseCommand
from marketapp.models import Item

class Command(BaseCommand):
    help = "Chose item in DB."


    def add_arguments(self, parser):
        parser.add_argument('price', type=int, help='Filter price')

    def handle(self, *args, **kwargs):
        in_price = kwargs['price']
        new_item = Item.objects.filter(price__lt=in_price)      # выборка мненьше чем Х
        self.stdout.write(f'{new_item}')
