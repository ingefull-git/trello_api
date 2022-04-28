from django.conf import settings
from rest_framework.response import Response
from rest_framework import status, generics
from .utils import TrelloAPI


class TrelloApiView(generics.GenericAPIView):

    def post(self, request):
        data = request.data
        api = TrelloAPI()
        msg = {}
        r_status = None
        try:
            msg['type'] = data.get('type', "")
            msg['name'] = data.get('title', "")
            msg['desc'] = data.get('description', "")
            msg['category'] = data.get('category', "")
            idlist = {}
            if msg['type'].lower() == 'issue':
                if msg['name'] and msg['desc']:
                    idlist['issue'] = settings.TRELLO_ISSUE
            elif msg['type'].lower() == 'bug':
                if msg['desc']:
                    idlist['bug'] = settings.TRELLO_BUG
            elif msg['type'].lower() == 'task':
                if msg['name'] and msg['category']:
                    idlist['task'] = settings.TRELLO_TASK
            response = api.create_card(msg, idlist)
            if response.status_code == 200:
                data = response.json()
                r_status = status.HTTP_201_CREATED
            else:
                data = {'error': 'There was an error and the card could not be created, please try again.'}
                r_status = status.HTTP_400_BAD_REQUEST
        except Exception as e:
            data = {'error': f'Error: {e}'}
            r_status = status.HTTP_404_NOT_FOUND
        return Response(data, status=r_status)

