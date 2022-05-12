import json
import requests
from unittest import mock
from django.urls import reverse
from rest_framework import status
from core_app.utils import TrelloAPI
import core_app
from core_app import utils
from django.conf import settings
import pytest

def get_response_200(*args, **kwargs):
    resp = requests.Response()
    resp.status_code = status.HTTP_200_OK
    resp._content = b'{"content":"this is the content of the response"}'
    return resp

def get_response_400(*args, **kwargs):
    resp = requests.Response()
    resp.status_code = status.HTTP_400_BAD_REQUEST
    resp._content = b'{"content":"this is the content of the response"}'
    return resp

def get_response_timeout(*args, **kwargs):
    resp = requests.Response()
    resp.status_code = status.HTTP_408_REQUEST_TIMEOUT
    return resp

def get_response_empty(*args, **kwargs):
    resp = {}
    return resp

def mock_response_ok(*args, **kwargs):
    resp = requests.Response()
    if kwargs:
        if 'labels' in kwargs['url']:
            resp.status_code = status.HTTP_200_OK
            resp._content = json.dumps({'ok':'label created'})
        elif not 'ID0001' in kwargs['url']:
            resp.status_code = status.HTTP_200_OK
            resp._content = json.dumps({'id':'ID0001'})
        else:
            resp.status_code = status.HTTP_200_OK
            resp._content = json.dumps({'error':'deleted'})
    return resp

def mock_response_fail(*args, **kwargs):
    resp = requests.Response()
    if kwargs:
        if 'labels' in kwargs['url']:
            resp.status_code = status.HTTP_400_BAD_REQUEST
            resp._content = json.dumps({'error':'label fail'})
        elif not 'ID0001' in kwargs['url']:
            resp.status_code = status.HTTP_200_OK
            resp._content = json.dumps({'id':'ID0001'})
        else:
            resp.status_code = status.HTTP_200_OK
            resp._content = json.dumps({'error':'card deleted'})
    return resp


# @pytest.mark.skip
@mock.patch('core_app.utils.requests.session')
def test_utils_trelloapi_post_issue_create_card_ok(m, fixt1, client):
    m.return_value.request.return_value.status_code = status.HTTP_200_OK
    m.return_value.request.return_value.content = json.dumps({'mock':'mock'})
    url = reverse('home')
    response = client.post(url, json.dumps(fixt1), content_type='application/json')
    assert response.status_code == status.HTTP_201_CREATED

# @pytest.mark.skip
@mock.patch('core_app.utils.requests.session')
def test_utils_trelloapi_post_bug_create_card_ok(m, fixt2, client):
    m.return_value.request.return_value.status_code = status.HTTP_200_OK
    m.return_value.request.return_value.content = json.dumps({'mock':'mock'})
    url = reverse('home')
    response = client.post(url, json.dumps(fixt2), content_type='application/json')
    assert response.status_code == status.HTTP_201_CREATED

# @pytest.mark.skip
@mock.patch('core_app.utils.requests.session')
def test_utils_trelloapi_post_task_create_card_ok(m, fixt3, client):
    m.return_value.request.side_effect = get_response_200
    url = reverse('home')
    response = client.post(url, json.dumps(fixt3), content_type='application/json')
    args = m.call_args_list
<<<<<<< HEAD
=======
    print(args)
>>>>>>> a337869bed3015809230e717ab8ee8d99a5e64e8
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.skip
@mock.patch('core_app.utils.requests.session')
def test_utils_trelloapi_post_task_delete_card_ok(m, client):
    m.return_value.request.return_value.status_code = status.HTTP_200_OK
    m.return_value.request.return_value.content = json.dumps({'id':'mockid'})
    api = TrelloAPI()
    response = api.delete_card('1234')
    assert response.status_code == status.HTTP_200_OK


# @pytest.mark.skip
@mock.patch.object(core_app.utils.requests, 'session')
def test_utils_create_card_ok(m1):
    m1.return_value.request.side_effect = get_response_200
    data = {
        'name': 'some name',
        'desc': 'some description'
    }
    id_list = {
        'idList': 'some id_list'
    }
    api = TrelloAPI()
    response = api.create_card(data, id_list)
<<<<<<< HEAD
=======
    print(m1.call_args_list)
>>>>>>> a337869bed3015809230e717ab8ee8d99a5e64e8
    assert response.status_code == 200

# @pytest.mark.skip
@mock.patch.object(core_app.utils.requests, 'session')
def test_utils_create_card_fail(m1):
    m1.return_value.request.side_effect = get_response_400
    data = {
        'name': 'some name',
        'desc': 'some description'
    }
    id_list = {
        'idList': 'some id_list'
    }
    api = TrelloAPI()
    response = api.create_card(data, id_list)
    assert response.status_code == 400

# @pytest.mark.skip
@mock.patch.object(core_app.utils.requests, 'session')
def test_utils_create_card_timeout(m1, fixt1, client):
    m1.return_value.request.side_effect = requests.exceptions.Timeout('Connection timed out')
    url = reverse('home')
    response = client.post(url, json.dumps(fixt1), content_type='application/json')
    assert response.status_code == 408
    assert response.data == {'error': 'Connection timed out'}

# @pytest.mark.skip
@mock.patch.object(core_app.utils.requests, 'session')
def test_utils_create_card_connection_error(m1, fixt1, client):
    m1.return_value.request.side_effect = requests.ConnectionError('Connection error')
    url = reverse('home')
    response = client.post(url, json.dumps(fixt1), content_type='application/json')
    assert response.status_code == 403
    assert response.data == {'error': 'Connection error'}


# @pytest.mark.skip
@mock.patch.object(core_app.utils.requests, 'session')
def test_utils_add_card_ok(m1, fixt3, client):
    m1.return_value.request.side_effect = mock_response_ok
    url = reverse('home')
    response = client.post(url, json.dumps(fixt3), content_type='application/json')
    args = m1.return_value.request.call_args_list
<<<<<<< HEAD
=======
    print(args)
>>>>>>> a337869bed3015809230e717ab8ee8d99a5e64e8
    assert response.status_code == 201
    assert response.data == {'ok': 'label created'}


# @pytest.mark.skip
@mock.patch.object(core_app.utils.requests, 'session')
def test_utils_add_card_fail(m1, fixt3, client):
    m1.return_value.request.side_effect = mock_response_fail
    url = reverse('home')
    response = client.post(url, json.dumps(fixt3), content_type='application/json')
    args = m1.return_value.request.call_args_list
<<<<<<< HEAD
=======
    print(args)
>>>>>>> a337869bed3015809230e717ab8ee8d99a5e64e8
    assert response.status_code == 204
    assert response.data == {'error': 'card deleted'}