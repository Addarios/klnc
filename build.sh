#!/usr/bin/env bash
# Wyjście przy błędzie
set -o errexit

# Instalacja paczek
pip install -r requirements.txt

# Zbieranie plików statycznych (CSS, JS, obrazy)
python manage.py collectstatic --no-input

# Migracje bazy danych
python manage.py migrate