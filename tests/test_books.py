from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_book():
    response = client.post("/books/", json={"title": "Test Book", "author": "Test Author"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Book"
    assert "id" in data

def test_list_books():
    response = client.get("/books/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
