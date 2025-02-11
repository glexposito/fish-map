from http import HTTPStatus

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == "Hello Fish Map! Let's get started!"


def test_get_python_version():
    response = client.get("/python-version")
    assert response.status_code == HTTPStatus.OK
