import json
import requests
from unittest import mock
from django.urls import reverse
from rest_framework import status
from core_app.utils import TrelloAPI
import core_app
from core_app import utils


def get_response_200(*args):
    resp = requests.Response()
    resp.status_code = status.HTTP_200_OK
    resp._content = b'{"content":"this is the content of the response"}'
    return resp

def get_response_400(*args):
    resp = requests.Response()
    resp.status_code = status.HTTP_400_BAD_REQUEST
    resp._content = b'{"content":"this is the content of the response"}'
    return resp

def get_response_empty(*args):
    resp = {}
    return resp

@mock.patch('core_app.utils.requests.session')
def test_utils_trelloapi_post_issue_create_card_ok(m, fixt1, client):
    m.return_value.post.return_value.status_code = status.HTTP_200_OK
    m.return_value.post.return_value.content = json.dumps({'mock':'mock'})
    url = reverse('home')
    response = client.post(url, json.dumps(fixt1), content_type='application/json')
    print(type(response))
    assert response.status_code == status.HTTP_201_CREATED

@mock.patch('core_app.utils.requests.session')
def test_utils_trelloapi_post_bug_create_card_ok(m, fixt2, client):
    m.return_value.post.return_value.status_code = status.HTTP_200_OK
    m.return_value.post.return_value.content = json.dumps({'mock':'mock'})
    url = reverse('home')
    response = client.post(url, json.dumps(fixt2), content_type='application/json')
    assert response.status_code == status.HTTP_201_CREATED

@mock.patch('core_app.utils.requests.post')
@mock.patch('core_app.utils.requests.session')
def test_utils_trelloapi_post_task_create_card_ok(m, m2, fixt3, client):
    m.return_value.post.return_value.status_code = status.HTTP_200_OK
    m.return_value.post.return_value.content = json.dumps({'id':'mockid'})
    m2.return_value.status_code = status.HTTP_200_OK
    m2.return_value.content = json.dumps({'mock':'mock'})
    url = reverse('home')
    response = client.post(url, json.dumps(fixt3), content_type='application/json')
    assert response.status_code == status.HTTP_201_CREATED

@mock.patch('core_app.utils.requests.delete')
def test_utils_trelloapi_post_task_delete_card_ok(m, client):
    m.return_value.status_code = status.HTTP_200_OK
    m.return_value.content = json.dumps({'mock':'mock'})
    api = TrelloAPI()
    response = api.delete_card('1234')
    assert response.status_code == status.HTTP_200_OK

@mock.patch('core_app.utils.requests.delete')
@mock.patch('core_app.utils.requests.post')
@mock.patch('core_app.utils.requests.session')
# @mock.patch.object (TrelloAPI, 'create_label', side_effect=get_response_400)
def test_utils_trelloapi_post_task_create_card_failed(m, m2, m3, fixt3, client):
    m.return_value.post.return_value.status_code = status.HTTP_200_OK
    m.return_value.post.return_value.content = json.dumps({'id':'mockid'})
    m2.return_value.status_code = status.HTTP_400_BAD_REQUEST
    m2.return_value.content = json.dumps({'mock':'mock'})
    m3.return_value.status_code = status.HTTP_200_OK
    m3.return_value.content = json.dumps({'mock':'mock'})
    url = reverse('home')
    response = client.post(url, json.dumps(fixt3), content_type='application/json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST

