from fastapi import FastAPI
from app.api import books, reviews

app = FastAPI(title="Book Review Service")

app.include_router(books.router)
app.include_router(reviews.router)

### book_review_service/app/api/books.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate, BookOut
from app.services.book_service import get_books, create_book
from app.db.session import get_db
from app.cache.redis_client import get_books_cache, set_books_cache
import logging

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[BookOut])
def list_books(db: Session = Depends(get_db)):
    try:
        cached_books = get_books_cache()
        if cached_books:
            return cached_books
    except Exception as e:
        logging.warning(f"Cache unavailable: {e}")

    books = get_books(db)

    try:
        set_books_cache(books)
    except Exception as e:
        logging.warning(f"Failed to update cache: {e}")

    return books

@router.post("/", response_model=BookOut)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)