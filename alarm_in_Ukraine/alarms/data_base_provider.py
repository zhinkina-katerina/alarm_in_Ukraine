from .models import States, Alarm
from django.db.models import Max


class DataBaseProvider:
    def set_states(self, response):
        if States.objects.first():
            return
        for item in response['states']:
            States.objects.create(id=item.get('id'), state=item.get('name'))

    def set_alarms(self, response):
        max_id = Alarm.objects.all().aggregate(Max('id')).get('id__max')
        new_alarms = list(filter(lambda x: x.get('id') > max_id, response))
        for item in new_alarms:
            state_id = int(item.get('state_id'))
            state = States.objects.only('id').get(id=state_id)

            alert = item.get('alert')
            Alarm.objects.create(id=item.get('id'),
                                 date=item.get('date'),
                                 state_id=state,
                                 alert=alert)