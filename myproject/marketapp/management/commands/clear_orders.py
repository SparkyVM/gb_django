from django.core.management.base import BaseCommand
from marketapp.models import Order

class Command(BaseCommand):
    help = "Clear orders table."

    def handle(self, *args, **kwargs):
        Order.objects.all().delete()
        self.stdout.write(f'Orders is cleared')