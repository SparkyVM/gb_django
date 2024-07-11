from django.core.management.base import BaseCommand
from marketapp.models import Item

class Command(BaseCommand):
    help = "Edit count item in DB."


    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Item ID')
        parser.add_argument('count', type=int, help='New count')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        new_count = kwargs['count']
        new_item = Item.objects.filter(pk=pk).first()      # выбор
        new_item.count = new_count
        new_item.save()
        self.stdout.write(f'{new_item}, new count: {new_count}')