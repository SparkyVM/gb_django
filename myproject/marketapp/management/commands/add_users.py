from django.core.management.base import BaseCommand
from marketapp.models import User
from datetime import  datetime
from random import randint

class Command(BaseCommand):
    help = "Add user in DB."


    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count users')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(1,count+1):
            rand_phone = randint(100_000, 999_999)
            new_user = User (name=f'user_{i}',
                             email=f'email_{i}@mail.ru',
                             phone=f'{rand_phone}',
                             adr=f'Baker Street, d.{i}',
                             date_add=datetime.now() )
            new_user.save()
            self.stdout.write(f'{new_user}')
