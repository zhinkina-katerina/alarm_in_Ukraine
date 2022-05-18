from api_connector import ApiConnector


class AlertsConnector(ApiConnector):
    def __init__(self):
        self.headers = {'Content-type': 'application/json',
                        'X-API-Key': '8eeb4d31d593fb40220a977745f49eb751d71abe'}

    def make_history_request(self):
        url = 'https://alerts.com.ua/api/history'
        method = 'GET'
        return self.make_request(self.headers, url, method)

    def make_states_request(self):
        url = 'https://alerts.com.ua/api/states'
        method = 'GET'
        return self.make_request(self.headers, url, method)
