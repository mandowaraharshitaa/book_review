from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.session import Base

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), index=True)
    review_text = Column(String)
    rating = Column(Integer)
