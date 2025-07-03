import redis
import json
from app.schemas.book import BookOut
from typing import List

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

BOOK_CACHE_KEY = "books:list"

def get_books_cache() -> List[BookOut] | None:
    data = r.get(BOOK_CACHE_KEY)
    if data:
        books = json.loads(data)
        return [BookOut(**book) for book in books]
    return None

def set_books_cache(books: List[BookOut]):
    r.set(BOOK_CACHE_KEY, json.dumps([book.dict() for book in books]), ex=60)