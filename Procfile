release:python alarm_in_Ukraine/manage.py migrate
web: python alarm_in_Ukraine/manage.py runserver 0.0.0.0:$PORT
worker: bash scripts/heroku_run & cd alarm_in_Ukraine & celery -A alarm_in_Ukraine worker & celery -A alarm_in_Ukraine beat -l INFO --pool=solo
