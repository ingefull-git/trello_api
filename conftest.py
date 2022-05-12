import pytest

@pytest.fixture
def fixt1(db):
    fixture = {
        'type': 'issue',
        'title': 'title fixt1',
        'description': 'description',
    }
    return fixture

@pytest.fixture
def fixt2(db):
    fixture = {
        'type': 'bug',
        'description': 'description',
    }
    return fixture

@pytest.fixture
def fixt3(db):
    fixture = {
        'type': 'task',
        'title': 'title fixt3',
        'description': 'description',
        'category': 'category fixt3'
    }
    return fixture

@pytest.fixture
def fixt_fail(db):
    fixture = {
        'type': 'task',
        'title': '',
        'description': 'description',
        'category': 'category fail'
    }
    return fixture

@pytest.fixture
def fixt5(db):
    fixture = {
        'type': 'task',
        'title': 'title fixt5',
        'description': 'description',
        'category': 'category fixt5'
    }
    return fixture