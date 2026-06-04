from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():

    response = client.get('/')

    assert response.status_code == 200

def test_child():

    response = client.post(
        '/predict',
        json={"age":4})   
    
    assert response.status_code == 200
    assert response.json()['category'] == 'Child'

def test_adult():

    response = client.post(
        '/predict',
        json={"age":35})   
    
    assert response.status_code == 200
    assert response.json()['category'] == 'Adult'

def test_senior():

    response = client.post(
        '/predict',
        json={"age":65})   
    
    assert response.status_code == 200
    assert response.json()['category'] == 'Senior Citizen'


