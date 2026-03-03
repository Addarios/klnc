from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Tworzy superużytkownika na podstawie zmiennych środowiskowych'

    def handle(self, *args, **options):
        username = os.environ.get('ADMIN_USERNAME')
        email = os.environ.get('ADMIN_EMAIL')
        password = os.environ.get('ADMIN_PASSWORD')

        if not all([username, email, password]):
            self.stdout.write(self.style.WARNING('Brak danych logowania w zmiennych środowiskowych. Pomijam.'))
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Superużytkownik "{username}" został stworzony!'))
        else:
            self.stdout.write(self.style.NOTICE(f'Użytkownik "{username}" już istnieje.'))