import os

from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alarm_in_Ukraine.settings')
app = Celery('alarms')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
     CELERY_ACCEPT_CONTENT = ['json'],
     CELERY_TASK_SERIALIZER = 'json',
     CELERY_RESULT_SERIALIZER = 'json',
)

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'set_states_to_db': {
        'task': 'alarms.tasks.set_states_to_db',
        'schedule': 60.0
    },
    'set_alarms_to_db': {
        'task': 'alarms.tasks.set_alarms_to_db',
        'schedule': 300.0
    },


}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
