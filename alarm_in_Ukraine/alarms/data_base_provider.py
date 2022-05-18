from .alerts_connector import AlertsConnector
from .models import States, Alarm
from django.db.models import Max


class DataBaseProvider:
    def set_states(self, response):
        if States.objects.first():
            return
        for item in response['states']:
            id_item = item.get('id')
            state = item.get('name')
            States.objects.create(id=id_item,
                                  state=state)

    def set_alarms(self, response):
        max_id = Alarm.objects.all().aggregate(Max('id')).get('id__max')
        new_alarms = response[max_id:]
        for item in new_alarms:
            id_item = item.get('id')
            date = item.get('date')

            state_id = int(item.get('state_id'))
            state_id = States.objects.only('id').get(id=state_id)

            alert = item.get('alert')
            Alarm.objects.create(id=id_item,
                                 date=date,
                                 state_id=state_id,
                                 alert=alert)

