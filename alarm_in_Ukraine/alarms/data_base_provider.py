from alerts_connector import AlertsConnector
from models import States, Alarm


class DataBaseProvider:
    def set_states(self, response):
        for item in response['states']:
            id = item.get('id')
            name = item.get('name')
            States.objects.create(id=id,
                                  name=name)

    def set_alarms(self, response):
        for item in response:
            id = item.get('id')
            date = item.get('date')
            state_id = item.get('state_id')
            alert = item.get('alert')
            Alarm.objects.create(id=id,
                                 date=date,
                                 state_id=state_id,
                                 alert=alert)

