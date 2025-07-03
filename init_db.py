# init_db.py
from app.db.session import Base, engine
from app import models  # This loads all model classes once

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("All tables created.")
