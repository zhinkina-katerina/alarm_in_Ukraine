import requests
import time

class HTTPError(Exception):
    pass


class ApiConnector:
    @staticmethod
    def make_request(headers, url, method, body=None):
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, json=body, headers=headers)
        else:
            time.sleep(60)
            raise HTTPError('Unknown method')
        if response.status_code != 200:
            raise HTTPError('{}: {}'.format(response.status_code, response.reason))

        return response.json()


