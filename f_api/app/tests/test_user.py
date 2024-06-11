from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/user/")
    assert response.status_code == 200

def test_new_user():
    pass
