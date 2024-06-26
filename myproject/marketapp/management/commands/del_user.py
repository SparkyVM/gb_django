from django.core.management.base import BaseCommand
from marketapp.models import User

class Command(BaseCommand):
    help = "Delete user in DB."


    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        new_user = User.objects.filter(pk=pk).first()      # выбор
        if new_user is not None:
            new_user.delete()
        self.stdout.write(f'{new_user} is deleted')