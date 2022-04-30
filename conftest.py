import pytest

@pytest.fixture
def fixt1(db):
    fixture = {
        'type':'issue',
        'title':'title',
        'description':'description',
        'category':'category'
    }
    return fixture

@pytest.fixture
def fixt2(db):
    fixture = {
        'type':'issue',
        'title':'',
        'description':'description',
        'category':'category'
    }
    return fixture