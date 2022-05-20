from celery import shared_task
from .data_base_provider import DataBaseProvider
from .alerts_connector import AlertsConnector

db_provider = DataBaseProvider()
alerts_connector = AlertsConnector()


@shared_task
def set_states_to_db():
    response = alerts_connector.make_states_request()
    db_provider.set_states(response)


@shared_task
def set_alarms_to_db():
    response = alerts_connector.make_history_request()
    db_provider.set_alarms(response)
