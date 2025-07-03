📚 Book Review Service - FastAPI Backend

This is a backend project for a Book Review Service built using FastAPI, SQLite, SQLAlchemy, and Redis (for caching).

🚀 Features

 Add & list books

 Add & list reviews per book

 Data stored in SQLite database (test.db)

Redis-based caching for fast book listing

 RESTful API with Swagger UI documentation

 Project Structure

book_review_service/
├── app/
│   ├── api/
│   │   ├── books.py         # Book API routes
│   │   └── reviews.py       # Review API routes
│   ├── cache/
│   │   └── redis_client.py  # Redis cache functions
│   ├── db/
│   │   └── session.py       # DB session setup
│   ├── models/
│   │   ├── book.py
│   │   └── review.py
│   ├── schemas/
│   │   ├── book.py          # Pydantic models for book
│   │   └── review.py        # Pydantic models for review
│   ├── services/
│   │   ├── book_service.py  # DB logic for books
│   │   └── review_service.py# DB logic for reviews
│   └── main.py              # FastAPI entry point
├── test.db                  # SQLite DB file (auto created)
└── tests/                   # Pytest test cases

🧠 Tech Stack

Tech

Description

FastAPI

API framework

SQLite

Lightweight local database

SQLAlchemy

ORM for DB handling

Redis

Caching for listing books

Pydantic

Schema validation

Uvicorn

ASGI server to run FastAPI app

⚙️ Setup Instructions

1. 📦 Install Dependencies

pip install -r requirements.txt

2. 🧠 Run Redis Server

Make sure Redis is running on port 6379. You can either:

Install Redis locally

OR use Memurai (Windows Redis alternative)

OR use RedisInsight to view your data

3. ▶️ Start the App

python -m uvicorn app.main:app --reload

4. 🧪 Run Tests

pytest

🌐 API Endpoints

📚 Books

GET /books/ → List all books (cached with Redis)

POST /books/ → Add new book

✍️ Reviews

GET /books/{book_id}/reviews/ → List reviews for a book

POST /books/{book_id}/reviews/ → Add a review

Swagger UI available at: http://127.0.0.1:8000/docs

🧊 Redis Caching

Cache key used: books:list

Data is cached for 60 seconds

Caching is used only on GET /books/

If Redis is not running, a warning is logged, but app still works.

🛠 How It Works

When you add a book → It is saved in test.db

When you hit GET /books/ →

First tries to get data from Redis

If not found → fetch from DB → cache it

Reviews are always stored in DB (not cached for now)

🔗 Sample Book Object

{
  "title": "The Alchemist",
  "author": "Paulo Coelho"
}

🔗 Sample Review Object

{
  "review_text": "Loved it! Very motivational.",
  "rating": 5
}

📂 Database

Using SQLite, DB file: test.db

Tables:

books

reviews

You can open test.db in DB Browser for SQLite or VS Code extensions

🧠 To Do (Future Improvements)

Add pagination for listing books/reviews

Add update/delete endpoints

Add authentication (JWT)

Store reviews in Redis for performance

🧑‍💻 Author

Made by harshita mandowara

📄 License

MIT License

