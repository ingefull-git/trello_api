from django.conf import settings
from rest_framework.response import Response
from rest_framework import status, generics
from .utils import TrelloAPI
import json

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
            valid = api.validate_data(msg)
            if valid:
                response = api.add_card(msg, valid)
                if response.status_code == 200:
                    data = json.loads(response.content)
                    r_status = status.HTTP_201_CREATED
                else:
                    data = json.loads(response.content)
                    r_status = response.status_code
            else:
                data = {'error': "the data is wrong, check if there is something missing."}
                r_status = status.HTTP_401_UNAUTHORIZED
        except Exception as e:
            data = {'error': f'Error: {e}'}
            print("\nExcept error: ", e)
            r_status = status.HTTP_404_NOT_FOUND
        return Response(data, status=r_status)
