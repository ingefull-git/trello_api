from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
class TestTrelloAPI(APITestCase):

    def test_trelloapi_post_view(self):
        url = reverse('home')
        response = self.client.post(url, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
