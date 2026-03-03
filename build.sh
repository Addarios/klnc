#!/usr/bin/env bash
set -o errexit

echo "--- INSTALACJA PACZEK ---"
pip install -r requirements.txt

echo "--- ZBIERANIE STATYK ---"
python manage.py collectstatic --no-input

echo "--- ROBIENIE MIGRACJI ---"
# Ta linia wymusi szukanie nowych zmian, jeśli Git coś pominął
python manage.py makemigrations --noinput 
# Ta linia stworzy tabele w PostgreSQL
python manage.py migrate --noinput

echo "--- TWORZENIE ADMINA ---"
python manage.py setup_admin

echo "--- KONIEC BUILD ---"