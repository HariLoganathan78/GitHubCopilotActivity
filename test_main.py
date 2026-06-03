from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_checksum():
    response = client.post(
        "/checksum",
        json={"text": "hello"}
    )

    assert response.status_code == 200
    assert "checksum" in response.json()
