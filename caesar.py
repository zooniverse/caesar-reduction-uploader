import requests
from panoptes_client import Panoptes

class CaesarClient:
    def __init__(self, username, password):
        Panoptes.connect(username=username, password=password)
        token = Panoptes.client().get_bearer_token()
        self.headers = {'authorization': "Bearer %s" % token}
        
    def update_reduction(self, workflow_id, subject_id, data):
        url = 'https://caesar.zooniverse.org/workflows/%i/reducers/swap/reductions' % workflow_id
        payload = {'reduction': {'subject_id': subject_id, 'data': data}}
        
        response = requests.put(url, json=payload, headers=self.headers)
        return response
