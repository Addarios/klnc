#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

# To polecenie sprawdzi status i spróbuje naprawić bazę
python manage.py migrate --fake-initial blog
python manage.py migrate


# Tworzenie superużytkownika z poziomu zmiennych środowiskowych
python manage.py shell <<EOF
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.getenv('ADMIN_USERNAME')
email = os.getenv('ADMIN_EMAIL')
password = os.getenv('ADMIN_PASSWORD')

if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"Superuser '{username}' został utworzony pomyślnie.")
    else:
        print(f"Superuser '{username}' już istnieje.")
else:
    print("BŁĄD: Brak zmiennych środowiskowych dla admina!")
EOF