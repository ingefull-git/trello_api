from rest_framework.response import Response
from rest_framework import status, generics


class TrelloApiView(generics.GenericAPIView):

    def post(self, request):
        data = request.data
        return Response(data, status=status.HTTP_200_OK)

