#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

# To jest kluczowa zmiana:
python manage.py makemigrations blog
python manage.py migrate --fake-initial blog || python manage.py migrate blog