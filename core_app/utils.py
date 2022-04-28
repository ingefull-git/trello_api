from requests import Session
from django.conf import settings


class TrelloAPI:
    def __init__(self):
        self.endpoint = settings.TRELLO_URL
        self.headers = {'Content-Type': 'aplication/json'}
        self.query = {
            'key': settings.TRELLO_KEY,
            'token': settings.TRELLO_TOKEN,
            }
        self.session = Session()
        self.session.headers.update(self.headers)

    def create_card(self, data, idlist):
        query = self.query
        query['idList'] = idlist.values()
        query['name'] = data.get('name')
        query['desc'] = data.get('desc')
        response = self.session.request('POST', self.endpoint + 'cards', params=query, headers=self.headers)
        return response

