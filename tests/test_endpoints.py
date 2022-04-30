from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status



def test_trelloapi_post_issue_created(fixt1):
    client = APIClient()
    url = reverse('home')
    response = client.post(url, fixt1, format='json')
    assert response.status_code == status.HTTP_201_CREATED

def test_trelloapi_post_issue_failed(fixt2):
    client = APIClient()
    url = reverse('home')
    response = client.post(url, fixt2, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


