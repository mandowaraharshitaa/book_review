from sqlalchemy.orm import Session
from app.models.review import Review
from app.schemas.review import ReviewCreate

def get_reviews(db: Session, book_id: int):
    return db.query(Review).filter(Review.book_id == book_id).all()

def create_review(db: Session, book_id: int, review: ReviewCreate):
    db_review = Review(**review.dict(), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review