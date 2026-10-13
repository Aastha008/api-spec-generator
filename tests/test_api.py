from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_generate_endpoint():
    response = client.post("/generate?repo_path=.")
    assert response.status_code == 200
    assert response.json()["status"] == "completed"