import pytest
import redis
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_addition(client):
    response = client.get('/add?a=2&b=3')
    assert response.status_code == 200
    assert response.json['result'] == 5

def test_cache():
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('test_key', 'test_value')
    assert r.get('test_key') == b'test_value'
