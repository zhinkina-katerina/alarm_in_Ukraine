release:python manage.py migrate
release:python states_siding.py
web: python manage.py runserver 0.0.0.0:$PORT
worker: celery -A alarm_in_Ukraine beat & celery -A alarm_in_Ukraine worker -l INFO
