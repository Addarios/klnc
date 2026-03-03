#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

echo ">>> WYMUSZAM MIGRACJE <<<"
python manage.py makemigrations --noinput
python manage.py migrate --noinput
echo ">>> MIGRACJE ZAKONCZONE <<<"

python manage.py setup_admin