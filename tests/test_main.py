from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API en ejecución 🚀"}

def test_upload_csv():
    csv_content = "name,value\nAlice,100\nBob,200"
    response = client.post("/upload", files={"file": ("test.csv", csv_content)})
    assert response.status_code == 200
    assert "message" in response.json()
