from .api_connector import ApiConnector
from .env_manager import env_manager


class AlertsConnector(ApiConnector):
    def __init__(self):
        self.headers = {
            'Content-type': 'application/json',
            'X-API-Key': env_manager.ALERTS_CONNECTOR_TOKEN
        }
        self.base_url = 'https://alerts.com.ua/api/'

    def make_history_request(self):
        url = self.base_url + 'history'
        method = 'GET'
        return self.make_request(self.headers, url, method)

    def make_states_request(self):
        url = self.base_url + 'states'
        method = 'GET'
        return self.make_request(self.headers, url, method)
