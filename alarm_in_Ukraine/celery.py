import os

from celery import Celery
from dotenv import load_dotenv
load_dotenv(
        os.path.join(os.path.dirname(__file__), '.env')
    )

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alarm_in_Ukraine.settings')
app = Celery('alarms')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'set_alarms_to_db': {
        'task': 'alarms.tasks.set_alarms_to_db',
        'schedule': 300.0
    },
    'set_states_to_db': {
        'task': 'alarms.tasks.set_states_to_db',
        'schedule': 86400.0
    },

}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
