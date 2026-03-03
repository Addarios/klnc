#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

# To polecenie sprawdzi status i spróbuje naprawić bazę
python manage.py migrate --fake-initial blog
python manage.py migrate