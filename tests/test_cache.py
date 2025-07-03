from fastapi.testclient import TestClient
from app.main import app
from app.cache.redis_client import r, BOOK_CACHE_KEY

client = TestClient(app)

def test_books_cache_miss():
    r.delete(BOOK_CACHE_KEY)  # Ensure cache is empty
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert r.get(BOOK_CACHE_KEY) is not None  # Cache should be repopulated