from pydantic import BaseModel

class ReviewBase(BaseModel):
    review_text: str
    rating: int

class ReviewCreate(ReviewBase):
    pass

class ReviewOut(ReviewBase):
    id: int
    book_id: int

    class Config:
        orm_mode = True