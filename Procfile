web: python website/manage.py runserver 0.0.0.0:$PORT
beat: celery -A alarm_in_Ukraine beat
worker: celery -A alarm_in_Ukraine worker -l INFO --pool=solo

