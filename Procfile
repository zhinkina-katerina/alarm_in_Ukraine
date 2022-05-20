release:python manage.py migrate
web: python manage.py runserver 0.0.0.0:$PORT
worker: celery -A alarm_in_Ukraine worker & celery -A alarm_in_Ukraine beat
