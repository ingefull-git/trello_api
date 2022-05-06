from requests import Session
from django.conf import settings
from rest_framework import status
import requests
import json


class TrelloAPI:
    def __init__(self):
        self.endpoint = settings.TRELLO_URL
        self.headers = {'Content-Type': 'aplication/json'}
        self.query = {
            'key': settings.TRELLO_KEY,
            'token': settings.TRELLO_TOKEN,
            }
        self.session = requests.session()
        self.session.headers.update(self.headers)

    def validate_data(self, data):
        idlist = {}
        if data['type'].lower() == 'issue':
            if data['name'] and data['desc']:
                idlist['issue'] = settings.TRELLO_ISSUE
        elif data['type'].lower() == 'bug':
            if data['desc']:
                idlist['bug'] = settings.TRELLO_BUG
        elif data['type'].lower() == 'task':
            if data['name'] and data['category']:
                idlist['task'] = settings.TRELLO_TASK
        return idlist

    def create_label(self, cardid, category):
        query = self.query
        query['name'] = category
        query['color'] = 'blue'
        response = self.session.post(url=self.endpoint + 'cards/' + cardid + '/labels' , params=query, headers=self.headers)
        return response

    def delete_card(self, cardid):
        query = self.query
        response = self.session.delete(url=self.endpoint + 'cards/' + cardid, params=query, headers=self.headers)
        return response

    def create_card(self, data, idlist):
        query = self.query
        query['idList'] = idlist.values()
        query['name'] = data.get('name')
        query['desc'] = data.get('desc')
        response = self.session.post(url=self.endpoint + 'cards', params=query, headers=self.headers)
        if response.status_code == 200:
            if 'task' in idlist:
                card = json.loads(response.content)
                cardid = card.get('id', "")
                category = data.get('category')
                label = self.create_label(cardid, category)
                if label.status_code == 200:
                    return label
                else:
                    deleted = self.delete_card(cardid)
                    if deleted.status_code == 200:
                        deleted.status_code = status.HTTP_204_NO_CONTENT
                    return deleted
        return response