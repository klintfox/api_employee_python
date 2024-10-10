import pytest
from app import app, db, Employee

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_employee(client):
    response = client.post('/employees', json={
        "name": "Klint",
        "email": "klint@rodriguez.cl",
        "password": "aPdo203adk",
        "phones": [
            {
                "number": "23456788",
                "citycode": 6,
                "countrycode": 8
            }
        ]
    })
    assert response.status_code == 201
    assert response.json['message'] == "Empleado registrado exitosamente!"
