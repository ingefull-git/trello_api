import json
import requests
from unittest import mock
from django.urls import reverse
from rest_framework import status
from core_app.utils import TrelloAPI
import pytest

def get_response_200(*args):
    resp = requests.Response()
    resp.status_code = status.HTTP_200_OK
    resp._content = b'{"content":"this is the content of the Mock response"}'
    return resp

def get_response_400(*args):
    resp = requests.Response()
    resp.status_code = status.HTTP_400_BAD_REQUEST
    resp._content = b'{"content":"this is the content of the Mock response"}'
    return resp

def get_response_empty(*args):
    resp = {}
    return resp

# @pytest.mark.skip
@mock.patch.object (TrelloAPI, 'create_card', side_effect=get_response_200)
def test_endpoints_trelloapi_post_issue_created(m, fixt1, client):
    url = reverse('home')
    response = client.post(url, json.dumps(fixt1), content_type='application/json')
    assert response.status_code == status.HTTP_201_CREATED

# @pytest.mark.skip
@mock.patch.object (TrelloAPI, 'create_card', side_effect=get_response_200)
def test_endpoints_trelloapi_post_bug_created(m, fixt2, client):
    url = reverse('home')
    response = client.post(url, json.dumps(fixt2), content_type='application/json')
    assert response.status_code == status.HTTP_201_CREATED

# @pytest.mark.skip
@mock.patch.object (TrelloAPI, 'create_card', side_effect=get_response_200)
@mock.patch.object (TrelloAPI, 'create_label', side_effect=get_response_200)
def test_endpoints_trelloapi_post_task_created(m_card, m_label, fixt3, client):
    url = reverse('home')
    response = client.post(url, json.dumps(fixt3), content_type='application/json')
    assert response.status_code == status.HTTP_201_CREATED

# @pytest.mark.skip
@mock.patch.object (TrelloAPI, 'create_card', side_effect=get_response_400)
def test_endpoints_trelloapi_post_issue_failed(m, fixt1, client):
    url = reverse('home')
    response = client.post(url, json.dumps(fixt1), content_type='application/json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST

# @pytest.mark.skip
def test_endpoints_trelloapi_post_issue_not_valid_data(fixt_fail, client):
    url = reverse('home')
    response = client.post(url, json.dumps(fixt_fail), content_type='application/json')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# @pytest.mark.skip
@mock.patch.object (TrelloAPI, 'create_card', side_effect=get_response_empty)
def test_endpoints_trelloapi_post_issue_exception(m, fixt5, client):
    url = reverse('home')
    response = client.post(url, json.dumps(fixt5), content_type='application/json')
    assert response.status_code == status.HTTP_404_NOT_FOUND