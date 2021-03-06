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

    def make_request(self, verb, url, query):
        try:
            response = self.session.request(verb, url=self.endpoint + url, params=query, headers=self.headers)
            response.raise_for_status()
        except (requests.ConnectionError, requests.Timeout) as e:
            resp = requests.Response()
            if 'timeout' in str(e).lower():
                resp.status_code = status.HTTP_408_REQUEST_TIMEOUT
            else:
                resp.status_code = status.HTTP_403_FORBIDDEN
            resp._content = bytes(json.dumps({'error': f'{e}'}), 'utf-8')
            return resp
        except requests.exceptions.HTTPError as e:
            if e:
                resp = e.response
                resp._content = bytes(json.dumps({'error': f'{e}'}), 'utf-8')
                return resp
        return response

    def create_label(self, cardid, category):
        query = self.query
        query['name'] = category
        query['color'] = 'blue'
        response = self.make_request('POST', 'cards1/' + cardid + '/labels', query)
        return response

    def delete_card(self, cardid):
        query = self.query
        response = self.make_request('DELETE', 'cards/' + cardid, query)
        return response

    def create_card(self, data, idlist):
        query = self.query
        query['idList'] = idlist.values()
        query['name'] = data.get('name')
        query['desc'] = data.get('desc')
        response = self.make_request('POST', 'cards/', query)
        return response
        
    
    def add_card(self, data, idlist):
        created = self.create_card(data, idlist)
        if created.status_code == 200:
            if 'task' in idlist:
                card = json.loads(created.content)
                cardid = card.get('id', "")
                category = data.get('category')
                label = self.create_label(cardid, category)
                if label.status_code == 200:
                    return label
                else:
                    deleted = self.delete_card(cardid)
                    if deleted.status_code == 200:
                        deleted.status_code = status.HTTP_204_NO_CONTENT
                        deleted._content = bytes(json.dumps({'error':'card culd not be created'}), 'utf-8')
                    return deleted
        return created
