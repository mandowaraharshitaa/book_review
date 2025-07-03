

### book_review_service/app/api/reviews.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.review import ReviewCreate, ReviewOut
from app.services.review_service import get_reviews, create_review
from app.db.session import get_db

router = APIRouter(prefix="/books/{book_id}/reviews", tags=["Reviews"])

@router.get("/", response_model=list[ReviewOut])
def list_reviews(book_id: int, db: Session = Depends(get_db)):
    return get_reviews(db, book_id)

@router.post("/", response_model=ReviewOut)
def add_review(book_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    return create_review(db, book_id, review)


